"""Unified AstroOS feature pipeline contract."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from astroos.analytics import posthog_client


@dataclass(frozen=True)
class PipelineConfig:
    zodiac: str = "tropical"
    house_system: str = "placidus"
    coordinate_system: str = "geocentric"
    aspect_set: str = "master"
    midpoint_set: str = "master"
    fixed_star_set: str = "master"
    dignity_model: str = "traditional_plus_modern"
    strength_model: str = "astroos_default"


@dataclass
class PipelineResult:
    chart: dict[str, Any]
    features: dict[str, Any] = field(default_factory=dict)


class AstroOSPipeline:
    """Orchestrates canonical chart calculation and analytical engines.

    Engine implementations are injected. This prevents PredictiveOS,
    SynastryOS, FinancialAstroOS, and AFM/AFA from coupling directly to the
    astronomical backend.
    """

    def __init__(self, ephemeris, engines: dict[str, Any] | None = None):
        self.ephemeris = ephemeris
        self.engines = engines or {}

    def run(self, chart: dict[str, Any], config: PipelineConfig | None = None) -> PipelineResult:
        config = config or PipelineConfig()
        features: dict[str, Any] = {}
        for name in ("aspects", "midpoints", "fixed_stars", "dignities", "strength"):
            engine = self.engines.get(name)
            if engine is not None:
                features[name] = engine.compute(chart, config)
        if posthog_client is not None:
            posthog_client.capture(
                "pipeline_run",
                distinct_id="$astroos_system",
                properties={
                    "zodiac": config.zodiac,
                    "house_system": config.house_system,
                    "coordinate_system": config.coordinate_system,
                    "aspect_set": config.aspect_set,
                    "engines_run": list(features.keys()),
                    "engine_count": len(features),
                    "$process_person_profile": False,
                },
            )
        return PipelineResult(chart=chart, features=features)
