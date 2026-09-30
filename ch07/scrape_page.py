import csv
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url, timeout=10)
response.encoding = "utf-8"
soup = BeautifulSoup(response.text, "html.parser")

books = []
for article in soup.find_all("article", class_="product_pod"):
    link = article.h3.a
    book = {
        "title": link.get("title"),
        "price": article.find("p", class_="price_color").text,
        "rating": article.find("p", class_="star-rating")["class"][1],
        "url": urljoin(url, link.get("href")),
    }
    books.append(book)

for book in books[:3]:
    print(f"{book['title']} | {book['price']} | {book['rating']}")
print(f"{len(books)} books found")

with open("books.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["title", "price", "rating", "url"])
    writer.writeheader()
    writer.writerows(books)
