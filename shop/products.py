from utils import get_products, update_products

def create():
    title = input("Введите название: ")
    price = float(input("Введите цену: "))
    # принимаем данные

    new_product = {"title":title, "price":price}
    # собираем в словарь

    products = get_products() 
    # получаем список старых продуктов
    products.append(new_product)
    # добавляем в список новые данные
    update_products(products)
    # перезаписываем файл с новыми данными

def read():
    products = get_products()
    # получаем список продуктов
    for product in products:
        # проходимся по каждому продукту и принтим
        print(f"""
==========================================
Название: {product['title']}
Цена: {product['price']}
==========================================
""")


