# Date:2019/9/25
# Author:Lingchen
# Mark:
#   解析商品网页，图片地址、价格、商品标题、评分量和评分星级
#   当要打开py文件所处的文件时只要使用相对路径就行了，而要使用其他文件夹的则需使用绝对路径,否则要借肋os库
#   文档: https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#find-all
import os
from bs4 import BeautifulSoup

# 相对路径: 获取当前文件上上级目录
folder_path = os.path.abspath('..')
path = folder_path + '/html/shop.html'
with open(path, 'r') as web_parse:
    soup = BeautifulSoup(web_parse, 'lxml')
    images = soup.select('body > div > div > div > div > div > div > img')
    prices = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right')
    titles = soup.select('body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a')
    scores = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right')
    # 为了从父节点开始取,此处保留:nth-of-type(2) 或者 p:nth-child(2),观察网页,多取几个星星的selector,就发现规律了
    stars = soup.select('body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-child(2)')
    # print(stars)

for img, price, title, score, star in zip(images, prices, titles, scores, stars):
    data = {
        'image': img.get('src'),
        'price': price.get_text(),
        'title': title.get_text(),
        'score': score.get_text(),
        # 统计有几颗星星, 运用find_all方法, 通过css来筛选
        'star': len(star.find_all('span', 'glyphicon glyphicon-star'))
    }
    print(data)