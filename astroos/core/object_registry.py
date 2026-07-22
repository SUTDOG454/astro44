"""Canonical celestial object registry for AstroSchema v3."""
from dataclasses import dataclass


@dataclass(frozen=True)
class AstroObject:
    id: str
    name: str
    category: str
    ephemeris_backend: str
    enabled_by_default: bool = True


CORE_OBJECTS = [
    AstroObject(x, x.replace("_", " ").title(), "planet", "swiss_ephemeris")
    for x in (
        "sun", "moon", "mercury", "venus", "mars", "jupiter", "saturn",
        "uranus", "neptune", "pluto", "mean_node", "true_node", "chiron"
    )
]

# Extended objects are registry entries first; calculation backends can be
# added without changing AstroSchema or downstream feature contracts.
EXTENDED_OBJECTS = [
    AstroObject("ceres", "Ceres", "asteroid", "swiss_ephemeris"),
    AstroObject("pallas", "Pallas", "asteroid", "swiss_ephemeris"),
    AstroObject("juno", "Juno", "asteroid", "swiss_ephemeris"),
    AstroObject("vesta", "Vesta", "asteroid", "swiss_ephemeris"),
    AstroObject("pholus", "Pholus", "centaur", "swiss_ephemeris"),
    AstroObject("nessus", "Nessus", "centaur", "swiss_ephemeris"),
    AstroObject("eris", "Eris", "tno", "swiss_ephemeris"),
    AstroObject("sedna", "Sedna", "tno", "swiss_ephemeris"),
    AstroObject("haumea", "Haumea", "tno", "swiss_ephemeris"),
    AstroObject("makemake", "Makemake", "tno", "swiss_ephemeris"),
]

OBJECT_REGISTRY = {obj.id: obj for obj in CORE_OBJECTS + EXTENDED_OBJECTS}
