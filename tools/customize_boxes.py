#!/usr/bin/env python3
"""Ten-item Charsi rewards and equal-weight boxes in goblin crafting pools."""
from pathlib import Path
from merge_patchstring import parse, build, verify

ROOT = Path(__file__).resolve().parents[1]
DESCRIPTION = b"Cube twice to receive 10 random crafting infusions or 10 catalyst shards."
GHEED_DESCRIPTION = b"Cube twice to receive 20 random perfect gems or 20 jewel fragments."
TEST_RECIPE = "TEST - Gheed box: Lesser Healing Potion + Town Portal Scroll"
ENABLE_GHEED_TEST_RECIPE = True


def edit_table(path, edit):
    raw = path.read_bytes()
    lines = raw.decode('latin1').split('\r\n')
    assert '\n' not in ''.join(lines), 'Expected CRLF'
    header = lines[0].split('\t')
    for i in range(1, len(lines)):
        if not lines[i].strip():
            continue
        cells = lines[i].split('\t')
        row = dict(zip(header, cells))
        edit(row)
        lines[i] = '\t'.join(row.get(k, '') for k in header)
    result = '\r\n'.join(lines).encode('latin1')
    if result != raw:
        path.write_bytes(result)


def apply_tc(path):
    def edit(row):
        if row['Treasure Class'] not in {'Treasure Fallen Craft N', 'Treasure Fallen Craft NM', 'Treasure Fallen Craft H'}:
            return
        weight = next(row[f'Prob{i}'] for i in range(1, 11) if row[f'Item{i}'] == 'crfv')
        for code in ('gcbx', 'ccbx'):
            slot = next((i for i in range(1, 11) if row[f'Item{i}'] == code), None)
            if slot is None:
                slot = next(i for i in range(1, 11) if not row[f'Item{i}'])
            row[f'Item{slot}'], row[f'Prob{slot}'] = code, weight
    edit_table(path, edit)


def apply_cube(path):
    def edit(row):
        if row['description'].startswith('SP+ Charsi:') and row['input 1'] == 'ccbx':
            code, qty = row['output'].split(',qty=')
            assert code in {'crfb', 'crfc', 'crfs', 'crfh', 'crfv', 'crfu', 'crfp', 'iwss'}
            assert qty in {'5', '10'}
            row['output'] = code + ',qty=10'
        if row['description'].startswith('SP+ Gheed:') and row['input 1'] == 'gcbx':
            code, qty = row['output'].split(',qty=')
            normal = {'gpvs': 'gpv', 'gpys': 'gpy', 'skzs': 'skz',
                      'gprs': 'gpr', 'gpws': 'gpw', 'gpbs': 'gpb', 'gpgs': 'gpg'}
            code = normal.get(code, code)
            assert code in set(normal.values()) | {'jewf'}
            assert qty in {'20', '50'}
            row['output'] = code + ',qty=20'
        if row['description'] == TEST_RECIPE:
            row['enabled'] = '1' if ENABLE_GHEED_TEST_RECIPE else '0'
    edit_table(path, edit)
    lines = path.read_bytes().decode('latin1').split('\r\n')
    header = lines[0].split('\t')
    if not any(line.split('\t', 1)[0] == TEST_RECIPE for line in lines[1:]):
        row = {key: '' for key in header}
        row.update({'description': TEST_RECIPE,
                    'enabled': '1' if ENABLE_GHEED_TEST_RECIPE else '0',
                    'version': '100', 'numinputs': '2', 'input 1': 'hp1',
                    'input 2': 'tsc', 'output': 'gcbx', '*eol': '0'})
        text = '\t'.join(row[key] for key in header)
        lines.insert(len(lines) - 1 if lines[-1] == '' else len(lines), text)
        path.write_bytes('\r\n'.join(lines).encode('latin1'))


def apply_strings(path):
    _, _, entries = parse(str(path))
    descriptions = {b'ccbxDesc': DESCRIPTION, b'gcbxDesc': GHEED_DESCRIPTION}
    pairs = [(e['key'], descriptions.get(e['key'], e['val']))
             for e in sorted(entries, key=lambda e: e['idx'])]
    assert sum(k == b'ccbxDesc' for k, _ in pairs) == 1
    blob, _ = build(pairs)
    bad, content_ok = verify(blob, pairs)
    assert bad == 0 and content_ok
    path.write_bytes(blob)


if __name__ == '__main__':
    apply_tc(ROOT / 'data/global/excel/TreasureClassEx.txt')
    apply_cube(ROOT / 'data/global/excel/CubeMain.txt')
    apply_strings(ROOT / 'data/local/LNG/ENG/patchstring.tbl')
    print('Applied ten-item Charsi rewards and equal-weight goblin boxes (all difficulties).')
