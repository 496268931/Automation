# coding=utf-8
from selenium import webdriver

import time

from com.aliyun.api.gateway.sdk.util import showapi

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class Param():
    pass



def main(taskUrl, account, password, text):
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
    print('wait')
    # driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
    # driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部
    # driver.switch_to.frame('iframe')

    ##############################################################

    # 点击登录
    driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/div[1]/div[1]/a').click()
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




        # 输入账号密码
    if isElementExist('//*[@id="loginForm"]/p[1]/input'):
        # driver.switch_to.frame('login_frame')


        # 输入账号
        # driver.find_element_by_xpath('//*[@id="YT-normalLogin"]/div[1]/label/span[1]').clear()
        driver.find_element_by_xpath('//*[@id="quickPostLogin"]/label[1]/input').send_keys(account)
        # 输入密码
        # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="quickPostLogin"]/label[2]/input').send_keys(password)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="quickPostLogin"]/div/a').click()
        time.sleep(2)



    driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[1]/a').click()  # 快速发帖
    time.sleep(2)
    # 输入评论
    driver.find_element_by_xpath('//*[@id="quickPostBody"]').clear()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="quickPostBody"]').send_keys(text.decode())
    # 打印评论内容
    print(driver.find_element_by_xpath('//*[@id="quickPostBody"]').get_attribute('value'))
    # 马上发表
    driver.find_element_by_xpath('//*[@id="quickPostForm"]/div/a').click()
    time.sleep(2)

    print('end')


    # driver.quit()


if __name__ == '__main__':
    main('http://comment.news.163.com/news2_bbs/CPMT4G4F0001899N.html','i493735',
         'aaafff', u'养狗要有责任心，对狗狗要负责任')