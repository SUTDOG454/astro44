"""Financial event ingestion contracts and normalized feature extraction."""
from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class MarketEvent:
    event_id:str; symbol:str; timestamp:datetime; event_type:str; value:float; metadata:dict

def normalize_event(raw):
    return MarketEvent(str(raw['event_id']),str(raw['symbol']),datetime.fromisoformat(str(raw['timestamp']).replace('Z','+00:00')),str(raw['event_type']),float(raw['value']),dict(raw.get('metadata',{})))

def event_features(events):
    return [{'event_id':e.event_id,'symbol':e.symbol,'timestamp':e.timestamp.isoformat(),'event_type':e.event_type,'value':e.value,'metadata':e.metadata} for e in events]
