# imported libraries
from bs4 import BeautifulSoup
import urllib
import re

TARGET = urllib.urlopen("http://www.courts.state.ny.us/reporter/slipidx/aidxtable_1.shtml").read()
soup = BeautifulSoup(TARGET)

"""
Remove html tags and useless
text from document.
"""
