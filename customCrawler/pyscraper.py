from bs4 import BeautifulSoup
from urlparse import urljoin,urlparse
import re


def get_link(html, url):
  """This function will return all the urls """
  urls = []
  for link in BeautifulSoup(html, parseOnlyThese = SoupStrainer('a')):
    if link.has_key('href'):
      if link['href']=='':
        continue
      link['href'] = link['href'].strip(' ')
      urls.append(urljoin(url, link['href']))
  return urls
