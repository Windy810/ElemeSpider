# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 14:30
# @FileName: main_spider.py
# @Software: VSCode
# @Comments: 饿了么爬虫，爬取商品信息|主函数

import ele_login
import merchant_spider
import data_process

if __name__=="__main__":
    # 自动登录并记录cookie
    ele_login.login_and_cookie_get()
    mycookie = ele_login.cookie_process()

    # 手动输入商家ID
    # ID格式为：E11239979582907458257
    inputid = input("请输入商家ID：")
    # 爬取信息
    merchant_spider.merchant_spider(inputid,mycookie)

    # 将爬取数据处理为excel格式
    data_process.json_to_excel()
