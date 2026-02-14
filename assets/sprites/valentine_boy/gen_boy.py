#!/usr/bin/env python3
"""Generate Valentine's boy character — hat, short hair (stops at eyes), dark blue robe with heart, blush."""
from PIL import Image

FW, FH = 28, 36

# Palette — same structure as player but dark blue robe, dark brown short hair
BP = {
    'F':'#c8956a',   # skin (light brown)
    'f':'#b07848',   # skin shadow
    'D':'#3b2517',   # hair dark brown
    'd':'#5a3a22',   # hair highlight brown
    'W':'#ffffff',   # eye highlight dot
    'E':'#1a1a22',   # eye black
    'C':'#ff5577',   # blush cheeks (strong pink, matches heart)
    'h':'#ff4477',   # heart bright
    'R':'#223388',   # robe main (dark blue)
    'r':'#1a2266',   # robe shadow/outline
    'S':'#3355aa',   # robe highlight/fold
    'K':'#e8a020',   # clasp gold
    'A':'#223388',   # hat main (dark blue)
    'a':'#1a2266',   # hat dark/outline
    'B':'#3355aa',   # hat mid
    'b':'#e8a020',   # hat band (gold)
    'T':'#ffcc44',   # hat star
    'N':'#8a7050',   # beard stubble (light brown)
    'n':'#7a6040',   # beard shadow
}

def hex_rgba(c):
    c = c.lstrip('#')
    return (int(c[0:2],16), int(c[2:4],16), int(c[4:6],16), 255)

# Boy has the same hat as the player, but short hair (Dd) that only
# covers the top of the head and stops at the eye rows — no flowing
# strands down the sides of the body. He has blush and the heart on
# the robe, just like the player.

# ── STAND ──
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
    '......DDfffffffDDDDDd.......',  # 10 face starts (hair on top only)
    '......DfFFFFFFFFFfDDd.......',  # 11
    '......DfFEEFFFEEFFfDd.......',  # 12 eyes top (hair stops here)
    '.......fFEEFFFEEFFf.........',  # 13 eyes middle (no hair)
    '.......fFEWFFFEWFFf.........',  # 14 eyes bottom + highlight
    '.......fFFFFFFFFFf..........',  # 15
    '.......fFFCFFFFCFf..........',  # 16 cheeks (blush)
    '.......fFFFFFFFFFf..........',  # 17 mouth
    '........ffFfFfFff...........',  # 18 chin — just a few dots
    '..........fKff..............',  # 19 clasp
    '.......rRRRRRRRRRRr........',  # 20 robe starts
    '......rRRSRRRRRRSRRr.......',  # 21
    '......rRRRRRRRRRRRRr.......',  # 22
    '......rRRR.hh.hh.RRr.......',  # 23 heart
    '.....rRRRRhhhhhhhRRRRr.....',  # 24
    '....rRRRRRhhhhhhhRRRRRr....',  # 25
    '....rRRSRR.hhhhh.RRSRRr....',  # 26
    '...rRRRRRR.hhh.RRRRRRRr....',  # 27
    '...rRRRRRRRR.h.RRRRRRRRr...',  # 28
    '..rRRSRRRRRRRRRRRRRSRRRr...',  # 29
    '..rRRRRRRRRRRRRRRRRRRRRRr..',  # 30
    '..rRSRRRRRSRRRRSRRRRRSRRr..',  # 31
    '...rrRRRRRrrrrrrRRRRRrr....',  # 32 hem
    '.....rrrrr....rrrrr........',  # 33
]

# ── STRIDE ──
pf2 = [
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
    '......DDfffffffDDDDDd.......',  # 10 face starts
    '......DfFFFFFFFFFfDDd.......',  # 11
    '......DfFEEFFFEEFFfDd.......',  # 12 eyes top (hair stops)
    '.......fFEEFFFEEFFf.........',  # 13 eyes middle
    '.......fFEWFFFEWFFf.........',  # 14 eyes bottom + highlight
    '.......fFFFFFFFFFf..........',  # 15
    '.......fFFCFFFFCFf..........',  # 16 cheeks (blush)
    '.......fFFFFFFFFFf..........',  # 17 mouth
    '........ffFfFfFff...........',  # 18 chin — just a few dots
    '..........fKff..............',  # 19 clasp
    '.......rRRRRRRRRRRr........',  # 20 robe starts
    '......rRRSRRRRRRSRRr.......',  # 21
    '......rRRRRRRRRRRRRr.......',  # 22
    '......rRRR.hh.hh.RRr.......',  # 23 heart
    '.....rRRRRhhhhhhhRRRRr.....',  # 24
    '....rRRRRRhhhhhhhRRRRRr....',  # 25
    '....rRRSRR.hhhhh.RRSRRr....',  # 26
    '...rRRRRRR.hhh.RRRRRRRr....',  # 27
    '...rRRRRRRRR.h.RRRRRRRRr...',  # 28
    '..rRRSRRRRRRRRRRRRRSRRRr...',  # 29
    '..rRRRRRRRRRRRRRRRRRRRRRr..',  # 30
    '..rRSRRRRRSRRRRSRRRRRSRRr..',  # 31
    '...rrRRRRrrrrrrrrRRRRrr....',  # 32 hem
    '......rrrr..rrrr..rr.......',  # 33
]

# ── CLIMB 1 ──
pClimb1 = [
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
    '......DDfffffffDDDDDd.......',  # 10 face starts
    '......DfFFFFFFFFFfDDd.......',  # 11
    '......DfFEEFFFEEFFfDd.......',  # 12 eyes top (hair stops)
    '.......fFEEFFFEEFFf.........',  # 13 eyes middle
    '.......fFEWFFFEWFFf.........',  # 14 eyes bottom + highlight
    '.......fFFFFFFFFFf..........',  # 15
    '.......fFFCFFFFCFf..........',  # 16 cheeks (blush)
    '.......fFFFFFFFFFf..........',  # 17 mouth
    '........ffFfFfFff...........',  # 18 chin — just a few dots
    'FF......fKff..........FF....',  # 19 arms out + clasp
    'FFf....rRRSRRRRSRRr..fFF...',  # 20
    'FFf..rRRR.hh.hh.RRr..fFF...',  # 21 heart
    'FF..rRRRRhhhhhhhRRRRr..FF..',  # 22
    '...rRRRRRhhhhhhhRRRRRr.....',  # 23
    '...rRRSRR.hhhhh.RRSRRr.....',  # 24
    '...rRRRRRR.hhh.RRRRRRr.....',  # 25
    '..rRRRRRRRR.h.RRRRRRRRr....',  # 26
    '..rRRSRRRRRRRRRRRRRSRRr....',  # 27
    '..rRRRRRRRRRRRRRRRRRRRRr...',  # 28
    '..rRSRRRRRSRRRRSRRRRRSRr...',  # 29
    '...rrRRRRRrrrrrrRRRRRrr....',  # 30
    '.....rrrrr....rrrrr........',  # 31
]

# ── CLIMB 2 ──
pClimb2 = [
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
    '......DDfffffffDDDDDd.......',  # 10 face starts
    '......DfFFFFFFFFFfDDd.......',  # 11
    '......DfFEEFFFEEFFfDd.......',  # 12 eyes top (hair stops)
    '.......fFEEFFFEEFFf.........',  # 13 eyes middle
    '.......fFEWFFFEWFFf.........',  # 14 eyes bottom + highlight
    '.......fFFFFFFFFFf..........',  # 15
    '.......fFFCFFFFCFf..........',  # 16 cheeks (blush)
    '.......fFFFFFFFFFf..........',  # 17 mouth
    '........ffFfFfFff...........',  # 18 chin — just a few dots
    'FF......fKff..........FF....',  # 19 arms out + clasp
    'fFF....rRRSRRRRSRRr..FFf...',  # 20
    'fFF..rRRR.hh.hh.RRr..FFf...',  # 21 heart
    '.FF.rRRRRhhhhhhhRRRRr.FF...',  # 22
    '...rRRRRRhhhhhhhRRRRRr.....',  # 23
    '...rRRSRR.hhhhh.RRSRRr.....',  # 24
    '...rRRRRRR.hhh.RRRRRRr.....',  # 25
    '..rRRRRRRRR.h.RRRRRRRRr....',  # 26
    '..rRRSRRRRRRRRRRRRRSRRr....',  # 27
    '..rRRRRRRRRRRRRRRRRRRRRr...',  # 28
    '..rRSRRRRRSRRRRSRRRRRSRr...',  # 29
    '...rrRRRRRrrrrrrRRRRRrr....',  # 30
    '.....rrrrr....rrrrr........',  # 31
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
            if ch != '.' and ch in BP:
                img.putpixel((ox + x, oy + y), hex_rgba(BP[ch]))

draw(pf1,     0,    0)
draw(pf2,     FW,   0)
draw(pClimb1, 0,    FH)
draw(pClimb2, FW,   FH)

out = '/home/nader-ahmed/Desktop/personal/nahder.github.io/assets/sprites/valentine_boy/boy.png'
img.save(out)
print(f"Saved {img.size[0]}x{img.size[1]} -> {out}")
