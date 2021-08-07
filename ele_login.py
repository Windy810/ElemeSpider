# -*- coding: utf-8 -*-
# @Time    : 2021/8/7 13:04
# @FileName: ele_login.py
# @Software: VSCode
# @Comments: 饿了么爬虫，爬取商品信息|此函数用于登录及cookie获取

import json 
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def login_and_cookie_get():
    # 设置selenium启动浏览器的配置项
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    # 反反爬虫：掩盖selenium浏览器指纹，可在控制台通过window.navigator.webdriver查看得false
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # chrome升级至v59以后，可用如下headless的方式使得不显示浏览器界面
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # 隐式等待
    driver.implicitly_wait(10)
    # 设置需访问的界面
    driver.get("https://tb.ele.me/wow/msite/act/login")

    # 等到登录页面出现再操作
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("alibaba-login-box")) 
    # print(driver.page_source)

    # 获取并自动填充手机号
    phone = driver.find_element_by_xpath('//input[@id="fm-sms-login-id"]')
    phonenumber = input('请输入手机号,回车键确认:') 
    phone.send_keys(phonenumber)

    # 发送验证码按钮
    driver.find_element_by_xpath("//a[@class='send-btn-link']").click()

    # 以前的协议同意按钮
    # driver.find_element_by_css_selector("input[@id='fm-agreement-checkbox']").click()

    # 验证码发送前的滑块验证
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("baxia-dialog-content")) 
    fuck=driver.find_element_by_xpath('//span[@id="nc_2_n1z"]')
    action =ActionChains(driver)
    action.click_and_hold(fuck)
    action.move_by_offset(300,0)
    action.release().perform()

    # 验证码输入及填充
    # 此次需返回父级iframe，才能获取到验证码输入等元素
    vali = input('请输入验证码,回车键确认:') 
    driver.switch_to.parent_frame()
    driver.find_element_by_xpath('//input[@id="fm-smscode"]').send_keys(vali)
    # 点击登录
    driver.find_element_by_xpath("//button[@type='submit']").click()

    # 应该是之前的滑块速度问题或者是浏览器指纹导致需要二次滑块验证
    time.sleep(3)
    WebDriverWait(driver,10).until(EC.frame_to_be_available_and_switch_to_it("baxia-dialog-content")) 
    fuck=driver.find_element_by_xpath('//span[@id="nc_2_n1z"]')
    action =ActionChains(driver)
    action.click_and_hold(fuck)
    action.move_by_offset(280,0)
    action.release().perform()

    # 再次点击登录
    driver.switch_to.parent_frame()
    driver.find_element_by_xpath("//button[@type='submit']").click()

    # 获取cookie并写入cookies.json文件
    time.sleep(5)
    #获取cookie
    dictCookies=driver.get_cookies()
    #json字符串编码
    jsonCookies=json.dumps(dictCookies)
    with open('cookies.json','w')as f:
        f.write(jsonCookies)
    print('cookie加载完毕')

def cookie_process():
    with open("./cookies.json","r") as f:
        load_data = json.load(f)
    for i in load_data:
        if(i["name"]=="SID"):
            mycookie = i["value"]
    return mycookie
    # print(cookies)