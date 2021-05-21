from bs4 import BeautifulSoup
import requests
import os.path

file_name = "site_content.html"
url = "https://www.muztorg.ru/category/ukulele?in-stock=1&pre-order=1&is_all=1&sort=price"


def make_file_form_url(url: str):
    """
    Сохраняет контент сайта в файл с кодировкой UTF-8.
    TODO: что будет, если сайт недоступен
    """
    response = requests.get(url)
    print("Ответ сервера:", response.status_code)
    response.encoding = 'utf-8'
    with open("site_content.html", "w", encoding="utf-8") as file:
        file.write(response.text)


def make_products_soup_from_file(file_name: str):
    """
    Читает файл с контентом сайта.
    Возвращает объект класса bs4.element.ResultSet
    """
    page_content = open(file_name, "r", encoding="utf-8")
    soup = BeautifulSoup(page_content, 'html.parser')
    products = soup.find_all("section", class_="product-thumbnail")
    return products


def make_product_dictionary(product) -> dict:
    """
    Ищет в продукте название, изображение и цену.
    Возвращает словарь с ключами: name, image, price.
    """
    product_title = product.find("div", class_="title")
    product_title_name = product_title.find("a").text
    product_image = product.find("img", class_="img-responsive")
    product_image_src = product_image.attrs["data-src"]
    product_price = product.attrs["data-price"]
    product_dictionary = {
        "name" : product_title_name,
        "image" : product_image_src,
        "price" : product_price
        }
    return product_dictionary


def make_products_list(products: dict) -> list:
    """
    Возвращает список словарей из свойств продуктов:
    (названия, изображения и цены)
    """
    products_list = []
    for product in products:
        new_item = make_product_dictionary(product)
        products_list.append(new_item)
    return products_list
        

def print_products_list(products_list: list):
    """
    Печатает список продуктов
    """
    for item in products_list:
        for value in item.values():
            print(value)
        print("")


# Чтобы не парсить каждый раз, проверим, есть ли файл с контентом сайта
if not os.path.isfile(file_name):
    make_file_form_url(url)

products = make_products_soup_from_file(file_name)
products_list = make_products_list(products)  
print_products_list(products_list)
