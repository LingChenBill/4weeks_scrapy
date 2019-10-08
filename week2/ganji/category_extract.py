# Date:2019/10/8
# Author:Lingchen
# Mark:
#   爬取赶集网-北京-二手市场的所有类目的链接信息

from bs4 import BeautifulSoup
import requests

start_url = 'http://bj.ganji.com/wu/'
url_host = 'http://bj.ganji.com'


def get_category_urls(url):
    web_data = requests.get(url)
    soup = BeautifulSoup(web_data.text, 'lxml')

    # 热门链接
    hot_links = soup.select('li.icon-hot > div.main-pop > dl > dd > a')
    for link in hot_links:
        # 获取a标签的href地址链接
        page_url = url_host + link.get('href')
        print(page_url)

    # 类目链接
    links = soup.select('div.main-pop > dl > dt > a')
    for link in links:
        # 获取a标签的href地址链接
        page_url = url_host + link.get('href')
        print(page_url)


get_category_urls(start_url)

# 打印的所有类目链接
category_urls = '''
    http://bj.ganji.com/ershoubijibendiannao/_macbook+pro/
    http://bj.ganji.com/ershoubijibendiannao/_macbook/
    http://bj.ganji.com/iphone/
    http://bj.ganji.com/ipodTouch/
    http://bj.ganji.com/iphone-iphone-4s/
    http://bj.ganji.com/mi-hongmi/
    http://bj.ganji.com/sanxingshouji-galaxy-s-iv/
    http://bj.ganji.com/sanxingshouji-galaxy-note-iii/
    http://bj.ganji.com/pingguo/
    http://bj.ganji.com/lianxiang/
    http://bj.ganji.com/thinkpad/
    http://bj.ganji.com/suoni/
    http://bj.ganji.com/daier/
    http://bj.ganji.com/huashuo/
    http://bj.ganji.com/ershoubijibendiannao/_New+iPad/
    http://bj.ganji.com/ershoubijibendiannao/_%E4%B9%90Pad/
    http://bj.ganji.com/psv/
    http://bj.ganji.com/shuma/_%E4%BD%B3%E8%83%BD/
    http://bj.ganji.com/shuma/_%E5%B0%BC%E5%BA%B7/
    http://bj.ganji.com/shuangrenchuang/
    http://bj.ganji.com/dianfengshan/
    http://bj.ganji.com/tongche/
    http://bj.ganji.com/qunzi/
    http://bj.ganji.com/fangshaishuang/
    http://bj.ganji.com/shouji/
    http://bj.ganji.com/shoujipeijian/
    http://bj.ganji.com/bijibendiannao/
    http://bj.ganji.com/taishidiannaozhengji/
    http://bj.ganji.com/diannaoyingjian/
    http://bj.ganji.com/wangluoshebei/
    http://bj.ganji.com/shumaxiangji/
    http://bj.ganji.com/youxiji/
    http://bj.ganji.com/xuniwupin/
    http://bj.ganji.com/jiaju/
    http://bj.ganji.com/jiadian/
    http://bj.ganji.com/zixingchemaimai/
    http://bj.ganji.com/rirongbaihuo/
    http://bj.ganji.com/yingyouyunfu/
    http://bj.ganji.com/fushixiaobaxuemao/
    http://bj.ganji.com/meironghuazhuang/
    http://bj.ganji.com/yundongqicai/
    http://bj.ganji.com/yueqi/
    http://bj.ganji.com/tushu/
    http://bj.ganji.com/bangongjiaju/
    http://bj.ganji.com/wujingongju/
    http://bj.ganji.com/nongyongpin/
    http://bj.ganji.com/xianzhilipin/
    http://bj.ganji.com/shoucangpin/
    http://bj.ganji.com/baojianpin/
    http://bj.ganji.com/laonianyongpin/
    http://bj.ganji.com/gou/
    http://bj.ganji.com/qitaxiaochong/
    http://bj.ganji.com/xiaofeika/
    http://bj.ganji.com/menpiao/
'''