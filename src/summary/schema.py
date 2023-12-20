


from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel,ConfigDict,field_serializer
from zoneinfo import ZoneInfo

from src.utils import convert_datetime_to_gmt


class SummarySchema(BaseModel):
    name : str
    shop_name : str
    first_date : datetime
    last_date  : datetime
    first_value : Optional[int]
    last_value : Optional[int]
    min_price : Optional[int]
    max_price : Optional[int]
    avg_price : Optional[float]
    min_offer : Optional[int]
    records : Optional[int]
    percent : Optional[float]
    
    class ConfigDict:
        from_attributes = True

    @field_serializer('first_date', 'last_date', mode='plain' , when_used='always')
    def serialize_dt(self, dt: datetime, _info):
        return convert_datetime_to_gmt(dt)


class SummarytResponseModel(BaseModel):
    data : List[SummarySchema]