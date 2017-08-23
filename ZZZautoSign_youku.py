# -*- coding: utf-8 -*-
import random
import time

import requests
import selenium
from selenium import webdriver

import urllib
import urllib2

from selenium.common.exceptions import TimeoutException

js = "var q=document.documentElement.scrollTop=10000"


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


loginURL = 'http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789&Code=UTF8'


def get(url):
    '''python3
    url = url + '&Code=UTF8'
    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')
    print(z_data)
    # return z_data
    '''
    url = url + '&Code=UTF8'
    req = urllib2.Request(url)
    # print req  <urllib2.Request instance at 0x026B05A8>
    res_data = urllib2.urlopen(req).read()
    print(res_data)

def getToken():
    '''python3
    url = "http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789&Code=UTF8"
    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')
    token = z_data[0:z_data.index('&')]
    # print(z_data)   #返回值
    # print(token)   #对返回值进行处理截取token
    return token

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
    url = "http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789&Code=UTF8"
    req = urllib2.Request(url)
    # print req  <urllib2.Request instance at 0x026B05A8>
    res_data = urllib2.urlopen(req).read()
    token = res_data[0:res_data.index('&')]
    return token

def refreshToken():  # 没啥用，每次调用getToken（）都会重新获取
    get('http://api.tianma168.com/tm/updateTime?token=' + getToken())


def getItems():
    # 优酷土豆注册项目id   759
    get('http://api.tianma168.com/TM/GetItems?token=' + getToken() + '&tp=ut')


def getPhone(token):
    '''python3
正确返回：13112345678;13698763743;13928370932;
注意：1.如果Count数量为20，获取后，确只返回了10个号码，则证明系统已经没有
      2.接口如有错误,或者没有获取到号码，前端都会有一个False:后面则是错误信息
      3.如果需要指定号码获取请在接口后面加上参数&Phone=指定的手机号

    # get('http://api.tianma168.com/tm/getPhone?&ItemId=759&token='+getToken())
    url = 'http://api.tianma168.com/tm/getPhone?ItemId=759&token=' + token + '&notPrefix=170&Code=UTF8'
    data = urllib.request.urlopen(url).read()
    z_data = data.decode('UTF-8')
    phone1 = z_data[0:11]
    return phone1
'''
    url = 'http://api.tianma168.com/tm/getPhone?ItemId=759&token=' + token + '&notPrefix=170&Code=UTF8'
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req).read()
    phone1 = res_data[0:11]
    return phone1

def getMessage(token,phone,driver):
    url = 'http://api.tianma168.com/tm/getMessage?token=' + token + '&itemId=759&phone=' + phone + '&Code=UTF8'
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req).read()


    #data = urllib.request.urlopen(url).read() python3
    #z_data = data.decode('UTF-8')             python3
    print(res_data)




    int = res_data.find('短信验证码是')
    if int == -1:
        #black(token,phone)
        print('接收验证码失败')
    else:

        yanzhengma = res_data.decode('UTF-8')[int - 10:int - 4]
        #print(yanzhengma)

        # 输入验证码
        driver.find_element_by_xpath('//*[@id="YT-mValidateCode"]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="YT-mValidateCode"]').send_keys(yanzhengma)
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="YT-loginFrameTitle"]').click()
        time.sleep(2)
        # 点击注册
        driver.find_element_by_xpath('//*[@id="YT-mRegSubmit"]').click()
        time.sleep(10)
        if driver.find_element_by_xpath('//*[@id="YT-regFrame-main"]/div[1]/div[3]').is_displayed():
            print('该账号已注册过或验证码有问题，本次注册失败')
        else:
            '''
            f = open('youku_account.txt', 'a')
            # f.write('token:'+token)
            # f.write('\n')
            f.write(phone)
            f.write('\n')
            f.write('abc' + phone)
            f.write('\n')
            f.write('\n')
            f.close()
            '''

            time.sleep(3)
            #nickName=driver.find_element_by_xpath('//*[@id="uerCenter"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/a[1]').text

            addCount(phone)

            print('手机号' + phone + '注册成功,本次注册结束')
            black(token,phone)
            # print(phone)
            # print('abc'+phone)
            # driver.quit()


def addCount(phone):

    url = r'http://114.215.170.176:4000/add-account'
    headers = {
        'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
        'Connection': 'keep-alive'}
    data = {'platform': '优酷', 'accountId': phone, 'password': 'abc' + phone}
    data = urllib.urlencode(data)
    req = urllib2.Request(url, headers=headers, data=data)
    response = urllib2.urlopen(req).read()
    print(response)
    '''python3
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, headers=headers, data=data)
    response = request.urlopen(req).read().decode('utf-8')
    print(response)
    '''
def black(token,phone):
    url = 'http://api.tianma168.com/tm/addBlack?token='+token+'&phoneList=759-'+phone+'&Code=UTF8'

    #data = urllib.request.urlopen(url).read()  python3
    #z_data = data.decode('UTF-8')              python3

    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    z_data = data.decode('UTF-8')
    print(z_data)
    print('已将该号码拉入黑名单')

def main():
    for num in range(1, 401):
        try:
            print(num)
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


            iplist = ['47.93.113.175:5818', '59.110.159.237:5818', '123.56.77.123:5818',
                      '123.56.76.207:5818', '123.56.72.115:5818', '123.56.154.24:5818',
                      '123.56.44.11:5818', '123.56.228.93:5818', '123.57.48.138:5818',
                      '101.200.76.126:5818']
            #proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
            proxy_ip = random.choice(iplist)
            ip_ip = proxy_ip.split(":")[0]
            ip_port = int(proxy_ip.split(":")[1])

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

            driver.get('http://www.youku.com/')
            driver.maximize_window()
            time.sleep(2)





            token = getToken()

            # print(token)

            phone = getPhone(token)

            # print(phone)

            # print('开始注册')

            print('开始注册，本次手机号为' + phone)



            # 点击注册
            driver.find_element_by_xpath('//*[@id="qheader_reg"]').click()
            time.sleep(2)

            # 输入手机号
            driver.find_element_by_xpath('//*[@id="YT-mPassport"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-mPassport"]').send_keys(phone)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-loginFrameTitle"]').click()
            time.sleep(1)

            # 输入密码
            driver.find_element_by_xpath('//*[@id="YT-mRegPassword"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-mRegPassword"]').send_keys('abc' + phone)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-loginFrameTitle"]').click()
            time.sleep(1)

            # 确认密码
            driver.find_element_by_xpath('//*[@id="YT-mRepeatPwd"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-mRepeatPwd"]').send_keys('abc' + phone)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-loginFrameTitle"]').click()
            time.sleep(1)

            # 点击获取验证码
            driver.find_element_by_xpath('//*[@id="YT-mGetMobileCode"]').click()

            # print('等待20s')
            time.sleep(30)
            # print('等待结束')

            getMessage(token, phone, driver)
            # print(message)

            time.sleep(2)

        except selenium.common.exceptions.TimeoutException as e1:
            print('超时', e1)


        except Exception as e:
            print(e)

        finally:
            print('---------我是分割线------------')
            driver.quit()

if __name__ == '__main__':
    main()
