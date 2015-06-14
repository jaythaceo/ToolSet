from browser import br
from bs4 import BeautifulSoup, SoupStrainer
from urlparse import urljoin
import pyscraper
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--url", "-u", type = str, help = "Url to scrape")
parser.add_argument("--depth", "-d", type = int, help = "scraping depth")
parser.add_argument("--scrapingtype", "-s", type = str, help = "use ")
parser.add_argument("--email", "-m", action = "store_true", help = "scrape page for emails")

args = parser.parse_args()

url = []
url.append(args.url)
depth = args.depth
#filetype=args.filetype

urls_visted = ['']
emails = []
scrapingtype = args.scrapingtype
