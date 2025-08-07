from datetime import datetime, timezone


def utc_naive_now() -> datetime:
    """Return UTC time as naive datetime (no tzinfo) for DB insertion."""
    return datetime.now(timezone.utc).replace(tzinfo=None)
