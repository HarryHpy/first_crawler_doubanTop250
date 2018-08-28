import requests
from bs4 import BeautifulSoup
zhihu_url = 'http://movie.douban.com/top250/'
r = requests.get(zhihu_url)
soup = BeautifulSoup(r.text, 'lxml')
blog=soup.find_all('li')
for cube in blog:

    hd = cube.find('div', attrs={'class': 'hd'})
    if hd != None:
        # print(hd)
        for a_tag in hd.find_all('a'):
            name = a_tag.find('span', attrs={'class': 'title'})
            othername =a_tag.find('span', attrs={'class': 'other'})
            b = a_tag.get('href')

            if name != None:
                print(name.getText(), othername.getText(), b)



    bd = cube.find('div', attrs={'class': 'bd'})
    if bd != None:
        actors_info = bd.find('p', attrs={'class': ''})
        comments= bd.find('p', attrs={'class': 'quote'})
        print(actors_info.get_text())
        print(comments.get_text())