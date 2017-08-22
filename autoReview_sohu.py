# coding=utf-8
import base64
import os
import re

import datetime
from selenium import webdriver
from PIL import Image
import time

from com.aliyun.api.gateway.sdk.util import showapi

driver = webdriver.Firefox()
# driver  = webdriver.Chrome()

# driver.get("http://news.sohu.com/20170717/n502205097.shtml")
#driver.get("http://www.sohu.com/a/158321994_162702?loc=1&focus_pic=0")
driver.get("http://www.sohu.com/a/160145302_467279")

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


'''
exist=True
i=0
while exist:

    if isElementExist('//*[@id="mpbox"]/div[2]/div/div[1]/textarea'):#找到输入框
        #exist=False
        print('找到输入框')
        break

    target = driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[1]/textarea')
    driver.execute_script("arguments[0].scrollIntoView();", target) #拖动到可见的元素去
    time.sleep(1)
    i+=1
    print(i)
'''
target = driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[1]/textarea')
driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
# 点击登录按钮
driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[3]').click()
time.sleep(2)
# 点击微博登录
driver.find_element_by_xpath('/html/body/div[4]/div[4]/ul/li[2]/a').click()
time.sleep(2)

# 获取当前窗口句柄
ch = driver.current_window_handle
time.sleep(2)
# 获取所有窗口句柄
wh = driver.window_handles

# 在所有窗口中查找弹出窗口
for line in wh:
    if line != ch:
        driver.switch_to_window(line)
        time.sleep(2)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="userId"]').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="userId"]').send_keys("mkt45196@sina.cn")
        #driver.find_element_by_xpath('//*[@id="userId"]').send_keys("zzs3634344@sina.cn")
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="passwd"]').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("faCTpTN5ukQy")
        #driver.find_element_by_xpath('//*[@id="passwd"]').send_keys("7B83Od9c9UOB")
        time.sleep(2)

        if driver.find_element_by_xpath(
                '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input').is_displayed():  # 判断是否有验证码
            picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                           str(datetime.datetime.now())) + '.png'
            driver.save_screenshot(picName)
            time.sleep(1)

            # 裁切图片
            img = Image.open(picName)
            region = (1096, 207, 1171, 238)
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
            json_res = req.addTextPara("typeId", "3050") \
                .addTextPara("img_base64", b_64) \
                .addTextPara("convert_to_jpg", "1") \
                .post()

            # print ('1')
            # print ('json_res data is:', json_res)
            print (json_res)
            json_res
            # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

            int = json_res.find('Result')
            yanzhengma = json_res[int + 11:int + 16]
            print(yanzhengma)

            driver.find_element_by_xpath(
                '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input').send_keys(
                yanzhengma)
            time.sleep(1)

        # 点击登录
        driver.find_element_by_xpath(
            '//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
        time.sleep(2)

        if isElementExist('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]'):
            # 点击授权
            driver.find_element_by_xpath(
                '//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
            time.sleep(2)

# driver.switch_to_window(ch)




target = driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[1]/textarea')
driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
print('找到评论输入框')
driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[1]/textarea').clear()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[1]/textarea').send_keys(
    u'文章讲的非常好，就是要紧跟时尚，享受生活')
time.sleep(2)

driver.find_element_by_xpath('//*[@id="mpbox"]/div[2]/div/div[3]').click()

print('end')


# driver.quit()
