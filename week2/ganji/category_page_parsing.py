# Date:2019/10/8
# Author:Lingchen
# Mark:
#   赶集列表页，爬取（个人）类目下的全部链接

from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random

# 设置Mongodb
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']
item_info = ganji['item_info']

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Connection': 'keep-alive'
}

# 免费代理站点: https://cn-proxy.com/, 防止ip被封
proxy_list = [
    'http://149.129.98.81:80',
    'http://117.131.119.116:80',
    'http://39.137.69.6:80'
]

# 随机获取代理IP
proxy_ip = random.choice(proxy_list)
proxies = {'http': proxy_ip}


# 获取祥情页面商品数据
def get_item_info(url, data=None):
    time.sleep(2)
    web_data = requests.get(url, headers=headers, proxies=proxies)

    if web_data.status_code == 404:
        pass
    else:
        soup = BeautifulSoup(web_data.text, 'lxml')
        data = {
            'title': soup.title.text.strip(),
            # 同一级的css样式查找方式
            'price': soup.select('.f22.fc-orange.f-type')[0].text.strip(),
            # \xa0:不间断空白符 &nbsp
            'publish_date': soup.select('.pr-5')[0].text.strip().split('\xa0')[0],
            # [<a href="/ershoubijibendiannao/" target="_blank"> 北京</a>, <a href="/ershoubijibendiannao/" target="_blank">海淀</a>]
            # 可迭代操作
            'area': list(map(lambda x: x.text.strip(), soup.select('ul.det-infor li > a'))),
            'phone': soup.select('.phoneNum-style')[0].text.strip().replace(' ', ''),
            'url': url
        }
        item_info.insert_one(data)


# 获取列表信息
def get_links_from(channel, pages, who_sells='o'):
    list_view = channel
    if pages > 1:
        list_view = '{}{}{}/'.format(channel, str(who_sells), str(pages))
    time.sleep(2)
    web_data = requests.get(list_view, headers=headers, proxies=proxies)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup.prettify())

    if soup.find('li', 'js-item'):
        for link in soup.select('li.js-item > a'):
            item_link = link.get('href')
            url_list.insert_one({'url': item_link})
            print(item_link)
            get_item_info(item_link)


# get_links_from('http://bj.ganji.com/ershoubijibendiannao/_macbook+pro/', 3)
# get_item_info('http://bj.ganji.com/ershoubijibendiannao/37712803847193x.htm')