# Phase 11 — Geographic Analysis

## Project
**Where Are Australia’s Next Community Cricketers?**

## Status
**COMPLETE — GEOGRAPHIC PATTERN ANALYSIS**

## Geographic boundary status
The official ABS ASGS 2025 LGA boundary service and 2025 shapefile have been verified. The service contains 567 LGA records including non-spatial/special-purpose records and unincorporated areas. The statistical master dataset contains 548 current population records. The current execution environment blocked transfer of the official ZIP/GeoJSON geometry, so this phase does not fabricate a national polygon choropleth. The boundary layer remains the required geometry source for the final GIS/Power BI implementation.

## Main geographic finding
The national Top 20 LGAs for absolute 2019–2024 growth in the 5–14 population are highly geographically concentrated rather than dispersed.

The Top 20 together added approximately **106,387** residents aged 5–14.

Four broad growth systems account for approximately **100,671**, or **94.6%**, of that Top-20 increase:

1. **Melbourne outer growth belt** — Wyndham, Melton, Casey, Hume, Whittlesea and Cardinia: **+42,505**.
2. **Western / south-west Sydney** — Blacktown, Camden, The Hills, Liverpool and Campbelltown: **+26,982**.
3. **South East Queensland** — Logan, Brisbane, Ipswich and Sunshine Coast: **+20,784**.
4. **Perth growth belt** — Swan, Armadale and Wanneroo: **+10,400**.

The remaining Top-20 growth is concentrated in Greater Geelong and the ACT.

## Interpretation
This suggests community-cricket acquisition planning should not treat high-growth LGAs as isolated municipalities. Several high-growth areas form contiguous or functionally connected urban-growth systems. A participation strategy could therefore be more effective when planned at corridor/system level—for example, coordinating club capacity, entry programs and facilities across multiple adjacent LGAs—rather than assigning one independent intervention to each council.

## Melbourne
Melbourne is the clearest concentration. Six LGAs in the national Top 20 collectively added **42,505** children aged 5–14 between 2019 and 2024:
- Wyndham +13,313
- Melton +8,438
- Casey +7,925
- Hume +5,973
- Whittlesea +4,315
- Cardinia +2,541

These locations span western, northern and south-eastern outer Melbourne rather than the established inner metropolitan core. Greater Geelong adds another +2,624 nearby but is kept separate from the Melbourne cluster.

## Sydney
Five Top-20 LGAs form a western/south-western Sydney concentration:
- Blacktown +9,571
- Camden +6,449
- The Hills +4,994
- Liverpool +3,100
- Campbelltown +2,868

Together they added **26,982** residents aged 5–14.

## South East Queensland
Logan, Brisbane, Ipswich and Sunshine Coast added **20,784** residents aged 5–14 in aggregate. Unlike Melbourne and Sydney, this cluster includes the very large Brisbane LGA itself alongside surrounding growth markets.

## Perth
Swan, Armadale and Wanneroo collectively added **10,400** residents aged 5–14. Phase 10 also found Western Australia had the strongest aggregate junior-population growth among the larger states, reinforcing the importance of the Perth growth system.

## Geographic implications for modelling
1. **Do not use a purely national ranking as the only output.**
2. Add **growth-corridor / peer-region interpretation** after LGA ranking.
3. Treat adjacent high-growth LGAs as potential shared delivery systems.
4. A future cricket-supply layer should test whether clubs/programs are concentrated in established areas while youth growth is occurring at metropolitan edges.
5. Case-study selection should include at least one LGA from each major growth system rather than selecting all cases from one state.
6. The eventual dashboard should support national → state → LGA drill-down.

## Hypothesis implications
- **H1** remains supported: geographic conditions vary materially.
- **H5** receives stronger support: outer-metropolitan growth corridors feature prominently, although a formal official metro/remoteness classification is still pending.
- **H6** remains only partial/suggestive: relative youth concentration reveals non-metropolitan areas, but absolute growth is strongly concentrated around major urban systems.
- **H12** remains supported: absolute market measures favour large urban LGAs.
- **H22** becomes more strategically interesting: if future cricket supply fails to match these growth corridors, the mismatch may operate at corridor scale rather than only individual-LGA scale.

## Boundary limitation
A full 2025 LGA polygon choropleth is deferred because the official geometry could not be transferred into the runtime during this phase. This does not alter the numeric geographic findings. The final GIS/dashboard build must use the official ABS 2025 LGA layer rather than a hand-drawn or third-party boundary substitute.

## Phase 11 conclusion
The most important geographic finding is **concentration**: Australia's strongest absolute junior-market growth is clustered around a small number of expanding metropolitan systems. This shifts the management question from only “Which LGA ranks highest?” toward **“Which growth corridors require coordinated cricket participation capacity?”**

No Opportunity Potential score has been constructed.
