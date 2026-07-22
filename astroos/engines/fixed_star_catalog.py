"""Versioned fixed-star catalog contract and epoch-aware propagation.

Catalog rows are intentionally data-driven: production deployments should load
all 1,127 rows from a versioned source file rather than embedding mutable star
positions in calculation code.
"""
from dataclasses import dataclass

@dataclass(frozen=True)
class FixedStar:
    id:str; name:str; longitude_j2000:float; latitude_j2000:float=0.0
    magnitude:float|None=None; keywords:tuple[str,...]=(); source:str='catalog'; catalog_version:str='1.0'

def propagate_longitude(star:FixedStar, epoch_year:float, precession_rate=0.013968):
    return (star.longitude_j2000 + (epoch_year-2000.0)*precession_rate) % 360.0

def catalog_provenance(star:FixedStar, epoch_year:float):
    return {'catalog_version':star.catalog_version,'source':star.source,'reference_epoch':2000.0,'target_epoch':epoch_year,'precession_model':'linear_default'}

def load_catalog(rows):
    return [FixedStar(r['id'],r['name'],float(r['longitude_j2000']),float(r.get('latitude_j2000',0)),r.get('magnitude'),tuple(r.get('keywords',())),r.get('source','catalog'),r.get('catalog_version','1.0')) for r in rows]

def epoch_star_rows(catalog,epoch_year):
    return [{'id':s.id,'name':s.name,'longitude':propagate_longitude(s,epoch_year),'latitude':s.latitude_j2000,'magnitude':s.magnitude,'keywords':list(s.keywords),'provenance':catalog_provenance(s,epoch_year)} for s in catalog]
