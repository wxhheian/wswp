from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError


try:
    html = urlopen('https://pythonscrapingthisurldoesnotexist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print("This server could not be found at all!")
else:
    print("It works")

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(),'html.parser')
print(bs.nonExistentTag)
print(bs.nonExistentTag.someTag)          #None的Tag引发AttributeError
