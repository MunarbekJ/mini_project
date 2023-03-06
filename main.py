import json
import requests
from 
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www..kivano.kg'

import json
def bulk_create(products):
    with open('db.json') as f:
        old = json.load(f)
        old.append(products)
    with open('new_db.json', 'a+') as f:
        res = json.load(f)
        new = []
        for i in old:
            for el in res:
                if i['id'] != el['id']:
                    new.append(i)
        f.write(json.dumps(new))

bulk_create([{'id': 100, 'title': 'product1', 'price': 1500, 'rating': 4.6}, {'id': 101, 'title': 'product2', 'price': 2004, 'rating': 1.2}, {'id': 102, 'title': 'product3', 'price': 2095, 'rating': 2.1}, {'id': 103, 'title': 'product4', 'price': 3200, 'rating': 5.0}])

import requests
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www.kivano.kg'

def get_soup(url:str) -> BS:
    response = requests.get(url)
    soup = BS(response.text, 'lxml')
    return soup

def get_products_info(products: BS) -> dict:
    title = products.find('div', {'class':'listbox_title'}).text.strip()
    title = products.find('div', {'class':'listbox_title'}).text.strip().split('\n')(0)
    image = products.find('div', {'class': 'listbox_img'}). find('img').get('srs')
    return {'title':title, 'price':price, 'image': BASE_URL+image}


    print(repr(price))

    
def get_all_product_list(url:str):
    res = []
    soup = get_soup(url)
    box = soup.find('div', {'class':'list-view'})
    products = box.find_all('div')
    for
    products = box.find_all('div', {'class':'list-view'})
    print(len(products))

def write_to_json(page:int, data:list):
    with open('db.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascil=False)   

def get_last_page(url:str) -> int:
    soup = get_soup(url)
    last = soup.find('li', {'class':'last'})
    return int(last.text)

def main():
    category = '/noutbuki'
    data = {}
    last_page = get_last_page(BASE_URL + category)

    for page in range(1, last_page+1):
        url = BASE_URL + category + '?page=' + str(page)
        print(url)
        one_page_data = get_all_products_from_page(url)
        data[page] = one_page_data
write_to_json()
        get_all__ (BASE_URL + category)

main()