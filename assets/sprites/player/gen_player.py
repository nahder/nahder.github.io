#!/usr/bin/env python3
"""Generate cute Valentine's character with long flowing hair."""
from PIL import Image

FW, FH = 28, 36

PP = {
    'F':'#c8956a',   # skin (light brown)
    'f':'#b07848',   # skin shadow
    'D':'#1a1a22',   # hair black
    'd':'#2a2a33',   # hair highlight
    'W':'#ffffff',   # eye highlight dot
    'E':'#1a1a22',   # eye black
    'C':'#ff5577',   # blush cheeks (strong pink, near heart)
    'h':'#ff4477',   # heart bright
    'R':'#7744bb',   # dress main (purple)
    'r':'#553399',   # dress shadow/outline
    'S':'#9966dd',   # dress highlight/fold
    'K':'#e8a020',   # clasp gold
    'A':'#6633aa',   # hat main (purple)
    'a':'#4a2288',   # hat dark/outline
    'B':'#7744bb',   # hat mid
    'b':'#e8a020',   # hat band (gold)
    'T':'#ffcc44',   # hat star
}

def hex_rgba(c):
    c = c.lstrip('#')
    return (int(c[0:2],16), int(c[2:4],16), int(c[4:6],16), 255)

# Hair is 1px wide strands (Dd) on each side, flowing all the way
# down alongside the dress to the hem.

# ── STAND ──
# Hair (Dd strands) stops where the heart begins (row 23).
pf1 = [
    '.............a..............',  # 0  hat tip
    '............aAa.............',  # 1
    '...........aAAAa............',  # 2
    '..........aAAAABa...........',  # 3
    '.........aAAAAABa...........',  # 4
    '........aAAAAAABBa..........',  # 5
    '.......aAAAAAAAABBa.........',  # 6
    '......bbbbbbbbbbbbbbb.......',  # 7  hat brim
    '.....bbTbbbbbbbbbbTbbb......',  # 8  brim stars
    '.....DDDDDDDDDDDDDDDDd......',  # 9  hair under brim
    '....DdDDfffffffDDDDDdDd.....',  # 10 face starts
    '....DdDfFFFFFFFFFfDDdDd.....',  # 11
    '....DdDfFEEFFFEEFFfDdDd.....',  # 12 eyes top
    '....DdDfFEEFFFEEFFfDdDd.....',  # 13 eyes middle
    '....DdDfFEWFFFEWFFfDdDd.....',  # 14 eyes bottom + highlight
    '....DdDfFFFFFFFFFfDDdDd.....',  # 15
    '....DdDfFFCFFFFCFfDDdDd.....',  # 16 cheeks
    '....DdDDfFFFFFFFfDDDdDd.....',  # 17
    '....DdDDDfffffffDDDDdDd.....',  # 18 face closes
    '.....DdDDDDDDDDDDDDdDd......',  # 19
    '.....DdDDDDKDDDDDDDdDd......',  # 20 clasp
    '.....DdrRRRRRRRRRRrdDd......',  # 21 dress starts (hair ends here)
    '....DdrRRSRRRRRRSRRrdDd.....',  # 22
    '....DdrRRRRRRRRRRRRrdDd.....',  # 23 last hair row
    '......rRRR.hh.hh.RRRr.......',  # 24 heart — no hair
    '.....rRRRRhhhhhhhRRRRr......',  # 25
    '....rRRRRRhhhhhhhRRRRRr.....',  # 26
    '....rRRSRR.hhhhh.RRSRRr.....',  # 27
    '...rRRRRRR.hhh.RRRRRRRr.....',  # 28
    '...rRRRRRRRR.h.RRRRRRRRr....',  # 29
    '..rRRSRRRRRRRRRRRRRSRRRr....',  # 30
    '..rRRRRRRRRRRRRRRRRRRRRRr...',  # 31
    '..rRSRRRRRSRRRRSRRRRRSRRr...',  # 32
    '...rrRRRRRrrrrrrRRRRRrr.....',  # 33 hem
    '.....rrrrr....rrrrr.........',  # 34
]

# ── STRIDE ──
pf2 = [
    '.............a..............',
    '............aAa.............',
    '...........aAAAa............',
    '..........aAAAABa...........',
    '.........aAAAAABa...........',
    '........aAAAAAABBa..........',
    '.......aAAAAAAAABBa.........',
    '......bbbbbbbbbbbbbbb.......',
    '.....bbTbbbbbbbbbbTbbb......',
    '.....DDDDDDDDDDDDDDDDd......',
    '....DdDDfffffffDDDDDdDd.....',
    '....DdDfFFFFFFFFFfDDdDd.....',
    '....DdDfFEEFFFEEFFfDdDd.....',
    '....DdDfFEEFFFEEFFfDdDd.....',
    '....DdDfFEWFFFEWFFfDdDd.....',
    '....DdDfFFFFFFFFFfDDdDd.....',
    '....DdDfFFCFFFFCFfDDdDd.....',
    '....DdDDfFFFFFFFfDDDdDd.....',
    '....DdDDDfffffffDDDDdDd.....',
    '.....DdDDDDDDDDDDDDdDd......',
    '.....DdDDDDKDDDDDDDdDd......',
    '.....DdrRRRRRRRRRRrdDd......',
    '....DdrRRSRRRRRRSRRrdDd.....',
    '....DdrRRRRRRRRRRRRrdDd.....',
    '......rRRR.hh.hh.RRRr.......',
    '.....rRRRRhhhhhhhRRRRr......',
    '....rRRRRRhhhhhhhRRRRRr.....',
    '....rRRSRR.hhhhh.RRSRRr.....',
    '...rRRRRRR.hhh.RRRRRRRr.....',
    '...rRRRRRRRR.h.RRRRRRRRr....',
    '..rRRSRRRRRRRRRRRRRSRRRr....',
    '..rRRRRRRRRRRRRRRRRRRRRRr...',
    '..rRSRRRRRSRRRRSRRRRRSRRr...',
    '...rrRRRRrrrrrrrrRRRRrr.....',
    '......rrrr..rrrr..rr........',
]

# ── CLIMB 1 ──
# Hair stops at row 19 (row 20 = heart start).
pClimb1 = [
    '.............a..............',
    '............aAa.............',
    '...........aAAAa............',
    '..........aAAAABa...........',
    '.........aAAAAABa...........',
    '........aAAAAAABBa..........',
    '.......aAAAAAAAABBa.........',
    '......bbbbbbbbbbbbbbb.......',
    '.....bbTbbbbbbbbbbTbbb......',
    '.....DDDDDDDDDDDDDDDDd......',
    '....DdDDfffffffDDDDDdDd.....',
    '....DdDfFFFFFFFFFfDDdDd.....',
    '....DdDfFEEFFFEEFFfDdDd.....',
    '....DdDfFEEFFFEEFFfDdDd.....',
    '....DdDfFEWFFFEWFFfDdDd.....',
    '....DdDfFFFFFFFFFfDDdDd.....',
    '....DdDfFFCFFFFCFfDDdDd.....',
    '....DdDDfFFFFFFFfDDDdDd.....',
    '....DdDDDDDKDDDDDDDdDd......',
    'FF..DdrRRRRRRRRRRrdDd..FF...',  # arms + hair
    'FFf.DdrRRSRRRRSRRrdDd.fFF...',  # last hair row
    'FFf...rRR.hh.hh.Rr....fFF...',  # heart — no hair, arms stay
    'FF....rRRhhhhhhhRRr.....FF...',  # no hair, arms stay
    '.....rRRRhhhhhhhRRRr........',
    '....rRRSR.hhhhh.RRSRr.......',
    '....rRRRRR.hhh.RRRRRr.......',
    '...rRRRRRRR.h.RRRRRRRr......',
    '...rRRSRRRRRRRRRRRSRRr......',
    '..rRRRRRRRRRRRRRRRRRRRRr....',
    '..rRSRRRRRSRRRRSRRRRRSRr....',
    '...rrRRRRRrrrrrrRRRRRrr.....',
    '.....rrrrr....rrrrr.........',
]

# ── CLIMB 2 ──
pClimb2 = [
    '.............a..............',
    '............aAa.............',
    '...........aAAAa............',
    '..........aAAAABa...........',
    '.........aAAAAABa...........',
    '........aAAAAAABBa..........',
    '.......aAAAAAAAABBa.........',
    '......bbbbbbbbbbbbbbb.......',
    '.....bbTbbbbbbbbbbTbbb......',
    '.....DDDDDDDDDDDDDDDDd......',
    '....DdDDfffffffDDDDDdDd.....',
    '....DdDfFFFFFFFFFfDDdDd.....',
    '....DdDfFEEFFFEEFFfDdDd.....',
    '....DdDfFEEFFFEEFFfDdDd.....',
    '....DdDfFEWFFFEWFFfDdDd.....',
    '....DdDfFFFFFFFFFfDDdDd.....',
    '....DdDfFFCFFFFCFfDDdDd.....',
    '....DdDDfFFFFFFFfDDDdDd.....',
    '....DdDDDDDKDDDDDDDdDd......',
    'FF..DdrRRRRRRRRRRrdDd..FF...',  # arms + hair
    'fFF.DdrRRSRRRRSRRrdDd.FFf...',  # last hair row
    'fFF...rRR.hh.hh.Rr....FFf...',  # heart — no hair, arms stay
    '.FF...rRRhhhhhhhRRr.....FF...',  # no hair, arms stay
    '.....rRRRhhhhhhhRRRr........',
    '....rRRSR.hhhhh.RRSRr.......',
    '....rRRRRR.hhh.RRRRRr.......',
    '...rRRRRRRR.h.RRRRRRRr......',
    '...rRRSRRRRRRRRRRRSRRr......',
    '..rRRRRRRRRRRRRRRRRRRRRr....',
    '..rRSRRRRRSRRRRSRRRRRSRr....',
    '...rrRRRRRrrrrrrRRRRRrr.....',
    '.....rrrrr....rrrrr.........',
]

def normalize(frames):
    out = []
    for row in frames[:FH]:
        if len(row) < FW:
            row = row + '.' * (FW - len(row))
        elif len(row) > FW:
            row = row[:FW]
        out.append(row)
    while len(out) < FH:
        out.append('.' * FW)
    return out

pf1 = normalize(pf1)
pf2 = normalize(pf2)
pClimb1 = normalize(pClimb1)
pClimb2 = normalize(pClimb2)

img = Image.new('RGBA', (FW * 2, FH * 2), (0, 0, 0, 0))

def draw(data, ox, oy):
    for y, row in enumerate(data):
        for x, ch in enumerate(row):
            if ch != '.' and ch in PP:
                img.putpixel((ox + x, oy + y), hex_rgba(PP[ch]))

draw(pf1,     0,    0)
draw(pf2,     FW,   0)
draw(pClimb1, 0,    FH)
draw(pClimb2, FW,   FH)

out = '/home/nader-ahmed/Desktop/personal/nahder.github.io/assets/sprites/player/player.png'
img.save(out)
print(f"Saved {img.size[0]}x{img.size[1]} -> {out}")
