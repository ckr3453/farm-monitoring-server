import datetime
from typing import List, Union
from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int
    value1: int
    value2: Union[int, None] = None
    start_time: Union[datetime.datetime, None] = None
    in_time: Union[datetime.datetime, None] = None

    class Config:
        orm_mode = True