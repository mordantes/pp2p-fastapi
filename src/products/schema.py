from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, field_serializer

from src.utils import convert_datetime_to_gmt


class ProductSchema(BaseModel):
    name: Optional[str]
    shop_name: Optional[str]
    category: Optional[str]
    sub_category: Optional[str]
    price: Optional[int]
    offer: Optional[int]
    parse_date: datetime

    @field_serializer("parse_date", mode="plain", when_used="always")
    def serialize_dt(self, dt: datetime, _info):
        return convert_datetime_to_gmt(dt)

    class ConfigDict:
        from_attributes = True


class ProductResponseModel(BaseModel):
    data: List[ProductSchema]
