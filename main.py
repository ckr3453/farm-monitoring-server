# -*- coding: utf-8 -*-
import json
from typing import List, Union
from fastapi import Depends, FastAPI, Response
from sqlalchemy.orm import Session
from starlette.middleware.cors import CORSMiddleware

import queries, models, schemas, database


models.database.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/listFilterResource")
def get_filter(response: Response, db: Session = Depends(get_db)):
    items, total_cnt = queries.get_list_filter_resource(db)
    response.headers['Content-Range'] = str(total_cnt)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    return items


@app.get("/FarmDatas", response_model=List[schemas.GeobongResponse])
def get_list(response: Response, filter: str, db: Session = Depends(get_db)):
    # range_list = json.loads(range)    # range: str
    # items, total_cnt = queries.get_list(db, skip=range_list[0], limit=range_list[1]-range_list[0]+1)
    items, total_cnt = queries.get_list(db, json.loads(filter))
    response.headers['Content-Range'] = str(total_cnt)
    response.headers['Access-Control-Expose-Headers'] = 'Content-Range'
    return items


@app.get("/FarmDatas/{id}", response_model=schemas.GeobongResponse)
def get_one(id: int, db: Session = Depends(get_db)):
    return queries.get_one(db, id)


@app.post("/FarmDatas", response_model=schemas.GeobongResponse)
def create(data: schemas.GeobongRequest, db: Session = Depends(get_db)):
    return queries.create(db, data)


@app.put("/FarmDatas/{id}", response_model=schemas.GeobongResponse)
def update(id: int, data: schemas.GeobongRequest, db: Session = Depends(get_db)):
    return queries.update(db, id, data)


@app.delete("/FarmDatas/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    return queries.delete(db, id)
