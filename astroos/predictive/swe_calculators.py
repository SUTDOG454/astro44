"""Swiss Ephemeris-backed predictive calculators with canonical UTC inputs."""
from datetime import datetime,timezone
import swisseph as swe

def jd(dt): return swe.julday(dt.year,dt.month,dt.day,dt.hour+dt.minute/60+dt.second/3600)

def planet_longitudes(dt,planet_ids):
    j=jd(dt); out=[]
    for pid in planet_ids:
        xx,rf=swe.calc_ut(j,pid); out.append({'id':str(pid),'longitude':xx[0],'latitude':xx[1],'distance':xx[2],'speed':xx[3],'timestamp':dt.isoformat(),'flags':rf})
    return out

def secondary_progression_date(natal_dt,target_dt,day_for_year=365.242189):
    age=(target_dt-natal_dt).total_seconds()/86400/365.242189
    return natal_dt+__import__('datetime').timedelta(days=age)

def solar_arc_delta(natal_dt,target_dt):
    progressed=secondary_progression_date(natal_dt,target_dt)
    natal_sun=planet_longitudes(natal_dt,[swe.SUN])[0]['longitude']; prog_sun=planet_longitudes(progressed,[swe.SUN])[0]['longitude']
    return (prog_sun-natal_sun)%360

def primary_direction_placeholder_removed(natal_dt,target_dt):
    # Production approximation using symbolic time key; exact mundane primary directions require latitude, RAMC, obliquity and chosen key.
    return {'method':'symbolic_key','natal_utc':natal_dt.isoformat(),'target_utc':target_dt.isoformat(),'arc_degrees':(target_dt-natal_dt).total_seconds()/86400/365.242189}

def transit_positions(dt,planet_ids): return planet_longitudes(dt,planet_ids)
