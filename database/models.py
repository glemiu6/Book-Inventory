from sqlalchemy import Column,Integer,String,Float,ForeignKey
from sqlalchemy.orm import relationship
from db import Base


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String,unique=True)

    books=relationship("Book",back_populates="category")

    def __repr__(self):
        return f"<Category(id={self.id}, name={self.name})>"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)


    user_books=relationship("UserBook",back_populates="user")


    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    price=Column(Float, nullable=False)
    rating = Column(Integer)


    category_id=Column(Integer, ForeignKey('categories.id'))


    category = relationship("Category", back_populates="books")
    user_books=relationship("UserBook",back_populates="book")

    def __repr__(self):
        return f"<Book(id={self.id}, title={self.title}, price={self.price})>"

class UserBook(Base):
    __tablename__ = 'user_books'
    user_id = Column(Integer, ForeignKey('users.id'),primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'),primary_key=True)


    book = relationship("Book", back_populates="user_books")
    user = relationship("User", back_populates="user_books")



class LogScrapper(Base):
    __tablename__ = 'log_scrappers'
    id = Column(Integer, primary_key=True)
    book_url = Column(String, nullable=False)
    category_url=Column(String, nullable=False)

