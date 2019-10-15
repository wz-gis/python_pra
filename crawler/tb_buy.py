"""
功能：定时结算，提交订单，期间有大概2s加载页面的时间
适用：抢购变价商品

Author: 王峥
Date: 2019-10-13
"""
from selenium import webdriver
import datetime
import time

def login():
    #扫码登陆淘宝
    browser.get("https://www.taobao.com")
    time.sleep(3)
    if browser.find_element_by_link_text("亲，请登录"):
        browser.find_element_by_link_text("亲，请登录").click()
        print("请在15s内完成扫码")
        time.sleep(15)
        browser.get("https://cart.taobao.com/cart.htm")#转到我的购物车
    #输出登陆时间
    now = datetime.datetime.now()
    print("login success", now.strftime('%Y-%m-%d %H:%M:%S'))
    time.sleep(3)

def buytime(times, choose):
    #若为单选
    if choose == 2:
        print("请手动勾选需要购买的商品")

    #若为全选
    if choose == 1:
        while True:
            try:
                if browser.find_element_by_id("J_SelectAll1"):
                    browser.find_element_by_id("J_SelectAll1").click()
                    break
            except:
                print("找不到购买按钮")

    #时间到了就结算，下订单
    while True:
        #now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        now = datetime.datetime.now()
        if now > times:
            # 点击结算按钮
            while True:
                try:
                    if browser.find_element_by_link_text("结 算"):
                        browser.find_element_by_link_text("结 算").click()
                        print(f"结算成功，准备提交订单")
                        break
                except:
                    pass
            # 点击提交订单按钮
            while True:
                try:
                    if browser.find_element_by_link_text('提交订单'):
                        browser.find_element_by_link_text('提交订单').click()
                        now = datetime.datetime.now()
                        print("buytime", now.strftime('%Y-%m-%d %H:%M:%S'))
                        print(f"抢购成功，请尽快付款")
                        break
                except:
                    print("再次尝试提交订单")

if __name__ == '__main__':
    #设置时间格式："2018-09-06 11:20:00.000000"
    #times = input("请输入抢购时间，格式如(2018-09-06 11:20:00.000000):")
    times = datetime.datetime(2019,10,15,16,20,00)

    browser = webdriver.Chrome()#使用谷歌浏览器
    browser.maximize_window()
    #登陆   
    login()
    #设置全选或者自动选择
    #choose = int(input("到时间自动勾选购物车请输入“1”，否则输入“2”："))
    choose = 2
    #定时下单
    buytime(times, choose)

