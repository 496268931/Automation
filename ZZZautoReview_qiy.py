# coding=utf-8
import base64
import os
import random
import re

import datetime

import requests
from selenium import webdriver
from PIL import Image
import time

from com.aliyun.api.gateway.sdk.util import showapi


class Param():
    pass


def main(taskUrl, accountId, password, content):
    try:
        print('开始本次评论任务')
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        '''
        iplist = ['123.56.154.24:5818', '59.110.159.237:5818', '47.93.113.175:5818',
                  '123.56.44.11:5818', '101.200.76.126:5818', '123.56.228.93:5818',
                  '123.57.48.138:5818', '123.56.72.115:5818', '123.56.77.123:5818',
                  '123.56.76.207:5818', '47.93.85.217:5818', '59.110.23.162:5818',
                  '47.92.32.50:5818', '47.91.241.124:5818']
        # proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
        proxy_ip = random.choice(iplist)
        ip_ip = proxy_ip.split(":")[0]
        ip_port = proxy_ip.split(":")[1]

        num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
        if num < 15:
            isDaili = 1  # 1使用代理
            print(requests.get('http://ip.chinaz.com/getip.aspx',
                               proxies={"http": 'http://' + proxy_ip}).text)
        else:
            isDaili = 0
            print(requests.get('http://ip.chinaz.com/getip.aspx').text)
        



        ip_ip = httpIp.split(":")[0]
        ip_port = int(httpIp.split(":")[1])


        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type', 0)
        profile.set_preference('network.proxy.http', ip_ip)
        profile.set_preference('network.proxy.http_port', ip_port)  # int
        profile.update_preferences()
        driver = webdriver.Firefox(firefox_profile=profile)
        '''
        driver = webdriver.Firefox()
        # args = Param()
        # driver  = webdriver.Chrome()
        # driver.get("http://www.iqiyi.com/v_19rr80hvpc.html#vfrm=24-9-0-1")
        driver.get(taskUrl)

        driver.maximize_window()
        time.sleep(2)
        # print('wait')
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


        i = 0
        while i < 30:


            if isElementExist('//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea') or isElementExist("//*[contains(@id, 'arguments')]"):
                # exist=False
                print('找到评论框')
                break
            driver.execute_script(js)
            i += 1
            time.sleep(2)
            print(i)


        if (driver.find_element_by_class_name('csPp_textarea').get_attribute('placeholder'))=='我来说两句...'.decode("utf-8"):
            print('进入1')

            # target = driver.find_element_by_xpath(
            #     '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea')
            # driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

            # 输入评论
            driver.find_element_by_xpath(
                '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea').clear()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea').send_keys(
                content)
            # 打印评论内容
            # print(driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[
            # 2]/div/div[1]/div/div/div[2]/div[1]/textarea').get_attribute('value'))
            # 点击评论
            driver.find_element_by_xpath(
                '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/a').click()
            time.sleep(2)

            # # 点击登录
            # driver.find_element_by_xpath(
            #     '//*[@id="widget-userregistlogin"]/span[2]/div[1]/a').click()
            # time.sleep(5)

            # 截图验证码并进行剪裁
            if isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div'):
                driver.switch_to.frame('login_frame')
                time.sleep(2)

                # 如果点击登陆之后要求扫码登录，选择点击账号密码登录
                if (driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div/div/div[6]').get_attribute(
                    'class')) == 'login-frame'.decode("utf-8"):
                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div/div/div[6]/div[2]/p/span/a[1]').click()

                # 输入账号
                driver.find_element_by_xpath(
                    '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
                    '2]/input').clear()
                time.sleep(2)
                driver.find_element_by_xpath(
                    '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
                    '2]/input').send_keys(accountId)
                # 输入密码
                # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
                time.sleep(2)
                driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div['
                                             '1]/div/div[2]/div/input[1]').send_keys(password)
                # 点击登录
                time.sleep(2)
                driver.find_element_by_xpath(
                    '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/a[2]').click()
                time.sleep(6)

                while isElementExist(
                        '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/img'):  # 如果存在验证码图片
                    print('有验证码')

                    picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
                        datetime.datetime.now())) + '.png'
                    driver.save_screenshot(picName)
                    time.sleep(1)

                    # 裁切图片
                    img = Image.open(picName)
                    # 改版前   2017-8-10之前
                    # region = (73, 110, 220, 160)
                    region = (124, 163, 284, 213)
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

                    int = json_res.find('Result')
                    yanzhengma = json_res[int + 11:int + 15]
                    print(yanzhengma)

                    time.sleep(3)
                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').click()
                    time.sleep(3)
                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').clear()
                    time.sleep(3)
                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').send_keys(
                        yanzhengma)
                    time.sleep(3)



                    driver.find_element_by_xpath(
                        '/html/body/div[2]/div[1]/div/div/div[2]/div/div/a[2]').click()
                    time.sleep(8)
                    os.remove(picName)
                    time.sleep(2)
                    os.remove(picNameCut)
                    time.sleep(2)

            print('登录成功')
            driver.switch_to_default_content()

            j = 0
            while j < 30:

                if isElementExist(
                        '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea') \
                        or isElementExist(
                    '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea'):
                    # exist=False
                    print('找到评论框')
                    break
                driver.execute_script(js)
                j += 1
                time.sleep(2)
                # print(j)

            # target = driver.find_element_by_xpath(
            #     '//*[@id="qitancommonarea"]/div[2]/div/div/div/div['
            #     '2]/div/div[1]/div/div/div[2]/div[1]/textarea')
            # driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
            #
            # time.sleep(5)
            # 输入评论
            driver.find_element_by_xpath(
                '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea').clear()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea').send_keys(
                content)
            # 打印评论内容
            # print(driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[
            # 2]/div/div[1]/div/div/div[2]/div[1]/textarea').get_attribute('value'))
            # 点击评论
            driver.find_element_by_xpath(
                '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[2]/a').click()
            time.sleep(2)

            print('本次评论任务成功')




        #之前的定位出现问题2018-01-10
        # if isElementExist('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[''2]/div[1]/textarea'):
        #     # print('进入1')
        #
        #     target = driver.find_element_by_xpath(
        #         '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea')
        #     driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        #
        #     # 输入评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea').clear()
        #     time.sleep(2)
        #     driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div['
        #                                  '2]/div/div[1]/div/div/div[2]/div[1]/textarea').send_keys(
        #         content)
        #     # 打印评论内容
        #     # print(driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[
        #     # 2]/div/div[1]/div/div/div[2]/div[1]/textarea').get_attribute('value'))
        #     # 点击评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[3]/a[2]').click()
        #     time.sleep(2)
        #
        #     # 点击登录
        #     driver.find_element_by_xpath(
        #         '//*[@id="widget-userregistlogin"]/span[2]/div[1]/a').click()
        #     time.sleep(5)
        #
        #     # 截图验证码并进行剪裁
        #     if isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div'):
        #         driver.switch_to.frame('login_frame')
        #         time.sleep(2)
        #
        #         # 如果点击登陆之后要求扫码登录，选择点击账号密码登录
        #         if (driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[6]').get_attribute(
        #             'class')) == 'login-frame'.decode("utf-8"):
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[6]/div[2]/p/span/a[1]').click()
        #
        #         # 输入账号
        #         driver.find_element_by_xpath(
        #             '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
        #             '2]/input').clear()
        #         time.sleep(2)
        #         driver.find_element_by_xpath(
        #             '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
        #             '2]/input').send_keys(accountId)
        #         # 输入密码
        #         # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
        #         time.sleep(2)
        #         driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div['
        #                                      '1]/div/div[2]/div/input[1]').send_keys(password)
        #         # 点击登录
        #         time.sleep(2)
        #         driver.find_element_by_xpath(
        #             '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/a[2]').click()
        #         time.sleep(6)
        #
        #         while isElementExist(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/img'):  # 如果存在验证码图片
        #             print('有验证码')
        #
        #             picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
        #                 datetime.datetime.now())) + '.png'
        #             driver.save_screenshot(picName)
        #             time.sleep(1)
        #
        #             # 裁切图片
        #             img = Image.open(picName)
        #             # 改版前   2017-8-10之前
        #             # region = (73, 110, 220, 160)
        #             region = (124, 163, 284, 213)
        #             cropImg = img.crop(region)
        #
        #             # 保存裁切后的图片
        #             picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
        #                 datetime.datetime.now())) + '.png'
        #             cropImg.save(picNameCut)
        #             time.sleep(2)
        #
        #             # 进行验证码验证
        #             f = open(picNameCut, 'rb')
        #             b_64 = base64.b64encode(f.read())
        #             f.close()
        #             req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode",
        #                                          "4e5510e696c748ca8d5033dd595bfbbc")
        #             json_res = req.addTextPara("typeId", "3040") \
        #                 .addTextPara("img_base64", b_64) \
        #                 .addTextPara("convert_to_jpg", "1") \
        #                 .post()
        #
        #             # print ('1')
        #             # print ('json_res data is:', json_res)
        #             print (json_res)
        #             json_res
        #             # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"
        #
        #             int = json_res.find('Result')
        #             yanzhengma = json_res[int + 11:int + 15]
        #             print(yanzhengma)
        #
        #             time.sleep(3)
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').click()
        #             time.sleep(3)
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').clear()
        #             time.sleep(3)
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').send_keys(
        #                 yanzhengma)
        #             time.sleep(3)
        #
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').clear()
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').clear()
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').clear()
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').clear()
        #             # time.sleep(1)
        #             #
        #             #
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').send_keys(yanzhengma[0:1])
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').send_keys(yanzhengma[1:2])
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').send_keys(yanzhengma[2:3])
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').send_keys(yanzhengma[3:4])
        #             # time.sleep(1)
        #
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/a[2]').click()
        #             time.sleep(8)
        #             os.remove(picName)
        #             time.sleep(2)
        #             os.remove(picNameCut)
        #             time.sleep(2)
        #
        #     print('登录成功')
        #     driver.switch_to_default_content()
        #
        #     j = 0
        #     while j < 30:
        #
        #         if isElementExist(
        #                 '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea') \
        #                 or isElementExist(
        #                     '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea'):
        #             # exist=False
        #             print('找到评论框')
        #             break
        #         driver.execute_script(js)
        #         j += 1
        #         time.sleep(2)
        #         # print(j)
        #
        #     target = driver.find_element_by_xpath(
        #         '//*[@id="qitancommonarea"]/div[2]/div/div/div/div['
        #         '2]/div/div[1]/div/div/div[2]/div[1]/textarea')
        #     driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        #
        #     time.sleep(5)
        #     # 输入评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea').clear()
        #     time.sleep(2)
        #     driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div['
        #                                  '2]/div/div[1]/div/div/div[2]/div[1]/textarea').send_keys(
        #         content)
        #     # 打印评论内容
        #     # print(driver.find_element_by_xpath('//*[@id="qitancommonarea"]/div[2]/div/div/div/div[
        #     # 2]/div/div[1]/div/div/div[2]/div[1]/textarea').get_attribute('value'))
        #     # 点击评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="qitancommonarea"]/div[2]/div/div/div/div[2]/div/div[1]/div/div/div[3]/div/div[3]/a[2]').click()
        #     time.sleep(2)
        #
        #     print('本次评论任务成功')
        #
        # else:
        #     # print('进入2')
        #     target = driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea')
        #     driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        #
        #     # 输入评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea').clear()
        #     time.sleep(2)
        #     driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea').send_keys(
        #         content)
        #     # 打印评论内容
        #     # print(driver.find_element_by_xpath('//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea').get_attribute('value'))
        #     # 点击评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[2]/div/div[2]/a').click()
        #     time.sleep(2)
        #
        #     # 点击登录
        #     driver.find_element_by_xpath(
        #         '//*[@id="widget-userregistlogin"]/span[2]/div[1]/a').click()
        #     time.sleep(5)
        #
        #     # 截图验证码并进行剪裁
        #     if isElementExist('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div'):
        #         driver.switch_to.frame('login_frame')
        #         time.sleep(2)
        #
        #         # 如果点击登陆之后要求扫码登录，选择点击账号密码登录
        #         if (driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[6]').get_attribute(
        #             'class')) == 'login-frame'.decode("utf-8"):
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[6]/div[2]/p/span/a[1]').click()
        #
        #         # 输入账号
        #         driver.find_element_by_xpath(
        #             '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
        #             '2]/input').clear()
        #         time.sleep(2)
        #         driver.find_element_by_xpath(
        #             '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[1]/div['
        #             '2]/input').send_keys(accountId)
        #         # 输入密码
        #         # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
        #         time.sleep(2)
        #         driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div['
        #                                      '1]/div/div[2]/div/input[1]').send_keys(password)
        #         # 点击登录
        #         time.sleep(2)
        #         driver.find_element_by_xpath(
        #             '/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/a[2]').click()
        #         time.sleep(6)
        #
        #         while isElementExist(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/img'):  # 如果存在验证码图片
        #             print('有验证码')
        #
        #             picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
        #                 datetime.datetime.now())) + '.png'
        #             driver.save_screenshot(picName)
        #             time.sleep(1)
        #
        #             # 裁切图片
        #             img = Image.open(picName)
        #             # 改版前   2017-8-10之前
        #             # region = (73, 110, 220, 160)
        #             region = (124, 163, 284, 213)
        #             cropImg = img.crop(region)
        #
        #             # 保存裁切后的图片
        #             picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
        #                 datetime.datetime.now())) + '.png'
        #             cropImg.save(picNameCut)
        #             time.sleep(2)
        #
        #             # 进行验证码验证
        #             f = open(picNameCut, 'rb')
        #             b_64 = base64.b64encode(f.read())
        #             f.close()
        #             req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode",
        #                                          "4e5510e696c748ca8d5033dd595bfbbc")
        #             json_res = req.addTextPara("typeId", "3040") \
        #                 .addTextPara("img_base64", b_64) \
        #                 .addTextPara("convert_to_jpg", "1") \
        #                 .post()
        #
        #             # print ('1')
        #             # print ('json_res data is:', json_res)
        #             print (json_res)
        #             json_res
        #             # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"
        #
        #             int = json_res.find('Result')
        #             yanzhengma = json_res[int + 11:int + 15]
        #             print(yanzhengma)
        #
        #             time.sleep(3)
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').click()
        #             time.sleep(3)
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').clear()
        #             time.sleep(3)
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input').send_keys(
        #                 yanzhengma)
        #             time.sleep(3)
        #
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').clear()
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').clear()
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').clear()
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').clear()
        #             # time.sleep(1)
        #             #
        #             #
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').send_keys(yanzhengma[0:1])
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').send_keys(yanzhengma[1:2])
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').send_keys(yanzhengma[2:3])
        #             # time.sleep(1)
        #             # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').send_keys(yanzhengma[3:4])
        #             # time.sleep(1)
        #
        #             driver.find_element_by_xpath(
        #                 '/html/body/div[2]/div[1]/div/div/div[2]/div/div/a[2]').click()
        #             time.sleep(8)
        #             os.remove(picName)
        #             time.sleep(2)
        #             os.remove(picNameCut)
        #             time.sleep(2)
        #
        #     print('登录成功')
        #     driver.switch_to_default_content()
        #
        #     j = 0
        #     while j < 30:
        #
        #         if isElementExist(
        #                 '//*[@id="qitancommonarea"]/div/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div[1]/div[1]/div/textarea') \
        #                 or isElementExist(
        #                     '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea'):
        #             # exist=False
        #             print('找到评论框')
        #             break
        #         driver.execute_script(js)
        #         j += 1
        #         time.sleep(2)
        #         # print(j)
        #
        #     target = driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea')
        #     driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        #
        #     time.sleep(5)
        #     # 输入评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea').clear()
        #     time.sleep(2)
        #     driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea').send_keys(
        #         content)
        #     # 打印评论内容
        #     # print(driver.find_element_by_xpath('//*[@id="arguments"]/div/div[1]/div/div/div/div[1]/div/textarea').get_attribute('value'))
        #     # 点击评论
        #     driver.find_element_by_xpath(
        #         '//*[@id="arguments"]/div/div[1]/div/div/div/div[2]/div/div[2]/a').click()
        #     time.sleep(2)
        #
        #     print('本次评论任务成功')





    except Exception as e:
        print('本次评论任务失败')
        print(e)
    finally:
        print('over')
        driver.quit()


if __name__ == '__main__':
    # http://www.iqiyi.com/v_19rr769c4s.html#vfrm=3-2-0-0
    main('http://www.iqiyi.com/v_19rrh3jnsj.html#curid=231814007_9191801d47496d7ad349a41fa4f9a4d9',
         '17156648992', 'abc17156648992',
         u'昨天七夕，真是个让人伤心欲断肠的日子','123.56.154.24:5818',0)
