"""Advanced predictive-system contracts and deterministic feature orchestration."""
from dataclasses import dataclass

@dataclass(frozen=True)
class PredictiveTechnique:
    name:str; weight:float; enabled:bool=True

DEFAULT_TECHNIQUES=(PredictiveTechnique('transits',1.0),PredictiveTechnique('secondary_progressions',1.0),PredictiveTechnique('solar_arcs',1.0),PredictiveTechnique('returns',0.8),PredictiveTechnique('primary_directions',1.2),PredictiveTechnique('firdaria',0.8),PredictiveTechnique('vimshottari',0.8),PredictiveTechnique('zodiacal_releasing',0.8))

def fuse_techniques(outputs,techniques=DEFAULT_TECHNIQUES):
    result={}; total=0.0
    for t in techniques:
        if not t.enabled: continue
        rows=outputs.get(t.name,[]); result[t.name]={'events':rows,'weight':t.weight,'count':len(rows)}; total+=t.weight*len(rows)
    result['aggregate_activity_score']=total
    return result

def firdaria_periods(start_year,sect='night',years=75):
    day=['sun','venus','mercury','moon','saturn','jupiter','mars']; night=['moon','saturn','jupiter','mars','sun','venus','mercury']; order=night if sect=='night' else day; durations={'sun':10,'venus':8,'mercury':13,'moon':25,'saturn':11,'jupiter':12,'mars':7}; out=[]; y=start_year
    for p in range(years//1):
        planet=order[p%7]; out.append({'planet':planet,'start_year':y,'end_year':y+durations[planet]}); y+=durations[planet]
        if y>=start_year+years: break
    return out

def vimshottari_sequence(start_year,years=120):
    order=['ketu','venus','sun','moon','mars','rahu','jupiter','saturn','mercury']; durations={'ketu':7,'venus':20,'sun':6,'moon':10,'mars':7,'rahu':18,'jupiter':16,'saturn':19,'mercury':17}; out=[]; y=start_year
    while y<start_year+years:
        for p in order:
            out.append({'planet':p,'start_year':y,'end_year':y+durations[p]}); y+=durations[p]
            if y>=start_year+years: break
    return out

def zodiacal_releasing_sequence(start_year,years=30):
    return [{'level':1,'start_year':start_year,'end_year':start_year+years,'lot':'fortune_or_spirit'}]
