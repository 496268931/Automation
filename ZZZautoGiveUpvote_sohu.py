# coding=utf-8
import random
import time

import requests
from selenium import webdriver


def main(taskUrl):
    for num in range(1, 5):
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
            driver.get(taskUrl)
            driver.maximize_window()
            time.sleep(2)
            #点赞
            driver.find_element_by_xpath('//*[@id="playtoolbar"]/div[1]/a').click()
            #踩
            #driver.find_element_by_xpath('//*[@id="playtoolbar"]/div[2]/a').click()

            time.sleep(2)

        except Exception as e:
            print (e)
        finally:

            driver.quit()

if __name__ == '__main__':
    main('http://tv.sohu.com/20170605/n495734949.shtml')