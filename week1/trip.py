# Date:2019/9/25
# Author:Lingchen
# Mark:
#   用Requests + BeautifulSoup 爬取Tripadvisor网页
#   1) 服务器与本地的交换机制
#   2) 解析真实网页的方法 - BeautifulSoup

# 在需要用户认证的网页爬取时，可以使用headers来模拟
# headers = {
#     'User-Agent': 'xxx',
#     'Cookie': 'xxxx'
# }
# web_data = requests.get(url, headers = headers)

import requests
from bs4 import BeautifulSoup

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'

# 标题
# titles = soup.select('#taplc_attraction_coverpage_attraction_0 > div > div > div > div '
#                   '> div.shelf_item_container.shelfItemsWithGrayBgWrapper > div > div.poi > div > div.item.name > a')

# 模拟手机端来爬取图片
# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
# }
#
# phone_data = requests.get(url, headers=headers)
# soup = BeautifulSoup(phone_data.text, 'lxml')
# imgs = soup.select('div.centering_wrapper > img')
# print(imgs)


# 构造函数
def get_attractions(url, data=None):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # 标题:简单写法
    titles = soup.select('div.item.name > a')
    # 图片
    images = soup.select('img[width="200"]')
    # 分类 div + css style来锁定
    cates = soup.select('div.detail > div:nth-child(4)')
    # print(cates)

    for title, img, cate in zip(titles, images, cates):
        data = {
            'title': title.get_text(),
            'img': img.get('src'),
            'cate': list(cate.stripped_strings)
        }
        print(data)


get_attractions(url)
