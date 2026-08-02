"""PredictiveOS timing feature generators."""
from dataclasses import dataclass

from astroos.analytics import posthog_client

@dataclass(frozen=True)
class TimingEvent:
    system:str; source:str; target:str; timestamp:str; score:float; metadata:dict

def aspect_hits(transits,natal,angles=(0,60,90,120,150,180),orb=1.0):
    out=[]
    for t in transits:
        for n in natal:
            d=abs((t['longitude']-n['longitude'])%360); d=min(d,360-d)
            for a in angles:
                if abs(d-a)<=orb:
                    out.append(TimingEvent('transit',t['id'],n['id'],t.get('timestamp',''),1-abs(d-a)/orb,{'aspect':a,'orb':abs(d-a)}))
    return out

def secondary_progression_features(progressions,natal): return [e.__dict__ for e in aspect_hits(progressions,natal)]
def solar_arc_features(arcs,natal): return [e.__dict__ for e in aspect_hits(arcs,natal)]
def return_features(return_bodies,natal): return [e.__dict__ for e in aspect_hits(return_bodies,natal,angles=(0,),orb=1.0)]

def fused_timing_features(natal,transits=None,progressions=None,solar_arcs=None,returns=None):
    result = {'transits':[e.__dict__ for e in aspect_hits(transits or [],natal)],'progressions':secondary_progression_features(progressions or [],natal),'solar_arcs':solar_arc_features(solar_arcs or [],natal),'returns':return_features(returns or [],natal)}
    if posthog_client is not None:
        posthog_client.capture(
            "timing_features_generated",
            distinct_id="$astroos_system",
            properties={
                "transit_hit_count": len(result["transits"]),
                "progression_hit_count": len(result["progressions"]),
                "solar_arc_hit_count": len(result["solar_arcs"]),
                "return_hit_count": len(result["returns"]),
                "$process_person_profile": False,
            },
        )
    return result
