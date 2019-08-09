from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError



# html = urlopen('http://pythonscraping.com/pages/page1.html')
# #print(html.read())
#
# # bs = BeautifulSoup(html.read(),'html.parser')     #BeautifulSoup(html,'html.parser')
# # print(bs.h1)
#
# # bs = BeautifulSoup(html,'html.parser')
# # print(bs)
#
# bs = BeautifulSoup(html.read(),'lxml')     #another parser:html5lib
# print(bs)
