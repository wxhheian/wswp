from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs = BeautifulSoup(html,"html.parser")
#print(bs.prettify())

# for child in bs.find('table',{'id':'giftList'}).children:          # .descendants  是打印出子标签后，再将子标签的后 代标签一层层循环打印出来
#     print(child)                                                   # .children 打印出子标签

# for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:             #next_siblings 兄弟标签，自己与自己不能成为兄弟
#     print(sibling)                                                           #使用bs.table.tr.next_siblings 也可以，但不太稳健

# .previous_siblings #定位上面的兄弟标签
# .next_sibling   #定位一个
# .previous_sibling

# text = bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text()            #父标签 parent  parents
# print(text)

# images = bs.find_all("img",{"src":re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
#
# print(images)
# for image in images:
#     print(image['src'])             #注意返回的是dictionary object

# tag = bs.find_all(lambda tag:len(tag.attrs) == 2)
# print(tag[:2])

print(bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?'))

print(bs.find_all('',text='Or maybe he\'s only resting?'))              #注意与31行代码输出的区别
