import requests
from bs4  import BeautifulStoneSoup as BS

"Пагинация в mashina.kg"

import = 
BASE_URL = 'https://www.mashina.kg/search/all/'

html = requests.get(BASE_URL).text
soup = BS(html, 'lxml')
pagination = soup.find('ul', {'class':'pagination'})
last_li = pagination.find_all('li')[-1]
last_page = last_li.find('a').get('data-page')
print(last_page)

"CSV"
import csv

data = [
    {'title':"hello", "price":342},
    {'title':"test", "price":7643},
    {'title':"aaa", "price":324},
    {'title':"bbb", "price":453},
]
with open("test.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(data[0].keys())
    for product in data:
        writer.writerow(product.values())