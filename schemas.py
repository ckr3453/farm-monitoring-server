import datetime
from typing import Union
from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int
    building_no: str
    room_no: int
    pig_count: Union[float, None] = None
    room_temp: Union[float, None] = None
    baby_food_date: Union[datetime.date, None] = None
    room_date: Union[datetime.date, None] = None
    shipment_date: Union[datetime.date, None] = None
    ilryung_days: Union[int, None] = None

    class Config:
        orm_mode = True
