"""SynastryOS cross-chart feature generation."""
from astroos.engines.aspects import angular_distance

def cross_chart_features(chart_a, chart_b):
    out=[]
    for a in chart_a:
        for b in chart_b:
            d=angular_distance(a["longitude"],b["longitude"])
            out.append({"a":a["id"],"b":b["id"],"separation":d,
                        "relative_speed":b.get("speed",0)-a.get("speed",0)})
    return out

def synastry_feature_vector(chart_a, chart_b):
    features=cross_chart_features(chart_a,chart_b)
    return {"pair_count":len(features),"cross_chart_features":features}
