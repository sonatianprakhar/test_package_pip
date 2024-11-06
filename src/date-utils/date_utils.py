
from datetime import datetime, timezone


def get_current_date():
    current_date = datetime.now(timezone.utc).strftime("%Y%m%d")
    return current_date