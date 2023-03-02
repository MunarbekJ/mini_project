import requests
from bs4 import BeautifulSoup

main_url = 'https://www.kivano.kg/'

response = requests.get(main_url) # отправляем запрос
# print(response.text) # html - str

soup = BeautifulSoup(response.text, 'lxml')

phones_span = soup.find('span', {"id":"phones"})
raw_phones = phones_span.text
phones_list = []

for ph in raw_phones.split("\n"):
    clear_phone = ph.replace('\r', '').strip()
    if clear_phone:
        phones_list.append(clear_phone)

print(phones_list)

'===================='
'- детализация продукта ========'
product_url = 'product/view/sotovyy-telefon-apple-iphone-14-pro-256gb-fioletovyy'
response = requests.get(main_url+product_url)
print(response)
soup = BeautifulSoup(response.text, 'lxml')
product_card = soup.find('div', {"class":"product-view"})
print(product_card)
title = product_card.find('h1').text


print(product_card.find_all('img'))
image_box = product_card.find('div', {'class':'img_full'})
image = image_box.find('img').get('src')
print(image)


price = product_card.find_all('span', {'itemprop':'price'}).text

data = {'title':title, 'image':image, 'price':price}
price(data)