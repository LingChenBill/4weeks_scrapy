# Date:2019/10/6
# Author:Lingchen
# Mark:
#   将祥情页中的数据存储到数据库

from bs4 import BeautifulSoup
import requests
import time
import pymongo

# mongodb数据库设置
client = pymongo.MongoClient('localhost', 27017)
city = client['58city']
url_list = city['url_list']
item_info = city['item_info']


# 列表访问链接
def get_links_from(channel, pages, who_sells=0):
    # https://bj.58.com/diannao/0/pn2/
    list_view = '{}{}/pn{}/'.format(channel, str(who_sells), str(pages))
    # 请求网址，解析网页
    wb_data = requests.get(list_view)
    time.sleep(1)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    # 判断当前列表是否有列表数据
    if soup.find('td', 't'):
        # #infolist > table > tbody > tr:nth-child(1) > td.t > a
        for link in soup.select('td.t a.t'):
            # https://bj.58.com/diannao/39671281540263x.shtml?link_abtest=&psid=194088949205829058130870855&entinfo=39671281540263_p&slot=-1
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)
    else:
        # Nothings!
        pass


# get_links_from('https://bj.58.com/shuma/', 2)


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # 判断访问的url是否是404页
    no_longer_exist = False
    if soup.find('script', type="text/javascript").get('src'):
        no_longer_exist = '404' in soup.find('script', type="text/javascript").get('src').split('/')

    if no_longer_exist:
        pass
    else:
        title = soup.title.text
        price = soup.select('span.infocard__container__item__main__text--price')[0].text\
            .replace('\r\n', '').replace('\t', '').replace(' ', '')
        date = soup.select('.detail-title__info__text')[0].text.split(' ')[0]
        area = soup.select('div.infocard__container__item__main > a')[0].text
        item_info.insert_one({'title': title, 'price': price, 'date': date, 'area': area})
        print({'title': title, 'price': price, 'date': date, 'area': area})


# url = 'xxx'
# wb_data = requests.get(url)
# soup = BeautifulSoup(wb_data.text, 'lxml')
# print(soup.prettify())
# # 判断404
# no_longer_exist = '404' in soup.find('script', type='text/javascript').get('src').split('/')

# get_item_info('https://bj.58.com/shuma/39638005279523x.shtml')
