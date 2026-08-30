# -*- coding: utf-8 -*-
"""Faixa de stacks em linhas categorizadas. Logos reais (simple-icons), monocromatico,
auto-hospedado. Entradas sem logo disponivel caem para chip de texto."""
import os
from simpleicons.all import icons

OUT  = "."
MONO = "ui-monospace,'SF Mono','Cascadia Mono','DejaVu Sans Mono',Menlo,Consolas,monospace"

ROWS = [
    ("LANGUAGES", [("python","Python"), ("typescript","TypeScript"),
                   ("javascript","JavaScript"), ("openjdk","Java"), ("lua","Lua")]),
    ("BACKEND",   [("nodedotjs","Node.js"), ("spring","Spring"), ("docker","Docker"),
                   ("postman","Postman"), ("git","Git")]),
    ("FRONTEND",  [("react","React"), ("tailwindcss","Tailwind"),
                   ("html5","HTML5"), ("css3","CSS3")]),
    ("DATA",      [("oracle","Oracle"), ("postgresql","PostgreSQL"), ("mysql","MySQL")]),
    ("ORIGIN",    [(None,"ADVPL"), (None,"PROTHEUS")]),
]

W, X0, STEP, ICON, RH, TOP = 840, 172, 118, 28, 68, 40
H = TOP + len(ROWS) * RH + 10

def build(ink, mut):
    css, body, n = [], [], 0
    for r, (cat, items) in enumerate(ROWS):
        y = TOP + r * RH
        body.append('  <text class="cat" x="40" y="%d">%s</text>' % (y + ICON - 6, cat))
        for c, (slug, label) in enumerate(items):
            cx = X0 + c * STEP
            css.append("  .n%d { animation-delay: %.2fs; }" % (n, 0.06 * n))
            if slug:                               # logo + legenda abaixo
                g = ('    <path class="lg" transform="translate(%.1f,%d) scale(%.4f)" d="%s"/>\n'
                     '    <text class="cap" x="%.1f" y="%d" text-anchor="middle">%s</text>'
                     % (cx - ICON / 2, y, ICON / 24.0, icons[slug].path,
                        cx, y + ICON + 17, label))
            else:                                  # sem logo -> chip com o texto DENTRO
                w = 11 * len(label) + 22
                g = ('    <rect class="chip" x="%.1f" y="%d" width="%d" height="%d" rx="3"/>\n'
                     '    <text class="cap" x="%.1f" y="%.1f" text-anchor="middle">%s</text>'
                     % (cx - w / 2, y, w, ICON, cx, y + ICON / 2 + 3.5, label))
            body.append('  <g class="item n%d">\n%s\n  </g>' % (n, g))
            n += 1
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d" role="img" aria-label="Stack">
<style>
  .lg   { fill: %s; }
  .chip { fill: none; stroke: %s; stroke-width: 1; opacity: .45; }
  .cap  { fill: %s; font-family: %s; font-size: 9px; letter-spacing: 1.1px; }
  .cat  { fill: %s; font-family: %s; font-size: 10px; letter-spacing: 2.6px; opacity: .85; }
  .item { opacity: 0; animation: rise .5s cubic-bezier(.22,1,.36,1) forwards; }
%s
  @keyframes rise { from { opacity: 0; transform: translateY(6px); }
                    to   { opacity: 1; transform: translateY(0); } }
</style>
%s
</svg>
''' % (W, H, W, H, ink, ink, mut, MONO, mut, MONO, "\n".join(css), "\n".join(body))

for theme, ink, mut in [("light", "#0d1117", "#6e7781"), ("dark", "#e6edf3", "#8b949e")]:
    p = os.path.join(OUT, "stack-%s.svg" % theme)
    open(p, "w", encoding="utf-8").write(build(ink, mut))
    print("  stack-%-6s %6d bytes  (%dx%d)" % (theme, os.path.getsize(p), W, H))
