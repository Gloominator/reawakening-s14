# Special skiller charm affix eligibility — 2026-11-09

User reported cubing the random-class GC card caused a halt. Installed log
D2261109.txt records Unrecoverable internal error 0328038d, line 882.
Empower fsem outputs cms,mag,pre=999,suf=0. cms uses lchs, which inherits char,
not ordinary-grand-charm lcha. The S14 merge omitted S11's lchs affix allowances,
leaving the special charm with no intended skiller-prefix pool.

Applied tools/restore_skiller_affixes.py to repository and install:
- Add lchs to an unused itype cell on the 21 Grand Charm skill-tree prefixes.
- Restore S11 lchs suffix eligibility on IDs 335-340 and 399 (life/movement).
- Also allow lchs on suffix 265 (12 FHR), required by Momentum Shift.
- No S14 affix values, frequencies, indices, row order or existing types changed.

Lifespring and Momentum Shift also create cms with forced skiller prefixes, so
they share this fix. Cube pre=999 was already outside the S11 table and is an
original force-random sentinel, not a shifted valid affix ID; it is retained.
D2MOO's vanilla affix roller falls back to a random eligible affix if a requested
positive prefix cannot be found. PD2 runtime behavior still needs testing.

Validated exactly 21 prefix and eight suffix eligibility-cell changes, identical
row widths, idempotent reapplication and installed/repository equality. Cleared
magicprefix.bin and magicsuffix.bin for rebuild. Does not prove the crash path
without an in-game retest; do not claim gameplay confirmation yet.

Backup: ProjectD2/backup-skiller-affixes-20261109-170918. No saves modified.
If rebuilding merged affix files, rerun the helper before deploying.
