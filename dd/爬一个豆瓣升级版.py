# -*- coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import xlwt

class Info:
    def __init__(self,mn,on,url,dr,acs,oi):
        movive_name=mn
        other_name=on
        url=self.url
        director=dr
        actors=acs
        other_info=oi

def P_one_page(url):
    r = requests.get(url)
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
                    print('电影名称： ', name.string)
                    #tem_otherN=othername.string
                    #tem_otherN=tem_otherN.replace('/','')
                    #tem_otherN=tem_otherN.stript()
                    bm = othername.string
                    index = bm.index('/')
                    end = len(bm)
                    bm = bm[index + 1:end]
                    print('别名：', bm)
                    print('访问网址： ', b)



            bd = cube.find('div', attrs={'class': 'bd'})
            if bd != None:
                actors_info = bd.find('p', attrs={'class': ''})
                comments = bd.find('p', attrs={'class': 'quote'})
                # print(actors_info.get_text())
                pl = str(actors_info.get_text())
                # print(pl)
                index1 = pl.index('导演:')
                # end1 = pl.index('主')
                for i in range(0, len(pl)):
                    if pl[i].isdigit():
                        end2 = i
                        break
                try:
                    end1 = pl.index('主')
                except Exception as err:
                    end1 = end2

                pldy = pl[index1:end1 - 1]
                plzy = pl[end1:end2].strip()
                plqt = pl[end2:len(pl) - 1].strip()
                print(pldy)
                print(plzy)
                print('其他信息： ',plqt)
                print(' ')
                print('----------------------')
                print(' ')


if __name__ == '__main__':
    page=0
    while page<=225:
        zhihu_url='https://movie.douban.com/top250?start=%s&filter=' %page
        P_one_page(zhihu_url)
        page += 25
