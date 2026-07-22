"""FinancialAstroOS feature generation from astro-market event states."""

def financial_feature_vector(chart_features, market=None, macro=None):
    market=market or {}; macro=macro or {}
    strengths=chart_features.get("strengths",[])
    aspects=chart_features.get("aspects",[])
    return {
        "planetary_strength_mean": sum(x.get("strength_score",0) for x in strengths)/len(strengths) if strengths else 0.0,
        "aspect_density": len(aspects),
        "market": market,
        "macro": macro,
    }

def kcil_regime(gdp_growth, unemployment, inflation, fed_funds, yield_curve):
    score=0
    score += 1 if gdp_growth>0 else -1
    score += 1 if unemployment<5 else -1
    score += 1 if inflation<3 else -1
    score += 1 if yield_curve>=0 else -1
    score += 1 if fed_funds<6 else -1
    regime="expansion" if score>=3 else "contraction" if score<=-3 else "transition"
    return {"score":score,"regime":regime}
