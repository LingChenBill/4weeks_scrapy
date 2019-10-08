# Date:2019/10/8
# Author:Lingchen
# Mark:
#   赶集列表页，爬取（个人）类目下的全部链接

from bs4 import BeautifulSoup
import requests
import time
import pymongo

# 设置Mongodb
client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
url_list = ganji['url_list']


# 获取列表信息
def get_links_from(url, pages):
    list_view = url
    if pages > 1:
        list_view = '{}/o{}/'.format(url, str(pages))

    time.sleep(2)
    web_data = requests.get(list_view)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup.prettify())

    # if soup.find('js-item'):
    for link in soup.select('li.js-item > a'):
        item_link = link.get('href')
        url_list.insert_one({'url': item_link})
        print(item_link)


get_links_from('http://bj.ganji.com/ershoubijibendiannao/_macbook+pro/', 3)