import requests
from bs4 import BeautifulSoup

# 第1页 网址 http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-1
# 第2页 网址 http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-2
# 第25页 网址 http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-25
# 确定一个网址
for page in range(1, 26):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    # 发送请求，获得响应
    html = requests.get(url).text
    # pattern = re.compile('<li>.*?class="list_num.*?>(\d+).</div>.*?src="(.*?)".*?</li>', re.S)
    # books = re.findall(pattern, html)
    soup = BeautifulSoup(html, "lxml")
    books = soup.find("ul", class_="bang_list clearfix bang_list_mode").find_all("li")
    iii = 0
    for book in books:
        img_src = book.find("img").get("src")  # 图像地址
        print(img_src)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        response = requests.get(url=img_src, headers=headers).content
        with open('./picture/img' + str(iii) + '.png', 'wb')as fp:
            fp.write(response)
        iii = iii + 1
