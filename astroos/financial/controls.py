"""Financial data integrity controls: survivorship and corporate actions."""
def apply_corporate_action(price,action):
    typ=action.get('type'); factor=float(action.get('factor',1.0))
    if typ in ('split','reverse_split','stock_dividend'): return price/factor if factor else price
    return price

def normalize_timestamp(ts,timezone_name='UTC'):
    from datetime import datetime,timezone
    from zoneinfo import ZoneInfo
    dt=datetime.fromisoformat(str(ts).replace('Z','+00:00'))
    if dt.tzinfo is None: dt=dt.replace(tzinfo=ZoneInfo(timezone_name))
    return dt.astimezone(timezone.utc)

def survivorship_filter(records,as_of):
    return [r for r in records if r.get('listed_from') is None or r['listed_from']<=as_of]

def point_in_time_join(astro_events,market_events,tolerance_seconds=86400):
    out=[]
    for a in astro_events:
        best=None; best_delta=None
        for m in market_events:
            d=abs((normalize_timestamp(a['timestamp'])-normalize_timestamp(m['timestamp'])).total_seconds())
            if d<=tolerance_seconds and (best_delta is None or d<best_delta): best,best_delta=m,d
        if best: out.append({'astro':a,'market':best,'delta_seconds':best_delta})
    return out
