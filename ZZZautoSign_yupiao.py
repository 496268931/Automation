# -*- coding: utf-8 -*-
import urllib
import urllib2
import time


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains


def getToken():
    url = "http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789&Code=UTF8"
    req = urllib2.Request(url)
    # print req  <urllib2.Request instance at 0x026B05A8>
    res_data = urllib2.urlopen(req).read()
    token = res_data[0:res_data.index('&')]
    return token



def getPhone(token):
    '''
正确返回：13112345678;13698763743;13928370932;
注意：1.如果Count数量为20，获取后，确只返回了10个号码，则证明系统已经没有
      2.接口如有错误,或者没有获取到号码，前端都会有一个False:后面则是错误信息
      3.如果需要指定号码获取请在接口后面加上参数&Phone=指定的手机号

'''
    #娱票   11518
    # get('http://api.tianma168.com/tm/getPhone?&ItemId=759&token='+getToken())
    url = 'http://api.tianma168.com/tm/getPhone?ItemId=11518&token=' + token + '&Code=UTF8'
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req).read()
    phone1 = res_data[0:11]
    return phone1



def getMessage(token, phone):
    url = 'http://api.tianma168.com/tm/getMessage?token=' + token + '&itemId=11518&phone=' + phone + '&Code=UTF8'
    req = urllib2.Request(url)
    res_data = urllib2.urlopen(req).read()
    #data = urllib.request.urlopen(url).read()
    #z_data = data.decode('UTF-8')

    print(res_data)
    int = res_data.find('亲爱的')
    #print(int)
    if int == -1:
        #black(token,phone)
        print('接收验证码失败')
    else:
        yanzhengma = res_data.decode('UTF-8')[int + 5:int + 11]
        #print(yanzhengma)

        time.sleep(2)

        driver.switch_to_default_content()
        time.sleep(3)
        #输入验证码
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[3]/p[1]/input').click()
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[3]/p[1]/input').send_keys(yanzhengma)
        time.sleep(2)
        #输入密码
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[4]/p['
                                 '1]/input').click()
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[4]/p['
                                 '1]/input').send_keys('abc'+phone)
        time.sleep(2)

        # 点击注册
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[5]/button').click()
        time.sleep(2)


        '''
        f = open('yupiao_account.txt', 'a')
        # f.write('token:'+token)
        # f.write('\n')
        f.write(phone)
        f.write('\n')
        f.write('abc' + phone)
        f.write('\n')
        f.write('\n')
        f.close()
        '''
        time.sleep(2)


        #nickName=driver.find_element_by_xpath('//*[@id="uerCenter"]/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/a[1]').text

        addCount(phone)

        print('手机号' + phone + '注册成功')
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
    data = {'platform': '娱票', 'accountId': phone, 'password': 'abc' + phone}
    data = urllib.urlencode(data)
    req = urllib2.Request(url, headers=headers, data=data)
    response = urllib2.urlopen(req).read()

    print(response)

def black(token,phone):
    url = 'http://api.tianma168.com/tm/addBlack?token='+token+'&phoneList=11518-'+phone+'&Code=UTF8'

    #data = urllib.request.urlopen(url).read()  python3
    #z_data = data.decode('UTF-8')              python3

    req = urllib2.Request(url)
    # print(req)  <urllib2.Request instance at 0x026B05A8>
    data = urllib2.urlopen(req).read()
    z_data = data.decode('UTF-8')
    print(z_data)

if __name__ == '__main__':

    for num in range(1, 51):
        print(num)
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        driver = webdriver.Firefox()
        driver.get('http://www.wepiao.com/')
        driver.maximize_window()
        time.sleep(2)

        token = getToken()

        #print(token)

        phone = getPhone(token)
        #phone = 17088927105
        print(phone)

        print('开始注册，本次手机号为' + phone)




        # 点击注册
        driver.find_element_by_xpath('//*[@id="register_click"]').click()
        time.sleep(2)

        #输入手机号
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[1]/p['
                                     '1]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[1]/p['
                                     '1]/input').send_keys(phone)
        time.sleep(1)




        try:
            #在循环验证码过程中，会卡在验证码的iframe里，在输入验证码的时候要跳到主iframe
            i=1
            exist=True
            while exist:
                #print(i)
                #点击验证码弹出滑动框
                driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[3]/p[1]/input').click()

                time.sleep(3)

                driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[2]/div[1]/iframe'))
                #print('切换')

                #定位元素的原位置
                element = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]')
                time.sleep(2)
                #定位元素要移动到的目标位置
                target = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[1]')
                #执行元素的移动操作
                ActionChains(driver).drag_and_drop(element, target).perform()

                #print(driver.find_element_by_xpath('/html/body/div/div[1]/p').text)
                if driver.find_element_by_xpath('/html/body/div/div[1]/p').text=='验证成功'.decode("utf-8"):
                    print('识别正确，开始接收验证码，并等待25s')
                    break


                driver.switch_to_default_content()
                #print('再切换')
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="registerDialog"]/div/div[2]/div[1]/p[1]/input').click()
                time.sleep(2)
                #print('---分割线---')


                i=i+1


            time.sleep(25)
            #输入验证码

            time.sleep(1)
            #print('获取验证码。。。')
            getMessage(token,phone)
        except WebDriverException as e:

            print(e)
            print('该手机号已注册过或注册过程发生异常，本次注册取消')
        finally:
            black(token,phone)
            print('---分割线---')
            driver.quit()
