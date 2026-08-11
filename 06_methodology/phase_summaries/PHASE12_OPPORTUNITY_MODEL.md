# Phase 12 — Participation Opportunity Model

## Project
**Where Are Australia’s Next Community Cricketers?**

## Status
**COMPLETE — COMMUNITY CRICKET OPPORTUNITY POTENTIAL MODEL V1**

## What Model V1 measures
Model V1 ranks Australian LGAs on demographic conditions relevant to future community-cricket acquisition. It does **not** measure actual cricket participation, hidden demand, registration penetration, or cricket-system readiness.

The model intentionally excludes:
- South Asian / cultural strategic-alignment variables, because that Census layer is still pending;
- cricket club/program supply, because a consistent national open dataset has not been obtained;
- SEIFA from scoring, because Phase 10 found it is better treated as contextual evidence.

## Eligibility universe
The national prioritisation ranking includes **365 LGAs**.

Guardrails:
- current total population of at least **5,000**;
- 2019 age 5–14 population of at least **500**;
- valid age data;
- residual unincorporated-area records excluded, except the ACT geography.

These safeguards reduce small-base growth volatility. Excluded areas remain in the project and can later be analysed through regional/peer benchmarking.

## Normalisation
Every model input is converted to a **percentile score from 0–100** among eligible LGAs.

Percentiles were selected because they:
- handle variables measured in different units;
- reduce domination by extreme absolute values;
- are easy for decision-makers to interpret;
- preserve relative national positioning.

## Baseline Model V1

### Pillar 1 — Market Size (33.33%)
Input: `AGE_5_14_2024`

Purpose: measures the scale of the current junior addressable market.

Phase 10 showed total population, total junior population and girls' junior population are nearly redundant. Therefore only one absolute market-size measure is included.

### Pillar 2 — Youth Concentration (33.33%)
Input: `AGE_5_14_SHARE_TOTAL_PCT`

Purpose: captures areas with unusually young demographic structures and stops the model becoming simply a ranking of Australia's largest councils.

### Pillar 3 — Growth Momentum (33.33%)
Built from:
- 50% percentile of `AGE_5_14_CHANGE_5Y`;
- 50% percentile of `AGE_5_14_GROWTH_5Y_PCT`.

Because Growth Momentum is one-third of the total model, each underlying growth indicator contributes approximately **16.67%** to the overall score.

This balances:
- **scale of additional children**, and
- **speed of junior-market growth**.

## Baseline formula

`Opportunity Potential = (Market Size + Youth Concentration + Growth Momentum) / 3`

This is a transparent prioritisation index, not a prediction model.

## Why equal pillar weights?
There is currently no observed LGA-level acquisition outcome with which to statistically optimise weights.

Assigning apparently precise weights such as 42%, 31% and 27% would therefore imply knowledge we do not possess.

Equal pillar weighting is used as the neutral baseline, followed by sensitivity analysis.

## Top 10 — Balanced Model V1

1. **Wyndham, Victoria** — 99.27
2. **Melton, Victoria** — 98.22
3. **Blacktown, New South Wales** — 97.21
4. **Ipswich, Queensland** — 96.58
5. **Camden, New South Wales** — 96.39
6. **Casey, Victoria** — 96.39
7. **Logan, Queensland** — 95.89
8. **Hume, Victoria** — 95.57
9. **The Hills, New South Wales** — 95.48
10. **Armadale, Western Australia** — 93.65

These LGAs should currently be described only as:
**higher demographic Opportunity Potential areas under Model V1**.

They must not yet be called Australia's greatest "untapped cricket markets."

## Robustness
The Top 20 is highly stable under alternative weighting assumptions:

- Growth-led model: **20/20** overlap with Balanced Top 20.
- Scale-led model: **18/20** overlap.
- Intensity-led model: **19/20** overlap.

Full-rank Spearman correlations with the Balanced model are approximately:
- Growth-led: **0.95**
- Scale-led: **0.94**
- Intensity-led: **0.98**

The following **18 LGAs** appear in the Top 20 under all four weighting scenarios:

Wyndham, Melton, Blacktown, Ipswich, Camden, Casey, Logan, Hume, The Hills, Armadale, Liverpool, Campbelltown (NSW), Whittlesea, Swan, Wanneroo, Playford, Cardinia, Rockingham

This stability indicates that the leading areas are not an artefact of one narrow set of weights.

## Guardrail sensitivity
Changing the eligibility thresholds also produces a stable Top 20:
- 2,500 population / 250 junior base: **19/20** overlap;
- 5,000 / 500 baseline: **20/20**;
- 10,000 / 1,000: **20/20**;
- 20,000 / 1,500: **19/20**.

Therefore the main candidate set is robust to reasonable small-market thresholds.

## What the model reveals
The leading areas are dominated by the same growth systems identified in Phase 11:
- Melbourne outer growth belt;
- western / south-west Sydney;
- South East Queensland;
- Perth growth belt.

This is expected because these areas combine:
1. meaningful current junior-market scale;
2. relatively young populations;
3. substantial recent junior-population growth.

## What the model does NOT yet reveal
Model V1 cannot determine:
- whether cricket participation is currently low or high;
- whether existing clubs have spare capacity;
- whether children in an LGA want to play cricket;
- whether South Asian or other culturally important cricket communities are well represented;
- whether investment will generate a specific number of registrations.

Those questions require additional evidence.

## Model interpretation
A high Model V1 score means:

> An LGA combines relatively strong current junior-market scale, youth concentration and recent junior-population growth compared with other sufficiently sized Australian LGAs.

It does **not** mean:

> Cricket Australia should automatically invest there.

The correct next question is:

> Does local cricket participation and delivery capacity match this demographic opportunity?

## Phase 12 conclusion
Model V1 successfully converts the Phase 10 and Phase 11 evidence into a reproducible national demographic opportunity index.

The model is intentionally simple, transparent and robust.

It should be treated as the **Opportunity Potential side** of the final decision-support framework. Cricket System Readiness remains a separate future dimension.

No final strategic segment or recommended intervention has yet been assigned.
