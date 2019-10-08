# Date:2019/10/8
# Author:Lingchen
# Mark:
#   监控程序

import time
from page_parsing import url_list

while True:
    print(url_list.find().count())
    time.sleep(5)