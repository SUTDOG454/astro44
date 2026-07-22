"""Hypothesis promotion gate with explicit validation requirements."""
def promotion_decision(metrics, min_oos_effect=0.0, min_replications=2):
    oos_effect=metrics.get("oos_effect",0.0)
    replications=metrics.get("replications",0)
    significant=bool(metrics.get("statistically_significant",False))
    robust=bool(metrics.get("robust",False))
    if significant and robust and oos_effect>min_oos_effect and replications>=min_replications:
        return "validated"
    if oos_effect>min_oos_effect:
        return "candidate"
    return "rejected"
