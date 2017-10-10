# -*- coding: utf-8 -*-
import base64
import json
import random
import time

import os

import datetime

import re

import requests
import weibo
from PIL import Image
from selenium import webdriver
import urllib
import urllib2

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

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

    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="userId"]')).click()
    #driver.find_element_by_xpath('//*[@id="userId"]').click()
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
    time.sleep(2)

    #点击登录
    driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    time.sleep(8)

    if driver.current_url == 'https://api.weibo.com/oauth2/authorize':
        print('点击授权')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
        time.sleep(4)



    if driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/span/img').is_displayed():# 如果存在验证码图片
        i = 0
        while i < 6:
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

            result = json.loads(str(json_res[1:-1]).replace('\\', ''))
            yanzhengma = result['showapi_res_body']['Result']


            print(yanzhengma)

            time.sleep(1)

            os.remove(picName)
            time.sleep(1)
            os.remove(picNameCut)
            time.sleep(1)

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
            time.sleep(8)

            if driver.current_url == 'https://api.weibo.com/oauth2/authorize':
                print('点击授权')
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
                time.sleep(4)

            if driver.current_url.find('code=') >= 0:
                print('授权回调页返回code')
                break
            if i == 5:
                print('验证码识别次数超过三次，取消本次授权')
                break
            i = i+1
    # else:
    #     print('没有验证码')
    #     #点击登录
    #
    #     driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    #     time.sleep(8)
    #     if driver.current_url == 'https://api.weibo.com/oauth2/authorize':
    #         print('点击授权')
    #         time.sleep(1)
    #         driver.find_element_by_xpath('//*[@id="outer"]/div/div[2]/form/div/div[2]/div/p/a[1]').click()
    #         time.sleep(4)




    # 获取页面title
    current_title = driver.title
    # 获取页面url
    current_url = driver.current_url
    print current_title
    print current_url

    code = current_url[current_url.index('code=')+5:]

    return code


def getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL):
    values = {'client_id': APP_KEY, 'client_secret': APP_SECRET, 'grant_type': 'authorization_code',
              'code': code, 'redirect_uri': CALLBACK_URL}
    # data = urllib.urlencode(values)
    # url = "https://api.weibo.com/oauth2/access_token"
    # request = urllib2.Request(url, data)    #使用post方法
    # # geturl = url+'?'+data
    # # request = urllib2.Request(geturl) #get()方法
    # response = urllib2.urlopen(request).read()
    # print(response)
    # response_dirctory = json.loads(response)
    # #print


    url = "https://api.weibo.com/oauth2/access_token"
    res = requests.post(url, data=values)
    response_dirctory = json.loads(res.text)


    return response_dirctory

    #{"access_token":"2.00i1J7HGHXeQBC1853323ba30a4yU_","remind_in":"145653","expires_in":145653,
    # "uid":"5606463752"}

def add_account(username, password, APP_KEY, APP_SECRET, CALLBACK_URL, platform, num):
    # accountId = '18513199891'
    # password = '1qaz2wsx'
    # platform = '微博'
    #{u'access_token': u'2.00ln3YSGzfFy9C0788e01f28cDD8JE', u'remind_in': u'2639952', u'expires_in': 2639952, u'uid': u'5770961845', u'isRealName': u'false'}
    #driver = webdriver.Firefox()
    iplist = ['123.56.154.24:5818', '59.110.159.237:5818', '47.93.113.175:5818',
              '123.56.44.11:5818', '101.200.76.126:5818', '123.56.228.93:5818',
              '123.57.48.138:5818', '123.56.72.115:5818', '123.56.77.123:5818',
              '123.56.76.207:5818', '47.93.85.217:5818', '59.110.23.162:5818',
              '47.92.32.50:5818', '47.91.241.124:5818']
    #proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
    proxy_ip = random.choice(iplist)
    # ip_ip = proxy_ip.split(":")[0]
    # ip_port = int(proxy_ip.split(":")[1])


    ip_ip = iplist[num-1].split(":")[0]
    ip_port = int(iplist[num-1].split(":")[1])
    print iplist[num-1]


    # num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    # if num < 15:
    #     isDaili = 1  # 1使用代理
    #     print(requests.get('http://ip.chinaz.com/getip.aspx',
    #                        proxies={"http": 'http://' + proxy_ip}).text)
    # else:
    #     isDaili = 0
    #     print(requests.get('http://ip.chinaz.com/getip.aspx').text)

    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 0)
    profile.set_preference('network.proxy.http', ip_ip)
    profile.set_preference('network.proxy.http_port', ip_port)  # int
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile)


    driver.get('http://httpbin.org/ip')
    time.sleep(3)
    code = getCode(driver, APP_KEY, CALLBACK_URL, username, password)
    print code

    response_dirctory = getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL)
    print response_dirctory

    driver.quit()
    time.sleep(2)


    response_str = json.JSONEncoder().encode(response_dirctory) #dict转str
    #print type(response_str)  #str
    #print response_str
    url ='http://114.215.170.176:4000/add-account'
    data = {'accountId': username, 'password': password, "platform": platform, 'data': response_str}
    s=requests.post(url, data=data)
    print s.text
def get_account(platform):
    url = 'http://114.215.170.176:4000/get-account'
    req = requests.get(url, params = {'platform': platform})  #json字符串

    #print type(req.text) #<type 'unicode'>
    r = json.JSONDecoder().decode(req.text)   #将获取的结果转成dict   #<type 'dict'>

    return r

def update_cookies(username, password, response_dirctory):
    url = 'http://114.215.170.176:4000/update-account'
    req = requests.post(url, data={'accountId': username, 'password': password, 'platform':
        '微博', 'data': json.JSONEncoder().encode(response_dirctory)})
    print req.text



def getWeiboContent(client, uid, i=0):

    s = client.statuses.user_timeline.get(uid = uid)
    weibocontent = s['statuses'][i]['text']
    return weibocontent


def sendWeibo(client, content, safeUrl):
    s = client.statuses.share.post(status=content + ' ' +safeUrl)
    return s

def commentWeibo(client, content, mid):
    s = client.comments.create.post(comment=content, id=mid)
    #print type(s)   #<class 'weibo.JsonDict'>
    return s

def main(APP_KEY, APP_SECRET, CALLBACK_URL, text, mid):

    # add_account('18354254831', 'pp9999', APP_KEY, APP_SECRET, CALLBACK_URL, '微博')
    # time.sleep(100)


    account_info = get_account('微博3')
    print account_info  #<type 'dict'>


    username= account_info['data']['accountId']
    password = account_info['data']['password']
    print username
    print password


    #print type(account_info['data']['data'])
    if type(account_info['data']['data']) == unicode:
        access_token = json.loads(account_info['data']['data'])['access_token']
        expires_in = json.loads(account_info['data']['data'])['expires_in']
    elif type(account_info['data']['data']) == dict:
        access_token = account_info['data']['data']['access_token']
        expires_in = account_info['data']['data']['expires_in']


    print access_token
    print expires_in


    r = requests.post('https://api.weibo.com/oauth2/get_token_info', data={'access_token': access_token})
    #print type(r.text)  #<type 'unicode'>
    #print type(r.content)   #<type 'str'>
    current_expire_in = json.loads(r.text)['expire_in']
    print '剩余时间为: %d'%current_expire_in

    if current_expire_in < 5:#如果有效期小于五秒钟，更新token
        driver = webdriver.Firefox()

        code = getCode(driver, APP_KEY, CALLBACK_URL, username, password)
        print code

        response_dirctory = getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL )
        print response_dirctory
        #print type(response_dirctory)   #<type 'dict'>

        update_cookies(username, password, response_dirctory)
        # print type(account_info['data']['data'])





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

    commentweibo = commentWeibo(client, text, mid)
    print commentweibo

    print('-----------')
    #http://open.weibo.com/wiki/2/statuses/user_timeline
    # # 获取某个用户最新发表的微博列表
    # getweibocontent = getWeiboContent(client, 5770961845)
    # print getweibocontent

    print('-----------')
    #http://open.weibo.com/wiki/2/users/show
    #获取用户信息
    #userInfo = getuserInfo(client)
    #print userInfo





    #print client.statuses.update.post(status=u'通过Python SDK发微博')
    #print client.friendships.friends.bilateral.ids.get(uid = 5606463752)


if __name__ == '__main__':
    print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    app_key = '2260324575' ## 填写应用程序的信息
    app_secret = 'fb8ec84988227c4cb6fd6b4f5091b7a1'
    callback_url = 'http://vpiao.wiseweb.com.cn/authformweibo'
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
    # username = 'dcu1234947@sina.cn'
    # password = 'vadjnrwa1701u'


    # f = open('weibo.txt')
    # lines = f.readlines()
    # # for line in lines:
    # #     print line
    # f.close()

    # for num in range(1, 6):
    #     # try:
    #         print num
    #         print lines[num-1].split('----')[0]
    #         add_account(lines[num-1].split('----')[0], lines[num-1].split('----')[1], app_key,
    #                     app_secret,
    #                     callback_url, '微博3', num)
    #         print '--------分割线--------'
    #         time.sleep(600)
    #     # except Exception as e:
    #     #     print e



    #接口调用频率
    # r = requests.get('https://api.weibo.com/2/account/rate_limit_status.json', params={
    #     'access_token': '2.00vpMElGzfFy9C90c1fef3c9Zvk3KB'})
    # print r.text




    # x = requests.get('https://api.weibo.com/2/users/show.json', params={'access_token':
    #                                                                         '2.00KtMXXGzfFy9C477e3f8f4eYjf1aC', 'screen_name': '阚掘聪烧八将'}).text
    #
    # xx = json.loads(x)
    # print xx
    # print xx['status']
    # print xx['status']['text']
    #
    #
    # print '----------------------'
    y = requests.get('https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': '2.00rKNXXGzfFy9C49cb5f2b09MaEBVB'}).text
    yy = json.loads(y)


    # print yy
    # print len(yy['statuses'])
    # for i in yy['statuses']:
    #     #print i
    #     print i['text']
    #     print i['user']['screen_name']

    content = yy['statuses'][0]['text']
    mid = yy['statuses'][0]['mid']
    print content
    print mid
    print '======================首次检测==========================='
    # print yy['statuses'][0]['user']
    # print yy['statuses'][0]['user']['screen_name']
    # print yy['statuses'][0]['user']['followers_count']


    text = '全是鹿晗体'

    while True:
        if content == json.loads(requests.get(
                'https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': '2.00rKNXXGzfFy9C49cb5f2b09MaEBVB'}).text)['statuses'][0]['text']:
            print '没有最新微博'

        else:

            print '有最新微博'
            content = json.loads(requests.get(
                'https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': '2.00rKNXXGzfFy9C49cb5f2b09MaEBVB'}).text)['statuses'][0]['text']
            mid = json.loads(requests.get(
                'https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': '2.00rKNXXGzfFy9C49cb5f2b09MaEBVB'}).text)['statuses'][0]['mid']

            main(app_key, app_secret, callback_url, text, mid)




        print content
        print mid
        print '----分割线----'
        time.sleep(30)