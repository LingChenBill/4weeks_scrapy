# Date:2019/9/25
# Author:Lingchen
# Mark:
#   解析本地网页
#   css selector: body > div.main-content > ul > li:nth-child(1) > img
#   XPath: /html/body/div[2]/ul/li[1]/img
#   1) 筛选网页信息
#   2) 筛选标签文本
#   3）筛选标签中的文本信息

import os
from bs4 import BeautifulSoup

folder_path = os.path.abspath('..')
path = folder_path + '/html/the_blah.html'
with open(path, 'r') as wb_data:
    # 获取整个网页内容
    Soup = BeautifulSoup(wb_data, 'lxml')
    # print(Soup)
    # images = Soup.select('body > div.main-content > ul > li:nth-child(1) > img')
    # 筛选图片
    images = Soup.select('body > div.main-content > ul > li > img')
    # 筛选标题
    titles = Soup.select('body > div.main-content > ul > li > div.article-info > h3 > a')
    # 筛选描述性文字
    descriptions = Soup.select('body > div.main-content > ul > li > div.article-info > p.description')
    # 筛选分数
    rates = Soup.select('body > div.main-content > ul > li > div.rate > span')
    # 筛选标签: 多个标签内容，指定到css selector的父级样式上
    cates = Soup.select('body > div.main-content > ul > li > div.article-info > p.meta-info')
    # print(images, titles, descriptions, rates, cates, sep='\n--------\n')

# for title in titles:
#     print(title.get_text())

info = []
for title, image, desc, rate, cate in zip(titles, images, descriptions, rates, cates):
    data = {
        'title': title.get_text(),
        'rate': rate.get_text(),
        'desc': desc.get_text(),
        # 'cate': cate.get_text(),
        'cate': list(cate.stripped_strings),
        'image': image.get('src')
    }
    info.append(data)
    # print(data)

# 筛选评分 > 3的标题和标签
for i in info:
    if float(i['rate']) > 3:
        print(i['title'], i['cate'])
