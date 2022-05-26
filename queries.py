import datetime
from sqlalchemy.orm import Session
import models


def get_list_filter_resource(db: Session):
    query = "SELECT distinct building_no from geobong"
    result = db.execute(query).mappings().all()
    print(result)
    return [result, len(result)]


def get_list(db: Session, skip: int, limit: int):
    # query = "SELECT *, datediff(now(), room_date)+22 as ilryung_days from geobong order by id limit {0}, {1}".format(skip, limit)
    query = "SELECT *, datediff(now(), room_date)+22 as ilryung_days from geobong order by id"
    result = db.execute(query).mappings().all()
    return [result, db.query(models.Geobong).count()]


def get_one(db: Session, id: int):
    query = "SELECT *, datediff(now(), room_date)+22 as ilryung_days from geobong where id={0}".format(id)
    result = db.execute(query).mappings().all()[0]
    return result


def create(db: Session, data: dict):
    if data['room_date'] == '':
        data['room_date'] = None
    if data['baby_food_date'] == '':
        data['baby_food_date'] = None
        data['shipment_date'] = None
    else:
        data['shipment_date'] = datetime.datetime.strptime(data['baby_food_date'], '%Y-%m-%d') + datetime.timedelta(
            days=158)
    data_instance = models.Geobong(building_no=data['building_no'], room_no=data['room_no'], pig_count=data['pig_count'], room_temp=data['room_temp'], baby_food_date=data['baby_food_date'], room_date=data['room_date'], shipment_date=data['shipment_date'])
    db.add(data_instance)
    db.commit()
    db.refresh(data_instance)
    return data_instance


def update(db: Session, id: int, data: dict):
    if data['room_date'] == '':
        data['room_date'] = None
    if data['baby_food_date'] == '':
        data['baby_food_date'] = None
        data['shipment_date'] = None
    else:
        data['shipment_date'] = datetime.datetime.strptime(data['baby_food_date'], '%Y-%m-%d') + datetime.timedelta(
            days=158)
    row = {
        'id': int(data['id']),
        'building_no': data['building_no'],
        'room_no': int(data['room_no']),
        'pig_count': float(data['pig_count']),
        'room_temp': float(data['room_temp']),
        'baby_food_date': data['baby_food_date'],
        'room_date': data['room_date'],
        'shipment_date': data['shipment_date']
    }
    db.query(models.Geobong).filter(models.Geobong.id == id).update(row)
    db.commit()

    return row


def delete(db: Session, id: int):
    db.query(models.Geobong).filter(models.Geobong.id == id).delete()
    return db.commit()
