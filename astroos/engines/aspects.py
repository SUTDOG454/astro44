"""Deterministic aspect detection engine."""
from dataclasses import dataclass

@dataclass(frozen=True)
class AspectRule:
    name: str
    angle: float
    orb: float
    weight: float

DEFAULT_ASPECTS = (
    AspectRule("conjunction", 0.0, 8.0, 1.00),
    AspectRule("opposition", 180.0, 8.0, 0.95),
    AspectRule("trine", 120.0, 7.0, 0.85),
    AspectRule("square", 90.0, 7.0, 0.90),
    AspectRule("sextile", 60.0, 5.0, 0.70),
    AspectRule("quincunx", 150.0, 3.0, 0.45),
)

def angular_distance(a: float, b: float) -> float:
    d = abs((a - b) % 360.0)
    return min(d, 360.0 - d)

def detect_aspects(bodies, rules=DEFAULT_ASPECTS):
    out = []
    for i, a in enumerate(bodies):
        for b in bodies[i + 1:]:
            separation = angular_distance(a["longitude"], b["longitude"])
            for rule in rules:
                delta = abs(separation - rule.angle)
                if delta <= rule.orb:
                    out.append({"a": a["id"], "b": b["id"], "aspect": rule.name,
                                "exact_angle": rule.angle, "orb": delta,
                                "applying": _applying(a, b, rule.angle), "weight": rule.weight})
                    break
    return out

def _applying(a, b, angle):
    # Approximate applying state from relative longitudinal velocity.
    sep = (b["longitude"] - a["longitude"]) % 360.0
    speed = b.get("speed", 0.0) - a.get("speed", 0.0)
    target = angle % 360.0
    return abs(((sep + speed) - target + 180) % 360 - 180) < abs((sep - target + 180) % 360 - 180)
