from database.queries import is_book_scraped,get_category_by_name,insert_category,book_exist,insert_book,mark_as_scraped
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def mark_book_processed(db,book_url:str,category_url:str):
    if not book_url.startswith("http"):
        logging.error("Invalid book url")
        return
    if is_book_scraped(db,book_url):
        logging.info("Book already scraped")
        return

    mark_as_scraped(db,book_url,category_url)
    logging.info(f"Book successfully marked as processed: {book_url} (Category: {category_url})")


def save_new_book(db,book_data:dict):
    category = get_category_by_name(db,book_data["category"])
    if category is None:
        logging.info("Category not found")
        insert_category(db,book_data["category"])
    title=book_data.get("title","Missing Title")
    price=float(book_data.get("price",0.1))
    rating=int(book_data.get("rating",1))

    insert_book(db,title,price,rating,category.id)
    logging.info("Book successfully saved")