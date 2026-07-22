"""Traditional essential dignity scoring engine."""
SIGNS = ["aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces"]
DOMICILE = {"sun":"leo","moon":"cancer","mercury":"gemini","venus":"taurus","mars":"aries","jupiter":"sagittarius","saturn":"capricorn"}
EXALTATION = {"sun":"aries","moon":"taurus","mercury":"virgo","venus":"pisces","mars":"capricorn","jupiter":"cancer","saturn":"libra"}
DETRIMENT = {"sun":"aquarius","moon":"capricorn","mercury":"sagittarius","venus":"scorpio","mars":"libra","jupiter":"gemini","saturn":"cancer"}
FALL = {"sun":"libra","moon":"scorpio","mercury":"pisces","venus":"virgo","mars":"cancer","jupiter":"capricorn","saturn":"aries"}
SCORE = {"domicile":5,"exaltation":4,"triplicity":3,"term":2,"face":1,"detriment":-5,"fall":-4,"peregrine":0}

def sign_of(longitude): return SIGNS[int(longitude % 360 // 30)]

def score_dignity(body_id, longitude):
    sign = sign_of(longitude)
    conditions=[]
    if DOMICILE.get(body_id)==sign: conditions.append("domicile")
    if EXALTATION.get(body_id)==sign: conditions.append("exaltation")
    if DETRIMENT.get(body_id)==sign: conditions.append("detriment")
    if FALL.get(body_id)==sign: conditions.append("fall")
    if not conditions: conditions=["peregrine"]
    return {"body":body_id,"sign":sign,"conditions":conditions,"score":sum(SCORE[c] for c in conditions)}

def compute_dignities(bodies):
    return [score_dignity(b["id"], b["longitude"]) for b in bodies]
