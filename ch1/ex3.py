from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None

    try:
        bs = BeautifulSoup(html.read(),'html.parser')
        title = bs.body.h1           #尝试title = bs.nonExistentTag.h1
    except AttributeError as e:
        print('hh')
        return None

    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("This title could not be found")
else:
    print(title)


#if server did not exist,html would be a None object,and html.read() would throw an AttributeError
