from bs4 import BeautifulSoup
import requests

url = "https://www.muztorg.ru/category/ukulele?in-stock=1&pre-order=1&is_all=1&sort=price"
response = requests.get(url)
print("Ответ сервера:", response.status_code)

response.encoding = 'utf-8'
page_content = response.text
soup = BeautifulSoup(page_content, 'html.parser')

# find находит первое упоминание
# find_all находит все упоминания (список BS тегов)
# id="myid"
# class_="myclass"
products = soup.find_all("section", class_="product-thumbnail")

# у каждого BS тега есть контент, забираем из него название и цену
product_content = products[0].contents

for i in product_content:
	print(i)
