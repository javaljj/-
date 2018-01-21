#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains


cookieList=[]


#
with open("cookies.txt","r+") as f:
    fx=f.read()
    if fx !='':
        cookieList = eval(fx)


douzi=['傻比白家军，不办牌子出门带节奏？',
       '60w关注，4000多粉丝牌，很牛逼？',
       '球球你们叫你们妈卖个逼，办个卡在带节奏吧',
       '关注一下今晚白家军办白事。骚白生前也是个体面人',
       '关注一下今晚白家军办白事。骚白生前也是个体面人',
       '关注一下今晚白家军办白事。骚白生前也是个体面人',
       '关注一下今晚白家军办白事。骚白生前也是个体面人',
       ]


driver = webdriver.Chrome()
driver.get('https://www.douyu.com/911')
time.sleep(10)

for cook in cookieList:
    print(cook["name"],end=" = ")
    print(cook['value'])
    driver.add_cookie({'name' : cook["name"], 'value' : cook['value']})

# 获得cookie信息
cookie= driver.get_cookies()
#将获得cookie的信息打印
print(cookie)
# 刷新cookies shijian
with open("cookies.txt","w") as f:
    f.write(str(driver.get_cookies()))


oldDanmu = ''
while(True):
    try:
        ele = driver.find_element_by_xpath('//*[@id="js-send-msg"]/textarea')
        send = driver.find_element_by_xpath('//*[@id="js-send-msg"]/div[1]')
        # damu=r"突"*random.randint(1,20)
        index= random.randint(0,len(douzi)-1)
        damu=douzi[index]
        if(damu == oldDanmu):
            damu = damu+ str(1)
        oldDanmu = damu
        ele.send_keys(damu)
        print(damu)
        ActionChains(driver).click(send).perform()
        send = driver.find_element_by_xpath('//*[@id="js-send-msg"]/div[1]')
        print("send content" + str(send.text))
        num = send.text
        ele.clear()
        if num != '发送':
            time.sleep(int(send.text))
        print("send end...")
        print("end...")
    except:
        print("exception...")

driver.close()




