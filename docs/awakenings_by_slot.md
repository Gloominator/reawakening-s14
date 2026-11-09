# Awakenings — every slot, effects and chances (S14 port)

Reference for the **local Reawakening S14 port**, derived from its current game tables on 2026-11-09. Includes **all 165 enabled Vial of Awakening outcomes**: 10 equipment categories × 16 outcomes, plus 5 unique-charm outcomes.

## Contents

- [How awakening works](#how-awakening-works)
- [Weapons](#weapons)
- [Helms](#helms)
- [Body armor](#body-armor)
- [Shields](#shields)
- [Gloves](#gloves)
- [Boots](#boots)
- [Belts](#belts)
- [Amulets](#amulets)
- [Rings](#rings)
- [Quivers](#quivers)
- [Unique charms](#unique-charms)
- [Special effects and interpretation notes](#special-effects-and-interpretation-notes)
- [Ember-awakened skills](#ember-awakened-skills)
- [Sources and verification](#sources-and-verification)

## How awakening works

1. Cube an eligible item with **1 Vial of Awakening (`dvia`)**. The initialization recipe assigns an awakening factor from **1 to 1000** and returns the vial.
2. **Transmute again with that vial** to apply the outcome selected by the factor. The item is retained and the vial is consumed. This is a two-stage roll, not two vial costs.
3. The success recipe marks the item awakened and adds an internal factor of 1001 to prevent ordinary repeated awakening. There is **no destruction/brick outcome in these Vial outcome tables**.

**Chances:** equipment categories have eight outcomes at **9.5% each** and eight at **3% each**. Unique charms have five outcomes at **20% each**. These are the probabilities implied by the 1–1000 factor and ascending first-match thresholds; see verification caveats below. They are **not** the `mod N chance=100` fields, which control application of a property after selection.

The **Factor** column shows the disjoint roll interval for that outcome. Each table covers 1–1000 exactly. An effect range such as `+100–150%` is the property's value range, not its outcome chance. Effects joined by semicolons are granted **together**, not alternative rolls. In-combat proc percentages are written explicitly in the effect column.

**Eligibility:** equipment recipes match item types without a quality restriction; charms explicitly require **unique** quality. Helms include circlets, Barbarian helms and Druid pelts through item-type inheritance. Shields include Paladin shields and Necromancer heads. Quivers use the missile-item type (`misl`). There are no separate Vial awakening pools for jewels or ordinary magic charms.

## Weapons

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +20% Faster Cast Rate |
| 9.5% | 96–190 | +100–150% Enhanced Damage |
| 9.5% | 191–285 | +40% Increased Attack Speed |
| 9.5% | 286–380 | +4–5% Fire Skill Damage |
| 9.5% | 381–475 | +4–5% Lightning Skill Damage |
| 9.5% | 476–570 | +50–80% Enhanced Damage; +6% Life Stolen per Hit |
| 9.5% | 571–665 | +4–5% Cold Skill Damage |
| 9.5% | 666–760 | +4–5% Poison Skill Damage |
| 3% | 761–790 | +30–40% Crushing Blow; +30–40% Enhanced Damage |
| 3% | 791–820 | +10% Faster Cast Rate; +10% Increased Attack Speed; −5–10% Enemy Fire Resistance |
| 3% | 821–850 | +10% Faster Cast Rate; +10% Increased Attack Speed; −5–10% Enemy Lightning Resistance |
| 3% | 851–880 | +10% Faster Cast Rate; +10% Increased Attack Speed; −5–10% Enemy Cold Resistance |
| 3% | 881–910 | +10% Faster Cast Rate; +10% Increased Attack Speed; −5–10% Enemy Poison Resistance |
| 3% | 911–940 | +30% Increased Attack Speed; +150–200% Enhanced Damage |
| 3% | 941–970 | +50 to Maximum Damage; −5% Enemy Physical Resistance |
| 3% | 971–1000 | +1 to All Skills |

## Helms

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +8% Physical Damage Reduction |
| 9.5% | 96–190 | +3–4% Fire Absorb |
| 9.5% | 191–285 | +3–4% Lightning Absorb |
| 9.5% | 286–380 | +3–4% Cold Absorb |
| 9.5% | 381–475 | +10–20% Faster Cast Rate; +2–4 Mana after Each Kill |
| 9.5% | 476–570 | +10–20% Increased Attack Speed; +20–30% Faster Run/Walk |
| 9.5% | 571–665 | +10–20% Increased Chance of Blocking; +20–30% Faster Block Rate |
| 9.5% | 666–760 | +15–20% Faster Hit Recovery; +3–8% Maximum Life; +3–8% Maximum Mana |
| 3% | 761–790 | +1 to All Skills; +10% Faster Cast Rate; +10% Increased Attack Speed |
| 3% | 791–820 | +2 to one random Class’s Skills (not necessarily your class) |
| 3% | 821–850 | +30–40 to Maximum Damage; −4–5% Enemy Physical Resistance |
| 3% | 851–880 | +20% Melee Splash Radius |
| 3% | 881–910 | +5–8% Fire Skill Damage; −4–5% Enemy Fire Resistance |
| 3% | 911–940 | +5–8% Lightning Skill Damage; −4–5% Enemy Lightning Resistance |
| 3% | 941–970 | +5–8% Cold Skill Damage; −4–5% Enemy Cold Resistance |
| 3% | 971–1000 | +5–8% Poison Skill Damage; −4–5% Enemy Poison Resistance |

## Body armor

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +10–15% Maximum Life |
| 9.5% | 96–190 | +10–15% Maximum Mana |
| 9.5% | 191–285 | +5–8 Life after Each Kill |
| 9.5% | 286–380 | +5–8 Mana after Each Kill |
| 9.5% | 381–475 | +3–5 Life after Each Kill; +3–5 Mana after Each Kill |
| 9.5% | 476–570 | +20% Faster Cast Rate |
| 9.5% | 571–665 | +20% Increased Attack Speed |
| 9.5% | 666–760 | +30% Faster Run/Walk |
| 3% | 761–790 | Level 36 Energy Shield when Equipped; +20 Energy Shield efficiency units (20/16; see notes) |
| 3% | 791–820 | +2 to one random Class’s Skills (not necessarily your class) |
| 3% | 821–850 | +5–8% Fire Skill Damage; −4–5% Enemy Fire Resistance |
| 3% | 851–880 | +5–8% Lightning Skill Damage; −4–5% Enemy Lightning Resistance |
| 3% | 881–910 | +5–8% Cold Skill Damage; −4–5% Enemy Cold Resistance |
| 3% | 911–940 | +5–8% Poison Skill Damage; −4–5% Enemy Poison Resistance |
| 3% | 941–970 | +1 Maximum Curse |
| 3% | 971–1000 | +30–40 to Maximum Damage; −4–5% Enemy Physical Resistance |

## Shields

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +20% Increased Chance of Blocking; +20% Faster Block Rate |
| 9.5% | 96–190 | +10% Faster Hit Recovery; +20% Faster Block Rate |
| 9.5% | 191–285 | 3% chance to cast level 12 Cyclone Armor on Casting |
| 9.5% | 286–380 | 6% chance to cast level 12 Cyclone Armor on Striking |
| 9.5% | 381–475 | 3% chance to cast level 12 Bone Armor on Casting |
| 9.5% | 476–570 | 6% chance to cast level 12 Bone Armor on Striking |
| 9.5% | 571–665 | Level 21 Chilling Armor when Equipped |
| 9.5% | 666–760 | Level 6 Quickness (Burst of Speed) when Equipped |
| 3% | 761–790 | +20% Faster Cast Rate |
| 3% | 791–820 | +2–3% to All Maximum Resistances |
| 3% | 821–850 | Level 12 Redemption Aura when Equipped |
| 3% | 851–880 | Level 12 Holy Freeze Aura when Equipped |
| 3% | 881–910 | Level 12 Vigor Aura when Equipped |
| 3% | 911–940 | Level 12 Defiance Aura when Equipped |
| 3% | 941–970 | Level 12 Fanaticism Aura when Equipped |
| 3% | 971–1000 | +1 to All Skills |

## Gloves

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +10% Faster Cast Rate; +2–3 Life after Each Kill |
| 9.5% | 96–190 | +10% Faster Cast Rate; +2–3 Mana after Each Kill |
| 9.5% | 191–285 | +60–90% Enhanced Damage; +25% Deadly Strike |
| 9.5% | 286–380 | +80–120% Enhanced Damage; Ignore Target’s Defense |
| 9.5% | 381–475 | +8–10% Fire Skill Damage |
| 9.5% | 476–570 | +8–10% Lightning Skill Damage |
| 9.5% | 571–665 | +8–10% Cold Skill Damage |
| 9.5% | 666–760 | +8–10% Poison Skill Damage |
| 3% | 761–790 | 13% chance to cast level 20 Lower Resist on Striking |
| 3% | 791–820 | Cannot Be Frozen |
| 3% | 821–850 | −10–15% Enemy Physical Resistance |
| 3% | 851–880 | −10–15% Enemy Fire Resistance |
| 3% | 881–910 | −10–15% Enemy Lightning Resistance |
| 3% | 911–940 | −10–15% Enemy Cold Resistance |
| 3% | 941–970 | −10–15% Enemy Poison Resistance |
| 3% | 971–1000 | +1 to All Skills |

## Boots

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +10% Increased Chance of Blocking; +100–150 Defense |
| 9.5% | 96–190 | +10% Faster Cast Rate |
| 9.5% | 191–285 | +10% Increased Attack Speed |
| 9.5% | 286–380 | +10–15 to All Resistances |
| 9.5% | 381–475 | +1% to All Maximum Resistances |
| 9.5% | 476–570 | +4–6% Life Stolen per Hit; +2–4 Life after Each Kill |
| 9.5% | 571–665 | +4–6% Mana Stolen per Hit; +2–4 Mana after Each Kill |
| 9.5% | 666–760 | +60–100% Enhanced Defense; +50–70% Better Chance of Getting Magic Items |
| 3% | 761–790 | +9% Physical Damage Reduction |
| 3% | 791–820 | Cannot Be Frozen |
| 3% | 821–850 | +4–6% Life Stolen per Hit; +4–6% Mana Stolen per Hit |
| 3% | 851–880 | +2–4 Life after Each Kill; +2–4 Mana after Each Kill |
| 3% | 881–910 | +10% Faster Run/Walk; +10% Faster Cast Rate |
| 3% | 911–940 | +10% Faster Run/Walk; +10% Increased Attack Speed |
| 3% | 941–970 | +10% Faster Run/Walk; +1–2 Life after Each Kill; +1–2 Mana after Each Kill |
| 3% | 971–1000 | +1 to All Skills |

## Belts

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +10% Faster Cast Rate |
| 9.5% | 96–190 | +10% Increased Attack Speed |
| 9.5% | 191–285 | +20% Faster Run/Walk |
| 9.5% | 286–380 | +10% Increased Chance of Blocking; +10–20% Faster Block Rate |
| 9.5% | 381–475 | +3–5% Maximum Life; +2–3 Life after Each Kill |
| 9.5% | 476–570 | +3–5% Maximum Mana; +2–3 Mana after Each Kill |
| 9.5% | 571–665 | +6–12 to All Attributes |
| 9.5% | 666–760 | +10–20 to All Resistances |
| 3% | 761–790 | +20% Faster Cast Rate |
| 3% | 791–820 | +20% Increased Attack Speed |
| 3% | 821–850 | +2–3% to All Maximum Resistances |
| 3% | 851–880 | +8% Physical Damage Reduction |
| 3% | 881–910 | +25 to Minimum Damage; +25 to Maximum Damage; +20% Deadly Strike |
| 3% | 911–940 | +2–3 Life after Each Kill; +2–3 Mana after Each Kill |
| 3% | 941–970 | Cannot Be Frozen |
| 3% | 971–1000 | +1 to All Skills |

## Amulets

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +12–15 to All Resistances |
| 9.5% | 96–190 | +2% to All Maximum Resistances |
| 9.5% | 191–285 | +4–6 Life after Each Kill |
| 9.5% | 286–380 | +4–6 Mana after Each Kill |
| 9.5% | 381–475 | +6–12 to All Attributes |
| 9.5% | 476–570 | +6–8% Maximum Life; +6–8% Maximum Mana |
| 9.5% | 571–665 | 2% chance to cast level 11 Bone Armor on Casting |
| 9.5% | 666–760 | 2% chance to cast level 11 Cyclone Armor on Casting |
| 3% | 761–790 | 13% chance to cast level 40 Bone Spear on Casting |
| 3% | 791–820 | 2% chance to cast level 35 Venom on Kill |
| 3% | 821–850 | 13% chance to cast level 40 Fist of the Heavens on Striking |
| 3% | 851–880 | 5% chance to cast level 5 Lesser Fade on Kill |
| 3% | 881–910 | 13% chance to cast level 40 Tornado on Casting |
| 3% | 911–940 | 13% chance to cast level 25 Holy Nova on Striking |
| 3% | 941–970 | 13% chance to cast level 25 Poison Nova on Striking |
| 3% | 971–1000 | +1 to All Skills |

## Rings

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +6–9% Life Stolen per Hit |
| 9.5% | 96–190 | +6–9% Mana Stolen per Hit |
| 9.5% | 191–285 | +4–6 Life after Each Kill |
| 9.5% | 286–380 | +4–6 Mana after Each Kill |
| 9.5% | 381–475 | +10% Faster Cast Rate |
| 9.5% | 476–570 | +10% Increased Attack Speed |
| 9.5% | 571–665 | +10% Faster Run/Walk |
| 9.5% | 666–760 | +10% Increased Chance of Blocking; +10% Faster Block Rate |
| 3% | 761–790 | Cannot Be Frozen |
| 3% | 791–820 | +2–4 Life after Each Kill; +2–4 Mana after Each Kill |
| 3% | 821–850 | +4–6% Life Stolen per Hit; +4–6% Mana Stolen per Hit |
| 3% | 851–880 | Level 10 Sanctuary Aura when Equipped |
| 3% | 881–910 | Level 10 Conviction Aura when Equipped |
| 3% | 911–940 | Level 10 Salvation Aura when Equipped |
| 3% | 941–970 | Level 10 Blade Shield when Equipped |
| 3% | 971–1000 | +1 to All Skills |

## Quivers

| Chance | Factor | Awakening effects |
|---|---|---|
| 9.5% | 1–95 | +3–6% Life Stolen per Hit |
| 9.5% | 96–190 | +10–20% Enhanced Damage |
| 9.5% | 191–285 | +20% Faster Run/Walk |
| 9.5% | 286–380 | +4–5% Fire Skill Damage |
| 9.5% | 381–475 | +4–5% Lightning Skill Damage |
| 9.5% | 476–570 | +4–5% Cold Skill Damage |
| 9.5% | 571–665 | +4–5% Poison Skill Damage |
| 9.5% | 666–760 | +10% Increased Attack Speed |
| 3% | 761–790 | +20% Increased Attack Speed |
| 3% | 791–820 | +35–45% Enhanced Damage |
| 3% | 821–850 | +10 to Minimum Damage; +15 to Maximum Damage; +10% Deadly Strike |
| 3% | 851–880 | −10–15% Enemy Physical Resistance |
| 3% | 881–910 | Level 12 Might Aura when Equipped |
| 3% | 911–940 | Level 12 Conviction Aura when Equipped |
| 3% | 941–970 | Level 12 Fanaticism Aura when Equipped |
| 3% | 971–1000 | +1 to All Skills |

## Unique charms

| Chance | Factor | Awakening effects |
|---|---|---|
| 20% | 1–200 | +1 to All Skills |
| 20% | 201–400 | +5–10% Maximum Life; +20–40 Life |
| 20% | 401–600 | +5–10% Maximum Mana; +20–40 Mana |
| 20% | 601–800 | +5–10 to All Resistances; +5–10 to All Attributes |
| 20% | 801–1000 | +5–10% Experience Gained |

## Special effects and interpretation notes

- **“Mastery” in recipe labels means +% elemental skill damage**, not an actual +skill bonus to the Sorceress mastery skill. The tables use the actual property effect.
- **Pierce** reduces enemy resistance to the named damage type. Physical pierce is not missile-piercing chance. Negative resistance wording in the tables describes the enemy debuff; the configured pierce magnitude is positive.
- **Random class skills:** the helm/body outcome grants **+2 to one class’s skills**, selected from the seven classes. It is not +2 All Skills and does not guarantee your own class. The outcome is 3%; assuming equal class selection, a particular class would be approximately **0.4286% per awakening** (3% ÷ 7). Equal class-selection probability was not engine-verified.
- **Body armor Energy Shield:** grants level 36 Energy Shield while equipped **and** `es-efficiency=20`. Properties.txt labels the latter in sixteenths (20/16 = 1.25 ratio units), not +20% absorption. Skills.txt applies it to the mana-cost ratio with a minimum of 14/16; do not read it as an uncapped additional 1.25 reduction on top of the minimum.
- **Equipped skills** are self-aura variants, distinct from a chance to cast. Quickness is the Burst of Speed effect; Blade Shield is the equipped self-aura variant rather than a party aura. Chilling Armor's local self-aura additionally has +5 blocking and a level-scaled defense bonus. Exact performance/damage follows the local skill tables.
- **Lower Resist on gloves** uses the `LowRes Proc` skill (ID 447), not the ordinary castable skill. Its local level-20 formula lowers fire/lightning/cold/poison resistance by 39 before any engine resistance rules.
- **Lesser Fade** is its own proc skill, not full Fade. Its local level-5 formulas grant 10 all elemental resistance, 18 curse resistance and 5 physical damage resistance for 750 frames (30 seconds at 25 fps).
- **Enhanced Defense vs. Enhanced Damage:** the common boots roll is **+60–100% Enhanced Defense** with +50–70% magic find. Keep these separate from off-weapon Enhanced Damage on gloves or quivers.
- **Flat damage:** separate minimum and maximum damage properties are listed individually. For example, belt +25 minimum and +25 maximum damage is a +25–25 damage bonus, not a random roll from +25 to +25 maximum only.
- **Orb of Unmaking:** the current recipes keep the item and existing bonuses, adjust its internal awakening markers, and add the one-use `unmaking` marker. The item description says this allows **one additional awakening while keeping properties intact**. The older cube-summary document’s “strips/scours” wording should not be used to interpret this mechanic. In-game acceptance testing remains advisable.

## Ember-awakened skills

These are a **separate system** from the random Vial bonuses above. The enabled recipes take **Hellfire Torch or Annihilus + 1 Hatred/Terror Ember**, with a class-specific recipe. They are deterministic for the matching class recipe, **not another roll from the Vial pool**. Do not interpret “100%” as bypassing recipe eligibility or allowing unlimited reapplication.

| Class | Hatred Ember | Terror Ember |
|---|---|---|
| Amazon | Awakened Multiple Shot | Awakened Cold Arrow |
| Sorceress | Awakened Charged Bolt | Awakened Blizzard |
| Necromancer | Awakened Teeth | Awakened Bone Spear |
| Paladin | Awakened Concentration | Awakened Blessed Hammer |
| Barbarian | Awakened Concentrate | Awakened War Cry |
| Druid | Awakened Cyclone Armor | Awakened Tornado |
| Assassin | Awakened Fade of Speed | Awakened Mind Blast |

This appendix identifies the separate skill conversions; it is not a full damage/synergy guide for those 14 skills. Their formulas are in Skills.txt and descriptions in SkillDesc.txt. Fate-card rewards that arrive already awakened are likewise fixed rewards, not additional random Vial outcomes (for example, Legacy of Cain’s +1 All Skills unique ring).

## Sources and verification

Paths below are relative to `reawakening-s14/`:

- [Existing cube-recipe summary](ra_cube_recipes.md), section 1: the first documentation checked. It lists broad outcome families, but lacks precise Vial chances and values.
- [`data/global/excel/CubeMain.txt`](../data/global/excel/CubeMain.txt): six initialization recipes named `add awaken factor ...`, followed by all 165 enabled Vial outcome recipes. Source of every effect, range, proc level/chance and outcome threshold above.
- [`data/global/excel/Properties.txt`](../data/global/excel/Properties.txt): property interpretation. `awakennum` maps to `awakener`; proc property annotations explicitly define parameter = skill, minimum = trigger chance, maximum = skill level. `randclassskill2` uses function 36 with a fixed +2 class-skill value.
- [`data/global/excel/ItemStatCost.txt`](../data/global/excel/ItemStatCost.txt): `awakener` is stat **487**, matching the ported CubeMain conditions.
- [`data/global/excel/Skills.txt`](../data/global/excel/Skills.txt): names/formulas for referenced skills, including equipped variants 554–557, Lesser Fade 391 and Lower Resist proc 447.
- [`data/global/excel/ItemTypes.txt`](../data/global/excel/ItemTypes.txt): slot/type inheritance.

**Static checks:** all 165 listed outcomes are enabled, use `op=16`/stat 487, and have guaranteed property application. Each equipment table’s threshold increments are 95 × 8 and 30 × 8; the charm table uses 200 × 5. Every pool sums to 100%. CubeMain.txt and Properties.txt were also confirmed byte-identical to their installed `ProjectD2/data/global/excel/` copies at inspection time.

**Probability caveat:** the percentages are data-derived under the standard inclusive 1–1000 uniform roll and first-matching `stat <= threshold` recipe interpretation. Ascending thresholds, the zero-factor initializer, and terminal marker support that interpretation; existing local documentation also describes `op=16` as ordered thresholds. The closed-source engine evaluator/RNG was not independently inspected, and no statistical in-game trial was performed. Matching text files does not establish which compiled BIN/MPQ files a running game loads. This document describes the local port’s configuration, not a claim about every upstream Reawakening version.
