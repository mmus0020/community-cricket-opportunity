# Phase 17 — Power BI Dashboard Specification

## Page 1 — Executive Overview
Purpose: Give a hiring manager a 30-second national view.

Visuals:
1. KPI cards:
   - Eligible LGAs
   - Very High Opportunity LGAs
   - Top-20 Robust LGAs
   - Total junior market represented
2. Horizontal bar chart: Top 15 LGAs by Opportunity Potential
3. Scatter plot:
   - X = Market Size percentile
   - Y = Growth Momentum percentile
   - Size = Age 5–14 population
   - Legend = Strategic Segment
4. Opportunity Tier donut/bar
5. Slicers: State, Opportunity Tier, Strategic Segment

## Page 2 — Geographic Opportunity
1. Filled map using official ABS 2025 LGA boundaries when loaded into Power BI
2. Map measure = Opportunity Potential
3. Tooltip:
   - Rank
   - Market Size
   - Youth Intensity
   - Growth Momentum
   - 5–14 population
   - 5-year junior growth
4. State slicer
5. Top-growth corridor text callout

## Page 3 — LGA Deep Dive
Use an LGA slicer.
Cards:
- National rank
- Opportunity score
- Current 5–14 population
- 5-year absolute junior growth
- 5-year growth %
Clustered bars:
- Market Size percentile
- Youth Intensity percentile
- Growth Momentum percentile
Context table:
- Opportunity Tier
- Strategic Segment
- Suggested response

## Page 4 — Strategic Segmentation
1. Scatter: Market Size vs Growth Momentum
2. Legend = Strategic Segment
3. Table of top LGAs by segment
4. Segment count chart
5. Text explaining:
   - Balanced High Opportunity
   - Large Growth
   - Emerging Young Growth
   - Large Established / Slower Growth
   - Rapid Growth
   - Mixed / Moderate

## Page 5 — Case Studies
Feature:
- Wyndham
- Blacktown
- Ipswich
- Armadale
- Maitland

For each:
- Model rank and score
- Pillar profile
- Local evidence
- Working interpretation
- Recommended next question

## Page 6 — Validation & Limitations
1. Weight sensitivity chart
2. Eligibility sensitivity chart
3. Validation status cards
4. Limitations table
5. Explicit warning:
   "Opportunity Potential is a relative demographic prioritisation score. It does not measure actual cricket demand, participation penetration, or System Readiness."

## Recommended theme
Clean Cricket Australia-inspired palette:
- Deep navy background/headers
- White cards
- Teal/green accents for opportunity
- Amber for caution
- Red only for limitations/critical warnings

Keep the dashboard professional and restrained; avoid decorative cricket imagery that reduces analytical clarity.
