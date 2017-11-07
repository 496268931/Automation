# -*- coding: utf-8 -*-
import base64
import json
import random
import socket

from bs4 import BeautifulSoup
import time

import os

import datetime

import re

import requests
import weibo
from PIL import Image
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait

from com.aliyun.api.gateway.sdk.util import showapi


User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

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


    if isElementExist('//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/span/img', driver):
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
                    '//*[@id="outer"]/div/div[2]/form/div/div[1]/div[1]/p[3]/input').send_keys(yanzhengma)
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


def getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL):#首次添加账号获取token
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

def getToken(APP_KEY, APP_SECRET, CALLBACK_URL, platform):
    #platform = 'XX微博'
    account_info = get_account(platform)
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


    if current_expire_in < 10:#如果有效期小于五秒钟，更新token
        driver = webdriver.Firefox()
        time.sleep(10)
        code = getCode(driver, APP_KEY, CALLBACK_URL, username, password)
        print code

        response_dirctory = getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL)
        print response_dirctory
        #print type(response_dirctory)   #<type 'dict'>

        update_cookies(username, password, response_dirctory, platform)
        # print type(account_info['data']['data'])

    return access_token, expires_in


def getFreeIp():
    proxy = []
    f = open("ip.txt","w")
    for i in range(1,2):
        try:
            url = 'http://www.xicidaili.com/nn/'+str(i)
            # req = urllib2.Request(url,headers=header)
            # res = urllib2.urlopen(req).read()
            r = requests.get(url=url, headers=header).text
            soup = BeautifulSoup(r,'html.parser')
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")

                # print tds[8].contents[0]

                if tds[8].contents[0].find(u'天')>=0:
                    if int(tds[8].contents[0][0:len(tds[8].contents[0])-1])>100:
                        #ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]
                        ip_temp = tds[1].contents[0]+':'+tds[2].contents[0]
                        proxy.append(ip_temp)
                        f.write(ip_temp+'\n')


        except:
            continue

    print '代理ip抓取完毕'
    f.close()
def getSocketIP():
    #链接服务端ip和端口
    ip_port = ('121.42.227.3',3838)
    #生成一个句柄
    sk = socket.socket()
    #请求连接服务端
    sk.connect(ip_port)
    #发送数据
    sk.sendall(bytes('wiseweb\r\n'))
    proxyIP=sk.makefile().readline()
    #打印接受的数据
    print(proxyIP)
    #关闭连接
    sk.close()
    return proxyIP
def add_account(username, password, APP_KEY, APP_SECRET, CALLBACK_URL, platform, ifip=1):#ifip是否使用代理ip，1是，0否
    # accountId = '18513199891'
    # password = '1qaz2wsx'
    # platform = '微博'
    #{u'access_token': u'2.00ln3YSGzfFy9C0788e01f28cDD8JE', u'remind_in': u'2639952', u'expires_in': 2639952, u'uid': u'5770961845', u'isRealName': u'false'}
    #driver = webdriver.Firefox()
    # iplist = ['123.56.154.24:5818', '59.110.159.237:5818', '47.93.113.175:5818',
    #           '123.56.44.11:5818', '101.200.76.126:5818', '123.56.228.93:5818',
    #           '123.57.48.138:5818', '123.56.72.115:5818', '123.56.77.123:5818',
    #           '123.56.76.207:5818', '47.93.85.217:5818', '59.110.23.162:5818',
    #           '47.92.32.50:5818', '47.91.241.124:5818']

    #proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
    # proxy_ip = random.choice(iplist)
    # ip_ip = proxy_ip.split(":")[0]
    # ip_port = int(proxy_ip.split(":")[1])


    # ip_ip = iplist[num-1].split(":")[0]
    # ip_port = int(iplist[num-1].split(":")[1])
    #print iplist[num-1]


    # num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    # if num < 15:
    #     isDaili = 1  # 1使用代理
    #     print(requests.get('http://ip.chinaz.com/getip.aspx',
    #                        proxies={"http": 'http://' + proxy_ip}).text)
    # else:
    #     isDaili = 0
    #     print(requests.get('http://ip.chinaz.com/getip.aspx').text)
    #180.125.17.243



    try:
        # #故意错误，为了测试抓取免费代理
        # print requests.get('http://httpbin.org/ip',proxies={"http":'http://59.40.51.99:8010'}).text

        current_ip = getSocketIP()
        ip_ip = current_ip.split(":")[0]
        ip_port = current_ip.split(":")[1]
    except:
        # 在整个while循环之内，是我写的抓免费代理ip
        print '通过socket获取IP失败，尝试抓取免费代理IP'
        while True:
            try:
                iplist = ['59.110.159.237:5818', '101.200.76.126:5818', '123.56.228.93:5818',
                      '123.57.48.138:5818', '123.56.77.123:5818', '123.56.76.207:5818',
                      '47.93.85.217:5818', '59.110.23.162:5818', '47.92.32.50:5818', '47.91.241.124:5818'
                      ]
                getFreeIp()
                with open('ip.txt', 'r') as fff:
                    for line in fff.readlines():
                        iplist.append(line)
                print iplist
                print len(iplist)

                getIP = random.choice(iplist)
                print getIP
                ip_ip = getIP.split(":")[0]
                ip_port = getIP.split(":")[1]
                # print ip_ip
                # print ip_port

                #driver.get('http://httpbin.org/ip')
                print requests.get('http://httpbin.org/ip',proxies={"http": 'http://' + ip_ip +':' + ip_port}).text
                time.sleep(3)
                print '代理可用'
                break
            except Exception as e1:
                print '当前代理不可用，重新选择'
                continue

    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', ifip)
    profile.set_preference('network.proxy.http', ip_ip)#ip_ip
    profile.set_preference('network.proxy.http_port', int(ip_port))  # int   ip_port
    # profile.set_preference('network.proxy.user_name', 'wiseweb')
    # profile.set_preference('network.proxy.password', 'wiseweb')
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get('http://httpbin.org/ip')
    time.sleep(2)




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

def update_cookies(username, password, response_dirctory, platform):
    url = 'http://114.215.170.176:4000/update-account'
    req = requests.post(url, data={'accountId': username, 'password': password, 'platform':
        platform, 'data': json.JSONEncoder().encode(response_dirctory)})
    print req.text



def getWeiboContent(client, uid, i=0):

    s = client.statuses.user_timeline.get(uid = uid)
    weibocontent = s['statuses'][i]['text']
    return weibocontent


def sendWeibo(client, content, safeUrl):
    s = client.statuses.share.post(status=content + ' ' +safeUrl)
    return s

def commentWeibo(client, comment, rid):
    s = client.comments.create.post(comment=comment, id=rid)
    #print type(s)   #<class 'weibo.JsonDict'>
    return s

def review(APP_KEY, APP_SECRET, CALLBACK_URL, comment, rid, platform):

    # add_account('18354254831', 'pp9999', APP_KEY, APP_SECRET, CALLBACK_URL, '微博')
    # time.sleep(100)

    # plat_from = '评论微博'
    # account_info = get_account(plat_from)
    # print account_info  #<type 'dict'>
    #
    #
    # username= account_info['data']['accountId']
    # password = account_info['data']['password']
    # print username
    # print password
    #
    #
    # #print type(account_info['data']['data'])
    # if type(account_info['data']['data']) == unicode:
    #     access_token = json.loads(account_info['data']['data'])['access_token']
    #     expires_in = json.loads(account_info['data']['data'])['expires_in']
    # elif type(account_info['data']['data']) == dict:
    #     access_token = account_info['data']['data']['access_token']
    #     expires_in = account_info['data']['data']['expires_in']
    #
    #
    # print access_token
    # print expires_in
    #
    #
    # r = requests.post('https://api.weibo.com/oauth2/get_token_info', data={'access_token': access_token})
    # #print type(r.text)  #<type 'unicode'>
    # #print type(r.content)   #<type 'str'>
    # current_expire_in = json.loads(r.text)['expire_in']
    # print '剩余时间为: %d'%current_expire_in
    #
    #
    # if current_expire_in < 10:#如果有效期小于五秒钟，更新token
    #     driver = webdriver.Firefox()
    #     time.sleep(10)
    #     code = getCode(driver, APP_KEY, CALLBACK_URL, username, password)
    #     print code
    #
    #     response_dirctory = getAccessToken(code, APP_KEY, APP_SECRET, CALLBACK_URL)
    #     print response_dirctory
    #     #print type(response_dirctory)   #<type 'dict'>
    #
    #     update_cookies(username, password, response_dirctory, plat_from)
    #     # print type(account_info['data']['data'])
    print '本次使用的评论微博信息为: '
    access_token, expires_in = getToken(APP_KEY, APP_SECRET, CALLBACK_URL, platform)



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

    commentweibo = commentWeibo(client, comment, rid)
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




def getText(key, userid, content):
    url = 'http://www.tuling123.com/openapi/api'
    data = {'key':key,'info':content,'loc':'北京市中关村','userid':userid}

    x = requests.post(url=url, data=data)
    text = json.loads(x.text)['text']

    return text
def getKeyWord(content):

    url = 'http://fileload.datagrand.com:8080/ner'
    data = {'text':content,'types':'person,location,org'}

    x = requests.post(url=url, data=data)
    print x.text
    # for i in json.loads(x.text)['person']:
    #     print i
    y = json.loads(x.text, encoding='utf-8')


    # if y['person'] and y['location']:
    #     keyword = y['person'][0] + y['location'][0]
    # elif y['person'] and not(y['location']):
    #     keyword = y['person'][0]
    # elif not(y['person']) and y['location']:
    #     keyword = y['location'][0]

    j = ''
    if y['person']:
        for i in y['person']:
            j = j + i
        keyword = j
    else:
        keyword = u'空'
    # print type(keyword) #<type 'unicode'>
    # print type('提取的') #<type 'str'>
    print u'提取的关键词为: ' +keyword
    return keyword



def count(platform):
    account_info = get_account(platform)
    #print account_info  #<type 'dict'>


    username= account_info['data']['accountId']
    #password = account_info['data']['password']
    #print username
    #print password
    i = 1
    while True:

        if username == get_account(platform)['data']['accountId']:
            break
        i = i + 1
    print i
    return i




def monitorandcomment(APP_KEY, APP_SECRET, CALLBACK_URL, key, userid):



    # print yy
    # print len(yy['statuses'])
    # for i in yy['statuses']:
    #     #print i
    #     print i['text']
    #     print i['user']['screen_name']


    # content = yy['statuses'][0]['text']
    # mid = yy['statuses'][0]['mid']

    content = u'随便一个内容，为了每次启动程序就能评论'
    print content
    # print mid
    print '======================首次检测==========================='
    # print yy['statuses'][0]['user']
    # print yy['statuses'][0]['user']['screen_name']
    # print yy['statuses'][0]['user']['followers_count']

    #while True:
    text = [
        '持续关注这个话题！',
        '这个微博的内容我都好喜欢啊',
        '不！错!',
        '每天一顶~',
        '我现在只关心鹿关啥时候分',
        '非常好',
        '哇塞，还有这么厉害的电影攻略微博',
        '互联网时代，用大数据说话',
        '大数据不错，干货满满 ',
        '很认真的一篇分析',
        '虽然有一点不足，但看的出来是在认真做作品',
        '想问下博主数据来源',
        '情绪地图对于媒体人来说是福音啊',
        '期待下一篇文章！',
        '大数据让我们的距离触手可及',
        '现在不懂点大数据都不好意思跟人聊天了。。。',
        '飘过~~~~',
        '看来关注的人还挺多的',
        '有更多的干货介绍给我们么？',
        '想看赵丽颖！可爱的颖宝',
        '杨幂大军降临！',
        '我是黑客，你们赞不了我的，不信试试！',
        '咦？最新电影的实时数据你们竟然也有？厉害了',
        '点个赞',
        '有没有时尚资讯？明星衣着什么的',
        '票房和作品质量成正比',
        '大数据，比较理性，不错 ',
        '只能说还行',
        '这个曲线图做的不错',
        '只能说很扯淡',
        '还是要理性看待，以大数据为辅，但是大数据永远不能取代情感和思想',
        '少把心思花在需求，多专注作品',
        '文娱+大数据 ',
        '马一个',
        '如果不买收视率不刷流量不控评，大数据还能这么漂亮吗？',
        '这就尴尬了',
        '不想玩大数据的厨子都不是冒险家',
        '涨知识了',
        '要灵活使用大数据，它毕竟没脑子',
        '给你打call',
        '完全没想到啊',
        '真心不错',
        '戏精啊我x ',
        '喜欢这种题材',
        '微博已经没得刷了 ',
        '还是不要戏太多',
        '这流量我是服气的',
        '也是拼了',
        '对这喜欢不起来不知道为啥',
        '虽然他人品不咋地，作品还是不错的',
        '没看懂，也许是我理解能力有问题吧',
        '干货，赞',
        '随手转发正能量',
        '信息量好大，哈哈哈',
        '此事并不简单 ',
        '涨知识了',
        '厉害了',
        '瞎说什么大实话',
        '黑人问号脸',
        '现在良心做剧可不多了'

    ]
    for i in range(1, 10000000):
        # print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # try:
            print '本次使用的监测微博信息为: '
            access_token, expires_in = getToken(APP_KEY, APP_SECRET, CALLBACK_URL, '监测微博')
            y = requests.get('https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': access_token}).text


            yy = json.loads(y)
            print yy
            print yy['statuses'][0]['text']
            time.sleep(1)
            if 'error' in yy.keys():
                print yy['error']
                print '访问过于频繁，等待一小时后重试'
                time.sleep(3600)
            else:


                #'2.00rKNXXGzfFy9C49cb5f2b09MaEBVB'
                # if content == json.loads(requests.get('https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': access_token}).text)['statuses'][0]['text']:
                #print type(yy['statuses'][0]['text'])
                if content == yy['statuses'][0]['text']:
                    print '没有最新微博'

                else:

                    print '有最新微博'
                    # content = json.loads(requests.get(
                    #     'https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': access_token}).text)['statuses'][0]['text']
                    # mid = json.loads(requests.get(
                    #     'https://api.weibo.com/2/statuses/home_timeline.json', params={'access_token': access_token}).text)['statuses'][0]['mid']
                    content = yy['statuses'][0]['text']
                    mid = yy['statuses'][0]['mid']
                    # print content
                    # print mid
                    #
                    nums = count('评论微博')

                    current_platform = '评论微博'






                    for ii in range(1, nums+1):
                        print '-------第 '+str(ii)+ '次评论--------'
                        keyword = getKeyWord(content)

                        if keyword==u'空':
                            #current_text = text[random.choice([0, len(text)-1])]
                            current_text = random.choice(text)
                        else:
                            current_text = getText(key, userid, keyword)

                        print '本次评论内容为: '
                        print current_text


                        try:
                            review(APP_KEY, APP_SECRET, CALLBACK_URL, current_text, mid, current_platform)
                            print '--------本次评论成功--------'
                        except Exception as e:
                            print e
                            print '本次评论账号有问题'
                            current_platform = '评论微博备份'
                            print '用评论微博备份'
                        finally:
                            print('---------评论分界线------------')
                        time.sleep(15)

                print content
                print mid

                time.sleep(7200)

        # except Exception as e:
        #     print e
        #
        # finally:
        #     print('---------我是分割线------------')
if __name__ == '__main__':
    print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    app_key = '2260324575' ## 填写应用程序的信息
    app_secret = 'fb8ec84988227c4cb6fd6b4f5091b7a1'
    callback_url = 'http://vpiao.wiseweb.com.cn/authformweibo'

    #图灵机器人
    key = 'c572878ae4774d8f94ae14a59b39562c'
    userid = '496268931@qq.com'



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






    # add_account('18328514791', 'asd55333', app_key, app_secret, callback_url, '评论微博备份')
    #

    # f = open('weibo.txt')
    # lines = f.readlines()
    # # for line in lines:
    # #     print line
    # f.close()
    #
    # for num in range(1, 4):
    #     # try:
    #         print num
    #         print lines[num-1].split('----')[0]
    #         add_account(lines[num-1].split('----')[0], lines[num-1].split('----')[1], app_key, app_secret, callback_url, '评论微博')
    #         print '--------分割线--------'
    #         time.sleep(5)
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

    monitorandcomment(app_key, app_secret, callback_url, key, userid)
    #count('微博3')


