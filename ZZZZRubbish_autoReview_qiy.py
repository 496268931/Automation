# coding=utf-8
import base64
import os
import re

import datetime
from selenium import webdriver
from PIL import Image
import time

from com.aliyun.api.gateway.sdk.util import showapi

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
# driver  = webdriver.Chrome()
# driver.get("http://www.iqiyi.com/v_19rr80hvpc.html#vfrm=24-9-0-1")
driver.get("http://www.iqiyi.com/v_19rr769c4s.html#vfrm=3-2-0-0")

driver.maximize_window()
time.sleep(2)
print('wait')
# driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部
# driver.switch_to.frame('iframe')

##############################################################


# 将页面滚动条拖到底部
# js = "var q=document.body.scrollTop=100000"
js = "var q=document.documentElement.scrollTop=10000"


#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def isElementExist(element):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag


exist = True
i = 0
while exist:

    if isElementExist(
            '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea'):
        # exist=False
        print('找到评论框')
        break
    driver.execute_script(js)
    i += 1
    #print(i)

target = driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea')
driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

# 输入评论
driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea').clear()
time.sleep(2)
driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea').send_keys(
    "超级无敌喜喜欢这部剧，使劲追".decode())
# 打印评论内容
#print(driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[
# 2]/div/div[1]/div/div/div[2]/div[1]/textarea').get_attribute('value'))
# 点击评论
driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[3]/a[2]').click()
time.sleep(2)

# 点击登录
driver.find_element_by_xpath('//*[@id="widget-userregistlogin"]/span[2]/div[1]/a').click()
time.sleep(5)

# 截图验证码并进行剪裁
if isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div'):
    driver.switch_to.frame('login_frame')
    time.sleep(2)

    # 输入账号
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
                                 '2]/input').clear()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
                                 '2]/input').send_keys("15011335008")
    # 输入密码
    # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
    time.sleep(2)
    driver.find_element_by_xpath(
        '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/input[1]').send_keys(
        "my0316WY")
    # 点击登录
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/a[2]').click()
    time.sleep(6)

    while isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/img'):  # 如果存在验证码图片
        print('有验证码')

        picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                       str(datetime.datetime.now())) + '.png'
        driver.save_screenshot(picName)
        time.sleep(1)

        # 裁切图片
        img = Image.open(picName)
        region = (73, 110, 220, 160)
        cropImg = img.crop(region)

        # 保存裁切后的图片
        picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                          str(datetime.datetime.now())) + '.png'
        cropImg.save(picNameCut)
        time.sleep(2)

        # 进行验证码验证
        f = open(picNameCut, 'rb')
        b_64 = base64.b64encode(f.read())
        f.close()
        req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode",
                                     "4e5510e696c748ca8d5033dd595bfbbc")
        json_res = req.addTextPara("typeId", "3040") \
            .addTextPara("img_base64", b_64) \
            .addTextPara("convert_to_jpg", "1") \
            .post()

        # print ('1')
        # print ('json_res data is:', json_res)
        print (json_res)
        json_res
        # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

        int = json_res.find('Result')
        yanzhengma = json_res[int + 11:int + 15]
        print(yanzhengma)

        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div['
                                     '2]/div/div/div/div/input[4]').clear()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div['
                                     '2]/div/div/div/div/input[3]').clear()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div['
                                     '2]/div/div/div/div/input[2]').clear()
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div['
                                     '2]/div/div/div/div/input[1]').clear()
        time.sleep(1)

        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').send_keys(
            yanzhengma[0:1])
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').send_keys(
            yanzhengma[1:2])
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').send_keys(
            yanzhengma[2:3])
        time.sleep(1)
        driver.find_element_by_xpath(
            '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').send_keys(
            yanzhengma[3:4])
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/a[2]').click()
        time.sleep(8)
"""
    while isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/p/span'):


        if isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/p/span'):
            picName='D:\\Program Files\\python\\'+re.sub(r'[^0-9]','',str(datetime.datetime.now()))+'.png'
            driver.save_screenshot(picName)
            time.sleep(1)


            #裁切图片
            img = Image.open(picName)
            region = (73,110,220,160)
            cropImg = img.crop(region)

            #保存裁切后的图片
            picNameCut='D:\\Program Files\\python\\'+re.sub(r'[^0-9]','',str(datetime.datetime.now()))+'.png'
            cropImg.save(picNameCut)
            time.sleep(2)


            #进行验证码验证
            f=open(picNameCut,'rb')
            b_64=base64.b64encode(f.read())
            f.close()
            req=showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode","4e5510e696c748ca8d5033dd595bfbbc")
            json_res=req.addTextPara("typeId","3040") \
                .addTextPara("img_base64",b_64) \
                .addTextPara("convert_to_jpg","1") \
                .post()

            #print ('1')
            #print ('json_res data is:', json_res)
            print (json_res)
            json_res
            #str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

            int=json_res.find('Result')
            yanzhengma=json_res[int+11:int+15]
            print(yanzhengma)

            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').send_keys(yanzhengma[0:1])
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').send_keys(yanzhengma[1:2])
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').send_keys(yanzhengma[2:3])
            time.sleep(1)
            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').send_keys(yanzhengma[3:4])
            time.sleep(1)

            driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/a[2]').click()

"""

print('登录成功')
driver.switch_to_default_content()

exist1 = True
j = 0
while exist1:

    if isElementExist(
            '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea'):
        # exist=False
        print('找到评论框')
        break
    driver.execute_script(js)
    j += 1
    #print(j)

target = driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea')
driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

time.sleep(25)

# 输入评论
driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea').clear()
time.sleep(2)
driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/textarea').send_keys(
    "超级无敌喜欢这部剧，使劲追".decode())
# 打印评论内容
#print(driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[
# 2]/div/div[1]/div/div/div[2]/div[1]/textarea').get_attribute('value'))
# 点击评论
driver.find_element_by_xpath(
    '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[3]/a[2]').click()
time.sleep(2)

print('评论成功')


# driver.quit()
