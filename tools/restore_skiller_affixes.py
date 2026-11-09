#!/usr/bin/env python3
"""Restore special RA skiller charm affix eligibility without changing S14 stats."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX_IDS = {base + delta for base in (430, 442, 454, 466, 478, 490, 502)
              for delta in range(3)}
SUFFIX_IDS = {265, 335, 336, 337, 338, 339, 340, 399}


def apply(path, ids):
    raw = path.read_bytes()
    lines = raw.decode('latin1').split('\r\n')
    header = lines[0].split('\t')
    id_column = next(header.index(k) for k in ('*ID', '*comment') if k in header)
    found = set()
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():
            continue
        cells = line.split('\t')
        value = cells[id_column]
        if not value.isdigit() or int(value) not in ids:
            continue
        found.add(int(value))
        types = [header.index(f'itype{j}') for j in range(1, 8)]
        assert 'lcha' in [cells[j] for j in types], value
        if 'lchs' not in [cells[j] for j in types]:
            slot = next(j for j in types if not cells[j])
            cells[slot] = 'lchs'
            lines[i] = '\t'.join(cells)
    assert found == ids, (found, ids)
    result = '\r\n'.join(lines).encode('latin1')
    path.write_bytes(result)
    print(path.name, len(found), 'skiller-compatible affixes verified')


if __name__ == '__main__':
    excel = ROOT / 'data/global/excel'
    apply(excel / 'MagicPrefix.txt', PREFIX_IDS)
    apply(excel / 'MagicSuffix.txt', SUFFIX_IDS)
    for name in ('magicprefix.bin', 'magicsuffix.bin'):
        (excel / name).unlink(missing_ok=True)
