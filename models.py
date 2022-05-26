from sqlalchemy import Column, Integer, String, DateTime, Float, Date
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

# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
