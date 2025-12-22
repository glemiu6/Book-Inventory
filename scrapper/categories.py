from scraping import fetch_page

def get_categories():
    homepage_url = "https://books.toscrape.com/"
    soup=fetch_page(homepage_url)
    side=soup.find('div',class_='side_categories')
    categories_ul=side.find('ul').find('ul')
    categories_items=categories_ul.find_all('li')
    categories={}
    for items in categories_items:

        a_tags=items.find('a')
        name=a_tags.text.strip()
        url=a_tags['href']
        categories[name]=url
    return categories
