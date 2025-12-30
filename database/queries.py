from models import Book, Category, LogScrapper


# ------- For Books----------
def insert_book(db, title: str, price: float, rating: int, category_id: int) -> Book:
    book = Book(
        title=title,
        price=price,
        rating=rating,
        category_id=category_id,
    )
    db.add(book)
    db.flush()
    return book


def get_all_books(db) -> list[Book]:
    return db.query(Book).all()


def get_books_by_category_id(db, categoty_id: int) -> list[Book]:
    return db.query(Book).filter(Book.category_id == categoty_id).all()


def get_books_by_price(db,max_price:float) -> list[Book]:
    return db.query(Book).filter(
        Book.price<=max_price
    ).all()

def get_books_by_rating(db,rating:int)->list[Book]:
    return db.query(Book).filter(
        Book.rating==rating
    ).all()


# --------- For category---------


def get_category_by_name(db, category_name: str) -> Category | None:
    return db.query(Category).filter(Category.name == category_name).first()


def insert_category(db, name: str) -> Category:
    category = Category(name=name)
    db.add(category)
    db.flush()
    return category


def get_category_by_id(db, category_id: int) -> Category | None:
    return db.query(Category).filter(Category.id == category_id).first()


# --------- For verification---------


def mark_as_scraped(db, book_url: str, category_url: str) -> None:
    log = LogScrapper(book_url=book_url, category_url=category_url)
    db.add(log)


def is_book_scraped(db, book_url: str) -> bool:
    return (
        db.query(LogScrapper).filter(LogScrapper.book_url == book_url).first()
        is not None
    )


def book_exist(db, title: str, category_id: int) -> bool:
    return (
        db.query(Book)
        .filter(Book.title == title, Book.category_id == category_id)
        .first()
    )
