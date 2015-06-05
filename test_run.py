from bs4 import BeautifulSoup
import urllib2

target = urllib2.urlopen("http://www.courts.state.ny.us/reporter/3dseries/2015/2015_04674.htm").read()
soup = BeautifulSoup(target)
#print type(soup)

print soup.prettify()