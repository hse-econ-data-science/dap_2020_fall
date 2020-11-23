import requests # скачиваем странички
from bs4 import BeautifulSoup # парсим страничку
from selenium import webdriver # управляем браузером
import pandas as pd

url = 'http://books.toscrape.com/catalogue/page-2.html'

response = requests.get(url)
response.status_code
response.elapsed
html_text = response.content

tree = BeautifulSoup(html_text)
tree.body
tree.body.h3
tree.body.h3.a

element = tree.body.h3.a

element.text
element.get('href')

all_price_elements = tree.find_all('p', {'class': 'price_color'})
all_price_elements

all_price_elements[0].text

prices = [float(pc.text[1:]) for pc in all_price_elements]
prices

currency = [pc.text[:1] for pc in all_price_elements]
currency

articles = tree.find_all('article')
articles[0].h3.a.text

titles = [article.h3.a.text for article in articles]
titles


prefix = 'http://books.toscrape.com/catalogue/'
prefix + articles[0].h3.a.get('href')

links = [prefix + article.h3.a.get('href') for article in articles]


all_rate_elements = tree.find_all('p', {'class': 'star-rating'})
all_rate_elements
all_rate_elements[0].get('class')[1]

ratings = [rate_element.get('class')[1] for rate_element in all_rate_elements]
ratings

books = pd.DataFrame({'price': prices, 
    'currency': currency,
    'title': titles,
    'link': links,
    'rating': ratings})
books


[i ** 2 for i in [2, 6, 9]]

# делаем функцию!

def get_books_info(html_text):
    """
    Функция парсит html странички с http://books.toscrape.com/catalogue/page-2.html
    """
    tree = BeautifulSoup(html_text)

    all_price_elements = tree.find_all('p', {'class': 'price_color'})
    prices = [float(pc.text[1:]) for pc in all_price_elements]
    currency = [pc.text[:1] for pc in all_price_elements]
    articles = tree.find_all('article')
    titles = [article.h3.a.text for article in articles]

    prefix = 'http://books.toscrape.com/catalogue/'
    links = [prefix + article.h3.a.get('href') for article in articles]

    all_rate_elements = tree.find_all('p', {'class': 'star-rating'})
    ratings = [rate_element.get('class')[1] for rate_element in all_rate_elements]

    books = pd.DataFrame({'price': prices, 
        'currency': currency,
        'title': titles,
        'link': links,
        'rating': ratings})
    return books


url = "http://books.toscrape.com/catalogue/page-36.html"
response = requests.get(url)

get_books_info(response.content)

# window: geckodriver + (Chrome())
# mac: Safari: разрешить внешнее автоматическое управление

lisichka = webdriver.Firefox()
url = 'https://www.google.com/'
lisichka.get(url)

sf = lisichka.find_element_by_name('q')
sf.click()
sf.send_keys('ВШЭ')

knopka = lisichka.find_element_by_name('btnK')
knopka.click()

html_text = lisichka.page_source
html_text

lisichka.close()