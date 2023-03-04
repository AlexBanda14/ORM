from models import Publisher, Book, Shop, Stock, create_tables
from connection import session, engine
from upload_data import upload_data


def get_shops(publisher):

    if publisher.isdigit():
        query_publisher_name = publisher
        query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
        query_result = (query_join.filter(Publisher.id == int(query_publisher_name))).all()
    else:
        query_publisher_name = publisher
        query_join = session.query(Shop).join(Stock).join(Book).join(Publisher)
        query_result = (query_join.filter(Publisher.name == query_publisher_name)).all()

    list_shop = []
    for result in query_result:
        list_shop.append(result.name)
    return list_shop

if __name__ == '__main__':
    publisher = input('Введите имя или идентификатором издателя: ')
    create_tables(engine)
    upload_data()
    print(f'Издатель найден в следующих магазинах: {" , ".join(get_shops(publisher))}')
    session.close()
