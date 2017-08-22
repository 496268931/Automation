# -*- coding: utf-8 -*
import base64
import os
import re
import time

import datetime

from PIL import Image
from selenium import webdriver

from com.aliyun.api.gateway.sdk.util import showapi
import sys
reload(sys)
sys.setdefaultencoding('utf8')
class Param():
    pass



def main(taskUrl, account, password, text):
    try:
        #args = Param()

        print('开始本次评论任务')
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        driver = webdriver.Firefox()
        driver.get(taskUrl)

        driver.maximize_window()
        time.sleep(2)


        # 点击登录
        driver.find_element_by_xpath('//*[@id="global_check_login"]/div/a[1]').click()
        time.sleep(5)
        #输入账号
        driver.find_element_by_xpath('//*[@id="loginname"]').send_keys(account)
        time.sleep(2)
        #输入密码
        driver.find_element_by_xpath('//*[@id="loginpassword"]').send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="dialogLoginCaptchaInput"]').click()

        ################验证码
        picName=os.path.abspath('.')+'\\'+re.sub(r'[^0-9]','',str(datetime.datetime.now()))+'.png'
        driver.save_screenshot(picName)
        time.sleep(1)


        #裁切图片
        img = Image.open(picName)
        region = (1070, 480, 1150, 515)
        cropImg = img.crop(region)

        #保存裁切后的图片
        picNameCut=os.path.abspath('.')+'\\'+re.sub(r'[^0-9]','',str(datetime.datetime.now()))+'.png'
        cropImg.save(picNameCut)
        time.sleep(2)


        #进行验证码验证
        f=open(picNameCut,'rb')
        b_64=base64.b64encode(f.read())
        f.close()
        req=showapi.ShowapiRequest(  "http://ali-checkcode.showapi.com/checkcode","4e5510e696c748ca8d5033dd595bfbbc"   )
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

        driver.find_element_by_xpath('//*[@id="dialogLoginCaptchaInput"]').send_keys(yanzhengma)
        time.sleep(1)
        ################验证码
        #点击登录
        driver.find_element_by_xpath('//*[@id="eventAccount"]/form/div[5]/input').click()
        time.sleep(2)

        target = driver.find_element_by_xpath('//*[@id="s_ui_walaList"]/div/div[1]/img')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        time.sleep(3)
        #点击输入框
        driver.find_element_by_xpath('//*[@id="wala_off"]/div/div[2]/div/div[1]/p').click()
        time.sleep(2)
        #点击评分   有10个等级
        driver.find_element_by_xpath('//*[@id="10"]').click()
        time.sleep(2)
        #输入标题
        driver.find_element_by_xpath('//*[@id="walaTitle"]').send_keys(text)
        time.sleep(2)


        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="publish"]/div[2]/div[1]/div[6]/div/div[2]/iframe'))
        driver.find_element_by_xpath('/html/body').click()
        time.sleep(2)


        #输入评论内容
        driver.find_element_by_xpath('/html/body').send_keys(text)
        time.sleep(2)
        driver.find_element_by_xpath('/html/body').get_attribute('value')
        time.sleep(1)
        driver.switch_to_default_content()
        time.sleep(2)

        #点击发布
        driver.find_element_by_xpath('//*[@id="publish"]/div[2]/div[2]/a').click()
        time.sleep(2)

        print('本次评论任务成功')


    except Exception as e:
        print(e)
        print('本次评论任务失败')
    finally:
        #print(e)
        driver.quit()



if __name__ == '__main__':
    main('http://www.gewara.com/movie/315849910', '17031511791', 'abc17031511791',
         u'像吴京这样努力的人，必然会成功的')
