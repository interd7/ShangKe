import time
import requests
import re
url = 'https://www.vmgirls.com/12985.html'
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
response = requests.get(url=url,headers = headers)
# print(response.request.headers)
html = response.text

# 解析网页
urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
print(urls)
# 保存图片
# for url in urls:
#     time.sleep(1)
#     # 图片的名字
#     file_name = url.split('/')[-1]
#     response = requests.get(url,headers=headers)
#     with open(file_name,'wb')as fp:
#         fp.write(response.content)
