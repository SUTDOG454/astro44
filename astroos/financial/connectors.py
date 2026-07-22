"""Provider-neutral financial/economic event ingestion adapters."""
from dataclasses import dataclass
from datetime import datetime,timezone
import csv,io
@dataclass(frozen=True)
class FinancialRecord:
    symbol:str; timestamp:datetime; open:float; high:float; low:float; close:float; volume:float; source:str

def parse_ohlcv_csv(text,source='csv'):
    out=[]
    for r in csv.DictReader(io.StringIO(text)):
        ts=datetime.fromisoformat(r['timestamp'].replace('Z','+00:00')).astimezone(timezone.utc)
        out.append(FinancialRecord(r['symbol'],ts,float(r['open']),float(r['high']),float(r['low']),float(r['close']),float(r.get('volume',0)),source))
    return out

def normalize_economic_event(event):
    ts=datetime.fromisoformat(event['timestamp'].replace('Z','+00:00')).astimezone(timezone.utc)
    return {'event_id':event['event_id'],'indicator':event['indicator'],'country':event.get('country'),'timestamp':ts.isoformat(),'actual':event.get('actual'),'forecast':event.get('forecast'),'previous':event.get('previous'),'source':event.get('source','unknown')}

def normalize_corporate_event(event):
    return {'event_id':event['event_id'],'symbol':event['symbol'],'event_type':event['event_type'],'effective_timestamp':datetime.fromisoformat(event['effective_timestamp'].replace('Z','+00:00')).astimezone(timezone.utc).isoformat(),'announcement_timestamp':datetime.fromisoformat(event['announcement_timestamp'].replace('Z','+00:00')).astimezone(timezone.utc).isoformat(),'payload':event.get('payload',{}),'source':event.get('source','unknown')}
