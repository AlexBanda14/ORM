import json
from pprint import pprint

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from main import create_tables, Publisher, Book, Shop, Stock, Sale
from db_login import *


DSN = f'postgresql://{login}:{password}@{localhost}/{name_db}'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)


Session = sessionmaker(bind=engine)
session = Session()

with open('C:/Users/What/PycharmProjects/pythonProject3/fixtures/test_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()


def searching_publisher_name():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    pprint(query_join)
    query_publisher_name = input('Введите имя (name) издателя: ')
    query_result = query_join.filter(Publisher.name == query_publisher_name)
    for result in query_result.all():
        print(f'Издатель "{query_publisher_name}" найден в магазине "{result.name}" с идентификатором {result.id}')

def searching_publisher_id():
    query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
    query_publisher_name = input('Введите идентификатор (id) издателя: ')
    query_result = query_join.filter(Publisher.id == query_publisher_name)
    for result in query_result.all():
        print(
            f'Издатель c id: {query_publisher_name} найден в магазине "{result.name}" '
            f'с идентификатором {result.id}')

if __name__ == '__main__':
    searching_publisher_name()
    searching_publisher_id()

session.close()