#!/usr/bin/env python3
"""Generate Elara turtle spirit sprite PNG from ASCII art."""
from PIL import Image

# Elara palette (red mystical turtle spirit)
EP = {
    'K':'#2e1518',  # shell outline (dark)
    'S':'#541d22',  # shell dark
    's':'#7a2d3d',  # shell mid
    'G':'#a83848',  # shell light
    'g':'#cc5868',  # shell highlight
    'P':'#ddb844',  # pattern gold
    'p':'#aa8833',  # pattern dark gold
    'H':'#6a2828',  # head dark
    'h':'#8a4444',  # head mid
    'E':'#ffffff',  # eye white
    'e':'#ffaa88',  # eye iris
    'L':'#4a1a1a',  # leg dark
    'l':'#6a3a3a',  # leg mid
    'W':'#ff8866',  # wisp bright
    'w':'#ffbb99',  # wisp light
    'T':'#5a4a2a',  # underbelly dark
    't':'#7a6a4a',  # underbelly mid
    'M':'#1a0a0a',  # mouth
}

elaraSp = [
    '..wW.Ww..............................',  # 0: spirit wisps
    '.wWWwWWw.............................',  # 1
    '..wW.Ww..............................',  # 2
    '.KKKKKKKKKKK.........................',  # 3: shell top
    'KKSSSsssssSSSKK......................',  # 4
    'KSSssGGGGGGGssSSK....................',  # 5
    'KSSsGGGgPPPgGGGsSSK.................',  # 6: patterns
    'KSSsGGPPPgPgPPPGGsSSK...............',  # 7
    'KSSsGGPPgPPPPPgPPGGsSSK.............',  # 8: widest
    'KSSsGgPgPgPgPgPgPgGGsSSK.hhHHh.....',  # 9: head at mid-shell
    'KSSsGGGPPPPgPPPPGGGGsSSKHhEeHh.....',  # 10: eyes
    'KSSssGGGggPPPggGGGssSSK.HhEeHh.....',  # 11
    '.KSSSsssGGGGGGsssSSSKK..HhHhHh.....',  # 12
    '..KKSSSSsssssssSSSSKKK...hHMHH.....',  # 13: mouth
    '...KTTTTTTTTTTTTTTTTK.....hHH.......',  # 14: underbelly
    '...KTtTTTTTTTTTtTTTK......H.........',  # 15
    '...KTTTTTTTTTTTTTTTTK..................',  # 16
    '..KLlLLLK.......KLLLlLK...............',  # 17: legs
    '...KLlK...........KLlK................',  # 18
    '....KK.............KK.................',  # 19: feet
]

def hex_rgba(c):
    c = c.lstrip('#')
    return (int(c[0:2],16), int(c[2:4],16), int(c[4:6],16), 255)

# Determine sprite dimensions from the ASCII art
height = len(elaraSp)
width = max(len(row) for row in elaraSp)

# Normalize rows to same width
for i in range(len(elaraSp)):
    if len(elaraSp[i]) < width:
        elaraSp[i] += '.' * (width - len(elaraSp[i]))

img = Image.new('RGBA', (width, height), (0, 0, 0, 0))

for y, row in enumerate(elaraSp):
    for x, ch in enumerate(row):
        if ch != '.' and ch in EP:
            img.putpixel((x, y), hex_rgba(EP[ch]))

out = '/home/nader-ahmed/Desktop/personal/nahder.github.io/assets/sprites/elara/elara.png'
img.save(out)
print(f"Saved {img.size[0]}x{img.size[1]} -> {out}")
