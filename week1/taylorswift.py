# Date:2019/9/27
# Author:Lingchen
# Mark:
#   抓取异步加载数据-图片，并下载到本地

from bs4 import BeautifulSoup
import requests
import urllib.request

url = 'https://weheartit.com/inspirations/taylorswift?scrolling=true&page={}&before=335623893'
path = '/Users/zhuyangze/Desktop/tmp/capture/taylorswift/'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36'
}

proxies = {"http": "http://121.69.29.162:8118"}


# 获取图片url
def get_image_url(num):
    image_url = []

    for page_num in range(1, num + 1):
        full_path = url.format(str(page_num))
        web_data = requests.get(full_path, proxies=proxies)
        soup = BeautifulSoup(web_data.text, 'lxml')
        # print(soup)
        # 通过样式来定位img
        images = soup.select('img.entry-thumbnail')
        # print(images)

        for image in images:
            image_url.append(image.get('src'))

    print(len(image_url), 'Images shall be download')
    return image_url


# 下载图片
def download_image(url):
    # https://data.whicdn.com/images/335695531/superthumb.jpg?t=1569530890
    names = url.split('?')[0].split('/')
    # 下载图片到本地
    urllib.request.urlretrieve(url, path + names[-2] + '_' + names[-1])
    print('Done')


for url in get_image_url(2):
    download_image(url)