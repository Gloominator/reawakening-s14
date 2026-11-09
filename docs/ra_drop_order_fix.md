# RA natural-drop dependency ordering fix — 2026-11-09

The data merge appended RA treasure classes after their callers. D2 resolves
TC entries while loading rows sequentially (see D2MOO MonsterTbls.cpp,
DATATBLS_LoadTreasureClassExTxt / DATATBLS_ParseTreasureClassItem), so references
to later classes are not resolved. The original S11 file placed Orbs and Fate
pools before Act Good; the merged S14 file did not.

`tools/fix_tc_order.py` now emits RA dependencies before their callers. It is
also invoked after TC writes by tc_apply_boosts.py and apply_spplus_port.py.
Only RA rows move; all original S14 rows retain their relative order, including
level-based groups. Every row's exact bytes, weights and line endings remain
unchanged. This covers Orbs, Boxes, Orbs (H), Map Orbs Drop, Fate pools and
Treasure Fallen sub-pools. Previously unreferenced boss/relic pools are not
connected to new callers by this fix.

Installed to ProjectD2/data/global/excel/TreasureClassEx.txt. The active local
Hiim_Mystery_Kryszard.filter also explicitly shows gcbx and ccbx in its early
RA currency rule. BH.dll and saves were not changed.

Backup: ProjectD2/backup-ra-drop-order-20261109-090505 (old installed TXT,
90 installed BINs, active filter, and 86 repository BINs in repo-bins/).
All installed BINs were cleared for a consistent next-launch rebuild; repository
monstats.bin and superuniques.bin were cleared because their TC indices changed.
Other repository BINs were preserved.

Validation:
- Exact row-byte multiset unchanged; original S14 row order unchanged.
- All references to RA pools point backward; repeat application is a no-op.
- Repository and installed TXT identical, CRLF retained.
- Normal/NM Act Good reach vials and all 60 cards, but neither box.
- Hell Act Good and T1 Map Good reach vials, all 60 cards and both boxes.
- Hell Treasure Fallen reaches vials, its original 30 common cards and boxes.
- Existing integrity checker still reports 1269 issues, unchanged baseline.
- No gameplay acceptance test yet. Launch ProjectD2/PlugY.exe (-direct -txt)
  and create a game to rebuild the compiled tables, then verify natural drops.

Run `python tools/fix_tc_order.py --check` to check the repository table.
