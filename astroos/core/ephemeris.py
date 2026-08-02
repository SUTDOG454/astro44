"""Swiss Ephemeris adapter with explicit calculation provenance."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

try:
    import swisseph as swe
except ImportError:  # pragma: no cover
    swe = None

from astroos.analytics import posthog_client


@dataclass(frozen=True)
class EphemerisConfig:
    ephe_path: str | None = None
    flags: int = 2  # Swiss Ephemeris default: SWIEPH


class SwissEphemerisAdapter:
    """Thin, deterministic adapter around pyswisseph.

    Object-specific registries should map canonical AstroSchema IDs to Swiss
    Ephemeris constants. Unsupported objects are rejected rather than silently
    falling back to synthetic positions.
    """

    PLANETS = {
        "sun": 0,
        "moon": 1,
        "mercury": 2,
        "venus": 3,
        "mars": 4,
        "jupiter": 5,
        "saturn": 6,
        "uranus": 7,
        "neptune": 8,
        "pluto": 9,
        "mean_node": 10,
        "true_node": 11,
        "chiron": 15,
    }

    def __init__(self, config: EphemerisConfig | None = None) -> None:
        if swe is None:
            raise RuntimeError("pyswisseph is required for the Swiss Ephemeris adapter")
        self.config = config or EphemerisConfig()
        if self.config.ephe_path:
            swe.set_ephe_path(self.config.ephe_path)

    def calculate(self, julian_day_ut: float, object_ids: Iterable[str]) -> list[dict]:
        results = []
        for object_id in object_ids:
            if object_id not in self.PLANETS:
                raise ValueError(f"Unsupported Swiss Ephemeris object: {object_id}")
            xx, flags = swe.calc_ut(julian_day_ut, self.PLANETS[object_id], self.config.flags)
            results.append({
                "id": object_id,
                "longitude": float(xx[0]) % 360.0,
                "latitude": float(xx[1]),
                "distance_au": float(xx[2]),
                "speed": float(xx[3]),
                "retrograde": float(xx[3]) < 0,
                "declination": None,
                "calculation_flags": int(flags),
            })
        if posthog_client is not None:
            posthog_client.capture(
                "chart_calculated",
                distinct_id="$astroos_system",
                properties={
                    "object_count": len(results),
                    "flags": self.config.flags,
                    "retrograde_count": sum(1 for r in results if r["retrograde"]),
                    "$process_person_profile": False,
                },
            )
        return results
