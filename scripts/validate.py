from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
MEASUREMENT_ID = "G-27Z932WEQQ"


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.h1_count = 0
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "title":
            self._in_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "link" and attributes.get("rel") == "canonical":
            self.canonical = attributes.get("href")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title += data


index = (ROOT / "index.html").read_text(encoding="utf-8")
parser = PageParser()
parser.feed(index)

assert parser.title.strip(), "index.html must have a title"
assert parser.h1_count == 1, "index.html must have exactly one h1"
assert parser.canonical == "https://routerfine.com/", "canonical URL mismatch"
assert index.count(MEASUREMENT_ID) >= 2, "GA4 tag is missing"
assert (ROOT / "404.html").is_file(), "404.html is missing"
assert "https://routerfine.com/sitemap.xml" in (ROOT / "robots.txt").read_text(encoding="utf-8")

sitemap = ElementTree.parse(ROOT / "sitemap.xml")
locations = [node.text for node in sitemap.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url/{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
assert locations == ["https://routerfine.com/"], "sitemap URL mismatch"

print("routerfine.com static validation passed")
