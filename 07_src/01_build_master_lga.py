from pathlib import Path
import zipfile, xml.etree.ElementTree as ET, re, csv, json
RAW=Path('/mnt/data/cricket_project/phase8/raw'); OUT=Path('/mnt/data/cricket_project/phase9'); PROC=OUT/'processed'; DOCS=OUT/'docs'
NS='http://schemas.openxmlformats.org/spreadsheetml/2006/main'
def ci(ref):
 n=0
 for ch in re.match(r'([A-Z]+)',ref).group(1): n=n*26+ord(ch)-64
 return n-1
def rows(path,sn):
 out=[]
 with zipfile.ZipFile(path) as z:
  ss=[]
  if 'xl/sharedStrings.xml' in z.namelist():
   rt=ET.fromstring(z.read('xl/sharedStrings.xml'))
   ss=[''.join(t.text or '' for t in x.iter('{%s}t'%NS)) for x in rt.findall('{%s}si'%NS)]
  rt=ET.fromstring(z.read(f'xl/worksheets/sheet{sn}.xml'))
  for rr in rt.iter('{%s}row'%NS):
   d={}
   for c in rr.findall('{%s}c'%NS):
    i=ci(c.attrib['r']); typ=c.attrib.get('t'); v=c.find('{%s}v'%NS)
    if typ=='inlineStr': val=''.join(t.text or '' for t in c.iter('{%s}t'%NS))
    elif v is None: val=''
    elif typ=='s': val=ss[int(v.text)]
    else: val=v.text
    d[i]=val
   if d:
    a=['']*(max(d)+1)
    for i,v in d.items(): a[i]=v
    out.append(a)
 return out
def n(x):
 try:
  s=str(x).strip().replace(',','')
  if s in ('','na','np','—','-','..'): return None
  return float(s)
 except: return None
def I(x):
 v=n(x); return None if v is None else int(round(v))
def pc(new,old): return None if new is None or old in (None,0) else (new-old)/old*100
def st(code): return {'1':'New South Wales','2':'Victoria','3':'Queensland','4':'South Australia','5':'Western Australia','6':'Tasmania','7':'Northern Territory','8':'Australian Capital Territory','9':'Other Territories'}.get(str(code)[:1],'Unknown')
def save(path,data):
 if not data:return
 with open(path,'w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=list(data[0]));w.writeheader();w.writerows(data)
# Population spine
R=rows(RAW/'abs_regional_population_lga_timeseries_2001_25.xlsx',2)
years=[int(x) for x in R[4][2:] if str(x).strip().isdigit()]
pop=[]
for r in R[6:]:
 if len(r)<3 or not str(r[0]).strip().isdigit():continue
 code=str(r[0]).strip(); vals={yr:I(r[2+i]) if 2+i<len(r) else None for i,yr in enumerate(years)}
 p20,p24,p25=vals.get(2020),vals.get(2024),vals.get(2025)
 pop.append({'LGA_CODE':code,'LGA_NAME':str(r[1]).strip(),'STATE':st(code),'TOTAL_POP_2020':p20,'TOTAL_POP_2024':p24,'TOTAL_POP_2025':p25,'POP_CHANGE_1Y':None if None in (p24,p25) else p25-p24,'POP_GROWTH_1Y_PCT':pc(p25,p24),'POP_CHANGE_5Y':None if None in (p20,p25) else p25-p20,'POP_GROWTH_5Y_PCT':pc(p25,p20),'IS_UNINCORPORATED':1 if 'unincorporated' in str(r[1]).lower() else 0})
popby={r['LGA_CODE']:r for r in pop}

def age_current(sn):
 out={}
 for r in rows(RAW/'abs_age_sex_lga_2024.xlsx',sn)[7:]:
  if len(r)<7 or not str(r[2]).strip().isdigit():continue
  a,b=I(r[5]),I(r[6]);code=str(r[2]).strip()
  out[code]={'STATE':str(r[1]).strip(),'AGE_5_9_2024':a,'AGE_10_14_2024':b,'AGE_5_14_2024':None if None in (a,b) else a+b}
 return out
male,female,persons=age_current(2),age_current(3),age_current(4)

def age_hist(sn):
 out={}
 for r in rows(RAW/'abs_age_sex_lga_timeseries_2001_24.xlsx',sn)[7:]:
  if len(r)<8:continue
  yr=I(r[0]);code=str(r[3]).strip()
  if yr not in (2019,2024) or not code.isdigit():continue
  a,b=I(r[6]),I(r[7]);out[(code,yr)]=None if None in (a,b) else a+b
 return out
hf,hp=age_hist(3),age_hist(4)
youth=[]
for code in sorted(set(persons)|set(female)):
 a=persons.get(code,{}).get('AGE_5_14_2024');g=female.get(code,{}).get('AGE_5_14_2024');p24=popby.get(code,{}).get('TOTAL_POP_2024');a19=hp.get((code,2019));g19=hf.get((code,2019))
 youth.append({'LGA_CODE':code,'STATE':persons.get(code,{}).get('STATE') or female.get(code,{}).get('STATE') or st(code),'AGE_5_9_2024':persons.get(code,{}).get('AGE_5_9_2024'),'AGE_10_14_2024':persons.get(code,{}).get('AGE_10_14_2024'),'AGE_5_14_2024':a,'AGE_5_14_SHARE_TOTAL_PCT':None if a is None or not p24 else a/p24*100,'AGE_5_14_2019':a19,'AGE_5_14_CHANGE_5Y':None if None in (a,a19) else a-a19,'AGE_5_14_GROWTH_5Y_PCT':pc(a,a19),'GIRLS_5_14_2024':g,'GIRLS_SHARE_OF_5_14_PCT':None if g is None or not a else g/a*100,'GIRLS_5_14_2019':g19,'GIRLS_5_14_CHANGE_5Y':None if None in (g,g19) else g-g19,'GIRLS_5_14_GROWTH_5Y_PCT':pc(g,g19)})
yby={r['LGA_CODE']:r for r in youth}
S=rows(RAW/'abs_seifa_lga_2021.xlsx',2)
seifa=[]
for r in S[6:]:
 if len(r)<10 or not str(r[0]).strip().isdigit(): continue
 seifa.append({'LGA_CODE':str(r[0]).strip(),'LGA_NAME_2021':str(r[1]).strip(),'IRSD_SCORE_2021':I(r[2]),'IRSD_DECILE_2021':I(r[3]),'IRSAD_SCORE_2021':I(r[4]),'IRSAD_DECILE_2021':I(r[5]),'IER_SCORE_2021':I(r[6]),'IER_DECILE_2021':I(r[7]),'IEO_SCORE_2021':I(r[8]),'IEO_DECILE_2021':I(r[9])})
sby={r['LGA_CODE']:r for r in seifa}
master=[]
for p in pop:
 code=p['LGA_CODE']; row=dict(p)
 for k,v in yby.get(code,{}).items():
  if k not in ('LGA_CODE','STATE'): row[k]=v
 for k,v in sby.get(code,{}).items():
  if k!='LGA_CODE': row[k]=v
 row['AGE_DATA_AVAILABLE']=int(code in yby)
 row['SEIFA_DATA_AVAILABLE']=int(code in sby)
 row['CULTURAL_DATA_AVAILABLE']=0
 row['CRICKET_SUPPLY_DATA_AVAILABLE']=0
 master.append(row)
codes=[r['LGA_CODE'] for r in master]
qa={
 'master_lga_count':len(master),
 'duplicate_master_codes':len(codes)-len(set(codes)),
 'age_joined_count':sum(r['AGE_DATA_AVAILABLE'] for r in master),
 'age_missing_count':sum(1-r['AGE_DATA_AVAILABLE'] for r in master),
 'seifa_joined_count':sum(r['SEIFA_DATA_AVAILABLE'] for r in master),
 'seifa_missing_count':sum(1-r['SEIFA_DATA_AVAILABLE'] for r in master),
 'unincorporated_count':sum(r['IS_UNINCORPORATED'] for r in master),
 'negative_population_count':sum(1 for r in master if r['TOTAL_POP_2025'] is not None and r['TOTAL_POP_2025']<0)
}
qa['age_not_equal_male_plus_female']=sum(1 for c,p in persons.items() if c in male and c in female and p.get('AGE_5_14_2024') is not None and p['AGE_5_14_2024']!=male[c]['AGE_5_14_2024']+female[c]['AGE_5_14_2024'])
qa['age_current_vs_timeseries_2024_mismatch']=sum(1 for c,p in persons.items() if (c,2024) in hp and p.get('AGE_5_14_2024')!=hp[(c,2024)])
qa['master_codes_missing_age']=[r['LGA_CODE']+': '+r['LGA_NAME'] for r in master if not r['AGE_DATA_AVAILABLE']]
qa['master_codes_missing_seifa']=[r['LGA_CODE']+': '+r['LGA_NAME'] for r in master if not r['SEIFA_DATA_AVAILABLE']]
qa['age_codes_not_in_master']=[c for c in sorted(yby) if c not in popby]
qa['seifa_codes_not_in_master']=[c for c in sorted(sby) if c not in popby]
agg={}
for r in master:
 x=agg.setdefault(r['STATE'],{'LGA_COUNT':0,'POP_2025':0,'AGE_5_14_2024':0,'AGE_ROWS':0})
 x['LGA_COUNT']+=1
 if r['TOTAL_POP_2025'] is not None:x['POP_2025']+=r['TOTAL_POP_2025']
 if r.get('AGE_5_14_2024') is not None:x['AGE_5_14_2024']+=r['AGE_5_14_2024'];x['AGE_ROWS']+=1
state=[{'STATE':k,**v} for k,v in sorted(agg.items())]
for name,data in [('population_lga.csv',pop),('youth_lga.csv',youth),('seifa_lga.csv',seifa),('master_lga.csv',master),('state_summary.csv',state)]: save(PROC/name,data)
DD=[
('LGA_CODE','Primary LGA join key','ABS Regional Population','2025 geography','Direct','Stored as text; no name-based joining'),
('TOTAL_POP_2025','Estimated resident population at 30 June 2025','ABS Regional Population','2025','Direct','Current market size'),
('POP_GROWTH_1Y_PCT','ERP growth from 2024 to 2025','Derived from ABS ERP','2024-25','Derived','Percentage'),
('POP_GROWTH_5Y_PCT','ERP growth from 2020 to 2025','Derived from ABS ERP','2020-25','Derived','Percentage'),
('AGE_5_14_2024','Observed population aged 5-14, 5-9 plus 10-14','ABS Regional Population by Age and Sex','2024','Derived from direct bands','Used instead of unavailable exact 5-12'),
('AGE_5_14_SHARE_TOTAL_PCT','Age 5-14 share of 2024 total population','Derived','2024','Derived','Uses TOTAL_POP_2024 denominator'),
('AGE_5_14_GROWTH_5Y_PCT','Growth in age 5-14 population, 2019 to 2024','Derived from ABS age time series','2019-24','Derived','Can be volatile in small LGAs'),
('GIRLS_5_14_2024','Female population aged 5-14','ABS Regional Population by Age and Sex','2024','Derived from direct bands','Overlaps total junior market'),
('GIRLS_SHARE_OF_5_14_PCT','Girls as share of age 5-14 population','Derived','2024','Derived','Diagnostic; not independent market size'),
('IRSD_SCORE_2021','Index of Relative Socio-economic Disadvantage score','ABS SEIFA','2021','Context','Not included in core opportunity score yet'),
('IRSD_DECILE_2021','IRSD national decile','ABS SEIFA','2021','Context','1 most disadvantaged, 10 least disadvantaged'),
('AGE_DATA_AVAILABLE','Age-data join flag','Derived QA','2024/25','QA','1 joined, 0 missing'),
('SEIFA_DATA_AVAILABLE','SEIFA join flag','Derived QA','2021/25','QA','1 joined, 0 missing'),
('CULTURAL_DATA_AVAILABLE','Cultural layer availability flag','Project','2021','QA','0 in Phase 9; extraction pending'),
('CRICKET_SUPPLY_DATA_AVAILABLE','Cricket supply layer availability flag','Project','2026','QA','0 in Phase 9; access unresolved')]
with open(PROC/'data_dictionary.csv','w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['VARIABLE_NAME','DESCRIPTION','SOURCE','REFERENCE_YEAR','EVIDENCE_TYPE','LIMITATION_OR_NOTE']);w.writerows(DD)
with open(DOCS/'phase9_quality_checks.json','w',encoding='utf-8') as f:json.dump(qa,f,indent=2)
print(json.dumps({k:v for k,v in qa.items() if not isinstance(v,list)},indent=2))
print('AGE_MISSING',qa['master_codes_missing_age'])
print('SEIFA_MISSING',qa['master_codes_missing_seifa'])
DD=[
('LGA_CODE','Primary LGA join key','ABS Regional Population','2025 geography','Direct','Stored as text; no name-based joining'),
('TOTAL_POP_2025','Estimated resident population at 30 June 2025','ABS Regional Population','2025','Direct','Current market size'),
('POP_GROWTH_1Y_PCT','ERP growth from 2024 to 2025','Derived from ABS ERP','2024-25','Derived','Percentage'),
('POP_GROWTH_5Y_PCT','ERP growth from 2020 to 2025','Derived from ABS ERP','2020-25','Derived','Percentage'),
('AGE_5_14_2024','Observed population aged 5-14, 5-9 plus 10-14','ABS Regional Population by Age and Sex','2024','Derived from direct bands','Used instead of unavailable exact 5-12'),
('AGE_5_14_SHARE_TOTAL_PCT','Age 5-14 share of 2024 total population','Derived','2024','Derived','Uses TOTAL_POP_2024 denominator'),
('AGE_5_14_GROWTH_5Y_PCT','Growth in age 5-14 population, 2019 to 2024','Derived from ABS age time series','2019-24','Derived','Can be volatile in small LGAs'),
('GIRLS_5_14_2024','Female population aged 5-14','ABS Regional Population by Age and Sex','2024','Derived from direct bands','Overlaps total junior market'),
('GIRLS_SHARE_OF_5_14_PCT','Girls as share of age 5-14 population','Derived','2024','Derived','Diagnostic; not independent market size'),
('IRSD_SCORE_2021','Index of Relative Socio-economic Disadvantage score','ABS SEIFA','2021','Context','Not included in core opportunity score yet'),
('IRSD_DECILE_2021','IRSD national decile','ABS SEIFA','2021','Context','1 most disadvantaged, 10 least disadvantaged'),
('AGE_DATA_AVAILABLE','Age-data join flag','Derived QA','2024/25','QA','1 joined, 0 missing'),
('SEIFA_DATA_AVAILABLE','SEIFA join flag','Derived QA','2021/25','QA','1 joined, 0 missing'),
('CULTURAL_DATA_AVAILABLE','Cultural layer availability flag','Project','2021','QA','0 in Phase 9; extraction pending'),
('CRICKET_SUPPLY_DATA_AVAILABLE','Cricket supply layer availability flag','Project','2026','QA','0 in Phase 9; access unresolved')]
with open(PROC/'data_dictionary.csv','w',newline='',encoding='utf-8-sig') as f:
 w=csv.writer(f);w.writerow(['VARIABLE_NAME','DESCRIPTION','SOURCE','REFERENCE_YEAR','EVIDENCE_TYPE','LIMITATION_OR_NOTE']);w.writerows(DD)
with open(DOCS/'phase9_quality_checks.json','w',encoding='utf-8') as f:json.dump(qa,f,indent=2)
print(json.dumps({k:v for k,v in qa.items() if not isinstance(v,list)},indent=2))
print('AGE_MISSING',qa['master_codes_missing_age'])
print('SEIFA_MISSING',qa['master_codes_missing_seifa'])
