


from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict,field_serializer
from zoneinfo import ZoneInfo

from src.utils import convert_datetime_to_gmt


class SummarySchema(BaseModel):
    name : str
    shop_name : str
    first_date : datetime
    last_date  : datetime
    first_value : int
    last_value : int
    min_price : int
    max_price : int
    avg_price : int
    min_offer : int
    records : int
    percent : float

    @field_serializer('first_date', 'last_date', mode='plain' , when_used='always')
    def serialize_dt(self, dt: datetime, _info):
        return convert_datetime_to_gmt(dt)

    class Config:
        orm_mode = True

class SummarytResponseModel(BaseModel):
    data : list[SummarySchema]