#!/usr/bin/env python3
"""Place RA treasure classes before their callers without changing row contents.

D2 resolves TC names while loading rows, not in a second pass. Only RA rows
are moved; the relative order of every vanilla row (including TC groups) stays.
"""
from collections import Counter
from pathlib import Path
import argparse

ROOT = Path(__file__).resolve().parents[1]
RA_NAMES = set("""Orbs|Map Boss TC|Replica|Prime Evil Embers|Map Orbs Drop|Fate Common A|Fate Common B|Fate Common C|Map Boss Uber Relic|Fate Uncommon A|Fate Uncommon B|Fate Rare A|Fate Drop|Treasure Fallen Cards N|Treasure Fallen Cards NM|Treasure Fallen Cards H|Treasure Fallen Orbs N|Treasure Fallen Orbs NM|Treasure Fallen Orbs H|Uber Diablo Legacy|Uber Diablo Replica|Uber Diablo Void|Rathma Legacy|Rathma Replica|Rathma Void|Uber Diablo Relics|Rathma Relics|Boxes|Orbs (H)""".split("|"))


def reorder(raw):
    lines = raw.splitlines(keepends=True)
    header = lines[0].rstrip(b"\r\n").decode("latin1").split("\t")
    item_columns = [header.index(f"Item{i}") for i in range(1, 11)]
    group_column = header.index("group")
    rows = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        cells = line.rstrip(b"\r\n").decode("latin1").split("\t")
        name = cells[0]
        if not name or name in rows:
            raise ValueError(f"Empty or duplicate TC name: {name!r}")
        rows[name] = (line, cells)
    active = RA_NAMES & rows.keys()
    for name in active:
        if rows[name][1][group_column] not in ("", "0"):
            raise ValueError(f"Cannot move grouped TC: {name}")
    output = [lines[0]]
    emitted, visiting = set(), set()

    def emit(name):
        if name in emitted:
            return
        if name in visiting:
            raise ValueError(f"TC dependency cycle: {name}")
        visiting.add(name)
        line, cells = rows[name]
        for column in item_columns:
            target = cells[column]
            if target in active:
                emit(target)
            elif name in active and target in rows and target not in emitted:
                raise ValueError(f"RA TC {name} needs unavailable vanilla TC {target}")
        visiting.remove(name)
        emitted.add(name)
        output.append(line)

    for line in lines[1:]:
        if line.strip():
            emit(line.split(b"\t", 1)[0].decode("latin1"))
        else:
            output.append(line)
    result = b"".join(output)
    if Counter(lines) != Counter(result.splitlines(keepends=True)):
        raise AssertionError("Row bytes changed")
    before = [n for n in rows if n not in active]
    after = [line.split(b"\t", 1)[0].decode("latin1")
             for line in output[1:] if line.strip()
             and line.split(b"\t", 1)[0].decode("latin1") not in active]
    assert before == after, "Vanilla order changed"
    positions = {line.split(b"\t", 1)[0].decode("latin1"): i
                 for i, line in enumerate(output[1:]) if line.strip()}
    for name, (_, cells) in rows.items():
        for column in item_columns:
            target = cells[column]
            if target in active:
                assert positions[target] < positions[name], (name, target)
    return result


def fix_file(path):
    raw = path.read_bytes()
    result = reorder(raw)
    assert reorder(result) == result, "Not idempotent"
    if raw != result:
        path.write_bytes(result)
        # TC indices also live in MonStats/SuperUniques.
        for compiled in path.parent.glob("*.bin"):
            if compiled.name.lower() in {"treasureclassex.bin", "monstats.bin", "superuniques.bin"}:
                compiled.unlink()
    print(f"{path}: {'reordered' if raw != result else 'order verified'}")
    return raw != result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path,
                        default=ROOT / "data/global/excel/TreasureClassEx.txt")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        raw = args.path.read_bytes()
        fixed = reorder(raw)
        assert fixed == raw, "RA treasure classes require reordering"
        assert reorder(fixed) == fixed
        print("PASS: RA references resolve backward; row bytes and vanilla order preserved; idempotent")
    else:
        fix_file(args.path)
