


from datetime import datetime
from typing import Optional
from pydantic import BaseModel,ConfigDict,field_serializer
from zoneinfo import ZoneInfo

def convert_datetime_to_gmt(dt: datetime) -> str:
    if not dt.tzinfo:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))

    return dt.strftime("%Y-%m-%d %H:%M:%S")


class ProductSchema(BaseModel):
    index : int
    name : str
    shop_name : str
    category : str
    sub_category : str
    price : int
    offer : Optional[int]
    parse_date : datetime

    @field_serializer('parse_date', mode='plain' , when_used='always')
    def serialize_dt(self, dt: datetime, _info):
        return convert_datetime_to_gmt(dt)

    # class Config:
    #     orm_mode = True

class ProductResponseModel(BaseModel):
    data : list[ProductSchema]