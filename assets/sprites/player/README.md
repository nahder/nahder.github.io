Upload your player spritesheet here as:

- `player.png`

Current expected layout (configured in `_layouts/valentine.html`):

- Frame size: `29x36`
- Rows:
  - Row `0`: stand (col 0) + stride (col 1) — used for idle & walk
  - Row `1`: climb frame 1 (col 0) + climb frame 2 (col 1)
- Idle uses only column `0`; walk alternates columns `0` and `1`
- Source character facing direction in sheet: `left`

Sheet size: `58x72` (2 columns x 2 rows, 4 frames total)

If your sheet uses different dimensions/rows/columns, update the
`uploadedPlayerSprite` config object in `_layouts/valentine.html`.

