from datetime import datetime

from sqlalchemy.orm import Session

import models
import schemas


def get_list(db: Session, skip: int, limit: int):
    return [db.query(models.Geobong).offset(skip).limit(limit).all(), db.query(models.Geobong).count()]


def get_one(db: Session, id: int):
    return db.query(models.Geobong).filter(models.Geobong.id == id).first()


def create(db: Session, data: dict):
    data_instance = models.Geobong(id=data['no'], value1=data['value1'], value2=data['value2'], start_time=data['start_time'], in_time=data['in_time'])
    db.add(data_instance)
    db.commit()
    db.refresh(data_instance)
    return data_instance


def update(db: Session, id: int, data: dict):
    print(data['start_time'][:10])
    try:
        row = {'id': data['id'], 'value1': data['value1'], 'value2': data['value2'], 'start_time': data['start_time'][:10], 'in_time': data['in_time'][:10]}
        db.query(models.Geobong).filter(models.Geobong.id == id).update(row)
        db.commit()
        data_instance = models.Geobong(id=data['id'], value1=data['value1'], value2=data['value2'], start_time=data['start_time'][:10], in_time=data['in_time'][:10])
        db.refresh(data_instance)
    except Exception as err:
        data_instance = {}
        print(err)
    return data_instance


def delete(db: Session, id: int):
    db.query(models.Geobong).filter(models.Geobong.id == id).delete()
    return db.commit()
