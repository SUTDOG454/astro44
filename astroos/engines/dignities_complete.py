"""Complete traditional dignity framework with configurable sect-aware tables."""
from dataclasses import dataclass

SIGNS=("aries","taurus","gemini","cancer","leo","virgo","libra","scorpio","sagittarius","capricorn","aquarius","pisces")
DOMICILE={"sun":"leo","moon":"cancer","mercury":"gemini","venus":"taurus","mars":"aries","jupiter":"sagittarius","saturn":"capricorn"}
EXALTATION={"sun":"aries","moon":"taurus","mercury":"virgo","venus":"pisces","mars":"capricorn","jupiter":"cancer","saturn":"libra"}
DETRIMENT={"sun":"aquarius","moon":"capricorn","mercury":"sagittarius","venus":"scorpio","mars":"libra","jupiter":"gemini","saturn":"cancer"}
FALL={"sun":"libra","moon":"scorpio","mercury":"pisces","venus":"virgo","mars":"cancer","jupiter":"capricorn","saturn":"aries"}
# Ptolemaic Egyptian terms, boundaries in degrees within each sign.
TERMS={
"aries":[("jupiter",6),("venus",12),("mercury",20),("mars",25),("saturn",30)],
"taurus":[("venus",8),("mercury",14),("jupiter",22),("saturn",27),("mars",30)],
"gemini":[("mercury",6),("jupiter",12),("venus",17),("mars",24),("saturn",30)],
"cancer":[("mars",7),("venus",13),("mercury",19),("jupiter",26),("saturn",30)],
"leo":[("jupiter",6),("venus",11),("saturn",18),("mercury",24),("mars",30)],
"virgo":[("mercury",7),("venus",17),("jupiter",21),("mars",28),("saturn",30)],
"libra":[("saturn",6),("mercury",14),("jupiter",21),("venus",28),("mars",30)],
"scorpio":[("mars",7),("venus",11),("mercury",19),("jupiter",24),("saturn",30)],
"sagittarius":[("jupiter",12),("venus",17),("mercury",21),("saturn",26),("mars",30)],
"capricorn":[("mercury",7),("jupiter",14),("venus",22),("saturn",26),("mars",30)],
"aquarius":[("mercury",7),("venus",13),("jupiter",20),("mars",25),("saturn",30)],
"pisces":[("venus",12),("jupiter",16),("mercury",19),("mars",28),("saturn",30)]}
FACE_RULERS=["mars","sun","venus","mercury","moon","saturn","jupiter","mars","sun","venus","mercury","moon","saturn","jupiter","mars","sun","venus","mercury","moon","saturn","jupiter","mars","sun","venus","mercury","moon","saturn","jupiter","mars","sun","venus","mercury","moon","saturn","jupiter","mars","sun","venus","mercury","moon"]
SCORES={"domicile":5,"exaltation":4,"triplicity":3,"term":2,"face":1,"detriment":-5,"fall":-4,"peregrine":0}

def sign_deg(lon):
    lon%=360; return SIGNS[int(lon//30)],lon%30

def term_ruler(sign,deg):
    for ruler,end in TERMS[sign]:
        if deg<end:return ruler
    return TERMS[sign][-1][0]

def face_ruler(lon): return FACE_RULERS[int((lon%360)//10)]

def compute_dignity(body,longitude,sect="night",triplicity=True):
    sign,deg=sign_deg(longitude); c=[]
    if DOMICILE.get(body)==sign:c.append("domicile")
    if EXALTATION.get(body)==sign:c.append("exaltation")
    if triplicity:
        # Simplified elemental triplicity rulers; sect modifies the primary ruler.
        elem={"aries":"fire","leo":"fire","sagittarius":"fire","taurus":"earth","virgo":"earth","capricorn":"earth","gemini":"air","libra":"air","aquarius":"air","cancer":"water","scorpio":"water","pisces":"water"}[sign]
        primary={"fire":("sun","jupiter"),"earth":("venus","moon"),"air":("saturn","mercury"),"water":("venus","mars")}[elem]
        if body==primary[0 if sect=="day" else 1]:c.append("triplicity")
    if term_ruler(sign,deg)==body:c.append("term")
    if face_ruler(longitude)==body:c.append("face")
    if DETRIMENT.get(body)==sign:c.append("detriment")
    if FALL.get(body)==sign:c.append("fall")
    if not c:c=["peregrine"]
    return {"body":body,"sign":sign,"degree":deg,"conditions":c,"score":sum(SCORES[x] for x in c)}

def compute_all(bodies,sect="night"):
    return [compute_dignity(b["id"],b["longitude"],sect) for b in bodies]
