#!/usr/bin/python
# encoding: utf-8
# -*- coding: utf8 -*-
"""
# @Time    : 2020/4/2
# @Author  : raincoat200
# @E-mail  : raincoat200@qq.com
# @Site    : https://github.com/raincoat200/
# @File    : sangfor.py
# @Software: PyCharm
"""
from fateadm_api import *
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # 导入chrome选项
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import date
from datetime import datetime, timedelta
import sys
import  os
import  shutil
import threading

import  subprocess
import  re

url='http://neris.csrc.gov.cn/shixinchaxun'
user='陈大大'
user_num='4452222000001010060'

codeimg='C:\\CSRC\\CODE.PNG'

def netstat(self):
    # 创建新线程
    self.thread1 = threading.Thread(target=self.diagnose)
    self.thread2 = threading.Thread(target=self.check)
    self.thread1.setDaemon(True)
    self.thread2.setDaemon(True)
    self.thread1.start()
    self.thread2.start()

def recognize():
    #菲菲打码平台模块参数
    pd_id           = "121954"     #用户中心页可以查询到pd信息
    pd_key          = "p5AnCsNshQA5sW46HzA3AQjyOyT4tCJc"
    app_id          = "321954"     #开发者分成用的账号，在开发者中心可以查询到
    app_key         = "YJI9a9xLOhldzbYLxC176GKrNOFKXogg"
    #识别类型，
    #具体类型可以查看官方网站的价格页选择具体的类型，不清楚类型的，可以咨询客服
    pred_type       = "30500"
    api             = FateadmApi(app_id, app_key, pd_id, pd_key)

    # 通过文件形式识别：
    file_name       = 'C:\\CSRC\\CODE.PNG'
    # 多网站类型时，需要增加src_url参数，具体请参考api文档: http://docs.fateadm.com/web/#/1?page_id=6
    #result =  api.PredictFromFileExtend(pred_type,file_name)   # 直接返回识别结果
    rsp = api.PredictFromFile(pred_type, file_name)  # 返回详细识别结果
    #print(rsp)
    if len(rsp.pred_rsp.value)!=5:
        just_flag = True
        print(len(rsp.pred_rsp.value))
        print("退款申请")
        if just_flag:
            if rsp.ret_code == 0:
                # 识别的结果如果与预期不符，可以调用这个接口将预期不符的订单退款
                # 退款仅在正常识别出结果后，无法通过网站验证的情况，请勿非法或者滥用，否则可能进行封号处理
                api.Justice(rsp.request_id)
    else:
        print("验证码:"+rsp.pred_rsp.value)
    return rsp.pred_rsp.value

start = time.perf_counter()
print("开始执行，请等待")
local1 = 'C:\\CSRC\\'
local2 = 'C:\\CSRC\\'+date.today().isoformat()
if os.path.exists(local1) is False:
    os.mkdir(local1)
if os.path.exists(local2) is False:
    os.mkdir(local2)
end = time.perf_counter()
duration = round(end - start, 3)
print("->初始化目录，耗时:", duration)
print("->")

# 开始爬虫
chrome_options = Options()
chrome_options.add_argument('--headless')  # 设置chrome浏览器无头模式
chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题
chrome_options.add_argument('disable-infobars')  # 调试提示
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

def input_data():
    WebDriverWait(driver, 20, 0.7).until(EC.title_contains('资本市场违法违规失信记录查询'))
    inputwd = driver.find_element_by_id("objName")
    inputwd.clear()  # 清楚文本框里的内容
    inputwd.send_keys(user)  # 输入姓名‘ ’
    driver.implicitly_wait(1)
    inputwd = driver.find_element_by_id("realCardNumber")
    inputwd.clear()  # 清楚文本框里的内容
    inputwd.send_keys(user_num)  # 输入身份证
    driver.implicitly_wait(1)

    # 截屏及加载识别模块
    driver.find_element_by_id('captcha_img').screenshot(local1 + 'CODE.PNG')
    codenum = recognize()
    #codenum = '55555'

    inputwd = driver.find_element_by_id("ycode")
    inputwd.clear()  # 清楚文本框里的内容
    inputwd.send_keys(codenum)  # 输入验证码
    driver.implicitly_wait(3)
    but = driver.find_element_by_id('querybtn')  # 搜索提交按钮
    but.click()  # but.click()  #点击按钮

input_data()

while True:
    try:
        a=driver.find_element_by_class_name("cx_text") #定位到查询结果
    except Exception as e1:
        print("定位不到查询结果："+e1)
        try:
            a = driver.find_elements_by_xpath("//td[@class='text_s']")[2]
            #b = a.find_element_by_xpath(".//../td[4]").text #定位到验证码错误提示框
            if a.find_element_by_xpath(".//../td[4]").text.find("验证码错误") >= 0:
                print("验证码错误")
        except Exception as e2:
            print("获取验证码状态异常："+e2)
            pass
        finally:
            driver.refresh()
            print("刷新")
            time.sleep(3)
            input_data()
    else:
        print("->")
        print("->验证码正确")
        break

end = time.perf_counter()
duration = round(end - start, 3)
print("->开始爬虫，耗时:", duration)
print("->")

# resize
driver.set_window_size(1000, 850)
driver.save_screenshot(local2+'\\'+user+'-'+user_num+'.png')
driver.close()
driver.quit()
os.system("start explorer "+local2)
