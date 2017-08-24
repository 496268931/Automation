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
     url = 'http://api.tianma168.com/tm/getPhone?ItemId=293&token=' + token + '&Code=UTF8'

    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')

    phone1 = z_data[0:11]
    return phone1
    '''

    url = 'http://api.tianma168.com/tm/getPhone?ItemId=293&token=' + token + '&Code=UTF8'
    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    phone1 = data[0:11]
    return phone1



def getMessage(token, phone, driver):
    #MSG&【格瓦拉】371598(格瓦拉注册动态码，请勿泄漏)，30分钟内有效；非本人或授权操作，请致电1010-1068

    url = 'http://api.tianma168.com/tm/getMessage?token=' + token + '&itemId=293&phone=' + phone + '&Code=UTF8'
    req=urllib2.Request(url)
    data = urllib2.urlopen(req).read()


    print(data)
    int = data.find('格瓦拉')
    #print(int)

    if int == -1:


        print('接收验证码失败，该号码已拉入黑名单')

    else:

        yanzhengma = data.decode('UTF-8')[int + 2:int + 8]
        #print(yanzhengma)


        #输入短信验证码
        driver.find_element_by_xpath('//*[@id="phoneLogin_content"]/div['
                                     '3]/label/label').send_keys(yanzhengma)
        time.sleep(2)
        #输入密码
        driver.find_element_by_xpath('//*[@id="phoneLogin_content"]/div[4]/label/label').send_keys(
            'abc'+phone)
        time.sleep(2)
        #确认密码
        driver.find_element_by_xpath('//*[@id="phoneLogin_content"]/div[5]/label/label').send_keys('abc'+phone)


        time.sleep(2)







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
    data = {'platform': '格瓦拉', 'accountId': phone, 'password': 'abc' + phone}
    data = urllib.urlencode(data)
    req = urllib2.Request(url, headers=headers, data=data)
    response = urllib2.urlopen(req).read()

    print(response)


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


# class Param():
#     driver = webdriver.Firefox()

def black(token, phone):
    url = 'http://api.tianma168.com/tm/addBlack?token=' + token + '&phoneList=293-' + phone + '&Code=UTF8'
    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    z_data = data.decode('UTF-8')
    print(z_data)

def main():
    for num in range(1, 2):
        try:
            print(num)
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            driver = webdriver.Firefox()
            driver.get('http://www.gewara.com/register.xhtml')
            driver.maximize_window()
            time.sleep(2)

            #args = Param()



            #输入手机号
            #driver.find_element_by_xpath('//*[@id="phoneLogin_content"]/div[1]/label/label').send_keys(
            # phone)

            ######################循环输入验证码
            #exist = True
            #i = 1
            #while exist:
            #print('进入手机号和图片验证码')
            time.sleep(2)

            token = getToken()

            #print(token)

            phone = getPhone(token)
            #phone = 17088927105
            print(phone)



            #输入手机号
            driver.find_element_by_xpath('//*[@id="mobile"]').send_keys(phone)
            time.sleep(2)

            i = 0
            while i < 11:
                driver.find_element_by_xpath('//*[@id="captchaMobileInput"]').clear()

                picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '',
                                                   str(datetime.datetime.now())) + '.png'
                driver.save_screenshot(picName)
                time.sleep(1)

                # 裁切图片
                img = Image.open(picName)
                region = (920, 168, 1000, 208)
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

            # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

                int = json_res.find('Result')
                yanzhengma = json_res[int + 11:int + 15]
                print(yanzhengma)


                driver.find_element_by_xpath('//*[@id="captchaMobileInput"]').send_keys(yanzhengma)

                time.sleep(1)

                os.remove(picName)
                time.sleep(1)
                os.remove(picNameCut)
                time.sleep(1)
                i = i+1

                # 点击获取短信验证码
                driver.find_element_by_xpath('//*[@id="sendDTPassword"]').click()
                time.sleep(1)

                if not isElementExist('//*[@id="phoneLogin_content"]/div[1]/div[2]', driver):
                    print('验证码正确')
                    break
                if i == 10:
                    print ('验证码判断超过十次，退出')
                    driver.quit()

            #print('当前尝试次数：'+i)
            #首次打开网页时 元素不存在， 手机号或验证码输错一次就存在了，但是如果输入正确，变成存在不可现




            if (driver.find_element_by_xpath('//*[@id="sendDTPassword"]').text).__contains__('秒后重新获取'.decode("utf-8")):
                print('手机号和图片验证码输入正确，点击获取验证码')
                time.sleep(30)
                getMessage(token, phone, driver)
                time.sleep(3)
                driver.find_element_by_xpath('//*[@id="sbmit"]').click()
                time.sleep(3)
                if not isElementExist('//*[@id="sbmit"]', driver):

                    addCount(phone)
                    time.sleep(2)
                    print('手机号' + phone + '注册成功')
                    #black(token, phone)
                    #print('已将该号码拉入黑名单')
                # f = open('gewala_account.txt', 'a')
                # # f.write('token:'+token)
                # # f.write('\n')
                # f.write(phone)
                # f.write('\n')
                # f.write('abc' + phone)
                # f.write('\n')
                # f.write('\n')
                # f.close()




            else:
                print('该手机号已注册过')




        except Exception as e:
            print(e)

        finally:

            print('本次注册结束')
            print('---------我是分割线------------')
            driver.quit()






        #########################



if __name__ == '__main__':
    main()




