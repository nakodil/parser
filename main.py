from bs4 import BeautifulSoup
import requests

url = "http://127.0.0.1:8000"
response = requests.get(url)
print("Ответ сервера:", response.status_code)

response.encoding = 'utf-8'
page_content = response.text
soup = BeautifulSoup(page_content, 'html.parser')

# find находит первое упоминание
# find_all находит все упоминания (список BS тегов)
# id="myid"
# class_="myclass"
products = soup.find_all("article")

# у каждого BS тега есть контент, забираем из него название и цену
for product in products:
	print(product.contents[3].text, product.contents[5].text)
