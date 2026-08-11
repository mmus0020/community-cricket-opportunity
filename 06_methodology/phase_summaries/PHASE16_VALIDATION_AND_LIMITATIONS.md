# Phase 16 — Validation & Limitations

## Project
**Where Are Australia's Next Community Cricketers?**

## Status
**COMPLETE — MODEL VALIDATION, CLAIM BOUNDARIES AND LIMITATIONS LOCKED**

## 1. Purpose
Phase 16 tests whether the project is sufficiently robust to present as a professional decision-support prototype and defines the boundaries of what the analysis can legitimately claim.

The validation standard is deliberately conservative. A model can be useful without being predictive, but it must not be described as more certain than the evidence permits.

## 2. Overall validation judgement

### Decision-support usefulness: **GREEN**
The model is suitable as a transparent national screening/prioritisation prototype.

### Ranking robustness: **GREEN**
Top opportunities remain highly stable under alternative weighting and eligibility assumptions.

### Data-processing integrity: **GREEN**
The core ABS joins and age calculations passed multiple reconciliation checks.

### Construct validity: **GREEN/AMBER**
EDA supports separate Market Size, Youth Concentration and Growth Momentum pillars and identified/removed major redundancy.

### External/face validity: **AMBER/GREEN**
Selected case studies provide independent local evidence consistent with the model identifying areas worth investigating.

### Predictive validity: **RED / NOT ESTABLISHED**
There is no future LGA-level cricket-registration outcome against which Model V1 can be tested.

### Full Opportunity × Readiness validity: **RED / INCOMPLETE**
The national Cricket System Readiness layer is not yet available.

## 3. Internal validation

### 3.1 Data integrity
Phase 9 established:
- 548 unique current LGA population records;
- no duplicate LGA codes;
- age data for 546;
- zero male+female reconciliation failures;
- zero inconsistencies between current and historical 2024 age tables;
- explicit handling of documented geography changes.

This supports confidence that the analytical variables are calculated from the intended source data.

### 3.2 Redundancy validation
Phase 10 found:
- total population vs age 5–14 population: Spearman ≈ 0.993;
- girls 5–14 vs total 5–14 count: Spearman ≈ 1.000.

This confirmed that multiple raw population counts should not be independently weighted. Model V1 therefore uses one Market Size signal.

### 3.3 Distinct growth construct
Total population growth and junior-population growth show only moderate rank association (≈0.57), supporting a distinct Growth Momentum pillar.

## 4. Sensitivity validation

### 4.1 Weight sensitivity
Compared with the Balanced Top 20:
- Growth-led: 20/20 overlap;
- Scale-led: 18/20;
- Intensity-led: 19/20.

Full-ranking Spearman correlations remain high.

**Interpretation:** the leading candidate set is robust to reasonable changes in the relative importance of scale, youth concentration and growth.

### 4.2 Eligibility sensitivity
Changing the minimum current population / junior-base guardrails results in 19–20 of the Balanced Top 20 remaining in the Top 20.

**Interpretation:** the national shortlist is not being manufactured by the chosen small-market threshold.

## 5. Geographic validation
Phase 11 found that the largest absolute junior-market increases are strongly concentrated around a small number of growth systems rather than randomly distributed.

This provides geographic face validity: the model highlights coherent population-growth systems.

However, geographic coherence is **not** independent predictive validation. It only shows that the results make demographic sense.

## 6. External case-study validation
Phase 14 deliberately tested five geographically diverse high-opportunity cases.

### Wyndham
Local evidence showed cricket participation growth and women/girls growth alongside facility-capacity investment.

**Validation strength:** strong.

### Blacktown
Council explicitly identified insufficient field supply for requested year-round cricket, while the local junior association demonstrates active program development.

**Validation strength:** strong for further capacity-gap investigation.

### Ipswich
Junior/Blast growth and new cricket-capable facilities align with the model's high demographic opportunity.

**Validation strength:** strong.

### Maitland
New growth-area cricket infrastructure and girls programming support the model's identification of a regional growth opportunity.

**Validation strength:** moderate/strong.

### Armadale
Infrastructure and demographic growth align, but direct recent participation evidence remains weaker.

**Validation strength:** moderate.

This is a useful result because validation is not uniformly positive. Armadale remains a genuine test case rather than being forced into the same narrative as Wyndham.

## 7. What is NOT validated

### 7.1 Future registrations
Model V1 has not been trained or tested against future new cricket registrations.

Therefore it is not predictive.

### 7.2 Participation penetration
There is no national public LGA dataset of registered cricket players that allows calculation of:

`registered cricket participants / target population`.

Therefore the model cannot identify actual low-penetration markets.

### 7.3 Cricket demand
Population characteristics do not directly measure desire to play cricket.

### 7.4 Cricket System Readiness
There is no nationally consistent readiness score based on clubs, programs, fields, capacity, utilisation and workforce.

### 7.5 Causality
The model is observational.

It cannot establish that population growth, age structure or any demographic factor causes cricket participation growth.

## 8. Critical limitations

### L1 — Missing cricket outcome data
This is the single biggest limitation.

Without LGA/club-catchment registration outcomes, the project cannot statistically test whether high Opportunity scores actually correspond to:
- higher acquisition;
- lower penetration;
- faster registration growth;
- unmet cricket demand.

### L2 — Missing System Readiness
The intended final framework is:

**Opportunity Potential × Cricket System Readiness**

Only the first dimension is currently quantitative.

Local readiness evidence from Phase 14 is qualitative and uneven.

### L3 — 5–14 rather than exact 5–12
Australian Cricket strategically emphasises ages 5–12, but the current ABS age workbook provides 5–9 and 10–14 bands.

Model V1 therefore uses directly observed 5–14 population rather than constructing a false-precision 5–12 estimate.

### L4 — Cultural strategic alignment absent from V1
The South Asian/cultural-demographic layer has not been integrated.

This means one important Australian Cricket strategic dimension remains outside the current score.

Importantly, even when added, cultural identity must remain a strategic-alignment variable rather than being treated as automatic cricket demand.

### L5 — Mixed reference years
The analytical evidence uses the best available source for each variable:
- 2021 Census/SEIFA context;
- 2024 age/sex;
- 2025 population;
- 2025/26 contextual cricket evidence.

The dataset must never be described simply as '2026 data.'

### L6 — Geographic changes
LGA boundaries change.

The East Arnhem/Groote Archipelago restructure creates a genuine historical-comparability issue. Other changes such as Moreland → Merri-bek can be corresponded because the nature of the change is different.

### L7 — LGA is not a true cricket catchment
Players may live in one council, attend school in another and play cricket in a third.

A production model should use smaller geography and/or actual club catchments where possible.

### L8 — Regional fairness
A national percentile model will naturally prioritise large metropolitan markets.

Smaller regional communities may be important within their own context even when they rank lower nationally.

A separate peer/remoteness benchmarking layer is required.

### L9 — Percentile interpretation
An Opportunity score of 95 means the LGA ranks very highly relative to eligible LGAs on the chosen model.

It does not mean:
- 95% chance of participation;
- 95% market penetration;
- 95% of children want cricket.

### L10 — Equal weights are not 'true' weights
Equal weighting is a neutral transparent baseline.

It is not empirically optimal because no outcome exists to estimate optimal weights.

Sensitivity analysis shows this choice is not driving the leading candidate set.

## 9. Bias risks

### Confirmation bias
Because the project began with an expectation that growth corridors would matter, later case studies could favour confirming examples.

**Control:** hypotheses were written before results; Armadale is retained as a weaker validation case; contradictory future cases should be actively sought.

### Large-market bias
Raw counts favour large urban LGAs.

**Control:** Youth Concentration and Growth Momentum are separate pillars; small/region peer benchmarking remains recommended.

### Demographic stereotyping
Strategic demographic variables can be misused to infer sporting preference.

**Control:** demographic identity is never equated with cricket demand; direct participation evidence is required.

### Availability bias
Councils/states with better public websites may appear to have stronger evidence.

**Control:** qualitative local evidence is not converted into a formal national readiness score.

## 10. Claim boundaries

### The project CAN say:
- certain LGAs have stronger demographic Opportunity Potential under the transparent Model V1;
- the Top 20 is stable under several reasonable modelling assumptions;
- some high-opportunity areas have independent local evidence that justifies deeper cricket-specific investigation;
- junior-market growth is geographically concentrated.

### The project CANNOT say:
- these are Australia's largest untapped cricket markets;
- these LGAs have low cricket participation rates;
- a high score predicts future registrations;
- a particular demographic community will play cricket;
- a specified investment will produce a quantified participant increase;
- Blacktown/Wyndham are formally capacity constrained relative to every other Australian LGA without a national readiness dataset.

## 11. Production-grade validation roadmap
With CA internal data, the model should be upgraded and tested as follows.

### Step 1 — Add actual outcomes
For every LGA/SA2/club catchment:
- new registrations;
- total registrations;
- returning registrations;
- churn;
- Blast → junior conversion.

### Step 2 — Test predictive association
Examine whether prior-year Opportunity Potential predicts subsequent:
- acquisition rate;
- registration growth;
- unmet demand.

### Step 3 — Build System Readiness
Add:
- club/program supply;
- playable facility hours;
- participant/team capacity;
- waitlists;
- volunteer/workforce;
- travel/access.

### Step 4 — Validate Opportunity × Readiness segments
Test whether:
- high opportunity + low readiness areas show more unmet demand;
- high opportunity + high readiness areas convert more new participants;
- large slower-growth markets require more retention activity.

### Step 5 — Calibrate weights
Only then consider statistical calibration or machine-learning approaches.

### Step 6 — Intervention evaluation
Where CA invests, use pre/post and comparison-area designs to test whether interventions materially improve participation outcomes.

## 12. Internal data priorities
Highest-priority data for the production model:

1. **PlayHQ registration histories**
2. **Club/program locations and capacity**
3. **Facility hours, utilisation and planned supply**
4. **Waitlists / unable-to-accommodate demand**
5. **Volunteer/workforce capacity**
6. **School-to-club pathway data**
7. **Participant barriers and motivations**
8. **Appropriately collected inclusion/demographic information**
9. **Historical intervention/investment data**
10. **Program and infrastructure cost data**

## 13. Final validation verdict

### Suitable for portfolio/report use?
**YES.**

### Suitable for describing a transparent public-data prioritisation prototype?
**YES.**

### Suitable for recommending areas for further investigation?
**YES.**

### Suitable for claiming actual untapped cricket demand?
**NO.**

### Suitable for predicting future registrations?
**NO.**

### Suitable for allocating CA investment without additional internal data?
**NO.**

## Phase 16 conclusion
The strongest feature of this project is not that Model V1 produces a ranking.

It is that the model is:
- reproducible;
- transparent;
- sensitivity-tested;
- explicit about missing evidence;
- designed to be upgraded with internal cricket data.

The defensible final position is:

> **Model V1 identifies where demographic conditions justify deeper participation investigation. It does not claim to directly measure cricket demand, penetration or system readiness.**

That boundary should remain visible in the dashboard, report, GitHub documentation and job application materials.
