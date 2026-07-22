"""Composite chart strength engine."""

def compute_strength(bodies, aspects=None, dignities=None, fixed_star_hits=None):
    aspects = aspects or []; dignities = dignities or []; fixed_star_hits = fixed_star_hits or []
    dignity_by_body={d["body"]:d["score"] for d in dignities}
    aspect_count={b["id"]:0 for b in bodies}
    for a in aspects:
        aspect_count[a["a"]]=aspect_count.get(a["a"],0)+1
        aspect_count[a["b"]]=aspect_count.get(a["b"],0)+1
    star_count={b["id"]:0 for b in bodies}
    for h in fixed_star_hits: star_count[h["body"]]=star_count.get(h["body"],0)+1
    out=[]
    for b in bodies:
        raw = dignity_by_body.get(b["id"],0) + aspect_count.get(b["id"],0)*0.5 + star_count.get(b["id"],0)*1.0
        out.append({"body":b["id"],"dignity_score":dignity_by_body.get(b["id"],0),
                    "aspect_count":aspect_count.get(b["id"],0),"fixed_star_hits":star_count.get(b["id"],0),
                    "strength_score":round(raw,3)})
    return out
