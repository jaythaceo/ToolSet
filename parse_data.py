from bs4 import BeautifulSoup

f = open('caseData.html', 'r')
soup = BeautifulSoup(f.read())

print soup