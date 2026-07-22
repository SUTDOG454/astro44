"""Configurable fixed-star conjunction engine.

Star longitudes are versioned inputs, not hard-coded truths; callers should
supply an epoch-appropriate catalog generated from the chosen reference source.
"""
def star_hits(bodies, stars, orb=1.0):
    hits = []
    for body in bodies:
        for star in stars:
            d = abs((body["longitude"] - star["longitude"]) % 360.0)
            d = min(d, 360.0 - d)
            if d <= star.get("orb", orb):
                hits.append({"body": body["id"], "star": star["id"],
                             "longitude": star["longitude"], "orb": d,
                             "magnitude": star.get("magnitude"),
                             "keywords": star.get("keywords", [])})
    return hits
