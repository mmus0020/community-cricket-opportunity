# Phase 17 — Power BI Dashboard

## Status
**COMPLETE — POWER BI-READY DASHBOARD PACKAGE**

A native `.pbix` cannot be generated in this environment, so Phase 17 delivers the complete reproducible build package: analysis-ready CSV tables, DAX measures, Power Query types, theme JSON, page specification, and visual prototype.

## Data model

### Fact / main analytical table
**Opportunity**
Source: `powerbi_opportunity_lga.csv`
Grain: one row per eligible LGA.

### Supporting table
**CaseStudies**
Source: `powerbi_case_studies.csv`
Grain: one row per Phase 14 case-study LGA.

### Supporting table
**Limitations**
Source: `powerbi_limitations.csv`
Grain: one row per documented limitation.

No relationship is required for Limitations. CaseStudies can relate to Opportunity via LGA_NAME if desired.

## Page 1 — Executive Overview
Purpose: 30-second national view.

KPI cards:
- LGA Count
- Very High Opportunity LGAs
- Robust Top-20 LGAs
- Junior Market

Visuals:
1. Top 15 horizontal bar chart:
   - Axis: LGA_NAME
   - Value: SCORE_BALANCED
   - Sort descending
2. Scatter:
   - X: SCORE_MARKET_SIZE
   - Y: SCORE_GROWTH_MOMENTUM
   - Size: AGE_5_14_2024
   - Legend: STRATEGIC_SEGMENT
3. Opportunity-tier bar/donut.
4. Slicers:
   - STATE
   - OPPORTUNITY_TIER
   - STRATEGIC_SEGMENT

Executive warning card:
"Opportunity Potential is a relative demographic prioritisation score. It does not measure actual cricket demand, participation penetration, or System Readiness."

## Page 2 — Geographic Opportunity
Use the official ABS 2025 LGA boundary layer.

Preferred visual:
- Shape Map / Azure Maps polygon layer
- Join field: LGA_CODE
- Fill: SCORE_BALANCED
- Tooltip:
  - RANK_BALANCED
  - SCORE_BALANCED
  - SCORE_MARKET_SIZE
  - SCORE_YOUTH_INTENSITY
  - SCORE_GROWTH_MOMENTUM
  - AGE_5_14_2024
  - AGE_5_14_CHANGE_5Y
  - AGE_5_14_GROWTH_5Y_PCT

Add a State slicer and a text callout:
"94.6% of the Top-20 absolute junior-population increase was concentrated in four major growth systems."

## Page 3 — LGA Deep Dive
Slicer: LGA_NAME

Cards:
- Selected LGA Rank
- Selected LGA Score
- Selected LGA Junior Market
- Selected LGA Junior Growth
- Selected LGA Growth %

Clustered column chart:
- Market Size percentile
- Youth Intensity percentile
- Growth Momentum percentile

Text/table:
- Opportunity Tier
- Strategic Segment
- Suggested Response

## Page 4 — Strategic Segmentation
Scatter:
- X = SCORE_MARKET_SIZE
- Y = SCORE_GROWTH_MOMENTUM
- Size = AGE_5_14_2024
- Legend = STRATEGIC_SEGMENT

Supporting table:
- LGA_NAME
- STATE
- SCORE_BALANCED
- OPPORTUNITY_TIER
- STRATEGIC_SEGMENT

This page answers:
**Why does an LGA rank highly?**

## Page 5 — Case Studies
Feature:
- Wyndham
- Blacktown
- Ipswich
- Armadale
- Maitland

For each show:
- rank / opportunity score
- pillar profile
- current junior market
- 5-year junior growth
- external evidence signal
- Phase 14 working interpretation
- next management question

## Page 6 — Validation & Limitations
Visuals:
1. Weight-sensitivity Top-20 overlap.
2. Eligibility-sensitivity Top-20 overlap.
3. Limitations table by severity.
4. Claim-boundary callout.

Primary message:
**The model is robust as a screening tool but is not predictively validated against future cricket registrations.**

## Interaction rules
- State slicer filters pages 1–4.
- LGA slicer on Deep Dive should be single-select.
- Clicking a Top-15 bar should cross-filter segmentation visuals.
- Tooltips should show the three pillar scores.
- Keep Case Studies and Limitations largely narrative to avoid false numerical precision.

## Visual design
Use `POWERBI_THEME.json`.

Principles:
- Deep navy headers.
- White cards on light grey background.
- Teal/green for opportunity.
- Amber for caution.
- Red only for critical limitations.
- Minimal decorative cricket imagery.
- Use whitespace and short chart titles.

## Portfolio output
When the PBIX is built:
1. Save as `Community_Cricket_Opportunity_Dashboard.pbix`.
2. Export all pages to PDF.
3. Capture Executive Overview and LGA Deep Dive screenshots for GitHub README.
4. Include the model limitation statement in the README.
