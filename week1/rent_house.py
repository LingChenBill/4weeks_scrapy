# Date:2019/9/26
# Author:Lingchen
# Mark:
#   进入小猪短租，从列表页点击进入第一个详情页
#   在详情页中爬取: 标题、地址、日租金、第一张房源图片链接、房东图片链接、房东性别和房东名字

import requests
from bs4 import BeautifulSoup

url = 'http://bj.xiaozhu.com/fangzi/108662280703.html'

page_link = []
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'cookie': 'Hm_lvt_92e8bc890f374994dd570aa15afc99e1=1569502647; gr_user_id=bbd0a629-c4fa-4666-ac09-c8fd9a2a7419; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id=53cdf86e-5298-4560-8d5a-171d626b6bc9; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_sid_with_cs1=53cdf86e-5298-4560-8d5a-171d626b6bc9; 59a81cc7d8c04307ba183d331c373ef6_gr_last_sent_cs1=N%2FA; 59a81cc7d8c04307ba183d331c373ef6_gr_session_id_53cdf86e-5298-4560-8d5a-171d626b6bc9=true; grwng_uid=52c18a09-da0d-4096-a0fb-6e8b71f0a88e; abtest_ABTest4SearchDate=b; TY_SESSION_ID=817ced07-d505-4a4a-ad82-7fd129d6ffda; _uab_collina=156950266009361987895171; _pykey_=d0a6d79c-b49a-5d0f-8d4d-9bf3faa76bb2; xzuuid=2480e462; rule_math=z3gzv9rpy0q; Hm_lpvt_92e8bc890f374994dd570aa15afc99e1=1569506419'
}

page_data = []


# 判断房东性别
def print_gender(class_name):
    if class_name == 'member_ico':
        return '男'
    elif class_name == 'member_ico1':
        return '女'
    else:
        return '未知'


# 构造网页数据函数
def get_page_data(url, page_data):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')
    # print(soup)

    # 因为是单页面，使用 select 方法获得的元素又是一个列表，那么列表中的第一个元素且也是唯一一个元素即是我们要找的信息 用 “[0]” 索引将其取出

    # 标题
    title = soup.select('div.pho_info > h4')[0].text
    # 地址
    # address = soup.select('p > span.pr5')[0].text
    # 和 get('href') 同理，他们都是标签的一个属性而已，我们只需要的到这个属性的内容即可
    address = soup.select('div.pho_info > p')[0].get('title')
    # 日租金 “#” 代表 id 这个找元素其实就是找他在页面的唯一
    rent = soup.select('#pricePart > div.day_l > span')[0].text
    # 第一张房源图片链接
    pic = soup.select('#curBigImage')[0].get('src')
    # 房东图片链接
    rent_man_pic = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > a > img')[0].get('src')
    # 房东性别
    if len(soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')[0].get('class')) == 0:
        rent_man_sex = '未知'
    else:
        rent_man_sex = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')[0].get('class')[0]
    # 房东名字
    rent_man_name = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')[0].text
    # print(title, address, rent, pic, rent_man_pic, rent_man_sex, rent_man_name, sep='\n')

    data = {
        'title': title.strip('\n'),
        'address': address,
        'rent': rent,
        'pic': pic,
        'rent_man_name': rent_man_name,
        'rent_man_pic': rent_man_pic,
        'rent_man_sex': print_gender(rent_man_sex)
    }

    # print(data)
    page_data.append(data)


def get_page_link(page_number, page_link):
    for each_num in range(2, page_number):
        print(each_num)
        full_path = 'http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(each_num)
        web_data = requests.get(full_path, headers=headers)
        soup = BeautifulSoup(web_data.text, 'lxml')
        # 通过样式来查找
        links = soup.select('a.resule_img_a')
        # print(links)
        for link in links:
            # 获取跳转到祥情页的链接
            # print(link.get('href'))
            page_link.append(link.get('href'))
            # 获取网页数据
            get_page_data(link.get('href'), page_data)


get_page_link(4, page_link)
# print(page_link)
print(page_data)











