#coding=utf-8
import base64
import json
import re
import threading
import time

import os
from telnetlib import EC

import datetime

from PIL import Image
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from com.aliyun.api.gateway.sdk.util import showapi

PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


d1 = '03d61be113b3d502'
d2 = '461dcf4'

desired_caps1 = {}
desired_caps1['platformName'] = 'Android'
desired_caps1['platformVersion'] = '4.4.2'
desired_caps1['deviceName'] = d1
desired_caps1['udid'] = d1
desired_caps1['appPackage'] = 'com.sina.weibo'
desired_caps1['appActivity'] = 'com.sina.weibo.SplashActivity'
desired_caps1['unicodeKeyboard'] = 'True'
desired_caps1['resetKeyboard'] = 'True'
#desired_caps['app'] = PATH('E:\\虎啸\\appiumTest\\CalculatorSuper.apk')
# driver1 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)

desired_caps2 = {}
desired_caps2['platformName'] = 'Android'
desired_caps2['platformVersion'] = '4.4.2'
desired_caps2['deviceName'] = d2
desired_caps1['udid'] = d2
desired_caps2['appPackage'] = 'com.sina.weibo'
desired_caps2['appActivity'] = 'com.sina.weibo.SplashActivity'
desired_caps2['unicodeKeyboard'] = 'True'
desired_caps2['resetKeyboard'] = 'True'
# driver2 = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps2)


def isElementExist(element, driver):
    flag = True

    try:
        driver.find_element_by_id(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag
def sendWeibo(driver):
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)



    #登录按钮
    #WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id('com.sina.weibo:id/titleSave')).click()
    WebDriverWait(driver, 60).until(lambda x: x.find_element_by_accessibility_id('我的资料')).click()
    time.sleep(2)

    if isElementExist('com.sina.weibo:id/btn_login', driver):
        print '未登录状态'
        driver.find_element_by_id('com.sina.weibo:id/btn_login').click()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').send_keys('17018036531')
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').send_keys('asd55333')
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/bnLogin').click()
        time.sleep(10)
        if True:
            if driver.find_element_by_id('com.sina.weibo:id/iv_access_image').is_displayed():# 如果存在验证码图片
                i = 0
                while i < 6:
                    print('有验证码')
                    print(i)

                    picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
                    driver.get_screenshot_as_file(picName)
                    time.sleep(1)

                    # 裁切图片
                    img = Image.open(picName)

                    region = (120, 567, 420, 647)
                    cropImg = img.crop(region)

                    # 保存裁切后的图片
                    picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
                        datetime.datetime.now())) + '.png'
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

                    result = json.loads(str(json_res[1:-1]).replace('\\', ''))
                    yanzhengma = result['showapi_res_body']['Result']


                    print(yanzhengma)

                    time.sleep(1)

                    os.remove(picName)
                    time.sleep(1)
                    os.remove(picNameCut)
                    time.sleep(1)

                    driver.find_element_by_id('com.sina.weibo:id/et_input').click()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').clear()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').send_keys(yanzhengma)
                    time.sleep(3)

                    #点击登录
                    driver.find_element_by_name('确定').click()
                    time.sleep(5)

                    if not isElementExist('com.sina.weibo:id/iv_access_image', driver):
                        print '验证码输入正确'
                        break
    else:
        print '已登录状态'
        driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/accountContent').click()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/exitAccountContent').click()
        time.sleep(2)

        driver.find_element_by_name('确定').click()
        time.sleep(2)

        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').send_keys('17018036531')
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').send_keys('asd55333')
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/bnLogin').click()
        time.sleep(10)
        if True:
            if driver.find_element_by_id('com.sina.weibo:id/iv_access_image').is_displayed():# 如果存在验证码图片
                i = 0
                while i < 6:
                    print('有验证码')
                    print(i)

                    picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
                    driver.get_screenshot_as_file(picName)
                    time.sleep(1)

                    # 裁切图片
                    img = Image.open(picName)

                    region = (120, 567, 420, 647)
                    cropImg = img.crop(region)

                    # 保存裁切后的图片
                    picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
                        datetime.datetime.now())) + '.png'
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

                    result = json.loads(str(json_res[1:-1]).replace('\\', ''))
                    yanzhengma = result['showapi_res_body']['Result']


                    print(yanzhengma)

                    time.sleep(1)

                    os.remove(picName)
                    time.sleep(1)
                    os.remove(picNameCut)
                    time.sleep(1)

                    driver.find_element_by_id('com.sina.weibo:id/et_input').click()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').clear()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').send_keys(yanzhengma)
                    time.sleep(3)

                    #点击登录
                    driver.find_element_by_name('确定').click()
                    time.sleep(5)

                    if not isElementExist('com.sina.weibo:id/iv_access_image', driver):
                        print '验证码输入正确'
                        break


    print 123333333333333333333
    time.sleep(10)
    #WebDriverWait(driver, 30).until(lambda x: x.find_element_by_accessibility_id('打开发布面板')).click()
    driver.find_element_by_id('com.sina.weibo:id/plus_icon').click()
    time.sleep(2)
    #点击文字 发微博
    driver.find_element_by_id('com.sina.weibo:id/composer_item_text').click()
    time.sleep(3)
    print 123
    driver.find_element_by_id('com.sina.weibo:id/sv_element_container').clear()
    time.sleep(2)
    driver.find_element_by_id('com.sina.weibo:id/sv_element_container').send_keys(u'今天天气不错呢')
    time.sleep(2)
    print 123
    driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
    time.sleep(2)
    print 123456789

    driver.quit()


threads = []
t1 = threading.Thread(target=sendWeibo,args=(webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1),))
threads.append(t1)
t2 = threading.Thread(target=sendWeibo,args=(webdriver.Remote('http://localhost:4730/wd/hub', desired_caps2),))
threads.append(t2)

def main():
    # driver1 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)
    # sendWeibo(driver1)

    # print 22222222222
    # driver2 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps2)
    # sendWeibo(driver2)



    for t in threads:
        t.setDaemon(True)
        t.start()

    t.join()

    print "all over %s" % time.ctime()

if __name__ == '__main__':
    main()



