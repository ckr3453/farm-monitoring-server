import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

base_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(base_dir, 'config.json')
config_json = json.loads(open(config_file).read())
database = config_json["database_info"]
database_url = f"mysql+pymysql://{database['username']}:{database['password']}@{database['host']}:{database['port']}/{database['database']}?charset=utf8"

engine = create_engine(
    database_url, encoding='utf-8'
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
