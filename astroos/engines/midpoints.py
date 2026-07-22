"""Midpoint engine using circular longitude geometry."""
def midpoint_longitude(a: float, b: float) -> float:
    a %= 360.0; b %= 360.0
    delta = (b - a) % 360.0
    return (a + delta / 2.0) % 360.0

def midpoint_axis(a: float, b: float):
    m = midpoint_longitude(a, b)
    return {"short_arc": m, "opposite": (m + 180.0) % 360.0}

def compute_midpoints(bodies, include_self=False):
    out = []
    for i, a in enumerate(bodies):
        start = i if include_self else i + 1
        for b in bodies[start:]:
            if a["id"] == b["id"] and not include_self:
                continue
            axis = midpoint_axis(a["longitude"], b["longitude"])
            out.append({"a": a["id"], "b": b["id"], "longitude": axis["short_arc"],
                        "opposite": axis["opposite"]})
    return out

def midpoint_hits(midpoints, bodies, orb=1.5):
    hits = []
    for mp in midpoints:
        for body in bodies:
            d = min(abs(mp["longitude"] - body["longitude"]) % 360,
                    abs(body["longitude"] - mp["longitude"]) % 360)
            d = min(d, 360-d)
            if d <= orb:
                hits.append({**mp, "body": body["id"], "orb": d})
    return hits
