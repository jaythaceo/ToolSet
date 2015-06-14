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

levels = [urls, [], [], [], []]

def writetofile():
  f = open('depth1.txt', 'w')
  for i in levels[1]:
    f.write(i)
    f.write('\n')
  f.close()

  f = open('depth1.txt', 'w')
  for i in levels[2]:
    f.write(i)
    f.write('\n')
  f.close()

  f = open('depth1.txt', 'w')
  for i in levels[3]:
    f.write(i)
    f.write('\n')
  f.close()

  f = open('depth1.txt', 'w')
  for i in levels[4]:
    f.write(i)
    f.write('\n')
  f.close()

  emails = list(set(emails))

  f = open('emails.txt', 'w')
  for email in emails:
    f.write(email)
    f.write('\n')
  f.close()

if scrapingtype == 'diff':
  for i in range(depth:
    print 'reached depth ', i
    for link in levels[i]:
      if link in urls_visted:
        continue
      tempurls = []
      try:
        r = br.open(link)

        html = r.read()
        tempurls = pyscraper.get_links(html, link)
        if args.email:
          tempemails = []
          tempemails = pyscraper.get_emails(html, link)
          emails = emails + tempemails

        levels[i + 1] = levels[i +1] + tempurls
        urls_visted.append(link)

      except:
        print link
        pass

    levels[i + 1] = list(set(levels[i + 1]))


writetofiles()