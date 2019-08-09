from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

bs = BeautifulSoup(html_doc,'html.parser')
#print(bs.prettify())

# print(bs.title)
# print(bs.title.name)
# print(bs.title.string)
# print(bs.title.parent.name)
# print(bs.p)
# print(bs.a)
# print(bs.find('a'))
# print(bs.find_all('a'))
print(bs.find_all(text='Tillie'))
#print(bs.find_all(id='link3'))
# print("***********")
# print(bs.find_all('p'))




# for link in bs.find_all('a'):
#     print(link.get('href'))
#
# #获取所有文字内容
# print(bs.get_text())
