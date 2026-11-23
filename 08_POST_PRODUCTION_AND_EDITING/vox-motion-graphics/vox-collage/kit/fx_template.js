/* Vox Collage animation template (by Kayo, @learnwithkayo).
   Premium mixed-media paper collage, 15 s, five scenes, one "voxcollage" special.
   Text and colours come from comp/config.json; images come from comp/img with fixed names:
     paper.jpg sky.jpg hero.png lm1.png..lm5.png strip1.jpg..strip5.jpg
     ornament.png vehicle.png band.png mover.png hands.png reach.png
   The layout is designed on a 1080x1080 stage. Other canvas sizes centre the stage and
   extend the backgrounds. Motion is smooth and eased; randomness only comes from fr(). */
(function () {
  const S0 = 1080, CX = 540, CY = 540;
  const IM = {};
  const NAMES = {
    paper: "paper.jpg", sky: "sky.jpg", hero: "hero.png", ornament: "ornament.png", vehicle: "vehicle.png",
    lm1: "lm1.png", lm2: "lm2.png", lm3: "lm3.png", lm4: "lm4.png", lm5: "lm5.png",
    band: "band.png", mover: "mover.png", hands: "hands.png", reach: "reach.png",
    strip1: "strip1.jpg", strip2: "strip2.jpg", strip3: "strip3.jpg", strip4: "strip4.jpg", strip5: "strip5.jpg",
  };
  let C = {
    title: "TITLE", heroCaption: "", coords: "", skyCaption: "", skylineCaption: "",
    edgeLeft: "", edgeRight: "", corner1: "", corner2: "", poster: ["", ""],
    colors: { ink: "#121212", disc: "#efbd2b", poster: "#2552b8", cream: "#f3efe7" },
    heroTip: 0.5, moverBW: true, moverFlip: false,
  };
  RRC.hook("init", async () => {
    try { const r = await fetch("/comp/config.json"); if (r.ok) { const j = await r.json(); C = Object.assign(C, j); C.colors = Object.assign({ ink: "#121212", disc: "#efbd2b", poster: "#2552b8", cream: "#f3efe7" }, j.colors || {}); } } catch (e) {}
    await Promise.all(Object.entries(NAMES).map(async ([k, f]) => {
      try { const im = new Image(); im.src = "/comp/img/" + f; await im.decode(); IM[k] = im; } catch (e) { /* optional image missing */ }
    }));
  });
  const col = (k) => C.colors[k];

  const cl = (v, a = 0, b = 1) => Math.max(a, Math.min(b, v));
  const L = (a, b, t) => a + (b - a) * t;
  const P = (t, a, b) => cl((t - a) / (b - a));
  const E = {
    o3: (t) => 1 - Math.pow(1 - t, 3),
    o4: (t) => 1 - Math.pow(1 - t, 4),
    i3: (t) => t * t * t,
    io3: (t) => (t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2),
    oB: (t, s = 1.4) => { if (t <= 0) return 0; if (t >= 1) return 1; const c = s + 1; return 1 + c * Math.pow(t - 1, 3) + s * Math.pow(t - 1, 2); },
  };
  const fr = (n) => { const s = Math.sin(n * 127.1 + 311.7) * 43758.5453; return s - Math.floor(s); };

  // canvas <-> stage
  let CW = S0, CH = S0, SC = 1, OX = 0, OY = 0, VIEW = { x0: 0, y0: 0, w: S0, h: S0 };
  function layout(w, h) {
    // tall frames (9:16) keep the stage on the bottom edge so ground, hands and towers stay grounded
    CW = w; CH = h; SC = Math.min(w, h) / S0; OX = (w - S0 * SC) / 2; OY = h / w > 1.4 ? h - S0 * SC : (h - S0 * SC) / 2;
    VIEW = { x0: -OX / SC, y0: -OY / SC, w: w / SC, h: h / SC };
  }

  function shadow(x, b = 16, dx = 5, dy = 9, a = 0.3) {
    const m = x.getTransform(), k = Math.hypot(m.a, m.b);
    x.shadowColor = `rgba(20,16,10,${a})`; x.shadowBlur = b * k; x.shadowOffsetX = dx * k; x.shadowOffsetY = dy * k;
  }
  function noShadow(x) { x.shadowColor = "transparent"; x.shadowBlur = 0; x.shadowOffsetX = 0; x.shadowOffsetY = 0; }
  function poly(x, pts) { x.beginPath(); pts.forEach((p, i) => (i ? x.lineTo(p[0], p[1]) : x.moveTo(p[0], p[1]))); x.closePath(); }
  function jag(a0, a1, c, seed, amp, step, vert) {
    const n = Math.max(2, Math.round(Math.abs(a1 - a0) / step)), pts = [];
    for (let i = 0; i <= n; i++) {
      const a = L(a0, a1, i / n), j = (fr(seed + i * 2.17) - 0.5) * 2 * amp + (fr(seed + i * 9.3) - 0.5) * amp * 0.5;
      pts.push(vert ? [c + j, a] : [a, c + j]);
    }
    return pts;
  }
  const TP = {};
  function torn(w, h, seed, amp = 4, step = 10) {
    const key = [Math.round(w), Math.round(h), seed, amp, step].join(",");
    if (TP[key]) return TP[key];
    const pts = [];
    const edge = (x0, y0, x1, y1, s) => {
      const len = Math.hypot(x1 - x0, y1 - y0), n = Math.max(2, Math.round(len / step)), nx = -(y1 - y0) / len, ny = (x1 - x0) / len;
      for (let i = 0; i < n; i++) { const u = i / n, j = (fr(s + i * 1.731) - 0.5) * 2 * amp; pts.push([L(x0, x1, u) + nx * j, L(y0, y1, u) + ny * j]); }
    };
    edge(-w / 2, -h / 2, w / 2, -h / 2, seed); edge(w / 2, -h / 2, w / 2, h / 2, seed + 101);
    edge(w / 2, h / 2, -w / 2, h / 2, seed + 202); edge(-w / 2, h / 2, -w / 2, -h / 2, seed + 303);
    return (TP[key] = pts);
  }
  function cover(x, im, X, Y, w, h, crop = 0, fx = 0.5, fy = 0.5) {
    if (!im) return;
    const sw = im.naturalWidth * (1 - 2 * crop), sh = im.naturalHeight * (1 - 2 * crop);
    const s = Math.max(w / sw, h / sh), dw = sw * s, dh = sh * s;
    x.drawImage(im, im.naturalWidth * crop, im.naturalHeight * crop, sw, sh, X + (w - dw) * fx, Y + (h - dh) * fy, dw, dh);
  }
  function camera(x, k, tx = 0, ty = 0, rot = 0, ox = CX, oy = CY) {
    x.translate(ox + tx, oy + ty); if (rot) x.rotate(rot); x.scale(k, k); x.translate(-ox, -oy);
  }
  // cut-out by width (default) or by height (o.byH); o.maxW caps the width; (ax, ay) anchor
  function cut(x, im, cx, cy, size, o = {}) {
    if (!im) return;
    const ar = im.naturalWidth / im.naturalHeight;
    let w = o.byH ? size * ar : size, h = o.byH ? size : size / ar;
    if (o.maxW && w > o.maxW) { w = o.maxW; h = w / ar; }
    x.save(); x.translate(cx, cy); x.rotate(o.rot || 0);
    const s = o.s ?? 1; x.scale(s * (o.flip ? -1 : 1), s);
    if (o.a != null) x.globalAlpha *= cl(o.a);
    if (o.filter) x.filter = o.filter;
    shadow(x, o.sb ?? 18, o.sdx ?? 6, o.sdy ?? 10, o.sa ?? 0.32);
    x.drawImage(im, -w * (o.ax ?? 0.5), -h * (o.ay ?? 0.5), w, h);
    x.restore();
  }
  function paperBG(x, tint) {
    cover(x, IM.paper, VIEW.x0 - 30, VIEW.y0 - 30, VIEW.w + 60, VIEW.h + 60, 0.02);
    if (tint) { x.save(); x.globalCompositeOperation = "multiply"; x.fillStyle = tint; x.fillRect(VIEW.x0, VIEW.y0, VIEW.w, VIEW.h); x.restore(); }
  }
  function skyBG(x, dx, dy) { cover(x, IM.sky, VIEW.x0 - 80 + dx, VIEW.y0 - 80 + dy, VIEW.w + 160, VIEW.h + 160, 0.0); }

  function title(x, text, x0, base, maxSize, maxW, t0, t, o = {}) {
    x.save(); x.font = `100px Abril`;
    let tw = 0; for (const ch of text) tw += x.measureText(ch).width;
    const size = Math.min(maxSize, (100 * maxW) / Math.max(1, tw));
    x.font = `${size}px Abril`; x.textBaseline = "alphabetic"; x.textAlign = "left";
    let xx = x0;
    for (let i = 0; i < text.length; i++) {
      const ch = text[i], w = x.measureText(ch).width, u = t - (t0 + i * (o.step ?? 0.07));
      if (u > 0) {
        const a = E.oB(cl(u / 0.32), 1.3);
        x.save(); x.translate(xx + w / 2, base - (1 - a) * 70);
        x.rotate((1 - a) * (fr(i + 3) - 0.5) * 0.6); const s = L(1.25, 1, a); x.scale(s, s);
        x.globalAlpha *= cl(u / 0.07);
        shadow(x, 10, 2, 5, 0.2); x.fillStyle = o.color || col("ink"); x.fillText(ch, -w / 2, 0);
        x.restore();
      }
      xx += w;
    }
    x.restore();
  }
  function mono(x, text, x0, y0, size, prog, o = {}) {
    if (!text || prog <= 0) return;
    const n = Math.min(text.length, Math.floor(text.length * prog + 0.0001));
    x.save(); x.font = `${o.w || 500} ${size}px Plex`; x.letterSpacing = (o.ls ?? 2) + "px";
    x.fillStyle = o.color || col("ink"); x.textAlign = o.align || "left"; x.textBaseline = "alphabetic";
    if (o.align === "right") x.fillText(text.slice(text.length - n), x0, y0); else x.fillText(text.slice(0, n), x0, y0);
    x.restore();
  }
  function bird(x, cx, cy, s, ph, t) {
    const f = Math.sin(t * 15 + ph);
    x.save(); x.translate(cx, cy); x.scale(s, s); x.fillStyle = col("ink");
    x.beginPath(); x.moveTo(-1, -0.25 * f);
    x.quadraticCurveTo(-0.45, -0.55 * f - 0.12, 0, 0.12);
    x.quadraticCurveTo(0.45, -0.55 * f - 0.12, 1, -0.25 * f);
    x.quadraticCurveTo(0.45, -0.3 * f + 0.1, 0, 0.34);
    x.quadraticCurveTo(-0.45, -0.3 * f + 0.1, -1, -0.25 * f);
    x.fill(); x.restore();
  }
  function flock(x, t, t0, list) {
    const u = t - t0; if (u < 0) return;
    list.forEach(([x0, y0, vx, vy, s, ph]) => bird(x, x0 + vx * u, y0 + vy * u + Math.sin(u * 2 + ph) * 6, s, ph, t));
  }
  function bez(p0, c, p1, n) {
    const pts = [];
    for (let i = 0; i <= n; i++) { const u = i / n, a = 1 - u; pts.push([a * a * p0[0] + 2 * a * u * c[0] + u * u * p1[0], a * a * p0[1] + 2 * a * u * c[1] + u * u * p1[1]]); }
    return pts;
  }
  function along(pts, prog) {
    const segs = []; let tot = 0;
    for (let i = 1; i < pts.length; i++) { const d = Math.hypot(pts[i][0] - pts[i - 1][0], pts[i][1] - pts[i - 1][1]); segs.push(d); tot += d; }
    let rem = tot * cl(prog);
    for (let i = 1; i < pts.length; i++) {
      if (rem <= segs[i - 1] || i === pts.length - 1) {
        const f = cl(rem / segs[i - 1]);
        return { p: [L(pts[i - 1][0], pts[i][0], f), L(pts[i - 1][1], pts[i][1], f)], a: Math.atan2(pts[i][1] - pts[i - 1][1], pts[i][0] - pts[i - 1][0]), i };
      }
      rem -= segs[i - 1];
    }
    return { p: pts[0], a: 0, i: 1 };
  }
  function dashed(x, pts, prog, t) {
    if (prog <= 0) return;
    const end = along(pts, prog);
    x.save(); x.strokeStyle = col("ink"); x.globalAlpha *= 0.85; x.lineWidth = 3; x.lineCap = "round";
    x.setLineDash([14, 12]); x.lineDashOffset = -t * 40;
    x.beginPath(); x.moveTo(pts[0][0], pts[0][1]);
    for (let i = 1; i < end.i; i++) x.lineTo(pts[i][0], pts[i][1]);
    x.lineTo(end.p[0], end.p[1]); x.stroke(); x.restore();
  }
  // vehicle.png has its nose pointing LEFT; it follows the path and leaves a dashed trail
  function flight(x, pts, prog, t, size) {
    if (!IM.vehicle) return;
    dashed(x, pts, prog * 0.97, t);
    const at = along(pts, prog), flip = Math.cos(at.a) > 0;
    cut(x, IM.vehicle, at.p[0], at.p[1], size, { rot: flip ? at.a : at.a - Math.PI, flip, sa: 0.25, sb: 22, sdy: 22 });
  }
  function skyStrip(x, y, h, u, seed) {
    if (u <= 0) return;
    const off = (1 - E.o4(u)) * -(VIEW.w + 220);
    const xa = VIEW.x0 - 60, xb = VIEW.x0 + VIEW.w + 60;
    x.save(); x.translate(off, 0);
    const top = jag(xa, xb, y, seed, 10, 16, false), bot = jag(xb, xa, y + h, seed + 50, 10, 16, false);
    const right = jag(y, y + h, xb, seed + 90, 14, 14, true);
    const pts = [...top, ...right, ...bot];
    shadow(x, 16, 0, 7, 0.28); x.fillStyle = col("cream");
    poly(x, pts.map((p) => [p[0], p[1] + (p[1] < y + h / 2 ? -7 : 7)])); x.fill(); noShadow(x);
    x.save(); poly(x, pts); x.clip(); cover(x, IM.sky, xa, y - 60, xb - xa, h + 120, 0.05); x.restore();
    x.restore();
  }
  function tornFrame(x, seed) {
    const xa = VIEW.x0 - 60, xb = VIEW.x0 + VIEW.w + 60;
    for (const [y0, dir, s] of [[VIEW.y0, 1, seed], [VIEW.y0 + VIEW.h, -1, seed + 40]]) {
      for (let k = 0; k < 2; k++) {
        const depth = k ? 46 : 78;
        const line = jag(xa, xb, y0 + dir * depth, s + k * 17, k ? 16 : 22, k ? 34 : 46, false);
        x.save(); x.beginPath(); x.moveTo(xa, y0 - dir * 60);
        line.forEach((p) => x.lineTo(p[0], p[1])); x.lineTo(xb, y0 - dir * 60); x.closePath();
        shadow(x, 14, 0, dir * 6, 0.22); x.fillStyle = k ? "#fbf8f1" : "#e9e4d8"; x.fill(); x.restore();
      }
    }
  }
  function disc(x, cx, cy, r, c) {
    if (r <= 0) return;
    x.save(); shadow(x, 20, 0, 10, 0.18); x.fillStyle = c; x.beginPath(); x.arc(cx, cy, r, 0, Math.PI * 2); x.fill(); noShadow(x);
    x.clip(); x.globalCompositeOperation = "multiply"; x.globalAlpha = 0.45; cover(x, IM.paper, cx - r, cy - r, r * 2, r * 2, 0.05);
    x.restore();
  }
  function band(x, yTop, w, t, o = {}) {
    const im = IM.band; if (!im) return;
    const h = (w * im.naturalHeight) / im.naturalWidth;
    const dx = Math.sin(t * (o.sp ?? 1.3) + (o.ph || 0)) * (o.amp ?? 26);
    x.save(); x.translate(CX + dx + (o.ox || 0), yTop + Math.sin(t * 2.1 + (o.ph || 0)) * 5);
    x.scale(o.flip ? -1 : 1, 1);
    shadow(x, 16, 0, -4, 0.22); x.drawImage(im, -w / 2, 0, w, h); x.restore();
  }
  const CACHE = {};
  function mkC(w, h) { const c = document.createElement("canvas"); c.width = Math.max(1, Math.ceil(w)); c.height = Math.max(1, Math.ceil(h)); return [c, c.getContext("2d")]; }
  function posterC(lines, size) {
    const key = lines.join("|") + size;
    if (CACHE[key]) return CACHE[key];
    const SS = 2, font = `${size}px Anton`;
    const [m, mg] = mkC(10, 10); mg.font = font;
    const lh = size * 0.98, tw = Math.max(...lines.map((s) => mg.measureText(s).width));
    const pw = tw + size * 0.7, ph = lh * lines.length + size * 0.55, M = 20;
    const [c, g] = mkC((pw + M * 2) * SS, (ph + M * 2) * SS);
    g.scale(SS, SS); g.translate(pw / 2 + M, ph / 2 + M);
    const pts = torn(pw, ph, 77, 2.2, 9);
    g.save(); poly(g, pts); g.clip();
    g.fillStyle = col("poster"); g.fillRect(-pw / 2, -ph / 2, pw, ph);
    g.globalCompositeOperation = "multiply"; g.globalAlpha = 0.6; cover(g, IM.paper, -pw / 2, -ph / 2, pw, ph, 0.1); g.globalAlpha = 1;
    g.globalCompositeOperation = "source-over";
    const gr = g.createLinearGradient(-pw / 2, 0, pw / 2, 0);
    gr.addColorStop(0.47, "rgba(255,255,255,0)"); gr.addColorStop(0.5, "rgba(255,255,255,0.16)"); gr.addColorStop(0.53, "rgba(0,0,0,0.12)"); gr.addColorStop(0.6, "rgba(0,0,0,0)");
    g.fillStyle = gr; g.fillRect(-pw / 2, -ph / 2, pw, ph);
    g.fillStyle = "#f4f1ea"; g.font = font; g.textAlign = "left"; g.textBaseline = "alphabetic";
    lines.forEach((s, i) => g.fillText(s, -pw / 2 + size * 0.35, -ph / 2 + size * 0.3 + lh * (i + 1) - size * 0.1));
    g.restore();
    return (CACHE[key] = { c, w: pw + M * 2, h: ph + M * 2 });
  }
  function poster(x, lines, size, cx, cy, rot, u) {
    lines = (lines || []).filter((s) => s);
    if (u <= 0 || !lines.length) return;
    const P0 = posterC(lines, size), a = E.oB(cl(u / 0.3), 1.3), s = L(1.35, 1, a);
    const fit = Math.min(1, 420 / P0.w);
    x.save(); x.translate(cx, cy); x.rotate(rot + (1 - a) * 0.2); x.scale(s * fit, s * fit); x.globalAlpha *= cl(u / 0.06);
    shadow(x, 16 + 20 * (1 - a), 5, 10 + 16 * (1 - a), 0.32); x.drawImage(P0.c, -P0.w / 2, -P0.h / 2, P0.w, P0.h); x.restore();
  }
  function rise(x, im, cx, baseY, h, maxW, t, t0, o = {}) {
    if (!im) return;
    const u = t - t0; if (u <= 0) return;
    const ar = im.naturalWidth / im.naturalHeight;
    h = Math.min(h, maxW / ar);
    const a = E.oB(cl(u / (o.d ?? 0.5)), o.over ?? 1.15);
    const y = L(baseY + h + 80, baseY, a);
    cut(x, im, cx, y + Math.sin(t * 1.6 + (o.ph || 0)) * 2, h, { byH: true, ax: 0.5, ay: 1, rot: (1 - a) * (o.tilt ?? 0.06), sa: 0.3 });
  }

  // ---------- A: hero rises on paper, title, torn sky strip (0.00 - 3.15) ----------
  function sA(x, t) {
    paperBG(x);
    x.save(); camera(x, 1.0 + 0.06 * E.io3(P(t, 0, 3.15)), 0, 10 * P(t, 0, 3.15));
    const us = E.o4(P(t, 0.1, 1.15));
    if (us > 0) cut(x, IM.ornament, L(860, 790, us), L(700, 300, us), 450, { rot: t * 0.1 - 0.5 * (1 - us), s: L(0.55, 1, us), sa: 0.22 });
    title(x, C.title || "", 54, 250, 168, 600, 0.85, t, { step: 0.07 });
    skyStrip(x, 520, 225, P(t, 1.3, 1.9), 61);
    flock(x, t, 1.5, [[-60, 600, 260, -18, 22, 0.3], [-150, 645, 280, -22, 17, 1.7], [-30, 670, 240, -12, 15, 2.9], [-230, 610, 290, -25, 19, 4.1], [-340, 655, 270, -10, 14, 5.3]]);
    if (IM.hero) {
      const ub = E.o4(P(t, 0, 1.35)), ar = IM.hero.naturalWidth / IM.hero.naturalHeight;
      const hh = Math.min(1260, 600 / ar);
      const top = L(430, 46, ub) - 22 * P(t, 1.35, 3.15);
      cut(x, IM.hero, L(800, 712, ub), top, hh, { byH: true, ax: C.heroTip ?? 0.5, ay: 0, rot: L(0.2, 0, ub), sa: 0.3, sb: 22 });
    }
    x.restore();
    mono(x, C.heroCaption, 54, 998, 26, P(t, 1.85, 2.4));
    mono(x, C.coords, 54, 1036, 26, P(t, 2.1, 2.7));
  }
  // ---------- B: into the sky, vehicle with a dashed path (2.95 - 5.25) ----------
  const TB = 2.95;
  const PATH_B = bez([1420, 860], [520, 330], [-460, 300], 80);
  function sB(x, t) {
    const lt = t - TB;
    skyBG(x, -lt * 22, lt * 6);
    x.save(); camera(x, 1.04 + 0.05 * P(lt, 0, 2.3));
    cut(x, IM.ornament, 930, 190, 470, { rot: t * 0.1, sa: 0.2 });
    flock(x, t, TB, [[1150, 300, -160, 8, 11, 0.5], [1220, 340, -170, 4, 9, 2.1], [1300, 280, -150, 10, 10, 3.3]]);
    flight(x, PATH_B, E.io3(P(lt, 0.05, 2.25)) * 0.85 + 0.15 * P(lt, 0.05, 2.25), t, 760);
    x.restore();
    tornFrame(x, 31);
    mono(x, C.skyCaption, 58, 1004, 24, P(lt, 0.5, 1.0), { color: "#1d1d1d" });
  }
  // ---------- C: the skyline builds itself over a disc (4.95 - 8.60) ----------
  const TC = 4.95;
  function sC(x, t) {
    const lt = t - TC;
    paperBG(x);
    x.save(); camera(x, 1.0 + 0.06 * E.io3(P(lt, 0, 3.65)), 0, 0);
    disc(x, 540, 540, 330 * E.oB(P(lt, 0.12, 0.62), 1.25), col("disc"));
    const base = 925;
    rise(x, IM.lm1, 150, base, 470, 260, lt, 0.62, { ph: 1 });
    rise(x, IM.hero, 560, base, 930, 340, lt, 0.3, { ph: 2, d: 0.6, over: 1.1 });
    rise(x, IM.lm2, 345, base, 690, 230, lt, 0.46, { ph: 3 });
    rise(x, IM.lm3, 790, base, 640, 300, lt, 0.54, { ph: 4 });
    rise(x, IM.lm4, 950, base, 560, 300, lt, 0.7, { ph: 5 });
    rise(x, IM.lm5, 300, base + 20, 300, 450, lt, 0.82, { ph: 6, tilt: 0.12 });
    if (lt > 1.2) flight(x, bez([-260, 260], [540, 90], [1320, 220], 70), E.io3(P(lt, 1.2, 3.6)), t, 300);
    const uw = E.o4(P(lt, 0.5, 1.0));
    band(x, L(1150, 860, uw), 1500, t, { flip: true, ox: 60, ph: 1.3, amp: 30 });
    const ud = P(lt, 1.15, 3.65);
    if (ud > 0 && IM.mover) cut(x, IM.mover, L(-260, 1260, ud), 905 + Math.sin(t * 3) * 7, 300, { rot: Math.sin(t * 2.6) * 0.05, flip: !!C.moverFlip, filter: C.moverBW ? "grayscale(1) contrast(1.15)" : "none", sa: 0.25 });
    band(x, L(1250, 925, uw), 1500, t, { ph: 0, amp: 24, sp: 1.6 });
    x.restore();
    mono(x, C.skylineCaption, 1022, 62, 24, P(lt, 0.9, 1.4), { align: "right" });
  }
  // ---------- D: hands, camera, photo strips fan out of the lens (8.40 - 11.25) ----------
  const TD = 8.4;
  const FAN = ["strip1", "strip2", "strip3", "strip4", "strip5"];
  function sD(x, t) {
    const lt = t - TD;
    paperBG(x, "rgba(255,238,210,0.55)");
    x.save(); camera(x, 1.0 + 0.05 * E.io3(P(lt, 0, 2.85)), 0, 0);
    const uh = E.o4(P(lt, 0, 0.5));
    const hw = 620, har = IM.hands ? IM.hands.naturalHeight / IM.hands.naturalWidth : 0.76, hh = hw * har;
    const hx = 540, hy = L(1080 + hh, 1080 + 40, uh);
    const ox = hx + ((C.lensX ?? 0.479) - 0.5) * hw, oy = hy - hh + (C.lensY ?? 0.006) * hh + 6;
    const N = FAN.length, span = 2.2, a0 = -Math.PI / 2 - span / 2, st = span / N;
    const order = [2, 1, 3, 0, 4];
    for (let i = 0; i < N; i++) {
      const u = lt - (0.42 + order[i] * 0.09); if (u <= 0 || !IM[FAN[i]]) continue;
      const g = E.o4(cl(u / 0.5)), R = 40 + 1500 * g;
      const aA = a0 + i * st, aB = aA + st;
      const pts = [[ox, oy], [ox + Math.cos(aA) * R, oy + Math.sin(aA) * R], [ox + Math.cos(aB) * R, oy + Math.sin(aB) * R]];
      x.save(); poly(x, pts); x.clip();
      const mid = (aA + aB) / 2, d = Math.min(R, 700) * 0.62, ccx = ox + Math.cos(mid) * d, ccy = oy + Math.sin(mid) * d;
      cover(x, IM[FAN[i]], ccx - 410, ccy - 730, 820, 1460, 0);
      x.restore();
      x.save(); x.strokeStyle = col("cream"); x.lineWidth = 10; x.lineJoin = "round"; poly(x, pts); x.stroke(); x.restore();
    }
    const ue = P(lt, 1.05, 1.9);
    if (ue > 0) {
      const edgeText = (ang, text) => {
        if (!text) return;
        x.save(); x.translate(ox, oy);
        const flipT = Math.cos(ang) < 0;
        x.rotate(flipT ? ang + Math.PI : ang);
        x.font = "500 22px Plex"; x.letterSpacing = "3px"; x.fillStyle = col("ink"); x.textBaseline = "middle"; x.textAlign = "left";
        const s = text.slice(0, Math.floor(text.length * ue));
        if (flipT) x.fillText(s, -575, 22); else x.fillText(s, 140, 22);
        x.restore();
      };
      edgeText(a0, C.edgeLeft);
      edgeText(a0 + span, C.edgeRight);
    }
    cut(x, IM.hands, hx, hy, hw, { ax: 0.5, ay: 1, sa: 0.35, sb: 24 });
    x.restore();
    mono(x, C.corner1, 46, 1006, 22, P(lt, 0.8, 1.2));
    mono(x, C.corner2, 46, 1038, 22, P(lt, 1.0, 1.45));
  }
  // ---------- E: hero collage on sky (11.20 - 15.00) ----------
  const TE = 11.2;
  function sE(x, t) {
    const lt = t - TE;
    skyBG(x, 30 - lt * 9, -10);
    x.save(); x.globalCompositeOperation = "multiply"; x.globalAlpha = 0.35; cover(x, IM.paper, VIEW.x0, VIEW.y0, VIEW.w, VIEW.h, 0.02); x.restore();
    x.save(); camera(x, 1.0 + 0.08 * E.io3(P(lt, 0, 3.8)), 0, 0, 0, 560, 520);
    const us = E.oB(P(lt, 0.05, 0.55), 1.2);
    if (us > 0) cut(x, IM.ornament, 870, 235, 430, { rot: t * 0.1, s: L(0.4, 1, us), sa: 0.22 });
    if (lt > 0.55) flight(x, bez([-280, 520], [520, 300], [1330, 330], 70), E.io3(P(lt, 0.55, 3.7)), t, 330);
    const base = 980;
    rise(x, IM.lm2, 330, base, 640, 230, lt, 0.12, { ph: 3, d: 0.45 });
    rise(x, IM.lm3, 760, base, 560, 300, lt, 0.2, { ph: 4, d: 0.45 });
    rise(x, IM.hero, 560, base + 30, 1010, 380, lt, 0.0, { ph: 2, d: 0.55, over: 1.08 });
    rise(x, IM.lm4, 935, base, 520, 300, lt, 0.28, { ph: 5, d: 0.45 });
    rise(x, IM.lm5, 190, base + 10, 290, 420, lt, 0.36, { ph: 6, d: 0.45, tilt: 0.12 });
    const ur = E.o4(P(lt, 0.75, 1.55));
    if (ur > 0) cut(x, IM.reach, L(-420, 150, ur), L(-280, 130, ur), 620, { rot: 0.42, sa: 0.3 });
    poster(x, C.poster, 92, 205, 520, -0.11, lt - 0.95);
    flock(x, t, TE + 1.2, [[-80, 420, 150, -10, 12, 0.2], [-160, 450, 160, -14, 9, 1.4], [-40, 470, 140, -6, 10, 2.6]]);
    band(x, L(1250, 905, E.o4(P(lt, 0.3, 0.8))), 1500, t, { ph: 0.7, amp: 26, sp: 1.5 });
    x.restore();
  }

  // ---------- transitions (canvas space) ----------
  let OA = null, OAX, OB, OBX;
  function offs(PX) {
    const pw = Math.round(CW * PX), ph = Math.round(CH * PX);
    if (!OA || OA.width !== pw || OA.height !== ph) { [OA, OAX] = mkC(pw, ph); [OB, OBX] = mkC(pw, ph); }
    for (const g of [OAX, OBX]) { g.setTransform(PX, 0, 0, PX, 0, 0); g.globalAlpha = 1; g.globalCompositeOperation = "source-over"; g.filter = "none"; g.clearRect(0, 0, CW, CH); noShadow(g); }
  }
  function run(x, fn, t) { x.save(); x.translate(OX, OY); x.scale(SC, SC); fn(x, t); x.restore(); }
  function pushInto(x, t, from, to, ta, tb, sx, sy) {
    const u = P(t, ta, tb), e = E.i3(u), fx = OX + sx * SC, fy = OY + sy * SC;
    run(x, to, t); run(OAX, from, t);
    const k = L(1, 5.5, e), a = 1 - P(u, 0.55, 1);
    for (let i = 3; i >= 0; i--) {
      const kk = k * (1 - 0.035 * i * e);
      x.save(); x.globalAlpha = a * (i ? 0.28 : 1); x.translate(fx, fy); x.scale(kk, kk); x.translate(-fx, -fy); x.drawImage(OA, 0, 0, CW, CH); x.restore();
    }
  }
  function ripH(x, t, from, to, ta, tb) {
    run(x, to, t); run(OAX, from, t);
    const u = E.io3(P(t, ta, tb)), d = u * CH * 0.6, ym = CH * 0.49;
    const line = jag(-60, CW + 60, ym, 707, 26, 30, false);
    [-1, 1].forEach((side) => {
      const pts = side < 0 ? [[-60, -60], [CW + 60, -60], ...line.slice().reverse()] : [...line, [CW + 60, CH + 60], [-60, CH + 60]];
      x.save(); x.translate(0, side * d); x.rotate(side * 0.035 * u);
      shadow(x, 26, 0, side * 10, 0.4); x.fillStyle = col("cream"); poly(x, pts); x.fill(); noShadow(x);
      x.save(); poly(x, pts.map((p) => (Math.abs(p[1] - ym) < 60 ? [p[0], p[1] + side * 9] : p))); x.clip(); x.drawImage(OA, 0, 0, CW, CH); x.restore();
      x.restore();
    });
  }
  function sheetIn(x, t, from, to, ta, tb) {
    const u = E.o4(P(t, ta, tb));
    x.save(); x.translate(-u * 260 * SC, 0); run(x, from, t); x.restore();
    run(OBX, to, t);
    const off = L(CW + 80, 0, u);
    const edge = jag(-60, CH + 60, 0, 811, 14, 26, true);
    const pts = [...edge, [CW + 300, CH + 60], [CW + 300, -60]];
    x.save(); x.translate(off, 0);
    shadow(x, 30, -12, 0, 0.42); x.fillStyle = col("cream"); poly(x, pts); x.fill(); noShadow(x);
    x.save(); poly(x, pts.map((p) => (p[0] < 60 ? [p[0] + 10, p[1]] : p))); x.clip(); x.drawImage(OB, -off, 0, CW, CH); x.restore();
    x.restore();
  }
  function post(x, t) {
    x.save();
    x.globalCompositeOperation = "multiply"; x.globalAlpha = 0.22; cover(x, IM.paper, 0, 0, CW, CH, 0.05);
    x.globalCompositeOperation = "source-over"; x.globalAlpha = 1;
    const R = Math.max(CW, CH);
    const vg = x.createRadialGradient(CW / 2, CH / 2, R * 0.42, CW / 2, CH / 2, R * 0.82);
    vg.addColorStop(0, "rgba(15,12,8,0)"); vg.addColorStop(1, "rgba(15,12,8,0.26)");
    x.fillStyle = vg; x.fillRect(0, 0, CW, CH);
    const f = t >= 11.15 ? 1 - P(t, 11.15, 11.55) : 0;
    if (f > 0) { x.fillStyle = `rgba(255,253,248,${0.95 * E.o3(f)})`; x.fillRect(0, 0, CW, CH); }
    x.restore();
  }
  RRC.register("SPECIALS", "voxcollage", {
    allow: ["grain"],
    draw(S, p, x) {
      const t = S.t, PX = x.getTransform().a || 1;
      layout(S.W, S.H);
      offs(PX);
      x.save();
      x.fillStyle = "#e8e3da"; x.fillRect(0, 0, CW, CH);
      if (t < 2.75) run(x, sA, t);
      else if (t < 3.15) pushInto(x, t, sA, sB, 2.75, 3.15, 560, 632);
      else if (t < 4.95) run(x, sB, t);
      else if (t < 5.3) ripH(x, t, sB, sC, 4.95, 5.3);
      else if (t < 8.3) run(x, sC, t);
      else if (t < 8.62) sheetIn(x, t, sC, sD, 8.3, 8.62);
      else if (t < 11.2) run(x, sD, t);
      else run(x, sE, t);
      x.restore();
      post(x, t);
    },
  });
})();
