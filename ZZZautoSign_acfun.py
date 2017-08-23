# -*- coding: utf-8 -*-
import base64
import os
import re
import urllib

import datetime

import urllib2

import time

from PIL import Image
from selenium import webdriver

from com.aliyun.api.gateway.sdk.util import showapi


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
    # print req  <urllib2.Request instance at 0x026B05A8>
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
     url = 'http://api.tianma168.com/tm/getPhone?ItemId=166&token=' + token + '&Code=UTF8'

    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')

    phone1 = z_data[0:11]
    return phone1
    '''

    url = 'http://api.tianma168.com/tm/getPhone?ItemId=5605&token=' + token + '&Code=UTF8'
    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    phone1 = data[0:11]
    return phone1


def getMessage(token, phone, driver):
    # MSG&【AcFun弹幕视频网】您的验证码为：926575。一起加入弹幕的世界，AC娘等你来玩哦(＾o＾)丿验证码5分钟内有效。

    url = 'http://api.tianma168.com/tm/getMessage?token=' + token + '&itemId=5605&phone=' + phone + \
          '&Code=UTF8'
    req = urllib2.Request(url)
    data = urllib2.urlopen(req).read()

    print(data)
    int = data.find('您的验证码为')
    print(int)

    if int == -1:

        print('接收验证码失败')
        time.sleep(2)
        driver.quit()


    elif int == 30:
        #int=30
        #MSG&【AcFun弹幕视频网】您的验证码为：573650。一起加入弹幕的世界，AC娘等你来玩哦(＾o＾)丿验证码5分钟内有效。[来自:1069044322656]

        yanzhengma = data.decode('UTF-8')[int - 7:int + -1]
        print(yanzhengma)


        # 输入短信验证码
        driver.find_element_by_xpath('//*[@id="ipt-mobile-code"]').send_keys(yanzhengma)
        time.sleep(2)
    else:
        #int=4
        #MSG&您的验证码为：269863。一起加入弹幕的世界，AC娘等你来玩哦(＾o＾)丿验证码5分钟内有效。【AcFun弹幕视频网】[来自:106901402656]
        yanzhengma = data.decode('UTF-8')[int + 7:int + 13]
        print(yanzhengma)


        # 输入短信验证码
        driver.find_element_by_xpath('//*[@id="ipt-mobile-code"]').send_keys(yanzhengma)
        time.sleep(2)



def addCount(token, phone):
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
    data = {'platform': 'acfun', 'accountId': phone, 'password': 'abc' + phone,
            'nickName': phone + token[:5]}
    data = urllib.urlencode(data)
    req = urllib2.Request(url, headers=headers, data=data)
    response = urllib2.urlopen(req).read()

    print(response)


def black(token, phone):
    url = 'http://api.tianma168.com/tm/addBlack?token=' + token + '&phoneList=5605-' + phone + '&Code=UTF8'
    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    z_data = data.decode('UTF-8')
    print(z_data)


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


def main():
    for num in range(1, 51):
        try:

            print(num)
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            time.sleep(2)
            driver = webdriver.Firefox()
            driver.get('http://www.acfun.cn/reg/')
            driver.maximize_window()
            time.sleep(2)

            while True:

                token = getToken()

                print(token)

                phone = getPhone(token)
                #phone = '17097517691'
                print(phone)
                print('开始注册，本次手机号为' + phone)

                # 输入手机号
                driver.find_element_by_xpath('//*[@id="ipt-mobile-reg"]').clear()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="ipt-mobile-reg"]').send_keys(phone)
                time.sleep(2)
                #点击其他输入框会显示手机号是否可用，为后面判断做准备
                driver.find_element_by_xpath('//*[@id="ipt-username-reg"]').click()
                time.sleep(2)

                if (driver.find_element_by_xpath('//*[@id="ipt-mobile-reg"]').get_attribute(
                        'class')) == 'mobile l success'.decode("utf-8"):
                    print('该手机号可用')
                    break
                print('------该手机号已注册过------')

            # 输入昵称
            driver.find_element_by_xpath('//*[@id="ipt-username-reg"]').send_keys(phone + token[:5])
            time.sleep(2)
            # if (driver.find_element_by_xpath('//*[@id="win-hint"]/div[1]').text)==None:
            #     break
            # else:
            #     driver.find_element_by_xpath('//*[@id="ipt-username-reg"]').click()
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="ipt-username-reg"]').clear()
            #     time.sleep(2)
            #     driver.find_element_by_xpath('//*[@id="ipt-username-reg"]').send_keys(token[:10])
            #     time.sleep(2)


            # 输入密码
            driver.find_element_by_xpath('//*[@id="ipt-pwd-reg"]').send_keys('abc' + phone)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="ipt-pwd-reg"]').click()
            time.sleep(2)
            # 确认密码
            driver.find_element_by_xpath('//*[@id="ipt-repwd-reg"]').send_keys('abc' + phone)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="ipt-repwd-reg"]').click()
            time.sleep(2)

            # if not isElementExist('/html/body/div[1]/div[1]/div/form/div[1]/span[2]/text()',driver):
            # print('该账号可用')
            # break





            # 点击免费获取短信动态码
            driver.find_element_by_xpath('//*[@id="send-mobile-code"]').click()
            time.sleep(2)

            i = 1
            while True:

                driver.find_element_by_xpath('//*[@id="popupCode"]').clear()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="popupCode"]').click()
                time.sleep(3)

                # 截图验证码
                picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                               str(
                                                                   datetime.datetime.now())) + '.png'
                driver.save_screenshot(picName)
                time.sleep(1)

                # 裁切图片
                img = Image.open(picName)
                region = (870, 400, 950, 440)
                cropImg = img.crop(region)

                # 保存裁切后的图片
                picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                                  str(
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

                # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

                int = json_res.find('Result')
                yanzhengma = json_res[int + 11:int + 15]
                print(yanzhengma)
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="popupCode"]').send_keys(yanzhengma)
                time.sleep(2)
                os.remove(picName)
                time.sleep(2)
                os.remove(picNameCut)
                time.sleep(2)

                # 点击确定
                driver.find_element_by_xpath(
                    '//*[@id="win-verifycode"]/div[2]/div/div[1]/a[2]').click()
                time.sleep(5)
                if not isElementExist('//*[@id="popupCode"]', driver):
                    break

                if i > 3:
                    print('已重试三次，退出')
                    driver.quit()

                i = i + 1

            time.sleep(30)

            getMessage(token, phone, driver)
            time.sleep(5)
            driver.find_element_by_xpath('//*[@id="form-reg"]/div[7]/a').click()
            time.sleep(8)

            if not isElementExist('//*[@id="form-reg"]/div[7]/a', driver):

                addCount(token, phone)
                time.sleep(1)
                print('手机号' + phone + '注册成功')
                black(token, phone)
            else:
                print('注册有误，退出')

        except Exception as e:
            print(e)

        finally:

            print('已将该号码拉入黑名单')
            print('本次注册结束')
            print('---------我是分割线------------')
            driver.quit()










            #########################


if __name__ == '__main__':
    main()
