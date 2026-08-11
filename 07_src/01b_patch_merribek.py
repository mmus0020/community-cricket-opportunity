import csv,json
from pathlib import Path
P=Path('/mnt/data/cricket_project/phase9/processed')
s=list(csv.DictReader(open(P/'seifa_lga.csv',encoding='utf-8-sig')))
x=next(r for r in s if r['LGA_CODE']=='25250')
f=open(P/'master_lga.csv',encoding='utf-8-sig'); m=list(csv.DictReader(f)); fields=list(m[0]); f.close()
for r in m:
    if r['LGA_CODE']=='24700':
        [r.__setitem__(k,v) for k,v in x.items() if k not in ('LGA_CODE','LGA_NAME_2021')]
        r['LGA_NAME_2021']='Moreland (2021; corresponded to Merri-bek)'
        r['SEIFA_DATA_AVAILABLE']='1'
f=open(P/'master_lga.csv','w',encoding='utf-8-sig',newline=''); w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(m); f.close()
qpath=Path('/mnt/data/cricket_project/phase9/docs/phase9_quality_checks.json')
q=json.load(open(qpath)); q['seifa_joined_count']=546; q['seifa_missing_count']=2; q['master_codes_missing_seifa']=['71500: East Arnhem','71700: Groote Archipelago']; q['manual_correspondences']={'SEIFA_2021_MORELAND_25250_TO_MERRI_BEK_24700':'Applied'}; json.dump(q,open(qpath,'w'),indent=2)
print('patched')
