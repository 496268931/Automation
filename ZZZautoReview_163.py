# coding=utf-8
import base64
import datetime

import os
import re

from PIL import Image
from selenium import webdriver

import time

from com.aliyun.api.gateway.sdk.util import showapi

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Param():
    pass



def main(taskUrl, account, password, text):

    try:
        #args = Param()

        print('开始本次评论任务')
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        driver = webdriver.Firefox()
        # driver  = webdriver.Chrome()

        # driver.get("http://comment.news.163.com/news2_bbs/CPISM0FT000189FH.html")
        driver.get(taskUrl)

        driver.maximize_window()
        time.sleep(2)

        #快速登录
        driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/div[1]/div[1]/a').click()
        time.sleep(2)

        # 输入账号
        # driver.find_element_by_xpath('//*[@id="YT-normalLogin"]/div[1]/label/span[1]').clear()
        driver.find_element_by_xpath('//*[@id="quickPostLogin"]/label[1]/input').send_keys(account)
        # 输入密码
        # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="quickPostLogin"]/label[2]/input').send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="quickPostLogin"]/div/a').click()
        time.sleep(2)




        #   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        def isElementExist(element):
            flag = True

            try:
                driver.find_element_by_class_name(element)
                return flag

            except:
                flag = False
                # driver.execute_script(js)
                return flag

        while driver.find_element_by_xpath("//*[contains(@id, 'x-URS-iframe')]").is_displayed():
            print('有验证码')
            driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]"))

            picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
                datetime.datetime.now())) + '.png'
            driver.save_screenshot(picName)
            time.sleep(1)


            # 裁切图片
            img = Image.open(picName)

            #region = (985, 522, 1097, 563)
            region =(220, 245, 335, 287)
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
            # str="{\"s大家都在发howapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

            int = json_res.find('Result')
            yanzhengma = json_res[int + 11:int + 15]
            print(yanzhengma)

            time.sleep(3)
            driver.find_element_by_xpath("//input[contains(@class, 'j-inputtext cktext')]").click()
            time.sleep(3)
            driver.find_element_by_xpath("//input[contains(@class, 'j-inputtext cktext')]").clear()
            time.sleep(3)
            driver.find_element_by_xpath("//input[contains(@class, 'j-inputtext cktext')]").send_keys(
                yanzhengma)
            time.sleep(3)



            driver.find_element_by_xpath('//*[@id="dologin"]').click()
            time.sleep(8)
            os.remove(picName)
            time.sleep(2)
            os.remove(picNameCut)
            time.sleep(2)

            if not isElementExist('//*[@id="dologin"]'):
                print('验证码正确')
                break





        driver.switch_to.default_content()


        #快速登录
        driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[1]/a').click()
        time.sleep(2)

        # 输入评论
        driver.find_element_by_xpath('//*[@id="quickPostBody"]').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="quickPostBody"]').send_keys(text)
        time.sleep(2)
        # 打印评论内容
        print(driver.find_element_by_xpath('//*[@id="quickPostBody"]').get_attribute('value'))
        # 马上发表
        driver.find_element_by_xpath('//*[@id="quickPostForm"]/div/a').click()
        time.sleep(2)

        print('本次评论任务成功')


    except Exception as e:
        print('本次评论任务失败')
        print(e)
    finally:
        #print(0)
        driver.quit()





if __name__ == '__main__':
    main('http://comment.news.163.com/news2_bbs/CPMT4G4F0001899N.html', 'i493735',
         'aaafff', u'游客飘过~~~~')