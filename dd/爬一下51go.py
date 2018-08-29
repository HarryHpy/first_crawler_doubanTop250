# -*- coding: -utf-8-*-
from bs4 import BeautifulSoup
import requests


url= 'https://www.51go.com.au/'
url1='https://www.51go.com.au//Category/baby-products'


class products:
    def __init__(self,iu,pn,pp,pd):
        product_img_url=iu
        product_name=pn
        product_price=pp
        product_descripe=pd

    def show_products(self):
        print('图片网址', self.product_img_url)
        print('产品名称', self.product_name)
        print('产品价格', self.product_price)
        print('产品描述', self.product_descripe)




def getHtml(url):
    html=requests.get(url)
    return html

def getSoup(html):
    soup=BeautifulSoup(html.text,'lxml')
    return soup

def showSoup(soup):
    print(soup)



#获取产品详细信息链接
def get_describe_url():
    describe_url=''
    return describe_url





#获取产品详细信息
def get_describe_detail():
    detail=''
    return detail


#获取所有分类的页面
def get_home_page_sub_url(soup):
    ul_blog=soup.find('ul', attrs={'class':'menu jz clearfix'})
    li_blog=ul_blog.find_all('li')
    a_dic={}
    for key in li_blog:
        tem_a=key.find('a')
        tem_a_list='https://www.51go.com.au/'+tem_a.get('href')
        a_dic[tem_a.string]=tem_a_list
    del a_dic['首页']
    for key in a_dic:
        print(key,a_dic[key])
    return a_dic


#分页里一个li的解析

def div_li_blog(li_blog):
    products_list = ()
    for key in li_blog:
        a_blog = key.find_all('a')
        print(a_blog[0].find('img').get('src'))
        print(a_blog[1].string.strip())
        print(key.find('p', attrs={'class':'jingxuan_money'}).string.strip())

    return products_list


# 获取分页面产品列表
def get_products_url(div_page_url):
    div_page_soup = getSoup(getHtml(div_page_url))
    ul_blog = div_page_soup.find('div', attrs={'class':'jingxua'})
    li_blog_level1 = ul_blog.find('div', attrs={'class':'index_con_same'})
    li_blog_level2 = li_blog_level1.find('ul', attrs={'class':'jingxuan_ul clearfix jz'})
    li_blog = li_blog_level2.find_all('li')
    #print(li_blog)
    return li_blog






if __name__ == '__main__':
    get_home_page_sub_url(getSoup(getHtml(url)))
    liblog = get_products_url(url1)
    div_li_blog(liblog)
