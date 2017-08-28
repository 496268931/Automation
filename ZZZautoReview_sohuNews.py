# coding=utf-8
from selenium import webdriver

import time



import sys


class Param():
    pass



def main(taskUrl, account, password, text):
    try:
        #args = Param()

        print('开始本次评论任务')
        # 格式化成2016-03-20 11:45:39形式
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

        driver = webdriver.Firefox()
        # driver  = webdriver.Chrome()

        # driver.get("http://comment.news.163.com/news2_bbs/CPISM0FT000189FH.html")
        driver.get(taskUrl)

        driver.maximize_window()
        time.sleep(2)

        # driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
        # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部
        # driver.switch_to.frame('iframe')

        ##############################################################

        # 点击登录
        driver.find_element_by_xpath('//*[@id="SOHU_MAIN"]/div[2]/div[3]/div/div[1]/div[2]').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="SOHU_MAIN"]/div[8]/div/div[2]/ul/li[1]/span').click()
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

        # 获取当前窗口句柄
        ch = driver.current_window_handle
        time.sleep(2)
        # 获取所有窗口句柄
        wh = driver.window_handles

        # 在所有窗口中查找弹出窗口
        for line in wh:
            if line != ch:
                driver.switch_to_window(line)
                time.sleep(2)
                driver.maximize_window()
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="email"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="email"]').clear()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="email"]').send_keys(account)
                time.sleep(1)


                driver.find_element_by_xpath('//*[@id="diglog_wrapper"]/div[3]/div/div[1]/ul/li['
                                             '1]').click()
                time.sleep(1)

                driver.find_element_by_xpath('//*[@id="password"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="password"]').clear()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
                time.sleep(1)

                driver.find_element_by_xpath('//*[@id="diglog_wrapper"]/div[3]/div/div[1]/ul/li['
                                             '1]').click()
                time.sleep(1)

                driver.find_element_by_xpath('//*[@id="ppcontid"]/form/ul/li[4]/a/input').click()
                time.sleep(2)


        driver.switch_to_window(ch)
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="SOHU_MAIN"]/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div[2]/div/textarea').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="SOHU_MAIN"]/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div[2]/div/textarea').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="SOHU_MAIN"]/div[2]/div[3]/div/div[2]/div[1]/div/div[3]/div[2]/div/textarea').send_keys(text)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="SOHU_MAIN"]/div[2]/div[3]/div/div[2]/div[1]/div/div[4]/div[2]/div/a/button').click()
        time.sleep(10)


        print('本次评论任务成功')
    except Exception as e:
        print('本次评论任务失败')
        print(e)
    finally:
        #print(0)
        driver.quit()







if __name__ == '__main__':
    main('http://pinglun.auto.sohu.com/pinglun/cyqemw6s1/508146864?qq-pf-to=pcqq.c2c','13690757552',
         'abc13690757552', u'车子看着不错，但是我更喜欢宝马，100万以上的那种')