# -*- coding: utf-8 -*-
# @Time    : 2021/8/6 12:12
# @FileName: merchant_spider.py
# @Software: VSCode
# @Comments: 饿了么爬虫，爬取商品信息|此函数用于爬取固定商家内商品信息

import requests
import json


def merchant_spider(merchantID, mycookie):

    # 样例格式
    # merchantID = E11239979582907458257
    # mycookie = KQAAAAEesy9K7AAGDwBbLyKEmp8S7L5nCS8HfVsyodeBoyI9Ym_U0kFd
    url = 'https://h5.ele.me/pizza/shopping/restaurants/{m}/batch_shop'.format(
        m=merchantID)
    cookie = {
        'SID': mycookie,
    }
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/71.0.3578.98 Safari/537.36',
        'Referer': 'https://h5.ele.me/pizza/shopping/restaurants/E14594189798467046744/batch_shop?user_id=4810026826&code=0.7331059914485989&extras=%5B%22activities%22%2C%22albums%22%2C%22license%22%2C%22identification%22%2C%22qualification%22%5D&terminal=h5&latitude=28.103027&longitude=112.99572',
    }
    response = requests.get(url, headers=header, cookies=cookie)

    # 将获取的值写入文件
    with open('cbd.json', 'w') as f:
        f.write(json.dumps(response.json(), ensure_ascii=False))
