# -*- coding: utf-8 -*-
import base64
import time

import os

import datetime

import re
from PIL import Image
from selenium import webdriver

#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
from com.aliyun.api.gateway.sdk.util import showapi


def isElementExist(element,driver):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag

def main(taskUrl, data_id, accountId, password, count):
    for num in range(1, int(count)+1):
        print(num)
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        js="var q=document.documentElement.scrollTop=-50"


        print('开始点赞')

        driver = webdriver.Firefox()
        driver.get(taskUrl)
        driver.maximize_window()
        time.sleep(3)

        #m = driver.find_element_by_xpath("//*[contains(@class,'c-comment-more')]").text
        #n = m.find(u'人参与')
        #i = m[2:n]


        while isElementExist("//*[contains(@class,'c-comment-more')]", driver):
            print('点击更多')
            target = driver.find_element_by_xpath("//*[contains(@class,'c-comment-more')]")
            driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

            time.sleep(3)
            if driver.find_element_by_xpath("//*[contains(@class,'close-sohu')]").is_displayed():
                print(0)
                driver.find_element_by_xpath("//*[contains(@class,'close-sohu')]").click()
            time.sleep(2)

            driver.execute_script(js)
            time.sleep(2)
            driver.find_element_by_xpath("//*[contains(@class,'c-comment-more')]").click()
            time.sleep(2)

        driver.find_element_by_xpath("//*[contains(@data-id,"+data_id+")]/div[2]/div[2]/div[2]/a[3]/i").click()
        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[1]/input').send_keys(accountId)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[2]/input').send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/div[2]/input').click()
        time.sleep(2)
        while driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[3]/img').is_displayed():
            print('有验证码')
            driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[3]/img').click()
            time.sleep(2)

            picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
                datetime.datetime.now())) + '.png'
            driver.save_screenshot(picName)
            time.sleep(1)

            # 裁切图片
            img = Image.open(picName)

            region = (955, 520, 1058, 556)
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

            f = json_res.find('Result')
            yanzhengma = json_res[f + 11:f + 15]
            print(yanzhengma)

            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[3]/input').click()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[3]/input').clear()
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[4]/div[3]/ul/li[3]/input').send_keys(yanzhengma)
            time.sleep(3)


            driver.find_element_by_xpath(
                '/html/body/div[4]/div[3]/div[2]/input').click()
            time.sleep(8)
            os.remove(picName)
            time.sleep(2)
            os.remove(picNameCut)
            time.sleep(2)
        driver.find_element_by_xpath("//*[contains(@data-id,"+data_id+")]/div[2]/div[2]/div[2]/a[3]/i").click()
        time.sleep(2)


if __name__ == '__main__':
    main('http://www.sohu.com/a/167750199_585752', '813024476', '13533234158', 'abc13533234158', '1')