# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :ShangKe
# @File     :paDemoFanyi
# @Date     :2020/10/28 9:48 上午
# @Author   :段益迈
# @Email    :dym0822@163.com
# @Software :PyCharm
-------------------------------------------------
"""
# -*- coding: utf-8 -*-

import requests
# 爬post操作流程
# 1.url = request url
while True:

    inputword = input('请输入你要查询的英语单词：\n')
    print('=====================================================================')
    url = 'https://fanyi.baidu.com/sug'
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    data = {'kw': '{}'.format(inputword)}
    # 2.发送请求：post请求：
    response = requests.post(url=url, data=data, headers=headers).json()
    # print(response)
    # 3.保存页面信息
    # with open('fanyi.json','w',encoding='utf-8')as fp:
    #     fp.write(str(response))# 写入必须是字符串信息，不能是字典
    # 4.优化代码
    # （1）提取翻译内容
    data = response.get('data')
    # (2) 遍历提取单词与翻译：
    for i in data:
        # (1) 获取单词
        words = i.get('k')
        fanyi = i.get('v')
        fanyi_danci = words + ':' + fanyi + '\n'
        print(fanyi_danci)
        with open('danci.txt', 'a', encoding='utf-8')as fp:
            fp.write(fanyi_danci)
    print('已写入单词本！')
    print('=====================================================================')
