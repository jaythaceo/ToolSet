# imported libraries
from bs4 import BeautifulSoup
import urllib

TARGET = urllib.urlopen("http://www.courts.state.ny.us/reporter/slipidx/aidxtable_1.shtml").read()
soup = BeautifulSoup(TARGET)
tags = soup('a')

for tag in tags:
  print tag.get('href', None)
