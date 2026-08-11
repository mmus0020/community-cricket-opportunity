# Phase 8 Data Collection Register

Project: Where Are Australia's Next Community Cricketers?
Collection date: 2026-08-11

## Successfully acquired raw files

1. `raw/abs_regional_population_lga_2024_25.xlsx`
   - Source: Australian Bureau of Statistics, Regional population 2024-25
   - URL: https://www.abs.gov.au/statistics/people/population/regional-population/2024-25/32180DS0002_2024-25.xlsx
   - Geography: LGA
   - Coverage: 2024 to 2025 estimates/components
   - Intended use: current population, annual population growth

2. `raw/abs_regional_population_lga_timeseries_2001_25.xlsx`
   - Source: Australian Bureau of Statistics, Regional population 2024-25
   - URL: https://www.abs.gov.au/statistics/people/population/regional-population/2024-25/32180DS0004_2001-25.xlsx
   - Geography: LGA
   - Coverage: 2001 to 2025 ERP
   - Intended use: 5-year and long-run population growth

3. `raw/abs_age_sex_lga_2024.xlsx`
   - Source: Australian Bureau of Statistics, Regional population by age and sex 2024
   - URL: https://www.abs.gov.au/statistics/people/population/regional-population-age-and-sex/2024/32350DS0003_2024.xlsx
   - Geography: LGA
   - Coverage: 2024
   - Detail: five-year age groups, male/female/total
   - Intended use: junior market proxy, female youth population
   - Important limitation: public workbook is grouped (5-9 and 10-14); it does not directly provide exact ages 5-12.

4. `raw/abs_age_sex_lga_timeseries_2001_24.xlsx`
   - Source: Australian Bureau of Statistics, Regional population by age and sex 2024
   - URL: https://www.abs.gov.au/statistics/people/population/regional-population-age-and-sex/2024/32350DS0006_2001-24.xlsx
   - Geography: LGA
   - Coverage: 2001 to 2024
   - Detail: five-year age groups by sex
   - Intended use: youth-cohort growth over time

5. `raw/abs_seifa_lga_2021.xlsx`
   - Source: Australian Bureau of Statistics, SEIFA 2021
   - URL: https://www.abs.gov.au/statistics/people/people-and-communities/socio-economic-indexes-areas-seifa-australia/2021/Local%20Government%20Area%2C%20Indexes%2C%20SEIFA%202021.xlsx
   - Geography: LGA 2021
   - Coverage: 2021
   - Intended use: contextual socioeconomic indicators (IRSD/IRSAD etc.)

## Verified sources not locally acquired in this phase

6. 2021 Census General Community Profile DataPack, LGA Australia
   - URL: https://www.abs.gov.au/census/find-census-data/datapacks/download/2021_GCP_LGA_for_AUS_short-header.zip
   - Status: verified, ZIP package; current transfer channel rejected ZIP retrieval
   - Intended use: detailed cultural-demographic variables / ancestry where suitable
   - Alternative: ABS TableBuilder, which supports custom 2021 Census tables and 2025 LGA geography.

7. LGA 2025 digital boundaries, GDA2020
   - URL: https://www.abs.gov.au/statistics/standards/australian-statistical-geography-standard-asgs/edition-3-july-2021-june-2026/access-and-downloads/digital-boundary-files/LGA_2025_AUST_GDA2020.zip
   - Status: verified, ZIP package; current transfer channel rejected ZIP retrieval
   - Intended use: national LGA maps and spatial joins

8. AusPlay January-December 2025 data tables
   - Source page: https://www.ausport.gov.au/clearinghouse/research/ausplay/results/data-tables
   - Status: verified downloadable workbooks; download links use expiring storage tokens and were not retained locally in this collection package
   - Intended use: national/state cricket participation context and benchmarking

9. Cricket Australia 2022-23 Australian Cricket Census
   - Source: https://www.cricket.com.au/news/3646243/cricket-census-reveals-cricket-participation-continues-to-grow
   - Status: authoritative web release, not a bulk dataset
   - Intended use: national registered-participation baseline / definitions

10. Cricket NSW 2025-26 Census-date participation results
   - Source: https://www.cricketnsw.com.au/news/4495523/cricket-nsw-celebrates-summer-of-record-participation
   - Status: authoritative web release
   - Intended use: recent state benchmark and validation context

11. Cricket Victoria 2024-25 Community Cricket Census results
   - Source: https://www.cricketvictoria.com.au/news/news/summer-of-cricket-begins-with-play-cricket-month-across-victoria/
   - Status: authoritative web release
   - Intended use: recent Victoria benchmark and validation context

12. Play Cricket Program Finder
   - Source: https://play.cricket.com.au/program-finder
   - Status: live search interface; no bulk export exposed publicly
   - Intended use: club/program supply if a compliant access method is identified
   - Related platform note: PlayHQ documents a Public API but requires users to contact their sport for an API key.

## Collection decisions locked in Phase 8

- Raw source files remain untouched.
- The master geographic key will ultimately be harmonised to 2025 LGA codes.
- Current age/sex data cannot directly produce exact 5-12 counts from the downloaded workbook; no interpolation will be performed during raw collection.
- Cultural-demographic extraction remains pending because the preferred national DataPack is ZIP-packaged; TableBuilder remains a legitimate alternative.
- Cricket club/program supply remains pending because public Play Cricket is a search interface rather than an openly downloadable national table.
- No scoring, weighting, imputation, or modelling has been performed in Phase 8.
