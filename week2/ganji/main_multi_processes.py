# Date:2019/10/8
# Author:Lingchen
# Mark:
#   多进程爬虫的数据抓取--爬取赶集二手信息列表链接

from multiprocessing import Pool
from category_extract import category_urls
from category_page_parsing import get_links_from


def get_all_links_from(channel):
    for num in range(1, 3):
        get_links_from(channel, num)


if __name__ == '__main__':
    # 开启多进程
    pool = Pool(processes=4)
    pool.map(get_all_links_from, category_urls.split())
    pool.close()
    pool.join()

