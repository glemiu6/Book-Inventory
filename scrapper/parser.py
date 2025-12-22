


def parse_book(book):
    title = book.h3.a['title']
    price =float(book.select_one('.price_color').text[1:])
    rating_star=book.p['class'][1]
    rating_map={
        "One":1,
        "Two":2,
        "Three":3,
        "Four":4,
        "Five":5
    }
    return {
        "title":title,
        "price":price,
        "rating":rating_map[rating_star],
        "category": None,
        "book_url": None
    }