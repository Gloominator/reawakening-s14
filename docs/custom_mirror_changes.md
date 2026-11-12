# CUSTOM: the owner's mirror and fate-card preferences

> **Warning: these changes are the owner's personal whim, not a faithful port of Reawakening to PD2 Season 14.** Do not attribute their balance or recipe design to Reawakening's author. Some ingredients came from Single Player Plus, but this combined behavior is a local customization.

The changes are recorded in a separate `CUSTOM` Git commit. The historical tool name `tools/apply_mirror_port.py` is retained for existing workflows; despite its name, it applies these custom rules, not an upstream parity port.

## Included gameplay changes

- Mirror quality-divisor values: Normal 15000, Nightmare 7500, Hell 2500; Set stays 100. These are the owner's selected values. Their actual engine drop rates have not been established by an offline probability test.
- One False Reflection card creates a mirror, instead of nine.
- Existing mirror recipes no longer add the `mirrored` property to their outputs. The intended behavior permits repeated mirroring and removes the new Mirrored affix line; previously stored items are not rewritten.
- Enables unique-ring and magic/rare/crafted-jewel mirror recipes.
- Adds mirroring for set equipment, maps (including corrupted maps), unique charms, selected currency and crafting materials, Awakening Stones, and class Invader Ears. Some equipment/charm recipes retain their non-corrupted-item condition; map recipes deliberately omit it.
- Adds 60 recipes using two matching fate cards plus a key to create a random fate card.
- Adds five enabled convenience/test recipes using inexpensive vendor items to create a mirror, Puzzle Piece, Puzzle Box, Orb of Unmaking, or Demonic Cube. These are part of this custom snapshot, not normal RA progression. They replace the previous Gheed-box test row.

## Files and validation

`data/global/excel/CubeMain.txt`, `data/global/excel/TreasureClassEx.txt`, and `tools/apply_mirror_port.py` contain the customization. The script also synchronizes those tables to ProjectD2 and removes their stale compiled bins when explicitly run.

For the Git checkpoint, source syntax and the existing table column counts/CRLF format were checked read-only. The script was not rerun, and gameplay behavior was not independently retested during the commit task.

Older recipe documentation describes the port baseline and can differ from this custom snapshot, particularly the mirror targets and False Reflection cost. Use this document and the current tables for the customized behavior.
