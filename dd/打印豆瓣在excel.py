# -*- coding: utf-8-*-
import requests
from bs4 import BeautifulSoup
import xlwt

class Info:
    def __init__(self,mn,on,url,dr,acs,oi):
        self.movive_name=mn
        self.other_name=on
        self.url=url
        self.director=dr
        self.actors=acs
        self.other_info=oi

def P_one_page(url):
    mn=''
    on=''
    geturl=''
    dr=''
    acs=''
    oi=''
    page_list=list()
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
                    # print('电影名称： ', name.string)
                    #tem_otherN=othername.string
                    #tem_otherN=tem_otherN.replace('/','')
                    #tem_otherN=tem_otherN.stript()
                    bm = othername.string
                    index = bm.index('/')
                    end = len(bm)
                    bm = bm[index+2:end]
                    # print('别名：', bm)
                    # print('访问网址： ', b)
                    geturl=b
                    mn=name.string
                    on=bm



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
                # print(pldy)
                # print(plzy)
                # print('其他信息： ',plqt)
                # print(' ')
                # print('----------------------')
                # print(' ')
                dr = pldy
                acs = plzy
                oi = plqt
            tem_info=Info(mn,on,geturl,dr,acs,oi)
            page_list.append(tem_info)
    return page_list




if __name__ == '__main__':
    page=0
    wb = xlwt.Workbook()
    ws = wb.add_sheet('A Test Sheet')
    line=1
    ws.write(0, 0, label='电影名字')
    ws.write(0, 1, label='电影别名')
    ws.write(0, 2, label='获取网址')
    ws.write(0, 3, label='电影导演')
    ws.write(0, 4, label='电影演员')
    ws.write(0, 5, label='其他信息')
    while page<=225:
        zhihu_url='https://movie.douban.com/top250?start=%s&filter=' %page
        pg=P_one_page(zhihu_url)
        for key in pg:
            print(key.movive_name)
            print(key.other_name)
            print(key.url)
            print(key.director)
            print(key.actors)
            print(key.other_info)
            print('----------------------')
            ws.write(line, 0, key.movive_name)
            ws.write(line, 1, key.other_name)
            ws.write(line, 2, key.url)
            ws.write(line, 3, key.director)
            ws.write(line, 4, key.actors)
            ws.write(line, 5, key.other_info)
            line = line + 1
        page += 25
    wb.save('Excel_test.xls')
