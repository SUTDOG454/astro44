"""PredictiveOS feature generation from canonical natal/transit states."""
from astroos.engines.aspects import angular_distance

def transit_features(natal_bodies, transit_bodies):
    out=[]
    natal={b["id"]:b for b in natal_bodies}
    for t in transit_bodies:
        for n in natal_bodies:
            d=angular_distance(t["longitude"],n["longitude"])
            out.append({"transit":t["id"],"natal":n["id"],"separation":d,
                        "relative_speed":t.get("speed",0)-n.get("speed",0)})
    return out

def predictive_feature_vector(natal_bodies, transit_bodies):
    features=transit_features(natal_bodies,transit_bodies)
    return {"transit_count":len(features),"transit_features":features}
