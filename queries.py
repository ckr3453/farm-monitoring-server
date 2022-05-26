from datetime import datetime

from sqlalchemy.orm import Session
from sqlalchemy import func

import models


def get_list(db: Session, skip: int, limit: int):
    return [db.query(models.Geobong).offset(skip).limit(limit).all(), db.query(models.Geobong).count()]


def get_one(db: Session, id: int):
    return db.query(models.Geobong).filter_by(id=id).first()


def create(db: Session, data: dict):
    # 수정필요
    # data['shipment_date'] = datetime.strptime(data['baby_food_date'],'%Y%m%d') - datetime.timedelta(days=158)
    data_instance = models.Geobong(pig_count=data['pig_count'], room_temp=data['room_temp'], baby_food_date=data['baby_food_date'], room_date=data['room_date'], shipment_date=data['shipment_date'])
    db.add(data_instance)
    db.commit()
    db.refresh(data_instance)
    return data_instance


def update(db: Session, id: int, data: dict):
    try:
        row = {'id': int(data['id']), 'value1': int(data['value1']), 'value2': data['value2'], 'start_time': data['start_time'][:10], 'in_time': data['in_time'][:10]}
        db.query(models.Geobong).filter(models.Geobong.id == id).update(row)
        db.commit()
        data_instance = models.Geobong(id=int(data['id']), value1=int(data['value1']), value2=data['value2'], start_time=datetime.strptime(data['start_time'][:10], '%Y-%m-%d'), in_time=datetime.strptime(data['in_time'][:10], '%Y-%m-%d'))
        #db.refresh(data_instance)
    except Exception as err:
        data_instance = {}
        print(err)
    return data_instance


def delete(db: Session, id: int):
    db.query(models.Geobong).filter(models.Geobong.id == id).delete()
    return db.commit()
