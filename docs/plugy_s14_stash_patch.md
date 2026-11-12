# Community S14 PlugY stash patch installed — 2026-11-12

Installed the unmodified MMPavlov/pd2-plugy-patch v6.2.0 release at the user's request to try native S14 special storage alongside existing PlugY pages. The game was not launched during installation. The user subsequently confirmed it works and also restores affix ranges, then reported overlapping tooltip windows. Disabling BH's legacy tooltip-hook installations did not remove the duplicate windows. The current follow-up also suppresses the original D2 item-tooltip routine only during the community wrapper's legacy panel pass, while retaining PD2's renderer and BH callbacks; see `docs/build_log.md` (2026-11-12). Visual acceptance of this targeted fix is pending.

Source: https://github.com/MMPavlov/pd2-plugy-patch/releases/tag/v6.2.0

Release archive SHA-256: `CBD37B253DE4413A9B2A78BD9FB3093388B4A6A69A4FC784CC799DAC12B883B9` (matched GitHub release digest).

## Backup

`C:\Diablo II - Lord of Destruction\ProjectD2\backup-plugy-s14-patch-20261112-174631`

615 files, 92,776,938 bytes, each copied and SHA-256 verified. Includes the full root Save tree, ProjectD2 executable/DLL/configuration files, BH single-player opt-in, data, PlugY assets, filters, and AppData. Paths inside the backup are relative to the game root: `ProjectD2\...` and `Save\...`.

The backup contains `manifest.csv`, `package-files.csv`, `patch-install.log`, and `verification.json`.

## Installed change

Copied all 14 original release files into ProjectD2 and ran:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\Patch-PD2-PlugY.ps1" -Path "C:\Diablo II - Lord of Destruction\ProjectD2" -NoPause
```

The patch modified only `ProjectD2\ProjectDiablo.dll` among existing backed-up files. Its independent `ProjectDiablo.dll.stock-backup` matches the pre-install DLL. The bundled SPPlus data patch and diagnostics were not run.

- Before DLL SHA-256: `E7EEC2564811C7B347BC62B9D738569329C4971055B8F79CE42A9A5A250E903B`
- After DLL SHA-256: `1F03358869D6AD5C085750B7F75FE090B23799B55879DB99FB9938DF56EB8DDC`
- Custom BH SHA-256 remains `9BBB14587C54B9C059FB48F1A74C845347327214FD9B0E924F8827BD89599531`.

PlugY, BH, configuration, mod data, filters and saves are unchanged by SHA-256. The PE timestamp/image-size/architecture and 25-byte signature at RVA `345629 - 12` still satisfy the existing BH summon fix's guards. This is static verification, not proof of runtime compatibility with the patch's rendering changes.

Patcher verified all writes and branch destinations. A second run returned `ALREADY PATCHED` after its structural checks.

## Launch and acceptance

Use `ProjectD2\Launch-PD2-PlugY.bat`. The existing PlugY.ini retains `Param=-3dfx -plugy -direct -txt`, so the normal new launcher still loads this port's loose mod data.

Expected arrangement: PlugY personal/shared pages in the Stash category; PD2 special categories handle native materials and compendium. Under PlugY, PD2 uses `Save\shared.stash` / `hc_shared.stash` and `shared.compendium` / `hc_shared.compendium`.

Test page switching, personal/shared switching, a small material/rejuv deposit and withdrawal, save/rejoin, Deposit Materials and Shift-right-click from Stash, and existing tooltip ranges/markers and oskill summons. Exact automatic routing from every PlugY page remains unverified. No additional custom routing/button implementation was made.

## Rollback

With the game closed, run `ProjectD2\Restore-Original.bat`, or copy the backed-up `ProjectD2\ProjectDiablo.dll` over the installed DLL. The release restore script restores only the DLL; it does not restore saves or remove the added launcher files.

If items have been moved into the new native material/compendium files during testing, withdraw them before disabling the patch so they remain accessible. A full save rollback means restoring the corresponding complete backed-up Save snapshot and discarding progress since that snapshot; do not mix individual old/new character and stash files casually.
