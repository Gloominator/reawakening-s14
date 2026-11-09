# S11 RA boss drops restored — 2026-11-09

Implemented with tools/restore_ra_boss_drops.py, pinned to upstream S11 v11.0.1
commit 308bca9. This supersedes the earlier documentation deferring boss drops.

- Hell Andariel/Mephisto/Diablo/Baal, both regular and quest TCs: S11 pick entries,
  weights and quality fields restored. Diablo/Baal essence slots now Uber Soul
  (dcso), as in S11; Nightmare and Normal boss rows unchanged.
- Key weights restored on Hell Countess Item, Summoner, Nihlathak, Blood Raven,
  Bloodwitch and Izual. Only each existing key's weight changed.
- T1-T3 Map Boss: S11 three-branch negative-picks wrapper, invoking a main pool,
  Replica (rofp 1 vs gold 10), Map Boss Uber Relic (rotv 1 vs gold 4999).
  Main loot uses S11 Map Boss TC values in three new RA Map Boss Main T1/T2/T3
  rows, but each keeps its matching S14 T1/T2/T3 map pool. T4 unchanged.
- UberAncients and ShadowOfMendeln: S11 pick contents/weights restored, including
  explicit Orbs/Fate Drop/rotv entries. Entire S11 distributions are used, not
  merely appending weights 63/80/etc to a differently scaled S14 denominator.
- MonStats uberdiablonew and rathmaBoneClone: Hell TC1/2/3 restored from S11,
  pointing to Uber Diablo Relics and Rathma Relics. No other monster fields
  changed. Do not assign these to all Rathma forms, which risks repeated drops.
- Existing relic wrappers include the S11 legacy roll too: Uber Diablo rotf
  1/70, rofp 1/4, rotv 1/110; Rathma rotf 1/50, guaranteed rofp, rotv 1/85.

The two uber assignments match the original mod; normal S14 rewards handled
outside these TXT TCs are not edited. Their coexistence needs in-game testing.

fix_tc_order.py recognizes the three added RA main pools; item codes take
precedence over same-named TC rows (lucc). Ordering verified after restoration.
If rebuilding the port from base data, run restore_ra_boss_drops.py LAST, after
tc_apply_boosts.py and apply_spplus_port.py. It is safe to rerun on this table.

Validation: exact S11 selected TC fields, key-only weight diffs, only the two
specified MonStats rows/three Hell TC fields changed, T4 unchanged, row widths
and dependency order checked. Existing integrity baseline remains 1269 issues.
Installed TXT files match repository; treasureclassex/monstats/superuniques BINs
cleared for consistent recompilation at next game creation. Gameplay pending.

Backup: ProjectD2/backup-ra-boss-drops-20261109-163531, containing affected
installed/repository TXT and available compiled BINs. No saves, DLLs, filters,
box recipes or unrelated pending user work were modified by this operation.
