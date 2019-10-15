"""
功能：定时结算，提交订单，期间有大概2s加载页面的时间，网速快的时候  可以在3s内抢购
适用：定时抢购变价商品
可以扫码，也可以密码登陆（需要手动验证）

Author: 王峥
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

# username = "写你的账号"
# pwd = "写你的密码"
# login(username,pwd)
login_er()
print("请手动选择商品")
buy_on_time(times)




    
    
            
            

    
    
            
            
