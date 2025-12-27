from models import Book,Category,LogScrapper

def insert_book(db,title:str,price:float,rating:int,category_id:int):
    book = Book(
        title=title,
        price=price,
        rating=rating,
        category_id=category_id,
    )
    db.add(book)
    db.flush()
    return book


def get_all_books(db):
    return db.query(Book).all()

def get_books_by_category_id(db,categoty_id:int):
    return (
        db.query(Book)
        .filter(Book.category_id == categoty_id)
        .all()
    )

def mark_as_scraped(db,book_url:str,category_url:str):
    log=LogScrapper(
        book_url=book_url,category_url=category_url)
    db.add(log)




def is_book_screaped(db,book_url:str):
    return (db.query(LogScrapper)
            .filter(LogScrapper.book_url == book_url)
            .first() is not None
            )

def get_category_by_name (db,category_name:str):
    return db.query(Category).filter(Category.name == category_name).first()



def insert_category(db,name:str):
    category = Category(name=name)
    db.add(category)
    db.flush()
    return category