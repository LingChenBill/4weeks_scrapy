# Date:2019/10/4
# Author:Lingchen
# Mark:
#   抓取小猪短租这个页面的前三页，把抓取结果存储到Mongodb数据库中
#   然后在数据库中筛选出所有价格大于等于500元的房源，并打印出来

from bs4 import BeautifulSoup
import requests
import time
import pymongo

# mongodb配置
client = pymongo.MongoClient('localhost', 27017)
xiaozhurent = client['xiaozhurent']
sheet_tab = xiaozhurent['rent_page_data']


def get_page_item(page_num):
    time.sleep(3)

    for index in range(1, page_num + 1):
        url = 'https://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(index))
        web_data = requests.get(url)
        soup = BeautifulSoup(web_data.text, 'lxml')
        # 标题
        titles = soup.select('span.result_title')
        # 价格
        prices = soup.select('span.result_price > i')
        # 规格
        styles = soup.select('em[class="hiddenTxt"]')

        for title, price, style in zip(titles, prices, styles):
            data = {
                'title': title.get_text(),
                'price': int(price.get_text()),
                'style': style.get_text().replace('\n', '').replace(' ', '')
            }
            sheet_tab.insert_one(data)
            # print(data)
    print('Mongodb insert done!')


# get_page_item(3)


for item in sheet_tab.find():
    if item['price'] == 520:
        print(item)


