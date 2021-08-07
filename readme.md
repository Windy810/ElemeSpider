# 饿了么商品信息爬虫

## 代码说明

1. 主目录下的脚本用于在已知[商家数据api名称](https://github.com/Windy810/ElemeSpider/blob/master/img/dataapi1.png)的情况下（如样例中为batch_shop），才能正常获取，如能找到其他类型商户的api，可以直接对url进行修改
2. 或者考虑第二种通用解法，登录获取页面html后，直接对html进行数据解析（见[/HtmlDataProcess](https://github.com/Windy810/ElemeSpider/tree/master/HtmlDataProcess)）

## 环境要求

1. python环境：python3.9
2. 运行环境：Linux（Debian）
3. 所需软件：selenium，chrome

## 环境安装

1. 下载chromedriver：  
`wget https://chromedriver.storage.googleapis.com/2.38/chromedriver_linux64.zip`
2. 解压到/usr/bin
3. 下载chrome：  
`wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb  `
4. 安装chrome：  
`dpkg -i google-chrome-stable_current_amd64.deb`

## 运行

`python3 main_spider.py`