import datetime

from sqlalchemy import Column, Integer, String, Float, Date
import database


class Geobong(database.Base):
    __tablename__ = "geobong"

    id = Column(Integer, primary_key=True, autoincrement=True)
    building_no = Column(String, nullable=False)
    room_no = Column(Integer, nullable=False)
    pig_count = Column(Float, nullable=False)
    room_temp = Column(Float)
    baby_food_date = Column(Date)
    room_date = Column(Date)
    shipment_date = Column(Date)

    def __init__(self, building_no, room_no, pig_count, room_temp, baby_food_date=None, room_date=None):
        # 여기서 그냥 초기화
        self.building_no = building_no
        self.room_no = room_no
        self.pig_count = pig_count
        self.room_temp = room_temp
        self.baby_food_date = baby_food_date
        self.room_date = room_date
        self.shipment_date = None if baby_food_date is None else datetime.datetime.strptime(baby_food_date, '%Y-%m-%d') + datetime.timedelta(days=158)

    def __repr__(self):
        return 'id=%s, building_no=%s, room_no=%s, pig_count=%s, room_temp=%s, baby_food_date=%s, room_date=%s, shipment_date=%s' % (
            self.id, self.building_no, self.room_no, self.pig_count, self.room_temp, self.baby_food_date, self.room_date, self.shipment_date)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'building_no': self.building_no,
            'room_no': self.room_no,
            'pig_count': self.pig_count,
            'room_temp': self.room_temp,
            'baby_food_date': self.baby_food_date,
            'room_date': self.room_date,
            'shipment_date': self.shipment_date
        }
