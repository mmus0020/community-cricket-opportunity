# Phase 10 — Exploratory Data Analysis (EDA)

## Project
**Where Are Australia’s Next Community Cricketers?**

## Status
**COMPLETE — CORE EDA ON PHASE 9 MASTER DATASET**

## Analytical population
- 548 current master geography records.
- 546 have age data.
- Main comparable ranking set: 542 records.
- Unincorporated ACT is retained because it represents the ACT geography.
- Four small residual unincorporated-area records in NSW, Victoria, South Australia and NT are excluded from comparative rankings.
- East Arnhem and Groote Archipelago remain unavailable for age-based analysis due to the 2025 geographic restructure.

## Main findings
1. Absolute junior market size is overwhelmingly a large-population signal (Spearman total population vs age 5–14 ≈ 0.993).
2. Girls 5–14 and total age 5–14 counts are essentially the same market-size signal (Spearman ≈ 1.000).
3. Five-year total population growth and junior growth are related but not interchangeable (Spearman ≈ 0.567).
4. Absolute size and demographic intensity identify different opportunities: only 3 LGAs overlap between the top 20 for junior count and top 20 for junior share using a 5,000+ population guardrail.
5. Major absolute junior growth areas include Wyndham, Blacktown, Melton, Casey, Logan, Camden and Hume.
6. Some very large junior markets are shrinking: Canterbury-Bankstown, Central Coast (NSW) and Northern Beaches have negative 2019–2024 junior growth.
7. Percentage-growth rankings are volatile for small populations, supporting use of absolute change and minimum-size/peer safeguards.
8. State/territory youth trajectories differ materially; Western Australia is strongest among the large states in aggregate 2019–2024 youth growth, while Tasmania is negative.
9. IRSD has only weak rank relationships with population and junior growth, supporting its current role as contextual rather than a direct opportunity-score component.

## Methodological decisions carried forward
- Represent market size once; do not fully weight total population, junior count and girls count independently.
- Keep Market Size, Demographic Intensity and Growth Momentum separate.
- Raw girls count should not become a separate full-strength opportunity factor.
- Use both absolute junior change and percentage junior growth.
- Apply guardrails before percentage-growth scoring.
- Do not create a final Opportunity Potential score until the cultural-demographic layer is resolved or formally excluded.
- System Readiness remains untestable until cricket supply data exists.

## Phase 10 conclusion
EDA supports the Phase 6 architecture but simplifies it. **Market size should be represented once, while growth and relative youth concentration add genuinely different information.** No final opportunity score or ranking has been created.
