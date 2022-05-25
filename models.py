from sqlalchemy import Column, Integer, String, DateTime, Float
import database


class Geobong(database.Base):
    __tablename__ = "geobong"

    id = Column('no', Integer, primary_key=True, nullable=False)
    value1 = Column(Integer, nullable=False)
    value2 = Column(Integer, default=None)
    start_time = Column(DateTime, default=None)
    in_time = Column(DateTime, default=None)


# class Item(Base):
#     __tablename__ = "items"
#
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))
