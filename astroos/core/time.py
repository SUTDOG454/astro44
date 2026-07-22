"""Historical timezone/DST normalization with explicit provenance."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from zoneinfo import ZoneInfo


@dataclass(frozen=True)
class NormalizedTime:
    local_datetime: str
    timezone_name: str
    utc_datetime: str
    utc_offset_seconds: int
    dst_applied: bool


def normalize_local_time(local_datetime: datetime, timezone_name: str) -> NormalizedTime:
    """Resolve a civil datetime using the IANA timezone database.

    Callers should reject ambiguous/nonexistent wall times at ingestion when the
    source does not provide a fold/transition policy. Python's zoneinfo is used
    here so historical offsets are derived from the system IANA tzdata rather
    than a fixed offset table.
    """
    if local_datetime.tzinfo is not None:
        raise ValueError("local_datetime must be timezone-naive")
    zone = ZoneInfo(timezone_name)
    aware = local_datetime.replace(tzinfo=zone)
    utc = aware.astimezone(timezone.utc)
    offset = aware.utcoffset()
    dst = aware.dst()
    return NormalizedTime(
        local_datetime=local_datetime.isoformat(),
        timezone_name=timezone_name,
        utc_datetime=utc.isoformat().replace("+00:00", "Z"),
        utc_offset_seconds=int(offset.total_seconds()) if offset else 0,
        dst_applied=bool(dst and dst.total_seconds() != 0),
    )
