# Build log

## 2026-11-05 — Stage 1 build installed

- `ProjectD2/pd2data.mpq` = merged S14+mod build (sha256 614e05d9..., 212 files incl. listfile,
  built by `tools/mpq_write.py` from this repo's data tree; 211/211 read-back verified)
- `ProjectD2/BH.dll` = mod's BH from pd2-reawakening repo v11.0.1 (sha256 ca17db07...)
  NOTE: built against S11 client DLLs. D2Game.dll is byte-identical S11<->S14; if BH
  features break or crash, fall back to S14 BH: `cp Live/BH.dll BH.dll` (sha256 4173b0c2...)
- PlugY.ini restored to normal mpq mode (Param=-3dfx -plugy)
- Loose data dir removed from ProjectD2 (data.removed-20261105-202331)
- Backups in ProjectD2: pd2data.mpq.reawakening-s11-backup (original S11 mod),
  pd2data.mpq.before-s14mod-20261105-202331 (S14 vanilla), BH.dll.before-s14mod-* (S14 vanilla),
  PlugY.ini.backup

### Crash fixes that got us here (in commit order)
1. Experience.txt: MaxLvl row must be first (table is positional)
2. TreasureClassEx/CharStats/ItemRatio: LF -> CRLF (parser requires CRLF)
3. Skills/Missiles: appended mod rows had duplicate Id values (Id must equal row index)
4. Skilldesc: 26 mod rows padded to 118-col header

### Not yet active
- Mod's drop-rate boosts in shared TC rows (see docs/stage2_deferred.md)
- Mastery rework (mod replaced skills 128/134; S14 versions kept, mod's appended as 614/615)
- Density variants (1x/2x/5x/10x mpqs)
