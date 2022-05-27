import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func, asc
import models
import schemas


def sql_query_exec(db: Session, query: str):
    print('query:', query)
    try:
        result = db.execute(query).mappings().all()
    except Exception as err:
        result = {}
        print(err)
    finally:
        db.close()

    return result


def get_list_filter_resource(db: Session):
    result = sql_query_exec(db, "SELECT distinct building_no as id, building_no "
                                "from geobong")
    return [result, len(result)]


def get_list(db: Session, filter: dict):
    # ilryung_days = func.datediff(func.current_date(), models.Geobong.room_date) + 22
    # result = db.query(models.Geobong, ilryung_days).filter(filter).order_by(asc(models.Geobong.id)).all()
    # response = [dict(tup) for tup in result]

    query = "SELECT *, datediff(now(), room_date)+22 as ilryung_days from geobong "
    if 'building_no' in filter:
        query += "where building_no='{0}'".format(filter['building_no'])
    result = sql_query_exec(db, query+" order by id")
    return [result, len(result)]


def get_one(db: Session, id: int):
    result = sql_query_exec(db, "SELECT *, datediff(now(), room_date)+22 as ilryung_days "
                                "from geobong "
                                "where id={0}"
                            .format(id))
    return result[0]


def create(db: Session, data: schemas.GeobongRequest):
    model_instance = models.Geobong(building_no=data.building_no, room_no=data.room_no,
                                    pig_count=data.pig_count, room_temp=data.room_temp,
                                    baby_food_date=data.baby_food_date, room_date=data.room_date)
    db.add(model_instance)
    db.commit()
    return model_instance


def update(db: Session, id: int, data: schemas.GeobongRequest):
    geobong = db.query(models.Geobong).filter(models.Geobong.id == id).first()
    geobong.building_no = data.building_no
    geobong.room_no = data.room_no
    geobong.pig_count = data.pig_count
    geobong.room_temp = data.room_temp
    geobong.baby_food_date = None if data.baby_food_date == '' else data.baby_food_date
    geobong.room_date = None if data.room_date == '' else data.room_date
    geobong.shipment_date = None if data.baby_food_date in ('', None) else datetime.datetime.strptime(data.baby_food_date, '%Y-%m-%d') \
                                                                     + datetime.timedelta(days=158)
    db.commit()

    return geobong


def delete(db: Session, id: int):
    db.query(models.Geobong).filter(models.Geobong.id == id).delete()
    return db.commit()
