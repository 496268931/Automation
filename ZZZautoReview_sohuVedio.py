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



def main(taskUrl, account, password, text):
    try:

        #args = Param()

        # driver  = webdriver.Chrome()

        print('开始本次评论任务')
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        '''
        iplist = ['47.93.113.175:5818', '59.110.159.237:5818', '123.56.77.123:5818',
                  '123.56.76.207:5818', '123.56.72.115:5818', '123.56.154.24:5818',
                  '123.56.44.11:5818', '123.56.228.93:5818', '123.57.48.138:5818',
                  '101.200.76.126:5818']
        # proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
        proxy_ip = random.choice(iplist)
        ip_ip = proxy_ip.split(":")[0]
        ip_port = proxy_ip.split(":")[1]

        num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        if num < 11:
            i = 1  # 1使用代理
            print(requests.get('http://ip.chinaz.com/getip.aspx',
                               proxies={"http": 'http://' + proxy_ip}).text)
        else:
            i = 0
            print(requests.get('http://ip.chinaz.com/getip.aspx').text)
        

        ip_ip = httpIp.split(":")[0]
        ip_port = int(httpIp.split(":")[1])

        profile = webdriver.FirefoxProfile()
        profile.set_preference('network.proxy.type', isDaili)
        profile.set_preference('network.proxy.http', ip_ip)
        profile.set_preference('network.proxy.http_port', ip_port)  # int
        profile.update_preferences()
        driver = webdriver.Firefox(firefox_profile=profile)
        '''


        driver = webdriver.Firefox()
        driver.get(taskUrl)
        driver.maximize_window()
        time.sleep(2)

        # driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部
        # driver.switch_to.frame('iframe')




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


        #点击登录
        driver.find_element_by_xpath('//*[@id="navLoginBt"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginform"]/div/div[1]/div[1]/p/input').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginform"]/div/div[1]/div[1]/p/input').send_keys(account)
        time.sleep(2)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginform"]/div/div[1]/div[2]/p/input').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="loginform"]/div/div[1]/div[2]/p/input').send_keys(password)
        time.sleep(2)
        #点击登录判断是否有验证码
        driver.find_element_by_xpath('//*[@id="loginform"]/div/div[3]/input').click()
        time.sleep(2)

        #验证码存在，判断是否可见
        while driver.find_element_by_xpath('//*[@id="verifyCode_img"]').is_displayed():
            driver.find_element_by_xpath('//*[@id="verifyCodeBox"]/div/input').clear()
            time.sleep(1)

            picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',str(datetime.datetime.now())) + '.png'
            driver.save_screenshot(picName)
            time.sleep(1)

            # 裁切图片
            img = Image.open(picName)
            region = (757, 490, 857, 524)
            cropImg = img.crop(region)

            # 保存裁切后的图片
            picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',str(datetime.datetime.now())) + '.png'
            cropImg.save(picNameCut)
            time.sleep(2)

            # 进行验证码验证
            f = open(picNameCut, 'rb')
            b_64 = base64.b64encode(f.read())
            f.close()
            req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode","4e5510e696c748ca8d5033dd595bfbbc")
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

            driver.find_element_by_xpath('//*[@id="verifyCodeBox"]/div/input').send_keys(yanzhengma)
            time.sleep(1)

            os.remove(picName)
            time.sleep(2)
            os.remove(picNameCut)
            time.sleep(2)

            #点击登录
            driver.find_element_by_xpath('//*[@id="loginform"]/div/div[3]/input').click()
            time.sleep(2)





        target = driver.find_element_by_xpath('//*[@id="commentTextarea"]')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        #输入评论内容
        driver.find_element_by_xpath('//*[@id="commentTextarea"]').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="commentTextarea"]').send_keys(text)
        time.sleep(2)


        driver.find_element_by_xpath('//*[@id="commentSubmit"]').click()
        time.sleep(2)
        print('本次评论任务成功')
        time.sleep(2)
    except Exception as e:
        print('本次评论任务失败')
        print(e)
    finally:
        print('over')
        driver.quit()





if __name__ == '__main__':
    main('https://tv.sohu.com/20180108/n600337536.shtml', '13535754749', 'abc13535754749',
         u'看无心全季，就在搜狐视频！追剧表奉上！')
