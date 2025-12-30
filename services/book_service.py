from database.models import Book
from database.queries import book_exist, get_all_books, get_category_by_id, insert_book,get_books_by_price,get_books_by_rating
from exceptions.book_execeptions import DuplicateBook, InvalidBookData


def add_book(db, title: str, price: float, category_id: int, rating=None) -> Book:
    title = title.strip().title()
    if rating is None:
        rating = 1

    if price <= 0:
        raise InvalidBookData("Price cannot be negative")
    if rating not in range(1, 6):
        raise InvalidBookData("Rating must be between 1 and 5")
    if not title.strip():
        raise InvalidBookData("Title cannot be empty")

    category = get_category_by_id(db, category_id)
    if not category:
        raise InvalidBookData("Category must Exist")

    if book_exist(db, title, category_id):
        raise DuplicateBook(f"{title} already in exists in the category {category}")

    return insert_book(db, title, price, rating, category_id)


def list_books(db) -> list[Book]:
    return get_all_books(db)


def filter_by_price(db, price: float):
    if price <= 0:
        raise InvalidBookData("Price must be positive")
    return get_books_by_price(db, price)



def filter_by_rating(db, rating: int):
    if rating not in range(1, 6):
        raise InvalidBookData("Rating must be between 1 and 5")
    return get_books_by_rating(db, rating)
