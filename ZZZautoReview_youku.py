# coding=utf-8
import random

import requests
from selenium import webdriver

import time




class Param():
    pass



def main(taskUrl, accountId, password, content):
    try:
        print('开始本次评论任务')
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        iplist = ['47.93.113.175:5818', '59.110.159.237:5818', '123.56.77.123:5818',
                  '123.56.76.207:5818', '123.56.72.115:5818', '123.56.154.24:5818',
                  '123.56.44.11:5818', '123.56.228.93:5818', '123.57.48.138:5818',
                  '101.200.76.126:5818']
        #proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
        proxy_ip = random.choice(iplist)
        ip_ip = proxy_ip.split(":")[0]
        ip_port = proxy_ip.split(":")[1]

        num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
        if num < 11:
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
        #args = Param()
        # driver  = webdriver.Chrome()

        # driver.get("http://v.youku.com/v_show/id_XMjgzNzM0NTYxNg==.html?spm=a2hww.20023042.m_223473.5~5
        # !2~5~5~A")
        # driver.get("http://v.youku.com/v_show/id_XMjkwMzE4ODYwMA==.html?spm=a2hww.20023042.m_223465.5~5
        # ~5~5~5~5~A")
        driver.get(taskUrl)
        driver.maximize_window()
        time.sleep(2)

        # driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部
        # driver.switch_to.frame('iframe')

        ##############################################################

        # 点击登录
        driver.find_element_by_id('qheader_login').click()
        time.sleep(2)

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


                # 截图验证码并进行剪裁

        if isElementExist('//*[@id="YT-ytaccount"]'):
            # driver.switch_to.frame('login_frame')


            # 输入账号
            # driver.find_element_by_xpath('//*[@id="YT-normalLogin"]/div[1]/label/span[1]').clear()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-ytaccount"]').send_keys(accountId)
            # 输入密码
            # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="YT-normalLogin"]/div[2]/label').send_keys(password)
            # 点击登录
            time.sleep(2)
            driver.find_element_by_id('YT-nloginSubmit').click()
            time.sleep(3)

        # 输入评论
        driver.find_element_by_xpath('//*[@id="commentAction"]/div/div/div[3]/textarea').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="commentAction"]/div/div/div[3]/textarea').send_keys(content)
        # 打印评论内容
        #print(driver.find_element_by_xpath('//*[@id="commentAction"]/div/div/div[
        # 3]/textarea').get_attribute('value'))
        # 点击评论
        driver.find_element_by_xpath('//*[@id="commentAction"]/div/div[2]/div[4]/div[1]/div[1]/a').click()
        time.sleep(2)

        print('本次评论任务成功')
    except Exception as e:
        print('本次评论任务失败')
        print(e)
    finally:
        #print(1)
        driver.quit()




if __name__ == '__main__':
    main('http://v.youku.com/v_show/id_XMTU2ODY2NjYyOA==.html?spm=a2h0j.8191423.module_basic_relation.5~5!2~5~5!24~5~5~A'
         '~5!2~A', '13434843854', 'abc13434843854', u'超级无敌喜欢这部剧')

