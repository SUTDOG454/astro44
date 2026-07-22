"""Composite and Davison chart calculation from two chart states."""
from datetime import datetime,timezone

def _mid(a,b):
    d=(b-a)%360; return (a+d/2)%360

def composite_positions(chart_a,chart_b):
    ids=sorted(set(x['id'] for x in chart_a)&set(x['id'] for x in chart_b)); A={x['id']:x for x in chart_a};B={x['id']:x for x in chart_b}
    return [{'id':i,'longitude':_mid(A[i]['longitude'],B[i]['longitude']),'latitude':(A[i].get('latitude',0)+B[i].get('latitude',0))/2,'speed':(A[i].get('speed',0)+B[i].get('speed',0))/2} for i in ids]

def davison_positions(chart_a,chart_b):
    # Davison requires midpoint in time and location; callers provide the two
    # source chart timestamps/coordinates and calculate ephemerides at midpoint.
    ta=datetime.fromisoformat(chart_a['utc_datetime'].replace('Z','+00:00'));tb=datetime.fromisoformat(chart_b['utc_datetime'].replace('Z','+00:00'))
    midpoint=ta+(tb-ta)/2
    return {'midpoint_utc':midpoint.astimezone(timezone.utc).isoformat().replace('+00:00','Z'),'latitude':(chart_a['latitude']+chart_b['latitude'])/2,'longitude':(chart_a['longitude']+chart_b['longitude'])/2}
