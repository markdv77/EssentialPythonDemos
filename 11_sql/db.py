import datetime
import os
import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy import Column, Integer, Date, String

# one base per DB instance
EntityBase = sqlalchemy.ext.declarative.declarative_base()


class Book(EntityBase):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True)
    sold_copies = Column(Integer, default=0)
    title = Column(String, nullable=False)
    published = Column(Date, default=datetime.datetime.now)


class DBORM:
    def __init__(self):
        conn_str = self.get_conn_string()
        self.engine = sqlalchemy.create_engine(conn_str, echo=True)

        # create the DB
        EntityBase.metadata.create_all(self.engine)

        self.session_factory = sqlalchemy.orm.sessionmaker(self.engine)

    def add_some_data(self):

        session = self.session_factory()

        count = session.query(Book).filter().count()
        print('There are {} books in the DB'.format(count))

        if count > 0:
            return

        book = Book()
        book.title = 'First time ORM games'
        book.sold_copies = 27
        book.published = datetime.date(2016,1,1)
        session.add(book)

        book = Book()
        book.title = 'Second time ORM games'
        book.sold_copies = 100
        book.published = datetime.date(2017,1,1)
        session.add(book)

        book = Book()
        book.title = 'SQL for fun and profit'
        book.sold_copies = 10
        book.published = datetime.date(2015,1,1)
        session.add(book)

        #print('NEW:', session.new)
        #print('DIRTY:', session.dirty)

        print('Before save: Id = {}'.format(book.id))
        session.commit()
        print('Before save: Id = {}'.format(book.id))

    def show_data(self):
        session = self.session_factory()

        #books = session.query(Book)
        #books = books.filter(Book.sold_copies > 0)
        #book = books.order_by(Book.sold_copies.desc())[0]

        books = session.query(Book)\
            .filter(Book.sold_copies>0)\
            .order_by(Book.sold_copies.desc())

        print('Second page books: {}'.format(len(books[5:10])))



        #print('Most popular book is:')
        #print(book.__dict__)

        #book.sold_copies += 1
        #session.delete(book)
        #session.commit()

    def get_conn_string(self):
        file = os.path.join(
            os.path.abspath('.'),
            'data',
            'sql_alc_orm.sqlite_db'
        )
        conn_str = 'sqlite:///' + file
        return conn_str
