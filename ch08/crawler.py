"""Collect details of books from books.toscrape.com"""
import csv
import logging
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE = "https://books.toscrape.com/"
TRAVEL = BASE + "catalogue/category/books/travel_2/index.html"
ALL_BOOKS = BASE + "catalogue/page-1.html"
RATINGS = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
FIELDS = ["title", "category", "price", "rating", "stock",
          "upc", "image", "url", "description"]


def parse_book(html, url):
    """Return the details of a book from its page"""
    soup = BeautifulSoup(html, "html.parser")
    main = soup.find("div", class_="product_main")
    table = {}
    for row in soup.find("table").find_all("tr"):
        table[row.th.text] = row.td.text
    stock = re.search(r"\d+", table["Availability"])
    price = main.find("p", class_="price_color").text
    rating = main.find("p", class_="star-rating")["class"][1]
    crumbs = soup.find("ul", class_="breadcrumb").find_all("a")
    image = soup.find("div", class_="item active").img
    heading = soup.find("div", id="product_description")
    description = ""
    if heading:
        description = heading.find_next_sibling("p").text

    return {
        "title": main.h1.text,
        "category": crumbs[2].text,
        "price": price.lstrip("£"),
        "rating": RATINGS[rating],
        "stock": int(stock.group()) if stock else 0,
        "upc": table["UPC"],
        "image": urljoin(url, image["src"]),
        "url": url,
        "description": description,
    }


class BookCrawler:
    def __init__(self, cache_dir="pages", offline=False, delay=1):
        self.cache = Path(cache_dir)
        self.cache.mkdir(exist_ok=True)
        self.offline = offline
        self.delay = delay
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "BookCrawler (learning)"

    def cache_file(self, url):
        name = url.replace(BASE, "").replace("/", "_")
        return self.cache / name

    def get_page(self, url):
        """Return the HTML of a page, from the cache or the web"""
        file = self.cache_file(url)
        if file.exists():
            logging.debug(f"From cache: {url}")
            return file.read_text(encoding="utf-8")
        if self.offline:
            logging.warning(f"Not in cache: {url}")
            return None

        logging.info(f"Downloading {url}")
        time.sleep(self.delay)
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            logging.error(f"{url}: {error}")
            return None
        response.encoding = "utf-8"
        file.write_text(response.text, encoding="utf-8")
        return response.text

    def book_links(self, url):
        """Links of the books in a list and its next pages"""
        links = []
        while url:
            html = self.get_page(url)
            if html is None:
                break
            soup = BeautifulSoup(html, "html.parser")
            for h3 in soup.find_all("h3"):
                links.append(urljoin(url, h3.a["href"]))
            next_page = soup.find("li", class_="next")
            if next_page:
                url = urljoin(url, next_page.a["href"])
            else:
                url = None
        return links

    def crawl(self, start_url):
        """Collect the details of all the books in a list"""
        links = self.book_links(start_url)
        print(f"{len(links)} book links found")
        books = []
        for link in links:
            html = self.get_page(link)
            if html is None:
                continue
            try:
                books.append(parse_book(html, link))
            except (AttributeError, KeyError, IndexError) as error:
                logging.error(f"Could not read {link}: {error!r}")
        return books


def save_csv(books, file_name):
    with open(file_name, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(books)


def main():
    logging.basicConfig(
        filename="crawler.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )
    start_url = ALL_BOOKS if "all" in sys.argv else TRAVEL
    crawler = BookCrawler(offline="--offline" in sys.argv)
    logging.info(f"Crawling started from {start_url}")
    books = crawler.crawl(start_url)
    save_csv(books, "books.csv")
    logging.info(f"Crawling finished, {len(books)} books")
    print(f"Saved {len(books)} books to books.csv")


if __name__ == "__main__":
    main()
