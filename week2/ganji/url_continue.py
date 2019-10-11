# Date:2019/10/9
# Author:Lingchen
# Mark:
#   断点续传，继续抓取url

# 查看python 库地址
# import sys
# print(sys.path)
from multiprocessing import Pool
from category_extract import category_urls
from category_page_parsing import get_links_from,url_list, item_info

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
print(x)
y = set(index_urls)
print(y)
url_continue = x - y
print(url_continue)


def get_all_links_from(channel):
    for num in range(1, 3):
        get_links_from(channel, num)


if __name__ == '__main__':
    # 开启多进程
    pool = Pool(processes=4)
    pool.map(get_all_links_from, category_urls.split())