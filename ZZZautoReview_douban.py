# coding=utf-8
import base64
import json
import random
import time

import datetime

import re

import os

from PIL import Image
from selenium import webdriver

from com.aliyun.api.gateway.sdk.util import showapi

'''
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

                            '''

def isElementExist(element, driver):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag

def main(account, password, text, keyword = 2017, pageNum = 1):
    #while True:
        time.sleep(2)
        try:
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            '''
            iplist = ['123.56.154.24:5818', '59.110.159.237:5818', '47.93.113.175:5818',
                  '123.56.44.11:5818', '101.200.76.126:5818', '123.56.228.93:5818',
                  '123.57.48.138:5818', '123.56.72.115:5818', '123.56.77.123:5818',
                  '123.56.76.207:5818', '47.93.85.217:5818', '59.110.23.162:5818',
                  '47.92.32.50:5818', '47.91.241.124:5818']
            #proxy_ip1 = iplist[random.randint(0, len(iplist)-1)]
            proxy_ip = random.choice(iplist)
            ip_ip = proxy_ip.split(":")[0]
            ip_port = int(proxy_ip.split(":")[1])

            num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
            if num < 15:
                isDaili = 1  # 1使用代理
                print(requests.get('http://ip.chinaz.com/getip.aspx',
                               proxies={"http": 'http://' + proxy_ip}).text)
            else:
                isDaili = 0
                print(requests.get('http://ip.chinaz.com/getip.aspx').text)

            profile = webdriver.FirefoxProfile()
            profile.set_preference('network.proxy.type', isDaili)
            profile.set_preference('network.proxy.http', ip_ip)
            profile.set_preference('network.proxy.http_port', ip_port)  # int
            profile.update_preferences()
            driver = webdriver.Firefox(firefox_profile=profile)
            '''

            driver = webdriver.Firefox()
            currentpage = str(15*(int(pageNum)-1))
            driver.get('https://movie.douban.com/subject_search?search_text='+str(keyword) +'&cat=1002&start='+currentpage)
            driver.maximize_window()
            time.sleep(2)

            pageMax=int(driver.find_element_by_xpath("//div[contains(@class, 'paginator')]/a[last()-1]").text)
            print str(keyword)+' 为关键词的搜索结果最大页数为 %d' %pageMax
            time.sleep(2)
            if int(pageNum) == int(1) and int(pageNum) <= pageMax:

                x = random.choice(range(1, pageMax+1))
                print '进入随机页 %d' %x
                randompage = str(15*(int(x)-1))
                driver.get('https://movie.douban.com/subject_search?search_text='+str(keyword)+'&cat=1002&start='+randompage)
                time.sleep(2)
            elif int(pageNum) != int(1) and int(pageNum) <= pageMax:
                print '进入指定的第 %d 页'%pageNum
                pageNum = str(15*(int(pageNum)-1))
                driver.get('https://movie.douban.com/subject_search?search_text='+str(keyword)+'&cat=1002&start='+pageNum)
                time.sleep(2)
            else:
                print '输入页码有误，退出'




            driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/a[1]').click()
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="email"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="email"]').clear()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="email"]').send_keys(account)
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="password"]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="password"]').clear()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
            time.sleep(2)

            if isElementExist('//*[contains(@class, "captcha_image")]', driver):

                # 如果存在验证码图片
                print('有验证码')

                picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
                datetime.datetime.now())) + '.png'
                driver.save_screenshot(picName)
                time.sleep(1)

                # 裁切图片
                img = Image.open(picName)

                region = (559, 266, 809, 308)
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
                json_res = req.addTextPara("typeId", "20") \
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

                print yanzhengma
                time.sleep(2)









                driver.find_element_by_xpath('//*[@id="captcha_field"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="captcha_field"]').clear()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="captcha_field"]').send_keys(yanzhengma)
                time.sleep(2)



                driver.find_element_by_xpath('//*[@id="lzform"]/div[7]/input').click()

                time.sleep(8)
                os.remove(picName)
                time.sleep(2)
                os.remove(picNameCut)
                time.sleep(2)

            else:
            #if isElementExist("//*[contains(@id, 'lzform')]", driver):
                print('无验证码')
                driver.find_element_by_xpath('//*[@id="lzform"]/div[6]/input').click()
                time.sleep(2)

















            #每个页面内链接个数
            linknum=len(driver.find_elements_by_xpath("//div[contains(@class, 'sc-ifAKCX ')]"))
            print '当前页面链接数为 %d'%linknum
            num = random.choice(range(1, linknum+1))
            print '随机选择第 %d 个'%num

            time.sleep(2)


            j = 0
            for link in driver.find_elements_by_tag_name("a"):
                #link.get_attribute("href")  是 unicode
                if None != link.get_attribute("href") and link.get_attribute("href") != '#' and str(
                        link.get_attribute("href").encode('utf-8')).find(
                    'https://movie.douban.com/subject/') >= 0 and str(
                    link.get_attribute("href").encode('utf-8')).find(
                    'cinema') == -1 and link.is_displayed():


                        j = j + 1

                        #同一个页面内链接是重复的，且两个重复的链接第一个无法点击，故选择第二个进行点击
                        if j%2 == 1:
                            i = (j+1)/2

                        else:

                            i = j/2

                            if num == i:

                                print(link.get_attribute("href"))
                                print('点击当前链接')
                                time.sleep(2)
                                link.click()
                                time.sleep(3)

                                break


            target = driver.find_element_by_xpath('//*[@id="comments-section"]/div[1]/a/span')
            driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="comments-section"]/div[1]/a/span').click()
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="star5"]').click()
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="comment"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="comment"]').clear()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="comment"]').send_keys(text)
            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="submits"]/span/input').click()
            time.sleep(2)

            print '本次自动评论成功'
            time.sleep(2)


        except Exception as e:
            print '操作有误'+ e

        finally:
            print('---------我是分割线------------')
            #driver.quit()


if __name__ == '__main__':
    main('18513199891', '1qaz2wsx', u'推荐大家看看')