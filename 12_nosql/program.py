import pymongo
from bson import ObjectId
from pymongo import MongoClient


def add_data(coll):
    if coll.find().count() > 0:
        print('Data already inserted')
        return

    book = {
        'title': 'First MongoDB book',
        'published': '2016-01-10',
        'sold_count': 1,
    }
    coll.save(book)

    book = {
        'title': 'Second MongoDB book',
        'published': '2017-01-10',
        'sold_count': 10
    }
    coll.save(book)

    book = {
        'title': 'Third MongoDB book',
        'published': '2015-01-10',
        'sold_count': 50
    }
    coll.save(book)

    person = {
        'name': 'john',
        'lastname': 'doe'
    }
    coll.save(person)


def buy_book(books, title):
    the_book = books.find_one(
        {'title': title}
    )
    print(the_book)
    print(the_book.get('subtitle'))

    the_book['sold_count'] += 1

    books.save(the_book)

    print('The book {} sold {} copies'.format(
        title, the_book['sold_count']
    ))

def buy_book_with_update(books, title):
    # atomic, and performance is better
    books.update_many({'title': title}, {'$inc': {'sold_count': 1}})

    the_book = books.find_one(
        {'title': title}
    )
    print(the_book)
    print('done')


def main():
    connection = MongoClient()

    # MongoDemo will be our db
    db = connection.MongoDemo

    # Books is a collection of documents (think table)
    books = db.Books

    add_data(books)
    #buy_book(books, 'First MongoDB book')
    buy_book_with_update(books, 'First MongoDB book')

    print('done')


if __name__ == '__main__':
    main()