# Date:2019/9/29
# Author:Lingchen
# Mark:
#   抓取58同城平板电脑版块上的信息:标题，价格，日期，地区

from bs4 import BeautifulSoup
import requests
import time

# url = 'https://bj.58.com/pingbandiannao/26062681492781x.shtml'


# 获取列表页跳转链接
def get_links_from(who_sells=0):
    time.sleep(3)
    urls = []
    # 确定是个人 还是 商家 列表
    list_view = 'https://bj.58.com/pbdn/{}/'.format(str(who_sells))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    for link in soup.select('td.t a.t'):
        # 获取跳转链接
        urls.append(link.get('href').split('?')[0])
    print(urls)
    return urls


# 获取点击量
def get_views_from(url):
    time.sleep(1)
    # https://jst1.58.com/counter?infoid=39501573434248&userid=&uname=&sid=0&lid=0&px=0&cfpath=
    id = url.split('/')[-1].strip('x.shtml')
    api = 'https://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api)
    # 返回结果解析: Counter58.userlist[0]={uid:'0',uname:'',face:'',vt:''};Counter58.total=76
    # 好像取不到返回值了。。。
    views = js.text.split('=')[-1]
    return views


# 获取58祥情页信息
def get_item_info(who_sells=0):
    time.sleep(3)
    # print('111')
    urls = get_links_from(who_sells)
    print(urls)
    # print('222')
    for url in urls:
        if url.find('.shtml') != -1:
            wb_data = requests.get(url)
            soup = BeautifulSoup(wb_data.text, 'lxml')
            title = soup.title.text
            price = soup.select('span.infocard__container__item__main__text--price')
            # print(price)
            date = soup.select('.detail-title__info__text')
            area = soup.select('div.infocard__container__item__main > a')
            # views = soup.select('.detail-title__info__totalcount')
            # print(views)
            data = {
                'title': title,
                # 视抓取时的网页格式而定，进行文本预处理
                'price': price[0].get_text().replace('\r\n', '').replace('\t', '').replace(' ', ''),
                'date': date[0].text.split(' ')[0],
                'area': area[0].text,
                'cate': '个人' if who_sells == 0 else '商家',
                'views': get_views_from(url)
            }
            print(data)


get_item_info(1)
#print(get_links_from(1))
