# 淘宝定时抢购python程序
注意：最近学习python，水平不高，写着玩玩；参考了一些资料，采用的浏览器自动化测试的方法，速度取决于网速，可以用于一些要求不高的任务，
#### 环境
1. win10系统 vscode编译器
2. python3.7 [下载链接](https://www.python.org/). 
3. 谷歌插件 
4. selenium库
#### 下载
1. python3.7 官网直接下载
2. 谷歌驱动  [下载链接](http://chromedriver.storage.googleapis.com/index.html). 
	注意：弄清楚自己浏览器的版本号，下载同版本的chorme.
3. selenium库
	注意：在CMD中直接pip install-U selenium
#### 运行流程
1. 登陆方式：账号密码登陆，手动拖动验证
2. 然后浏览器跳转至我的购物车
3. 在购物车选中购买商品
4. 定时时间到，自动结算，提交订单，提交订单页面需要加载后才能提交，大概耗费1-2s加载时间，取决于网速

#### 代码
```
"""
功能：定时结算，提交订单，期间有大概2s加载页面的时间
适用：抢购变价商品

Author: wz
Date: 2019-10-13
"""
from selenium import webdriver
import datetime
import time


driver = webdriver.Chrome()
driver.maximize_window()

#账户登陆    
def login(username, pwd):
    driver.get("https://www.jd.com/")
    while True:
        if driver.find_element_by_link_text("你好，请登录"):
            driver.find_element_by_link_text("你好，请登录").click()
        time.sleep(1)
        if driver.find_element_by_link_text("账户登录"):
            driver.find_element_by_link_text("账户登录").click()
        time.sleep(1)
        if driver.find_element_by_name("loginname"):
            driver.find_element_by_name("loginname").send_keys(username)
        if driver.find_element_by_name("nloginpwd"):
            driver.find_element_by_name("nloginpwd").send_keys(pwd)
        time.sleep(1)
        if driver.find_element_by_id("loginsubmit"):
            driver.find_element_by_id("loginsubmit").click()
        time.sleep(1)
        
    time.sleep(3)
    driver.get("https://cart.jd.com/cart.action")
    #输出登陆时间
    now = datetime.datetime.now()
    print("login success", now.strftime('%Y-%m-%d %H:%M:%S'))

#二维码登陆
def login_er():
    driver.get("https://www.jd.com/")
    if driver.find_element_by_link_text("你好，请登录"):
        driver.find_element_by_link_text("你好，请登录").click()
        print("请在15s内完成扫码")
        time.sleep(15)
        driver.get("https://cart.jd.com/cart.action")#转到我的购物车
    #输出登陆时间
    now = datetime.datetime.now()
    print("login success", now.strftime('%Y-%m-%d %H:%M:%S'))


def buy_on_time(times):
    while True:
        now = datetime.datetime.now()
        if now > times:
            #点结算
            while True:
                try:
                    if driver.find_element_by_class_name("submit-btn"):
                        driver.find_element_by_class_name("submit-btn").click()
                    if driver.find_element_by_id("order-submit"):
                        driver.find_element_by_id("order-submit").click()
                        now = datetime.datetime.now()
                        print("抢购成功", now.strftime('%Y-%m-%d %H:%M:%S'))
                        break
                except:
                    print("再次尝试提交订单")
        
                    
times = datetime.datetime(2019,10,13,21,55,00)

username = "京东账号"
pwd = "京东密码"
login(username,pwd)
#login_er()
print("请手动选择商品")
buy_on_time(times)


```

github 地址
https://github.com/wz-gis/python_pra/tree/master/crawler
