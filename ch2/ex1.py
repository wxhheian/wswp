from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bs = BeautifulSoup(html,"html.parser")
#print(bs.prettify())

# nameList = bs.find_all('span',{'class':'green'})
# for name in nameList:
#     print(name.get_text())

nameList = bs.find_all(text="the prince")
print(len(nameList))
title = bs.find_all(id='title',class_='text')   #[]
print(title)
alltext = bs.find_all(id='text')
print(alltext[0].get_text())

#bs.find_all(class='green')  #报错  因为python中class属于reserved word  可以修改为bs.find_all(class_='green')  或者  bs.find_all('',{'class':'green'})











##bsobj.find_all(tag,attribute,recursive,text,limit,keywords)
##bsobj.find(tag,attribute,recursive,text,keywords)
