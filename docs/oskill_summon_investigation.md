# Item-granted summon loss with awakened equipment

## Reproduction and A/B result (2026-11-11)

Amazon, Undead Crown granting Raise Skeleton level 6:

- With awakened equipment and +3 all skills: tooltip level9/cap5, actual surviving count3.
- With awakened equipment and no +all skills: actual surviving count1.
- Removing awakened equipment, keeping only the crown: tooltip cap4 and four skeletons survive (user confirmed).
- Carrion Wind charged level11 Poison Creeper disappears in town while equipped, with charges remaining.

## Evidence

Read-only elevated process snapshots show both client and server have correct oskill97/layer70=6 and allskills127=3; each has one skeleton entry and a charged creeper entry level11 with eight charges. Server skeleton list stores max5 while only3 survive.

The successful 90-second read-only recording captures skeleton count4->3 with max5 in all samples. Creeper current1/max2 becomes current0/max0. Removals align approximately with one-second game ticks. Sampling at ~1ms cannot exclude shorter destructive limit updates.

PD2 runtime disassembly confirms a conditional 25-frame equipment refresh:

1. ProjectDiablo RVA345400, frame modulo25 remainder1.
2. Equipped-item check RVA382c40; computed item stat487/layer0 is read.
3. Any eligible item returning a positive result triggers RVA34566d -> D2Game RVAd24b0.
4. That routine detaches then reapplies owned item statlists through D2Common RVA3a5d0 and3ac90.
5. Item-stat callbacks can synchronously enforce reduced summon limits: oskill branch D2Game RVAd97ed; charged branch RVAd9a87; updater RVA9f600; setter RVA96ea0.

Stat487 was repurposed from S14 `item_dmgpercent_permissinghppercent` to RA `awakener`. Equipped items in the reproduction have positive stat487 values, including Carrion Wind. Crown itself has no marker. Together with the A/B result, this strongly supports the stat-ID collision as the trigger. A full setter call stack has not been captured.

## Compatibility constraints

- `docs/itemstatcost_mapping.md` incorrectly describes stat487 as dead. It remains engine-read even though table references were absent.
- Do not blindly renumber stat487: existing items encode their awakening marker using the current stat layout.
- Do not hardcode petmax, raise basemax or disable general pet cleanup.
- Blood Golem has separate PD2 handling; post-swap lifetime is not established as the same bug.
- Skeleton Mastery effectiveness has not been independently validated.

## Current status

Root-cause lead validated by equipment A/B testing. A candidate BH build now suppresses only the periodic stat487 predicate call at ProjectDiablo RVA345629, replacing the five-byte call with `31 C0 90 90 90`. Guards require explicit `BH.ReawakeningSinglePlayer.enable` opt-in beside BH, loaded D2Game, the inspected PD2 PE timestamp/image size/architecture and an exact 25-byte surrounding signature. This opt-in declares the whole process SP-only; it is not automatic online detection. Shutdown restores bytes only if they still belong to this helper. Save-stat IDs, awakening markers and other stat getters are unchanged.

Candidate: temporary investigation directory `BH.oskill-candidate.dll`. Source: `scout/BH-s14-src/BH/ReawakeningCompat.h`, installed/restored from `BH.cpp`. Native x86 build and mocked guard/install/restore tests passed; in-game acceptance remains pending. Deployed with the game closed on 2026-11-11: candidate copied to `ProjectD2/BH.dll` and repository `bin/BH.dll`; opt-in file created in ProjectD2. Previous live DLL preserved as `ProjectD2/BH.dll.before-oskill-fix-20261111-134240`. Deployed SHA256: `9BBB14587C54B9C059FB48F1A74C845347327214FD9B0E924F8827BD89599531`. Source committed as `9887821` in the local BH source repository; delta preserved in `tools/bh-oskill-refresh-fix.patch`. No save or data-table edits were made. User confirmed the deployed fix works in game. The previously reported item-granted summon problem no longer reproduces with the candidate installed. To roll back, close the game, restore the backup as BH.dll, remove the opt-in file and restart. Test awakened equipment with crown and Carrion Wind, existing tooltip/affix markers, ordinary equipment changes and game re-entry.

Diagnostic artifacts are in `C:\Users\govno\AppData\Local\Temp\opencode\oskill-investigation` (snapshots, runtime module images, scripts, reports). Runtime addresses must be resolved from module bases; the values above are RVAs for the inspected build only.
