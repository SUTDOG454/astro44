"""Primary direction primitives using spherical right-ascension geometry."""
import math

def _norm(x): return x%360.0

def obliquity(jd):
    # IAU-style mean obliquity approximation, arcseconds polynomial.
    T=(jd-2451545.0)/36525.0
    sec=84381.448-4680.93*T-1.55*T*T+1999.25*T**3-51.38*T**4
    return sec/3600.0

def ecliptic_to_equatorial(lon,lat,eps):
    r=math.radians; L=r(lon); B=r(lat); E=r(eps)
    ra=math.degrees(math.atan2(math.sin(L)*math.cos(E)-math.tan(B)*math.sin(E),math.cos(L)))%360
    dec=math.degrees(math.asin(math.sin(B)*math.cos(E)+math.cos(B)*math.sin(E)*math.sin(L)))
    return ra,dec

def arc_to_years(arc, key=1.0): return arc/key

def symbolic_primary_direction(planet, angle, significator, promissor, key=1.0):
    return {'planet':planet,'angle':angle,'significator':significator,'promissor':promissor,'arc_degrees':_norm(angle),'years_from_natal':arc_to_years(_norm(angle),key),'key':key,'method':'RA-spherical-contract'}
