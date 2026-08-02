"""Hypothesis promotion gate with explicit validation requirements."""
from astroos.analytics import posthog_client
def promotion_decision(metrics, min_oos_effect=0.0, min_replications=2):
    oos_effect=metrics.get("oos_effect",0.0)
    replications=metrics.get("replications",0)
    significant=bool(metrics.get("statistically_significant",False))
    robust=bool(metrics.get("robust",False))
    if significant and robust and oos_effect>min_oos_effect and replications>=min_replications:
        decision = "validated"
    elif oos_effect>min_oos_effect:
        decision = "candidate"
    else:
        decision = "rejected"
    if posthog_client is not None:
        posthog_client.capture(
            "hypothesis_evaluated",
            distinct_id="$astroos_system",
            properties={
                "decision": decision,
                "oos_effect": oos_effect,
                "replications": replications,
                "statistically_significant": significant,
                "robust": robust,
                "$process_person_profile": False,
            },
        )
    return decision
