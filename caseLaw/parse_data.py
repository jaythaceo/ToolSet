from bs4 import BeautifulSoup


data = open('caseData.html', 'r')
soup = BeautifulSoup(data.read())
element = soup.find_all('td', {"align": 'center'})
category = soup.find_all('p')

def stripTags(data):
  category = data
  if category is None:
    return None
  return category

print stripTags(category)