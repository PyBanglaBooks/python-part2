import re
from pathlib import Path

BOOK = re.compile(
    r'<div class="book">\s*<a href="(.*?)">\s*<img src="(.*?)">'
    r'.*?<h2 class="title">(.*?)</h2>',
    re.S,
)
FOLDER = re.compile(r"book/(\d+)/(\w+)-(\w+)")


def folder_name(link):
    match = FOLDER.search(link)
    return "_".join(match.groups())


def main():
    html = Path("books.html").read_text(encoding="utf-8")
    main_folder = Path("books")
    main_folder.mkdir(exist_ok=True)

    for link, image, title in BOOK.findall(html):
        folder = main_folder / folder_name(link)
        folder.mkdir(exist_ok=True)
        info = f"{title}\n{link}\n{image}\n"
        (folder / "info.txt").write_text(info, encoding="utf-8")
        print(f"Saved {folder.name}")


if __name__ == "__main__":
    main()
