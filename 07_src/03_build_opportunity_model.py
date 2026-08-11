"""
Build Community Cricket Opportunity Potential Model V1.

Input:
    04_data/processed/master_lga.csv
Output:
    ranked opportunity CSV

Model:
- eligible if TOTAL_POP_2025 >= 5000 and AGE_5_14_2019 >= 500
- excludes residual unincorporated records except ACT
- percentile rank Market Size = AGE_5_14_2024
- percentile rank Youth Concentration = AGE_5_14_SHARE_TOTAL_PCT
- Growth Momentum = average percentile ranks of:
    AGE_5_14_CHANGE_5Y
    AGE_5_14_GROWTH_5Y_PCT
- Opportunity Potential = equal average of the three pillars
"""
import csv, math
from pathlib import Path
from scipy.stats import rankdata

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "04_data/processed/master_lga.csv"
OUTPUT = ROOT / "04_data/model_outputs/reproduced_opportunity_model_v1.csv"

def num(row, col):
    try:
        return float(row[col]) if row.get(col) not in ("", None) else math.nan
    except Exception:
        return math.nan

with INPUT.open(encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

eligible = [
    r for r in rows
    if r["AGE_DATA_AVAILABLE"] == "1"
    and (r["IS_UNINCORPORATED"] == "0" or r["STATE"] == "Australian Capital Territory")
    and num(r, "TOTAL_POP_2025") >= 5000
    and num(r, "AGE_5_14_2019") >= 500
]

def pct(values):
    return rankdata(values, method="average") / len(values) * 100

market = pct([num(r,"AGE_5_14_2024") for r in eligible])
intensity = pct([num(r,"AGE_5_14_SHARE_TOTAL_PCT") for r in eligible])
growth_abs = pct([num(r,"AGE_5_14_CHANGE_5Y") for r in eligible])
growth_rate = pct([num(r,"AGE_5_14_GROWTH_5Y_PCT") for r in eligible])

out = []
for i,r in enumerate(eligible):
    growth = (growth_abs[i] + growth_rate[i]) / 2
    score = (market[i] + intensity[i] + growth) / 3
    out.append({
        "LGA_CODE": r["LGA_CODE"], "LGA_NAME": r["LGA_NAME"], "STATE": r["STATE"],
        "SCORE_MARKET_SIZE": market[i], "SCORE_YOUTH_INTENSITY": intensity[i],
        "SCORE_GROWTH_MOMENTUM": growth, "SCORE_BALANCED": score
    })

out.sort(key=lambda r:r["SCORE_BALANCED"], reverse=True)
for i,r in enumerate(out,1):
    r["RANK_BALANCED"] = i

with OUTPUT.open("w", newline="", encoding="utf-8-sig") as f:
    w=csv.DictWriter(f, fieldnames=list(out[0].keys()))
    w.writeheader(); w.writerows(out)

print(f"Wrote {len(out)} ranked LGAs to {OUTPUT}")
