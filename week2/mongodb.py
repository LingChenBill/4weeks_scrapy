# Date:2019/10/4
# Author:Lingchen
# Mark:
#   mongodb使用
#   给数据库命名: 给Excel文件命名
#   在文件下创建表单: 在Excel中增加sheet
#   往数据库写入数据: 在Excel中填写每一行数据
#   展示数据库中的数据
#   数据库操作

import pymongo

client = pymongo.MongoClient('localhost', 27017)
# 数据库名称
walden = client['walden']
sheet_tab = walden['sheet_tab']

# path = '/Users/zhuyangze/Documents/fork/4weeks_scrapy/week2/data/walden.txt'
# with open(path, 'r') as f:
#     lines = f.readlines()
#     for index, line in enumerate(lines):
#         data = {
#             'index': index,
#             'line': line,
#             'words': len(line.split())
#         }
#         sheet_tab.insert_one(data)

# 展示mongodb中的数据,查找数据:运用find
# for item in sheet_tab.find({'words':0}):
# for item in sheet_tab.find():
# $lt/$lte/$gt/$gte/$ne，依次等价于</<=/>/>=/!=,(l表示less,g表示greater,e表示equal,n表示not)
for item in sheet_tab.find({'words': {'$lt': 5}}):
    print(item)
    # print(item['line'])