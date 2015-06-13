# imported libraries
from bs4 import BeautifulSoup
import urllib

TARGET = urllib.urlopen("http://www.courts.state.ny.us/reporter/3dseries/2015/2015_04674.htm")

def fetch_data():
  data = TARGET.read()
  files = open("caseData.html", "wb")
  files.write(data)
  files.close()

fetch_data()
