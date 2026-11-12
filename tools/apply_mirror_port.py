#!/usr/bin/env python3
"""Apply the owner's CUSTOM Lilith's Mirror and fate-card gameplay preferences.

WARNING: This is a personal customization, not a faithful RA-to-S14 port.
Some recipes draw from Single Player Plus, but the resulting rules and balance
are the owner's own choices. See docs/custom_mirror_changes.md. The historical
filename is retained for existing workflows; it does not imply upstream parity.

Idempotent. Data-only; no DLL or engine change.

What it does:
  * TreasureClassEx.txt: sets the Ancient-Orb-anchored quality scalars on the
    three `Lillith Mirror N/NM/H` rows (Unique 15000 -> 15000/7500/2500, Set 100).
    These rows carry no picks and no items; ProjectDiablo.dll resolves the
    mirror by row name, so the `Unique` cell *is* the drop rate. NOTE the column
    is a quality DIVISOR: lower value = more common. SP+'s 75000/37500/5000
    was therefore a Normal/Nightmare nerf, not the uniform increase it looks
    like, so it is deliberately not copied.
  * CubeMain.txt:
      - reduces The False Reflection turn-in from 9 cards to 1.
      - strips the `mirrored` (ItemStatCost 486) mod from every recipe that
        consumes `llmr`, so mirrored copies stay re-mirrorable and carry no
        "Mirrored" affix line. Nothing in any table gates on stat 486.
      - enables the mirror rows PD2 ships disabled (unique ring, magic / rare /
        craft jewel).
      - appends the SP+ set-item rows plus the extra targets: maps, jewels,
        unique charms, Larzuk's Puzzle Box/Piece, Orb of Unmaking, Demonic Cube,
        Catalyst Shard, Standard of Heroes, Worldstone Shards and Invader Ears.
        Map rows carry no op=18 corruption gate, so corrupted (and heroic /
        mapevent-sharded) maps mirror with all their map_* mods intact.
      - appends `2x <card> + key -> random fate card` for all 60 fate shards,
        reusing the existing `void` ItemType output proven by
        "1 of The Void -> random card".
      - replaces the superseded `TEST - Gheed box` row with five cheap vendor
        sink recipes (potion + scroll/key) for in-game verification.
  * Deletes stale cubemain.bin / treasureclassex.bin so the game recompiles,
    syncs both edited tables to the ProjectD2 install tree.

Preserves CRLF, Latin-1, 105 CubeMain / 33 TCEx column widths and *eol/Term=0.
Run from anywhere: `python3 tools/apply_mirror_port.py`.
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
CUBE = ROOT / "data/global/excel/CubeMain.txt"
TCEX = ROOT / "data/global/excel/TreasureClassEx.txt"
INSTALL = ROOT.parent / "ProjectD2/data/global/excel"

STALE_BINS = ["cubemain.bin", "treasureclassex.bin"]

# TreasureClassEx Unique/Set are QUALITY DIVISORS: lower value = more common.
# Evidence: docs/tc_boosts.md calls the mod's 37500/25000 -> 15000 change "more
# generous", and ItemRatio's Uber row is more generous than the Normal row with a
# lower divisor. So SP+'s 75000/37500/5000 is NOT a uniform increase: it makes
# Normal and Nightmare far RARER than the flat 15000 this tree shipped.
#
# Anchored to the Ancient Orb (`mfo`), which the Fate/Orbs route makes reachable:
#   Hell  Act X Good : ~1/2343 per roll   Map Good t1-t3 : ~1/1237 per roll
# Mirror target: no Nerf on Normal, double Nightmare, and Hell in the Ancient-Orb
# ballpark. These rows have no picks and no items and are resolved by
# ProjectDiablo.dll by row name, so the value cannot be verified offline.
MIRROR_TC = {
    "Lillith Mirror N": ("15000", "100"),
    "Lillith Mirror NM": ("7500", "100"),
    "Lillith Mirror H": ("2500", "100"),
}

# The False Reflection turn-in: PD2 asks for 9 cards, we want 1.
CARD_TO_MIRROR = {
    "old": "9 of The False Reflection -> mirror",
    "new": "1 of The False Reflection -> mirror",
    "input": "fsfr,qty=1",
}

# PD2 ships these mirror rows disabled (`enabled=0`); SP+ turns them on.
ENABLE_BY_DESC = [
    "Lillith's Mirror ring (uni)",
    "Lillith's Mirror jewl (magic)",
    "Lillith's Mirror jewl (rare)",
    "Lillith's Mirror jewl (craft)",
]

# (description, input 1, non-corrupted gate) - appended after the shipped rows.
# The gate is op=18 / param=361 / value=0, the same filter SP+ uses on gear.
NEW_MIRROR = [
    ("Mirror set armor", "armo,set", True),
    ("Mirror set weapon", "weap,set", True),
    ("Mirror set ring", "ring,set", True),
    ("Mirror set amulet", "amul,set", True),
    # `map` already resolves t1m/t2m/t3m and the t1me..t5me exc types; t4m and
    # t5m have a blank Equiv1 so they need their own rows.
    ("Mirror map", "map", False),
    ("Mirror map t4", "t4m", False),
    ("Mirror map t5", "t5m", False),
    # Stackable currency uses ,qty=1 to match PD2's own rows (a bare code on a
    # stackable can consume the whole stack).
    ("Mirror Larzuk's Puzzle Box", "lbox,qty=1", False),
    ("Mirror Larzuk's Puzzle Piece", "lpp,qty=1", False),
    ("Mirror Orb of Unmaking", "oou,qty=1", False),
    ("Mirror Demonic Cube", "imrn,qty=1", False),
    ("Mirror Catalyst Shard", "iwss,qty=1", False),
    ("Mirror Standard of Heroes", "std,qty=1", False),
    ("Mirror Worldstone Shard", "wss,qty=1", False),
    ("Mirror Corrupted Worldstone Shard", "cwss,qty=1", False),
    ("Mirror Awakening Stone", "awst,qty=1", False),
    ("Mirror Invader Ear (Amazon)", "ivez,qty=1", False),
    ("Mirror Invader Ear (Assassin)", "ivea,qty=1", False),
    ("Mirror Invader Ear (Barbarian)", "iveb,qty=1", False),
    ("Mirror Invader Ear (Druid)", "ived,qty=1", False),
    ("Mirror Invader Ear (Necromancer)", "iven,qty=1", False),
    ("Mirror Invader Ear (Paladin)", "ivep,qty=1", False),
    ("Mirror Invader Ear (Sorceress)", "ives,qty=1", False),
    ("Mirror unique small charm", "cm1,uni", True),
    ("Mirror unique large charm", "cm2,uni", True),
    ("Mirror unique grand charm", "cm3,uni", True),
]

CARD_ROWS_MARK = "SP+ 2 of a kind -> random fate card"

# Superseded dev row from the SP+ box stage; the mirror test rows below replace it.
OLD_TEST_DESC = "TEST - Gheed box: Lesser Healing Potion + Town Portal Scroll"

# Throwaway cube rows for in-game checks: cheap Akara potions + scrolls/key.
# Enable with vendor mats so each target can be produced on demand.
TEST_RECIPES = [
    ("TEST - Mirror: Lesser Healing Potion + Town Portal Scroll", "hp1", "tsc", "llmr"),
    ("TEST - Puzzle Piece: Lesser Mana Potion + Town Portal Scroll", "mp1", "tsc", "lpp"),
    ("TEST - Puzzle Box: Lesser Mana Potion + Identify Scroll", "mp1", "isc", "lbox"),
    ("TEST - Orb of Unmaking: Lesser Healing Potion + Identify Scroll", "hp1", "isc", "oou"),
    ("TEST - Demonic Cube: Lesser Healing Potion + Skeleton Key", "hp1", "key,qty=1", "imrn"),
]


# ---------------------------------------------------------------- I/O helpers
def read_txt(path: Path):
    text = path.read_bytes().decode("latin1")
    return text.replace("\r\n", "\n").split("\n"), "\r\n" in text


def write_txt(path: Path, lines, crlf: bool):
    out = "\n".join(lines)
    if crlf:
        out = out.replace("\n", "\r\n")
    path.write_bytes(out.encode("latin1"))


def append_row(lines, row):
    """Insert before the terminal empty line produced by a trailing newline."""
    if lines and lines[-1] == "":
        lines.insert(len(lines) - 1, row)
    else:
        lines.append(row)


CUBE_W = 105
TCEX_W = 33


def cube_row(**kw):
    c = [""] * CUBE_W
    c[0] = kw.get("description", "")
    c[1] = str(kw.get("enabled", "1"))
    c[2] = str(kw.get("ladder", ""))
    c[3] = str(kw.get("min diff", ""))
    c[4] = str(kw.get("version", "100"))
    c[5] = str(kw.get("op", ""))
    c[6] = str(kw.get("param", ""))
    c[7] = str(kw.get("value", ""))
    c[9] = str(kw.get("numinputs", "1"))
    c[10] = kw.get("input_1", "")
    c[11] = kw.get("input_2", "")
    c[17] = kw.get("output", "")
    c[19] = str(kw.get("plvl", ""))
    c[21] = kw.get("mod_1", "")
    c[22] = str(kw.get("mod_1_chance", ""))
    c[23] = str(kw.get("mod_1_param", ""))
    c[24] = str(kw.get("mod_1_min", ""))
    c[25] = str(kw.get("mod_1_max", ""))
    c[46] = kw.get("output_b", "")
    c[50] = kw.get("b_mod_1", "")
    c[51] = str(kw.get("b_mod_1_chance", ""))
    c[53] = str(kw.get("b_mod_1_min", ""))
    c[54] = str(kw.get("b_mod_1_max", ""))
    c[104] = "0"
    return "\t".join(c)


# ---------------------------------------------------------------- CubeMain
def do_cube():
    lines, crlf = read_txt(CUBE)
    hdr = lines[0].split("\t")
    assert len(hdr) == CUBE_W, len(hdr)
    H = {h: i for i, h in enumerate(hdr)}
    e_i, d_i = H["enabled"], H["description"]
    inputs = [H[f"input {k}"] for k in range(1, 8)]
    mods = [(H[f"mod {k}"], H[f"mod {k} chance"], H[f"mod {k} param"],
             H[f"mod {k} min"], H[f"mod {k} max"]) for k in range(1, 6)]
    bmods = [(H[f"b mod {k}"], H[f"b mod {k} chance"], H[f"b mod {k} param"],
              H[f"b mod {k} min"], H[f"b mod {k} max"]) for k in range(1, 6)]

    stripped = enabled = renamed = 0
    existing = set()
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():
            continue
        c = line.split("\t")
        assert len(c) == CUBE_W, (i + 1, len(c))
        if c[d_i] == OLD_TEST_DESC:
            # Superseded by TEST_RECIPES below; drop the whole row.
            lines[i] = None
            continue
        if c[d_i] == CARD_TO_MIRROR["old"]:
            # The False Reflection turn-in: 9 cards -> 1 card. This row creates
            # the mirror, so it is matched before the consumes-llmr check below.
            assert c[inputs[0]] == "fsfr,qty=9", c[inputs[0]]
            c[d_i] = CARD_TO_MIRROR["new"]
            c[inputs[0]] = CARD_TO_MIRROR["input"]
            lines[i] = "\t".join(c)
            renamed += 1
        existing.add(c[d_i])
        if "llmr" not in [c[j] for j in inputs]:
            continue
        # Check PD2/SP+ ship `dye` then `mirrored` and nothing after, so
        # clearing the mirrored slot in place leaves no gap in the mod chain.
        assert c[mods[0][0]] in ("dye", ""), (c[d_i], c[mods[0][0]])
        assert c[mods[2][0]] == "", ("unexpected mod 3 on mirror row", c[d_i])
        for grp in (mods, bmods):
            for (code, chance, param, mn, mx) in grp:
                if c[code] == "mirrored":
                    for j in (code, chance, param, mn, mx):
                        c[j] = ""
                    stripped += 1
        if c[e_i] != "1" and c[d_i] in ENABLE_BY_DESC:
            c[e_i] = "1"
            enabled += 1
        lines[i] = "\t".join(c)

    added = 0
    for desc, inp, gate in NEW_MIRROR:
        if desc in existing:
            continue
        row = dict(
            description=desc, numinputs="2", input_1=inp, input_2="llmr",
            output="useitem",
            mod_1="dye", mod_1_chance="100", mod_1_min="4", mod_1_max="4",
            output_b="useitem",
            b_mod_1="dye", b_mod_1_chance="100", b_mod_1_min="21", b_mod_1_max="21",
        )
        if gate:
            row.update(op="18", param="361", value="0")
        append_row(lines, cube_row(**row))
        added += 1

    # Every fate shard is type2=void, and `void` is an ItemType (The Void Cards)
    # whose members the cube resolves randomly - the same mechanism as the
    # shipped "1 of The Void -> random card" row.
    # Membership in the `void` output type comes from Misc.txt type2, not type.
    misc, _ = read_txt(ROOT / "data/global/excel/Misc.txt")
    mh = misc[0].split("\t")
    ci, ti, t2i = mh.index("code"), mh.index("type"), mh.index("type2")
    cards = []
    for r in misc[1:]:
        if not r.strip():
            continue
        c = r.split("\t")
        if c[ti] != "fash":
            continue
        assert c[t2i] == "void", (c[ci], c[t2i])
        cards.append(c[ci])
    assert len(cards) == 60, len(cards)
    card_rows = 0
    test_rows = 0
    for code in cards:
        desc = f"{CARD_ROWS_MARK} ({code})"
        if desc in existing:
            continue
        append_row(lines, cube_row(
            description=desc, numinputs="2",
            input_1=f"{code},qty=2", input_2="key,qty=1",
            output="void", plvl="100",
        ))
        card_rows += 1

    for desc, mat1, mat2, out in TEST_RECIPES:
        if desc in existing:
            continue
        append_row(lines, cube_row(
            description=desc, numinputs="2",
            input_1=mat1, input_2=mat2, output=out,
        ))
        test_rows += 1

    # Rows superseded above are marked None; drop them before writing.
    lines = [l for l in lines if l is not None]

    assert len(lines[0].split("\t")) == CUBE_W
    for line in lines[1:]:
        if line.strip():
            assert len(line.split("\t")) == CUBE_W, line[:80]
    write_txt(CUBE, lines, crlf)
    return stripped, enabled, added, card_rows, test_rows, renamed


# ---------------------------------------------------------------- TCEx
def do_tcex():
    lines, crlf = read_txt(TCEX)
    hdr = lines[0].split("\t")
    assert len(hdr) == TCEX_W, len(hdr)
    H = {h: i for i, h in enumerate(hdr)}
    changed = []
    for i, line in enumerate(lines[1:], 1):
        if not line.strip():
            continue
        c = line.split("\t")
        assert len(c) == TCEX_W, (i + 1, len(c))
        want = MIRROR_TC.get(c[0])
        if not want:
            continue
        if (c[H["Unique"]], c[H["Set"]]) != want:
            c[H["Unique"]], c[H["Set"]] = want
            lines[i] = "\t".join(c)
            changed.append(c[0])
    write_txt(TCEX, lines, crlf)
    return changed


# ---------------------------------------------------------------- install
def sync():
    removed = []
    for d in (ROOT / "data/global/excel", INSTALL):
        for name in STALE_BINS:
            p = d / name
            if p.exists():
                p.unlink()
                removed.append(str(p.relative_to(ROOT.parent)))
    copied = []
    for p in (CUBE, TCEX):
        dst = INSTALL / p.name
        if not dst.exists() or dst.read_bytes() != p.read_bytes():
            shutil.copy2(p, dst)
            copied.append(p.name)
    return removed, copied


def main():
    stripped, enabled, added, cards, tests, renamed = do_cube()
    tce = do_tcex()
    removed, copied = sync()
    print(f"cube: stripped {stripped} mirrored mods, enabled {enabled} rows, "
          f"added {added} mirror + {cards} card + {tests} test recipes, "
          f"renamed {renamed} turn-in")
    print(f"tc:   {', '.join(tce) if tce else 'already at target'}")
    print(f"bins removed: {', '.join(removed) if removed else 'none'}")
    print(f"sync: {', '.join(copied) if copied else 'install already current'}")


if __name__ == "__main__":
    main()
