from bs4 import BeautifulSoup
import urllib2

TARGET = "http://www.courts.state.ny.us/reporter/3dseries/2015/2015_04674.htm"

def get_info(info):
  html = urllib2.urlopen(info).read()
  soup = BeautifulSoup(html)
  paras = soup.find_all("p")
  return paras