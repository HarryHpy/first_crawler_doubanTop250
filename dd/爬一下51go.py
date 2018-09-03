# -*- coding: -utf-8-*-
from bs4 import BeautifulSoup
import requests
import xlwt


url = 'https://www.51go.com.au/'
url1 = 'https://www.51go.com.au//Category/baby-products'


class products:

    def __init__(self,iu,pn,pp,link):
        self.product_img_url=iu
        self.product_name=pn
        self.product_price=pp
        self.product_descripe=''
        self.product_link=link

    def show_products(self):
        print('图片网址： ', self.product_img_url)
        print('产品名称： ', self.product_name)
        print('产品价格： ', self.product_price)
        print('产品描述： ', self.product_descripe)
        print('产品页面： ', self.product_link)
        print('---------------------------------------------')

def add_to_sheet(ws,category_products_list):
    line = 1
    ws.write(0, 0, label='产品名称')
    ws.write(0, 1, label='产品价格(澳元)')
    ws.write(0, 2, label='产品描述')
    for key in category_products_list:
        ws.write(line, 0, key.product_name)
        ws.write(line, 1, key.product_price)
        ws.write(line, 2, key.product_descripe)
        line=line+1



def getHtml(url):
    html = requests.get(url)

    return html

def getSoup(html):
    soup=BeautifulSoup(html.text,'lxml')
    return soup

def showSoup(soup):
    print(soup)



#获取产品详细信息链接
def get_describe_url(li_blog):
    describe_url=''
    li_blog.find('a', attrs={'class':'jingxuan_img'})

    return describe_url





#获取产品详细信息
def get_describe_detail(products):
    detail=''
    soup=getSoup(getHtml(products.product_link))
    detail=soup.find('div', attrs={'class':'pro_con_t_rt_xinx'}).string.strip()
    #print(detail)
    return detail


#获取所有分类的页面
def get_home_page_sub_url(soup):
    ul_blog=soup.find('ul', attrs={'class':'menu jz clearfix'})
    li_blog=ul_blog.find_all('li')
    a_dic={}
    for key in li_blog:
        tem_a = key.find('a')
        tem_a_list = 'https://www.51go.com.au/'+tem_a.get('href')
        a_dic[tem_a.string]=tem_a_list
    del a_dic['首页']
    #for key in a_dic:
        #print(key,a_dic[key])
    return a_dic





#分页里一个li的解析

def div_li_blog(li_blog):
    products_list = list()
    for key in li_blog:
        a_blog = key.find_all('a')
        iu=a_blog[0].find('img').get('src')
        pn=a_blog[1].string.strip()
        pp=key.find('p', attrs={'class':'jingxuan_money'}).string.strip()
        a_pro_link=key.find('a', attrs={'class':'jingxuan_img'})
        link ='https://www.51go.com.au/'+a_pro_link.get('href')
        # print(iu)
        # print(pn)
        # print(pp)
        # print(link)
        # print('--------------------------------------------------------------------------')
        tem_products = products(iu,pn,pp,link)
        tem_products.product_descripe=get_describe_detail(tem_products)
        products_list.append(tem_products)


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



#获取页数
def get_end_page(star_url):
    end_page=''
    a_blog=getSoup(getHtml(star_url)).find('div',attrs={'class':'page'})
    last_page=a_blog.find_all('a')
    # print(last_page)
    end_element=last_page[len(last_page)-2]
    end_page=end_element.string.strip('.')
    # print(end_page)
    return end_page




if __name__ == '__main__':
    wb=xlwt.Workbook()
    category_map= get_home_page_sub_url(getSoup(getHtml(url)))
    for key in category_map:
        n = 0
        category_products_list=list()
        print('页面：'+key)
        page=get_end_page(category_map[key])
        ws=wb.add_sheet(key)
        for i in range(1,int(page)+1):
            tem_url=category_map[key]+"?pageIndex=%s&pageSize=20"%i
            # print(tem_url)
            page_pro_list=div_li_blog(get_products_url(tem_url))
            category_products_list=category_products_list+page_pro_list
            n=n+1
            print('完成%s页'%n)
        add_to_sheet(ws, category_products_list)

    wb.save('products')
        # for j in category_products_list:
        #     j.show_products()













    # get_home_page_sub_url(getSoup(getHtml(url)))
    # liblog = get_products_url(url1)
    # a=div_li_blog(liblog)
    # for i in a:
    #     i.show_products()
    # get_end_page('https://www.51go.com.au/Category/fashion')
