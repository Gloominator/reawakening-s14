# Gheed normal-gem rewards and temporary test recipe — 2026-11-09

Gheed's eight reward recipes now give quantity 20. Seven gem/skull outcomes use
the native S14 item codes gpv/gpy/skz/gpr/gpw/gpb/gpg, rather than their separate
legacy *s stack counterparts. The eighth gives jewf,qty=20. Reward-selection
thresholds and probabilities are unchanged. Native gems remain stackable; this
is a normal-ID quantity stack, not 20 separate cube output slots.

Gheed's tooltip now states 20 perfect gems or 20 jewel fragments.

Temporary enabled recipe:
- Lesser Healing Potion (hp1) + Town Portal Scroll (tsc) -> Gheed's Curious Box.
- Description: TEST - Gheed box: Lesser Healing Potion + Town Portal Scroll.
- Normal two-transmute box-opening process remains unchanged.

To disable later, set ENABLE_GHEED_TEST_RECIPE=False in tools/customize_boxes.py,
run apply_cube (or the port tool), deploy CubeMain.txt and clear cubemain.bin.
The helper updates the existing test row instead of duplicating it.

Updated installed and repository CubeMain.txt/patchstring.tbl; affected cube
BINs removed for rebuild. Confirmed eight expected reward outputs, one enabled
test recipe, correct tooltip, and idempotent reapplication. Gameplay pending.
Backup: ProjectD2/backup-gheed-normal-gems-20261109-153616.
