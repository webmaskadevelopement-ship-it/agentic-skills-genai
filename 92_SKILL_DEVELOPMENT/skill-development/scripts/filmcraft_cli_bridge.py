#!/usr/bin/env python3
"""
FilmCraft CLI & Skill Bridge Layer
Bridges the Autonomous Post-Production Monorepo Skill instructions ([001]-[720])
with the native FilmCraft CLI binary (701 commands) and live GUI loopback control.
"""

import argparse
import json
import os
import socket
import subprocess
import sys
import time

CLI_PATH = "/Volumes/DISK 1/AGENTS TRAIN/EDITING_SYSTEM/filmcraft-cli-0.9.0-macos-universal/filmcraft-cli"
DEFAULT_BRIDGE_HOST = "127.0.0.1"
DEFAULT_BRIDGE_PORT = 9876

# Master Command -> Native FilmCraft CLI Command Mapping Table
SKILL_TO_FILMCRAFT_MAP = {
    # Cluster 01: Ingest & Assistant Editing (480-485)
    "CMD_INGEST_VERIFY_MEDIA_HASHES": {"subcommand": "probe", "native_cmds": ["media.status", "events.list"]},
    "CMD_INGEST_PARSE_CAMERA_METADATA": {"subcommand": "probe", "native_cmds": ["media.colorInfo", "metadata.get"]},
    "CMD_INGEST_SYNC_MULTICAM_AND_AUDIO": {"subcommand": "exec", "native_cmds": ["multicam.switchAngle", "multicam.audioFollowsVideo"]},
    "CMD_INGEST_LOAD_TIMED_TRANSCRIPT": {"subcommand": "exec", "native_cmds": ["transcript.generate", "transcript.inspect"]},
    "CMD_INGEST_INDEX_VISUAL_SHOTS": {"subcommand": "inspect", "native_cmds": ["project.select", "sequence.revealInProject"]},
    "CMD_INGEST_BUILD_NLE_BIN_STRUCTURE": {"subcommand": "exec", "native_cmds": ["file.newBin", "project.moveToBin"]},

    # Cluster 02: Editorial Craft & Pacing (486-496)
    "CMD_EDIT_EVALUATE_AND_RANK_TAKES": {"subcommand": "exec", "native_cmds": ["clip.sourceSettings", "markers.markIn", "markers.markOut"]},
    "CMD_EDIT_DISQUALIFY_FLAWED_TAKES": {"subcommand": "exec", "native_cmds": ["labels.presets", "project.delete"]},
    "CMD_EDIT_TRIM_SILENT_OPENERS_AND_TAILS": {"subcommand": "exec", "native_cmds": ["timeline.trim", "playhead.set"]},
    "CMD_EDIT_GENERATE_PAPER_EDIT": {"subcommand": "exec", "native_cmds": ["transcript.search", "transcript.inspect"]},
    "CMD_EDIT_COMPILE_ASSEMBLY_SEQUENCE": {"subcommand": "exec", "native_cmds": ["timeline.place", "sequence.open"]},
    "CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT": {"subcommand": "exec", "native_cmds": ["timeline.razor", "timeline.move", "timeline.selectGap"]},
    "CMD_EDIT_CALCULATE_JL_SPLIT_TRANSITIONS": {"subcommand": "exec", "native_cmds": ["trim.edit", "markers.markSplitVideoIn"]},
    "CMD_EDIT_VERIFY_MURCH_SIX_PRIORITIES": {"subcommand": "inspect", "native_cmds": ["sequence.inspect", "timeline.select"]},
    "CMD_EDIT_PROFILE_RHYTHM_AND_PACING": {"subcommand": "inspect", "native_cmds": ["sequence.inspect", "perf.stats"]},
    "CMD_EDIT_VALIDATE_EDL_TIMECODE_MONOTONICITY": {"subcommand": "inspect", "native_cmds": ["sequence.inspect", "markers.markIn"]},
    "CMD_EDIT_EMIT_EDL_MANIFEST": {"subcommand": "inspect", "native_cmds": ["sequence.inspect"]},

    # Cluster 03: Color Grading & Look Dev (497-506)
    "CMD_COLOR_LOAD_SHOT_METADATA": {"subcommand": "exec", "native_cmds": ["media.colorInfo", "color.spaces"]},
    "CMD_COLOR_ANALYZE_SCOPES": {"subcommand": "exec", "native_cmds": ["scopes.read"]},
    "CMD_COLOR_BUILD_NODE_GRAPH": {"subcommand": "exec", "native_cmds": ["effects.apply", "effects.setParam"]},
    "CMD_COLOR_SET_PRIMARY_BALANCE": {"subcommand": "exec", "native_cmds": ["lumetri.setLook", "effects.setParam"]},
    "CMD_COLOR_APPLY_HSL_QUALIFIER": {"subcommand": "exec", "native_cmds": ["masks.add", "masks.set", "effects.setParam"]},
    "CMD_COLOR_SHAPE_TONAL_CURVES": {"subcommand": "exec", "native_cmds": ["effects.setParam"]},
    "CMD_COLOR_MATCH_TO_REFERENCE": {"subcommand": "exec", "native_cmds": ["scopes.read", "lumetri.applyPreset"]},
    "CMD_COLOR_APPLY_FILM_LOOK_AND_FX": {"subcommand": "exec", "native_cmds": ["lut.import", "lumetri.setInputLut", "lumetri.applyPreset"]},
    "CMD_COLOR_VALIDATE_GRADE_LEGAL_RANGE": {"subcommand": "exec", "native_cmds": ["scopes.read"]},
    "CMD_COLOR_EMIT_GRADE_SPEC": {"subcommand": "exec", "native_cmds": ["lumetri.presets", "lut.export"]},

    # Cluster 05: Subtitling & Captioning (507-514)
    "CMD_SUB_SEGMENT_CUES": {"subcommand": "exec", "native_cmds": ["captions.newTrack", "captions.add"]},
    "CMD_SUB_CALCULATE_METRICS": {"subcommand": "exec", "native_cmds": ["captions.setStyle", "transcript.inspect"]},
    "CMD_SUB_CONDENSE_HIGH_CPS_TEXT": {"subcommand": "exec", "native_cmds": ["graphics.setText", "captions.setStyle"]},
    "CMD_SUB_SNAP_TO_SHOT_CHANGES": {"subcommand": "exec", "native_cmds": ["playhead.step", "captions.add"]},
    "CMD_SUB_INJECT_SDH_AND_FN_TAGS": {"subcommand": "exec", "native_cmds": ["captions.setStyle", "captions.add"]},
    "CMD_SUB_ENFORCE_STANDARD": {"subcommand": "exec", "native_cmds": ["captions.setStyle"]},
    "CMD_SUB_GENERATE_FORMAT": {"subcommand": "exec", "native_cmds": ["captions.setStyle", "export.presets.get"]},
    "CMD_SUB_EMIT_COMPLIANCE_REPORT": {"subcommand": "exec", "native_cmds": ["captions.setStyle"]},

    # Cluster 04: Sound Design & Mixing (515-522)
    "CMD_SOUND_CLEAN_AND_LEVEL_DIALOGUE": {"subcommand": "exec", "native_cmds": ["essentialSound.inspect", "essentialSound.setType", "essentialSound.set"]},
    "CMD_SOUND_SYNTHESIZE_ROOM_TONE_FILLS": {"subcommand": "exec", "native_cmds": ["timeline.place", "trim.applyDefaultTransition"]},
    "CMD_SOUND_SPOT_FOLEY_AND_HARD_SFX": {"subcommand": "exec", "native_cmds": ["timeline.place", "clipMixer.set"]},
    "CMD_SOUND_LAYER_AMBIENCE_AND_REVERB": {"subcommand": "exec", "native_cmds": ["mixer.addSubmix", "mixer.setValue", "effects.apply"]},
    "CMD_SOUND_ALIGN_MUSIC_AND_DUCKING": {"subcommand": "exec", "native_cmds": ["essentialSound.set", "mixer.setValue"]},
    "CMD_SOUND_CALIBRATE_LUFS_AND_TRUE_PEAK": {"subcommand": "exec", "native_cmds": ["mixer.inspect", "mixer.setValue"]},
    "CMD_SOUND_VERIFY_DME_STEM_PARITY": {"subcommand": "exec", "native_cmds": ["mixer.inspect"]},
    "CMD_SOUND_EMIT_MIX_SPEC": {"subcommand": "exec", "native_cmds": ["mixer.inspect", "export.presets.save"]},

    # Cluster 06: VFX & Conforming (523-524)
    "CMD_VFX_RELINK_AND_CONFORM_RAW": {"subcommand": "exec", "native_cmds": ["media.relink", "media.linkMedia"]},
    "CMD_VFX_GENERATE_EXR_PULL_SHEET": {"subcommand": "exec", "native_cmds": ["export.presets.list", "render"]},

    # Cluster 07: Finishing & QC (525-529)
    "CMD_FINISH_CONFIGURE_MASTER_CODEC": {"subcommand": "exec", "native_cmds": ["export.presets.save", "export.presets.list"]},
    "CMD_FINISH_ASSEMBLE_LEADERS_AND_2POP": {"subcommand": "exec", "native_cmds": ["project.matteColor", "timeline.place", "audio.voiceover.sync"]},
    "CMD_FINISH_RUN_AUTOMATED_QC_GATES": {"subcommand": "exec", "native_cmds": ["scopes.read", "mixer.inspect", "perf.stats"]},
    "CMD_FINISH_PACKAGE_IMF_OR_DCP": {"subcommand": "exec", "native_cmds": ["export.presets.get", "jobs.list"]},
    "CMD_FINISH_EMIT_DELIVERY_SPEC": {"subcommand": "exec", "native_cmds": ["export.presets.list", "help.systemReport"]}
}


def is_live_app_running(host=DEFAULT_BRIDGE_HOST, port=DEFAULT_BRIDGE_PORT):
    """Check if FilmCraft GUI is running and listening on the bridge port."""
    try:
        s = socket.create_connection((host, port), timeout=0.5)
        s.close()
        return True
    except (socket.error, ConnectionRefusedError):
        return False


def run_cli_command(args, use_bridge=True, host=DEFAULT_BRIDGE_HOST, port=DEFAULT_BRIDGE_PORT, project=None):
    """Run a filmcraft-cli command, optionally bridging to the live app."""
    cmd = [CLI_PATH]
    if use_bridge and is_live_app_running(host, port):
        cmd.extend(["--bridge", f"{host}:{port}"])
    elif project:
        cmd.extend(["--project", project])

    cmd.extend(args)
    proc = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
        "command": " ".join(cmd)
    }


def execute_native_command(cmd_id, params=None, host=DEFAULT_BRIDGE_HOST, port=DEFAULT_BRIDGE_PORT, project=None):
    """Execute a single native FilmCraft command by ID."""
    args = ["exec", cmd_id]
    if params:
        if isinstance(params, dict):
            args.append(json.dumps(params))
        elif isinstance(params, str):
            args.append(params)
    return run_cli_command(args, use_bridge=True, host=host, port=port, project=project)


def inspect_target(target="both", host=DEFAULT_BRIDGE_HOST, port=DEFAULT_BRIDGE_PORT, project=None):
    """Inspect project tree, sequence, or both."""
    args = ["inspect"]
    if target in ["project", "sequence"]:
        args.append(target)
    return run_cli_command(args, use_bridge=True, host=host, port=port, project=project)


def route_skill_command(skill_cmd_name, params=None, host=DEFAULT_BRIDGE_HOST, port=DEFAULT_BRIDGE_PORT, project=None):
    """
    Route an Autonomous Post-Production Monorepo Skill Master Command
    to the corresponding native FilmCraft CLI execution.
    """
    if skill_cmd_name not in SKILL_TO_FILMCRAFT_MAP:
        return {
            "status": "error",
            "message": f"Unknown Skill Master Command: '{skill_cmd_name}'. Available: {list(SKILL_TO_FILMCRAFT_MAP.keys())}"
        }

    mapping = SKILL_TO_FILMCRAFT_MAP[skill_cmd_name]
    subcmd = mapping["subcommand"]
    native_cmds = mapping["native_cmds"]

    results = []
    if subcmd == "inspect":
        res = inspect_target(host=host, port=port, project=project)
        results.append(res)
    elif subcmd == "exec":
        # Execute each native command in sequence
        for nc in native_cmds:
            res = execute_native_command(nc, params=params, host=host, port=port, project=project)
            results.append(res)
    elif subcmd == "probe":
        media_path = params.get("media_path") if isinstance(params, dict) else str(params)
        res = run_cli_command(["probe", media_path], use_bridge=True, host=host, port=port, project=project)
        results.append(res)

    success = all(r["returncode"] == 0 for r in results)
    return {
        "status": "pass" if success else "fail",
        "skill_command": skill_cmd_name,
        "native_commands_executed": native_cmds,
        "results": results
    }


def list_filmcraft_commands(filter_query=None):
    """Return all 701 commands from filmcraft-cli."""
    res = run_cli_command(["commands", "--json"])
    if res["returncode"] != 0:
        return []
    try:
        data = json.loads(res["stdout"])
        if filter_query:
            q = filter_query.lower()
            return [c for c in data if q in c["id"].lower() or q in c.get("label", "").lower()]
        return data
    except Exception as e:
        return []


def main():
    parser = argparse.ArgumentParser(description="FilmCraft CLI & Skill Bridge Layer")
    subparsers = parser.add_subparsers(dest="action", help="Action to execute")

    # exec subcommand
    exec_parser = subparsers.add_parser("exec", help="Execute native FilmCraft command")
    exec_parser.add_argument("cmd_id", help="Native command ID (e.g. timeline.razor)")
    exec_parser.add_argument("params", nargs="?", default=None, help="JSON params or key=value string")

    # route subcommand
    route_parser = subparsers.add_parser("route", help="Route Skill Master Command to FilmCraft")
    route_parser.add_argument("skill_cmd", help="Skill Master Command (e.g. CMD_EDIT_REFINE_ROUGH_TO_FINE_CUT)")
    route_parser.add_argument("params", nargs="?", default="{}", help="JSON params dictionary")

    # inspect subcommand
    insp_parser = subparsers.add_parser("inspect", help="Inspect project or sequence")
    insp_parser.add_argument("target", nargs="?", default="both", choices=["project", "sequence", "both"])

    # list subcommand
    list_parser = subparsers.add_parser("list", help="List native FilmCraft commands")
    list_parser.add_argument("filter", nargs="?", default=None, help="Filter query")

    # status subcommand
    subparsers.add_parser("status", help="Check live GUI connection and CLI status")

    args = parser.parse_args()

    if args.action == "status":
        live = is_live_app_running()
        print(f"FilmCraft CLI binary: {CLI_PATH} (exists: {os.path.exists(CLI_PATH)})")
        print(f"FilmCraft Live GUI on 127.0.0.1:{DEFAULT_BRIDGE_PORT}: {'ONLINE' if live else 'OFFLINE (Headless mode active)'}")
    elif args.action == "exec":
        p = json.loads(args.params) if args.params and args.params.startswith("{") else args.params
        res = execute_native_command(args.cmd_id, p)
        print(res["stdout"] if res["returncode"] == 0 else f"ERROR: {res['stderr']}")
    elif args.action == "route":
        p = json.loads(args.params) if args.params else {}
        res = route_skill_command(args.skill_cmd, p)
        print(json.dumps(res, indent=2))
    elif args.action == "inspect":
        res = inspect_target(args.target)
        print(res["stdout"] if res["returncode"] == 0 else f"ERROR: {res['stderr']}")
    elif args.action == "list":
        cmds = list_filmcraft_commands(args.filter)
        print(f"Found {len(cmds)} commands:")
        for c in cmds[:50]:
            print(f"  {c['id']} ({c.get('label', '')}) - params: {c.get('params', '{}')}")
        if len(cmds) > 50:
            print(f"  ... and {len(cmds) - 50} more.")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
