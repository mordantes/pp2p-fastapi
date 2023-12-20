

from datetime import datetime
from zoneinfo import ZoneInfo
from src.database import Base

def convert_datetime_to_gmt(dt: datetime) -> str:
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))

    return dt.strftime("%Y-%m-%d %H:%M:%S")

