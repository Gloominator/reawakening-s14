#!/usr/bin/env python3
"""Restore selected S11 v11.0.1 RA boss drops on the S14 base.

Map boss main pools retain their matching S14 map tier; T4 is unchanged.
Source is pinned, never the changing upstream main branch.
"""
from pathlib import Path
import csv
import io
import urllib.request
from fix_tc_order import fix_file

ROOT = Path(__file__).resolve().parents[1]
SOURCE = 'https://raw.githubusercontent.com/synpoox/pd2-reawakening/308bca9/data/global/excel/'
CAMPAIGN = [f'{name}{quest} (H)' for name in ('Andariel', 'Mephisto', 'Diablo', 'Baal')
            for quest in ('', 'q')]
KEYS = ['Countess Item (H)', 'Summoner (H)', 'Nihlathak (H)',
        'Blood Raven (H)', 'Bloodwitch (H)', 'Izual (H)']


def read_table(path):
    raw = path.read_bytes()
    assert raw.count(b'\r\n') == raw.count(b'\n'), 'CRLF required'
    lines = raw.decode('latin1').split('\r\n')
    header = lines[0].split('\t')
    return header, [dict(zip(header, line.split('\t'))) for line in lines[1:] if line.strip()]


def write_table(path, header, rows):
    content = '\r\n'.join(['\t'.join(header)] +
                          ['\t'.join(row.get(k, '') for k in header) for row in rows]) + '\r\n'
    path.write_bytes(content.encode('latin1'))


def upstream(filename):
    data = urllib.request.urlopen(SOURCE + filename, timeout=60).read().decode('latin1')
    return list(csv.DictReader(io.StringIO(data), delimiter='\t'))


def apply():
    tc = ROOT / 'data/global/excel/TreasureClassEx.txt'
    header, rows = read_table(tc)
    by = {r['Treasure Class']: r for r in rows}
    source = {r['Treasure Class']: r for r in upstream('TreasureClassEx.txt')}
    fields = ['Picks', 'Unique', 'Set', 'Rare', 'Magic', 'NoDrop'] + [
        k for i in range(1, 11) for k in (f'Item{i}', f'Prob{i}')]

    def copy_picks(target, original):
        for key in fields:
            target[key] = original.get(key, '')

    for name in CAMPAIGN + ['UberAncients', 'ShadowOfMendeln']:
        copy_picks(by[name], source[name])
    for name in KEYS:
        target, original = by[name], source[name]
        for i in range(1, 11):
            code = original[f'Item{i}']
            if code not in {'pk1', 'pk2', 'pk3'}:
                continue
            slot = next(j for j in range(1, 11) if target[f'Item{j}'] == code)
            target[f'Prob{slot}'] = original[f'Prob{i}']
    for tier in range(1, 4):
        name = f'Map Boss T{tier}'
        main_name = f'RA Map Boss Main T{tier}'
        main = by.get(main_name)
        if main is None:
            main = {key: '' for key in header}
            main.update({'Treasure Class': main_name, 'Term': '0'})
            rows.insert(rows.index(by[name]), main)
            by[main_name] = main
        copy_picks(main, source['Map Boss TC'])
        main['Item3'] = f'T{tier} Map Drop'
        copy_picks(by[name], source[name])
        by[name]['Item1'] = main_name
    write_table(tc, header, rows)
    fix_file(tc)

    mon = ROOT / 'data/global/excel/MonStats.txt'
    mh, monsters = read_table(mon)
    source_mon = {r['Id']: r for r in upstream('MonStats.txt')}
    for row in monsters:
        if row['Id'] in {'uberdiablonew', 'rathmaBoneClone'}:
            for i in range(1, 4):
                key = f'TreasureClass{i}(H)'
                row[key] = source_mon[row['Id']][key]
    write_table(mon, mh, monsters)
    for name in ('treasureclassex.bin', 'monstats.bin', 'superuniques.bin'):
        (tc.parent / name).unlink(missing_ok=True)
    print('Restored RA boss drops from pinned S11 source; S14 map tiers retained.')


if __name__ == '__main__':
    apply()
