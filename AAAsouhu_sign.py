# -*- coding: utf-8 -*-
import base64
import os
import random
import re
import urllib

import datetime
import parse
import urllib2

import time

import requests
from PIL import Image
from selenium import webdriver

from com.aliyun.api.gateway.sdk.util import showapi
#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def isElementExist(element, driver):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag

def getToken():
    '''
    python3写法
    url = "http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789&Code=UTF8"

    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')

    token = z_data[0:z_data.index('&')]
    # print(z_data)   #返回值
    # print(token)   #对返回值进行处理截取token
    return token
'''
    url = "http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789&Code=UTF8"
    req = urllib2.Request(url)
    #print req  <urllib2.Request instance at 0x026B05A8>
    res_data = urllib2.urlopen(req).read()
    token = res_data[0:res_data.index('&')]
    return token
    '''
登录token&账户余额&最大登录客户端个数&最多获取号码数&单个客户端最多获取号码数&折扣

登录后，如果在5分钟没有再次调用更新token接口，则登录token会被系统自动回收，
如果再用以前的token去访问，则会返回：Session过期，这样需重新再次登陆，使用新的token。

获取号码在20分钟内没有被用户释放，系统会强制进行释放。


注意：
    1.每一次登录的token都是不一样的,但是登录成功后的token是不变的可以一直使用，
    所以登录方法只需要调用一次获取到token即可，程序运行中请不要重复调用
    
    2.登录后，如果在10分钟没有再次用token访问其他接口信息，则登录token会被系统自动回收，
    如果再用以前的token去访问，则会返回：Session过期，这样需重新再次登陆，使用新的token。
    3.接口如有错误,或者没有登陆成功，前端都会有一个False:后面则是错误信息
    '''

def getPhone(token):
    '''
正确返回：13112345678;13698763743;13928370932;  
注意：1.如果Count数量为20，获取后，确只返回了10个号码，则证明系统已经没有 
      2.接口如有错误,或者没有获取到号码，前端都会有一个False:后面则是错误信息
      3.如果需要指定号码获取请在接口后面加上参数&Phone=指定的手机号                       
      4. 搜狐 2870                 
'''
    '''python3 写法
     url = 'http://api.tianma168.com/tm/getPhone?ItemId=2870&token=' + token + '&Code=UTF8'

    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')

    phone1 = z_data[0:11]
    return phone1
    '''

    url = 'http://api.tianma168.com/tm/getPhone?ItemId=2870&token=' + token + \
          '&notPrefix=170|171|177&Code=UTF8'
    req = urllib2.Request(url)
   # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    phone1 = data[0:11]
    return phone1



def getMessage(token, phone, driver):
    #MSG&【搜狐】我的注册验证码 764523
    url = 'http://api.tianma168.com/tm/getMessage?token=' + token + '&itemId=2870&phone=' + phone + '&Code=UTF8'
    req=urllib2.Request(url)
    data = urllib2.urlopen(req).read()

    print(data)
    int = data.find('我的注册验证码')
    #print(int)
    #print(123)
    if int == -1:

        print('接收验证码失败，该号码已拉入黑名单')

    else:
        yanzhengma = data.decode('UTF-8')[16:22]
        print(yanzhengma)



        #输入短信验证码
        driver.find_element_by_xpath('//*[@id="regForm"]/div[4]/label/span[2]/input').send_keys(yanzhengma)
        time.sleep(2)

        '''
        f = open('souhu_account.txt', 'a')
        # f.write('token:'+token)
        # f.write('\n')
        f.write(phone)
        f.write('\n')
        f.write('abc' + phone)
        f.write('\n')
        f.write('\n')
        f.close()
        time.sleep(2)
        '''






def addCount(phone):
    '''python3
    url = r'http://114.215.170.176:4000/add-account'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'}
    data = {'platform': '搜狐', 'accountId': phone, 'password': 'abc' + phone}
    data = parse.urlencode(data).encode('utf-8')
    req = urllib2.Request(url, headers=headers, data=data)
    response = urllib2.urlopen(req).read().decode('utf-8')

    print(response)
    '''
    url = r'http://114.215.170.176:4000/add-account'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'}
    data = {'platform': '搜狐', 'accountId': phone, 'password': 'abc' + phone}
    data = urllib.urlencode(data)
    req = urllib2.Request(url, headers=headers, data=data)
    response = urllib2.urlopen(req).read()

    print(response)


def black(token,phone):
    url = 'http://api.tianma168.com/tm/addBlack?token='+token+'&phoneList=2870-'+phone+'&Code=UTF8'
    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    z_data = data.decode('UTF-8')
    print(z_data)
    print('已拉入黑名单，本次注册结束')
    #data = urllib.request.urlopen(url).read()
    #z_data = data.decode('UTF-8')
    #print(z_data)


def main():
    for num in range(1, 2):
        try:

            print(num)
            print('开始注册')
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            #print('开始注册，本次手机号为' + phone)

            iplist = ['47.93.113.175:5818', '59.110.159.237:5818', '123.56.77.123:5818',
                      '123.56.76.207:5818', '123.56.72.115:5818', '123.56.154.24:5818',
                      '123.56.44.11:5818', '123.56.228.93:5818', '123.57.48.138:5818',
                      '101.200.76.126:5818']
            #proxy_ip = iplist[random.randint(0, len(iplist)-1)]
            proxy_ip = random.choice(iplist)
            ip_ip = proxy_ip.split(":")[0]
            ip_port = (proxy_ip.split(":")[1])

            if num%10 < 7:
                i = 1 #1使用代理
                print(requests.get('http://ip.chinaz.com/getip.aspx',
                                   proxies={"http":'http://'+proxy_ip}).text)
            else:
                i = 0
                print(requests.get('http://ip.chinaz.com/getip.aspx').text)

            profile = webdriver.FirefoxProfile()
            profile.set_preference('network.proxy.type', i)
            profile.set_preference('network.proxy.http', ip_ip)
            profile.set_preference('network.proxy.http_port', ip_port)  # int
            profile.update_preferences()
            driver = webdriver.Firefox(firefox_profile=profile)

            #driver = webdriver.Firefox()
            driver.get('https://passport.sohu.com/signup')
            driver.maximize_window()
            time.sleep(2)


            i = 0
            while i < 21:


                token = getToken()

                #print(token)
                time.sleep(1)

                phone = getPhone(token)
                #phone = 17088927105
                #print(phone)
                time.sleep(1)

                driver.find_element_by_xpath('//*[@id="regForm"]/div[2]/label/span[2]/input').clear()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="regForm"]/div[2]/label/span[2]/input').send_keys(phone)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="regForm"]/div[3]/label/span[2]/input').click()
                time.sleep(2)

                if not isElementExist('//*[@id="regForm"]/div[2]/div/a', driver):
                    print(phone + '该手机号可注册')
                    break
                #if not driver.find_element_by_xpath('//*[@id="regForm"]/div[2]/div').is_displayed():
                # break
                i = i+1
                if i == 20:
                    driver.quit()







            driver.find_element_by_xpath('//*[@id="regForm"]/div[3]/label/span[2]/input').clear()
            driver.find_element_by_xpath('//*[@id="regForm"]/div[3]/label/span[2]/input').send_keys(
                'abc' + phone)
            time.sleep(2)

            # 获取图片验证码
            driver.find_element_by_xpath('//*[@id="regForm"]/div[4]/label/a').click()
            time.sleep(2)
            #print('已经点击验证码')

            ######################循环输入验证码

            j = 0
            while j < 6:
                if not driver.find_element_by_xpath('/html/body/div[3]/div[2]/div['
                                            '1]/span/a/img').is_displayed():
                    print('输入正确，退出')

                    break
                #print('进入验证码')

                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/label/span/input').clear()

                picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                       str(datetime.datetime.now())) + '.png'
                driver.save_screenshot(picName)
                time.sleep(1)

                # 裁切图片
                img = Image.open(picName)
                region = (988, 337, 1116, 383)
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

                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[1]/label/span/input').send_keys(
                    yanzhengma)
                time.sleep(1)

                # 点击确认
                driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[3]/input').click()
                time.sleep(2)
                #print(i)

                os.remove(picName)
                time.sleep(2)
                os.remove(picNameCut)
                time.sleep(2)
                j = j + 1
                if j == 5:
                    driver.quit()

            #########################

            time.sleep(35)
            getMessage(token, phone, driver)
            time.sleep(2)


            #同意条款
            driver.find_element_by_xpath('//*[@id="regForm"]/div[5]/div/span/label/input').click()
            time.sleep(2)

            #注册
            driver.find_element_by_xpath('//*[@id="regForm"]/div[6]/div/span/input').click()
            time.sleep(2)

            addCount(phone)
            time.sleep(2)
            print('手机号' + phone + '注册成功')
            time.sleep(2)
            # print(phone)
            # print('abc'+phone)
            # driver.quit()
            black(token, phone)
            time.sleep(2)
        except Exception as e:
            print (e)
        finally:
            print('---------我是分割线------------')
            #driver.quit()

if __name__ == '__main__':
    main()