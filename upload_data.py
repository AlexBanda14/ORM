import json
from models import Publisher, Book, Shop, Stock, Sale
from connection import session

def upload_data():
    with open('/fixtures/test_data.json', 'r') as fd:
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
        session.close()

if __name__ == '__main__':
    upload_data()
