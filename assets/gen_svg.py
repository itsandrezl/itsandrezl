# -*- coding: utf-8 -*-
"""Header banner for André Felipe (Data Analyst & Data Engineer)."""
import os

OUT = "assets"
MONO = "ui-monospace,'SF Mono','Cascadia Mono','DejaVu Sans Mono',Menlo,Consolas,monospace"

HEADER = u'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 840 200" width="840" height="200" role="img" aria-label="André Felipe — Data Analyst &amp; Data Engineer">
<style>
  .ink   {{ fill: {ink}; }}
  .mut   {{ fill: {mut}; }}
  .strk  {{ stroke: {ink}; fill: none; }}
  .strkm {{ stroke: {mut}; fill: none; }}
  .name  {{ font-family: {mono}; font-size: 34px; letter-spacing: 6px; opacity: 0;
            animation: fade .8s ease-out .15s forwards; }}
  .sub   {{ font-family: {mono}; font-size: 12px; letter-spacing: 4.5px; opacity: 0;
            animation: fade .8s ease-out 1.25s forwards; }}
  .meta  {{ font-family: {mono}; font-size: 10px; letter-spacing: 2.5px; opacity: 0;
            animation: fade .8s ease-out 1.6s forwards; }}
  .rule  {{ stroke-width: 1.25; stroke-dasharray: 760; stroke-dashoffset: 760;
            animation: draw 1.5s cubic-bezier(.22,1,.36,1) .35s forwards; }}
  .tick  {{ stroke-width: 1; opacity: 0; animation: fade .6s ease-out 1.8s forwards; }}
  .cur   {{ opacity: 0; animation: show 0s linear 1.05s forwards, blink 1.15s steps(1) 1.05s infinite; }}
  .corner{{ stroke-width: 1.25; opacity: 0; animation: fade .7s ease-out 1.9s forwards; }}
  @keyframes fade  {{ to {{ opacity: 1; }} }}
  @keyframes show  {{ to {{ opacity: 1; }} }}
  @keyframes draw  {{ to {{ stroke-dashoffset: 0; }} }}
  @keyframes blink {{ 0%,49%{{opacity:1}} 50%,100%{{opacity:0}} }}
</style>

<!-- frame corners -->
<path class="strkm corner" d="M 28 26 L 28 12 L 46 12"/>
<path class="strkm corner" d="M 812 26 L 812 12 L 794 12"/>
<path class="strkm corner" d="M 28 174 L 28 188 L 46 188"/>
<path class="strkm corner" d="M 812 174 L 812 188 L 794 188"/>

<text class="ink name" x="40" y="86">ANDRÉ FELIPE</text>
<rect class="ink cur" x="500" y="62" width="16" height="30"/>

<line class="strk rule" x1="40" y1="112" x2="800" y2="112"/>

<!-- ruler ticks under the line -->
<g class="strkm tick">
  <line x1="40"  y1="112" x2="40"  y2="120"/>
  <line x1="230" y1="112" x2="230" y2="117"/>
  <line x1="420" y1="112" x2="420" y2="117"/>
  <line x1="610" y1="112" x2="610" y2="117"/>
  <line x1="800" y1="112" x2="800" y2="120"/>
</g>

<text class="ink sub"  x="40" y="146">DATA ANALYST  ·  DATA ENGINEER  ·  BUSINESS INTELLIGENCE</text>
<text class="mut meta" x="40" y="170">BRAZIL</text>
</svg>
'''

THEMES = {
    "light": dict(ink="#0d1117", mut="#6e7781"),
    "dark":  dict(ink="#e6edf3", mut="#8b949e"),
}

os.makedirs(OUT, exist_ok=True)
for theme, c in THEMES.items():
    open(os.path.join(OUT, "header-%s.svg" % theme), "w", encoding="utf-8").write(
        HEADER.format(mono=MONO, ink=c["ink"], mut=c["mut"]))
    print("  header-%-6s ok" % theme)
