# Date:2019/10/9
# Author:Lingchen
# Mark:
#   断点续传，继续抓取url

# 查看python 库地址
# import sys
# print(sys.path)
from category_page_parsing import url_list, item_info

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
print(x)
y = set(index_urls)
print(y)
url_continue = x - y
print(url_continue)