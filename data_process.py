# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 13:44
# @FileName: data_process.py
# @Software: VSCode
# @Comments: 饿了么爬虫，爬取商品信息|此脚本用于数据处理

import json
import pandas as pd


def json_to_excel():
    # 获取json数据
    with open("./data/cbd.json", "r") as f:
        load_data = json.load(f)

    # 定义商品类型及名字、描述、主要原料等
    menudata = load_data["menu"]
    foodname = []
    fooddescription = []
    foodmaterials = []
    category = []

    # 循环获取数据
    for i in menudata:
        foods = i["foods"]
        for j in foods:
            foodname.append(j["name"])
            fooddescription.append(j["description"])
            foodmaterials.append(j["materials"])
            category.append(i["name"])

        # 处理数据格式
        categorycol = pd.DataFrame(category)
        foodnamecol = pd.DataFrame(foodname)
        foodmaterialscol = pd.DataFrame(foodmaterials)
        # 横向拼接
        result = pd.concat(
            [categorycol, foodnamecol, foodmaterialscol], axis=1)
        # 更改dataframe列名称
        result.columns = ['所属类别', '商品名', '主要原料']
        # 保存为excel文件
        result.to_excel(r"./data/cbd.xlsx", index=None)
