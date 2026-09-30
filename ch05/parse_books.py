import re
from pathlib import Path

book_pattern = re.compile(
    r'<div class="book">\s*<a href="(.*?)">\s*<img src="(.*?)">'
    r'.*?<h2 class="title">(.*?)</h2>',
    re.S,
)

html = Path("books.html").read_text(encoding="utf-8")
for link, image, title in book_pattern.findall(html):
    print(f"Name: {title}")
    print(f"Link: {link}")
    print(f"Image: {image}")
    print()
