import requests
from bs4 import BeautifulSoup

zhihu_url = 'http://movie.douban.com/top250/'
r= requests.get(zhihu_url)
print(r.status_code)
# soup=BeautifulSoup(r.text,'lxml')
# data0=soup.select('span.f-thide.cataName.f-ib')
# data1=soup.select('#j-package > div > div > div > a')
# for x in data0:
#     print(x.get_text())
# for y in data1:
#     print(y.get_text())


soup=BeautifulSoup(r.text,'lxml')
# print(soup.attrs)
# print(soup.find_all('a'))
# print(soup.find('span', attrs={'class': 'title'}).getText())
#print(soup.prettify())
print(soup.title.string)
#print(soup.p)

#输出名字

for key in soup.find_all('a'):
    name = key.find('span', attrs={'class': 'title'})
    othername= key.find('span', attrs={'class': 'other'})
    b=key.get('href')

    if name != None:
        print(name.getText(), othername.getText(), b)
