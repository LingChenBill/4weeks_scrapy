# Date:2019/10/8
# Author:Lingchen
# Mark:
#   多进程爬虫的数据抓取
#   引入自己写的模块:
#       1) 将自己的程序xxx.py放到/Users/xxx/PycharmPro/aconda/lib/python3.6/site-packages

from multiprocessing import Pool
from page_parsing import get_links_from
from channel_extract import channel_list

# import sys
# print(sys.path)


def get_all_links_from(channel):
    for num in range(1, 101):
        get_links_from(channel, num)


if __name__ == '__main__':
    # 开启多进程
    pool = Pool(processes=4)
    pool.map(get_all_links_from, channel_list.split())
