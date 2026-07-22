from datetime import datetime

from astroos.core.time import normalize_local_time


def test_historical_dst_resolution():
    result = normalize_local_time(datetime(1974, 4, 10, 19, 2, 0), "America/New_York")
    assert result.utc_datetime == "1974-04-10T23:02:00Z"
    assert result.utc_offset_seconds == -14400
    assert result.dst_applied is True
