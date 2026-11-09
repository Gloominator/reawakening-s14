# Box reward/goblin customization — 2026-11-09

User requested ten crafting essences per Charsi box and both boxes in the
crafting-essence treasure goblin pool, each equal to one essence type.

Applied by tools/customize_boxes.py, also called by the relevant stages of
apply_spplus_port.py and tc_apply_boosts.py:

- Eight SP+ Charsi phase-two recipes: qty=5 -> qty=10, including catalyst shards.
  Roll thresholds unchanged; Gheed rewards unchanged.
- ccbxDesc updated to describe ten infusions or ten catalyst shards.
- Treasure Fallen Craft N, NM and H each gain gcbx:1 and ccbx:1, matching
  crfv and every other individual crafting infusion. Existing Picks, NoDrop,
  essence weights and other goblin sub-pools unchanged.
- Boxes now can drop from crafting goblins in ALL difficulties, an intentional
  exception to their earlier Hell-only Orbs (H) route. Existing orb route stays.
- Equal weight means equal probability within that sub-pool, not a fixed percent
  per goblin kill; NoDrop, player count and parent-table picks also matter.

Validation: exactly three TC rows and eight cube output fields changed; only
ccbxDesc changed in the string table, all string indices preserved. TC dependency
order remains valid, scripts are idempotent, table row widths/CRLF preserved.
Installed TXT/TBL copied from repository and cubemain/treasureclassex BINs removed
for next game rebuild. Gameplay acceptance pending.

Backup: ProjectD2/backup-box-rewards-20261109-120205 (both installed and repository
versions of affected data and existing affected compiled tables).
