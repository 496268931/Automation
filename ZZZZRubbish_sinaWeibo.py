# -*- coding: utf-8 -*-
import base64
import json
import time

import os

import datetime

import re
import weibo
from PIL import Image
from selenium import webdriver
import urllib
import urllib2

from selenium.webdriver.common.keys import Keys

from com.aliyun.api.gateway.sdk.util import showapi

def isElementExist(element, driver):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag

def getCode(driver, APP_KEY, CALLBACK_URL, username, password):

    #driver.get('https://api.weibo.com/oauth2/authorize?response_type=code&client_id=1851011061
    # &redirect_uri=https://api.weibo.com/oauth2/default.html')
    driver.get('https://api.weibo.com/oauth2/authorize?response_type=code&client_id='+APP_KEY+'&redirect_uri='+CALLBACK_URL)

    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="userId"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="userId"]').clear()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="userId"]').send_keys(username)
    time.sleep(2)

    driver.find_element_by_xpath('//*[@id="passwd"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="passwd"]').clear()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="passwd"]').send_keys(password)
    time.sleep(3)



    #while True:
    if driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/span/img').is_displayed():# 如果存在验证码图片
        i = 0
        while i < 4:
            print('有验证码')
            print(i)

            picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
            driver.save_screenshot(picName)
            time.sleep(1)

            # 裁切图片
            img = Image.open(picName)

            region = (1095, 208, 1169, 240)
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

            time.sleep(3)

            os.remove(picName)
            time.sleep(2)
            os.remove(picNameCut)
            time.sleep(2)

            driver.find_element_by_xpath(
                '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input').click()
            time.sleep(1)
            driver.find_element_by_xpath(
                '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input').clear()
            time.sleep(1)
            driver.find_element_by_xpath(
                '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input').send_keys(
                yanzhengma)
            time.sleep(3)

            #点击登录
            driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
            time.sleep(6)

            if driver.current_url == 'https://api.weibo.com/oauth2/authorize':
                print('点击授权')
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
                time.sleep(3)

            if driver.current_url.index('code=') >= 0:
                print('授权回调页返回code')
                break
            if i == 3:
                print('验证码识别次数超过三次，取消本次授权')
                break
            i = i+1
    else:
        print('没有验证码')
        #点击登录
        driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
        time.sleep(5)






    # if isElementExist('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]', driver):
    #     print('点击授权')
    #     time.sleep(2)
    #
    #     driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    #     time.sleep(3)



    # 获取页面title
    current_title = driver.title
    # 获取页面url
    current_url = driver.current_url
    print current_title
    print current_url

    code = current_url[current_url.index('code=')+5:]
    print(code)
    return code


def getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL):
    values={}
    values['client_id'] = APP_KEY
    values['client_secret'] = APP_SECRET
    values['grant_type'] = 'authorization_code'
    values['code'] = code
    values['redirect_uri'] = CALLBACK_URL
    data = urllib.urlencode(values)
    url = "https://api.weibo.com/oauth2/access_token"
    request = urllib2.Request(url, data)    #使用post方法
    # geturl = url+'?'+data
    # request = urllib2.Request(geturl) #get()方法
    response = urllib2.urlopen(request).read()
    print(response)
    response_dirctory = json.loads(response)
    #print response_dirctory
    return response_dirctory

    #{"access_token":"2.00i1J7HGHXeQBC1853323ba30a4yU_","remind_in":"145653","expires_in":145653,
    # "uid":"5606463752"}


def getWeiboContent(client, uid, i=0):

    s = client.statuses.user_timeline.get(uid = uid)
    weibocontent = s['statuses'][i]['text']
    return weibocontent

def sendWeibo(client, content, safeUrl):
    s = client.statuses.share.post(status=content + ' ' +safeUrl)
    return s

def commentWeibo(client, content, weiboId):
    s = client.comments.create.post(comment=content, id=weiboId)
    return s

def main():

    APP_KEY = '2260324575' ## 填写应用程序的信息
    APP_SECRET = 'fb8ec84988227c4cb6fd6b4f5091b7a1'
    CALLBACK_URL = 'http://vpiao.wiseweb.com.cn/authformweibo'
    #APP_KEY = '1851011061' ## 填写应用程序的信息
    #APP_SECRET = '4f46048f5c6d1bb1038a0b379bda30b8'
    #CALLBACK_URL = 'https://api.weibo.com/oauth2/default.html'
    #没有验证码的 5606463752
    #username = 'umo090751@sina.cn'
    #password = 'Y5tJl57xBg9W'
    #有验证码的
    #username = 'kva84723526@sina.cn'
    #password = 'EO1iRkiNLBPy'
    #需要授权的 爱闹的守候 5770961845
    username = 'dcu1234947@sina.cn'
    password = 'vadjnrwa1701u'
    driver = webdriver.Firefox()
    code = getCode(driver, APP_KEY, CALLBACK_URL, username, password)
    time.sleep(2)
    response = getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL )

    access_token = response['access_token']
    expires_in = float(response['expires_in'])
    print access_token
    print expires_in

    client = weibo.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    client.set_access_token(access_token, expires_in)

    print('-----------')
    #http://open.weibo.com/wiki/2/statuses/share
    #第三方分享一条链接到微博
    #sendweibo = sendWeibo(client, '支持豌豆荚','http://www.wandoujia.com/apps/com.eico.weico ')
    #print sendweibo


    print('-----------')
    #http://open.weibo.com/wiki/2/comments/create
    #对一条微博进行评论

    #commentweibo = commentWeibo(client, '支持豌豆荚', 4148645941125493)
    #print(commentweibo)

    print('-----------')
    #http://open.weibo.com/wiki/2/statuses/user_timeline
    ## 获取某个用户最新发表的微博列表
    getweibocontent = getWeiboContent(client, 5770961845)
    print getweibocontent






    #print client.statuses.update.post(status=u'通过Python SDK发微博')
    #print client.friendships.friends.bilateral.ids.get(uid = 5606463752)

def abc():
    APP_KEY = '2260324575' ## 填写应用程序的信息
    APP_SECRET = 'fb8ec84988227c4cb6fd6b4f5091b7a1'
    CALLBACK_URL = 'http://vpiao.wiseweb.com.cn/authformweibo'
    client = weibo.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    url = client.get_authorize_url()
    print url
    # # 获取URL参数code:
    # code = your.web.framework.request.get('code')
    # client = APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=CALLBACK_URL)
    # r = client.request_access_token(code)
    # access_token = r.access_token # 新浪返回的token，类似abc123xyz456
    # expires_in = r.expires_in # token过期的UNIX时间：http://zh.wikipedia.org/wiki/UNIX%E6%97%B6%E9%97%B4
    # # TODO: 在此可保存access token
    # client.set_access_token(access_token, expires_in)
if __name__ == '__main__':
    main()
