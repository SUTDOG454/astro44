"""Composite/Davison angle and house calculations."""
import math

def _wrap(x): return x%360.0

def local_sidereal_time(jd,longitude):
    T=(jd-2451545.0)/36525.0
    gst=(280.46061837+360.98564736629*(jd-2451545)+0.000387933*T*T-T*T*T/38710000)%360
    return _wrap(gst+longitude)

def asc_mc(jd,lat,lon,eps=23.439291):
    theta=math.radians(local_sidereal_time(jd,lon)); phi=math.radians(lat); e=math.radians(eps)
    mc=math.degrees(math.atan2(math.sin(theta)*math.cos(e),math.cos(theta)))%360
    asc=math.degrees(math.atan2(-math.cos(theta),math.sin(theta)*math.cos(e)+math.tan(phi)*math.sin(e)))%360
    return {'ascendant':asc,'mc':mc}

def whole_sign_houses(asc):
    rising=int(asc//30)*30
    return [{'house':i,'cusp':(rising+(i-1)*30)%360} for i in range(1,13)]

def composite_angles(jd,lat,lon):
    angles=asc_mc(jd,lat,lon); return {**angles,'houses':whole_sign_houses(angles['ascendant']),'house_system':'whole_sign'}
