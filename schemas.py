import datetime
from typing import Union
from pydantic import BaseModel


class GeobongResponse(BaseModel):
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


class GeobongRequest(BaseModel):
    building_no: str
    room_no: str
    pig_count: Union[str, None] = None
    room_temp: Union[str, None] = None
    baby_food_date: Union[str, None] = None
    room_date: Union[str, None] = None
    shipment_date: Union[str, None] = None
    ilryung_days: Union[str, None] = None


# class Pagination(BaseModel):
#     page: Union[str, None] = None
#     perPage: Union[str, None] = None
#
#
# class Sort(BaseModel):
#     field: Union[str, None] = None
#     order: Union[str, None] = None
#
#
# class GetListRequest(BaseModel):
#     pagination: Pagination
#     sort: Sort
#     filter: Union[dict, None] = None

