import requests
from bs4 import BeautifulSoup
from parser import parse_book


def fetch_page(url:str):
    response=requests.get(url,timeout=10)
    if response.status_code!=200:
        return None
    return BeautifulSoup(response.text,"html.parser")

def scrape_all_books():
    page=1
    while True:
        url=f"https://books.toscrape.com/catalogue/page-{page}.html"
        soup=fetch_page(url)

        if soup is None:
            break
        books=soup.select("article.product_pod")
        if not books:
            break

        for book in books:
            book_data=parse_book(book)
            yield book_data
        page+=1


