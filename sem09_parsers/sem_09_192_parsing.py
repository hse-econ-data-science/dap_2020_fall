import requests # скачивать страничку
from bs4 import BeautifulSoup # превращать в дерево
import pandas as pd


url = 'http://books.toscrape.com/catalogue/page-2.html'

response = requests.get(url)

response.status_code
response.content

tree = BeautifulSoup(response.content)

tree
tree.body
tree.body.h3
tree.body.h3.a

tree.body.h3.a.text
tree.body.h3.a.get('href')


all_a = tree.find_all('a')
all_a

links = [a.get('href') for a in all_a]
links

def get_books_info(html_text):
    """
    Функция парсит список книг с books.toscrape 
    из заранее скачанной html
    """
    tree = BeautifulSoup(html_text)


    all_ratings = tree.find_all('p', {'class': 'star-rating'})
    ratings_list = [rating.get('class') for rating in all_ratings]

    books = pd.DataFrame(ratings_list, columns=['junk', 'rating'])

    all_prods = tree.find_all('article')
    books['title'] = [prod.h3.a.text for prod in all_prods]

    books['link'] = [prod.h3.a.get('href') for prod in all_prods]

    price_colors = tree.find_all('p', {'class': 'price_color'})
    books['price'] = [float(pc.text[1:]) for pc in price_colors]

    books['currency'] = [pc.text[:1] for pc in price_colors]

    books.drop(columns='junk', inplace=True)

    return books


url = "http://books.toscrape.com/catalogue/page-4.html"

response = requests.get(url)
response.encoding
response.elapsed
response.status_code

html_text = requests.get(url).content
get_books_info(html_text)

# покликать или что-то ввести в поле
from selenium import webdriver

lisichka = webdriver.Firefox()
url = 'https://www.google.com/'
lisichka.get(url)

sf = lisichka.find_element_by_name('q')
sf.click()
sf.send_keys('ВШЭ')

knopka = lisichka.find_element_by_name('btnK')
knopka.click()

content = lisichka.page_source

content
lisichka.close()
