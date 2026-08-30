# -*- coding: utf-8 -*-
"""Gera um GIF monocromatico de terminal digitando sozinho.
Tudo e desenhado em 2x e reduzido no fim (antialias)."""
import os
from PIL import Image, ImageDraw, ImageFont

S       = 2                                  # supersampling
W, H    = 820, 430                           # tamanho final exibido
BG, CHROME, LINE = (10,10,10), (23,23,23), (56,56,56)
FG, MID, DIM, LEAD = (243,243,243), (170,170,170), (125,125,125), (66,66,66)
MONO  = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONOB = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

f_body  = ImageFont.truetype(MONO,  24*S)
f_bold  = ImageFont.truetype(MONOB, 24*S)
f_title = ImageFont.truetype(MONO,  16*S)

ADV     = f_body.getlength("M")               # avanco de 1 caractere (espaco 2x)
PADX, CHROME_H, TOP, LH = 40, 52, 34, 34
COL = 18                                      # coluna onde todo valor comeca

def row(label, value):
    """Monta 'label ....  value' com o pontilhado calculado, nao chutado."""
    return label, " " + "." * (COL - len(label) - 3) + "  ", value

SCRIPT = [
    ("cmd", "whoami", None),
    ("out", ("andre felipe", "", " — data analyst & engineer")),
    ("gap", "", None),
    ("cmd", "cat now.txt", None),
    ("out", row("building", "sql queries · power bi · data pipelines")),
    ("out", row("learning", "python · azure data factory · databricks")),
    ("out", row("outside",  "weightlifting · footvolley · tech reading")),
    ("gap", "", None),
]

def draw_frame(state, cursor_on):
    img = Image.new("RGB", (W*S, H*S), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W*S-1, CHROME_H*S], fill=CHROME)
    d.line([0, CHROME_H*S, W*S, CHROME_H*S], fill=LINE, width=S)
    d.rectangle([0, 0, W*S-1, H*S-1], outline=LINE, width=S)
    for i in range(3):
        cx, cy, r = (24+i*22)*S, (CHROME_H//2)*S, 5*S
        d.ellipse([cx-r, cy-r, cx+r, cy+r], outline=DIM, width=S)
    t = "andre@data-dev — zsh"
    d.text(((W*S - f_title.getlength(t))/2, (CHROME_H/2 - 11)*S), t, font=f_title, fill=DIM)
    y = (CHROME_H + TOP) * S
    for kind, payload in state:
        x = PADX * S
        if kind in ("cmd", "prompt"):
            d.text((x, y), "$", font=f_bold, fill=DIM); x += ADV*2
            d.text((x, y), payload, font=f_body, fill=FG)
            if kind == "prompt" and cursor_on:
                cx = x + f_body.getlength(payload)
                d.rectangle([cx, y+3*S, cx+ADV, y+28*S], fill=FG)
        elif kind == "out":
            for seg, col in zip(payload, (MID, LEAD, FG)):
                d.text((x, y), seg, font=f_body, fill=col)
                x += f_body.getlength(seg)
        y += LH * S
    return img.resize((W, H), Image.LANCZOS)

frames, delays, built = [], [], []
def push(extra, cursor_on, ms):
    frames.append(draw_frame(built + extra, cursor_on)); delays.append(ms)

push([("prompt", "")], True, 1100)
for kind, payload, *_ in SCRIPT:
    if kind == "cmd":
        for i in range(1, len(payload)+1):
            push([("prompt", payload[:i])], True, 85)
        push([("prompt", payload)], False, 650)
        built.append(("cmd", payload))
    else:
        built.append((kind, payload if kind == "out" else ""))
        push([("prompt", "")], False, 420 if kind == "out" else 180)

for on, ms in [(True, 650), (False, 650)]*3 + [(True, 2200)]:
    push([("prompt", "")], on, ms)

frames = [f.convert("P", palette=Image.ADAPTIVE, colors=24) for f in frames]
frames[0].save("assets/terminal.gif", save_all=True, append_images=frames[1:],
               duration=delays, loop=0, optimize=True, disposal=1)
print("%d frames · %.0f KB · %dx%d" % (len(frames),
      os.path.getsize("assets/terminal.gif")/1024, W, H))
