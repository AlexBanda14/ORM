import sqlalchemy
from sqlalchemy.orm import sessionmaker
from db_login import *


DSN = f'postgresql://{login}:{password}@{localhost}/{name_db}'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()
