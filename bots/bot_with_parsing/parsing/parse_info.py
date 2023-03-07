from bs4 import BeautifulSoup as BS


def get_product_info(product: BS) -> dict:
    title = product.find('div', {'class':'listbox_title'}).text.strip()
    price = product.find('div', {'class':'listbox_price'}).text.strip().split('\n')[0]
    image = product.find('img').get('src')
    return {'title':title, 'price':price, 'image':image}

def get_all_products_from_page(soup:BS) -> list:
    res = []
    box = soup.find('div', {'class':'list-view'})
    products = box.find_all('div', {'class':'product_listbox'})
    for product in products:
        product_info = get_product_info(product)
        res.append(product_info)
    return res
