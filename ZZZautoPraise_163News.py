# -*- coding: utf-8 -*-

import time

from selenium import webdriver

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


def main(taskUrl, created_time, count):
    for num in range(1, int(count) + 1):
        try:
            print(num)
            # 格式化成2016-03-20 11:45:39形式
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

            js = "var q=document.documentElement.scrollTop=-50"

            print('开始点赞')
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
            driver.get(taskUrl)
            driver.maximize_window()
            time.sleep(2)



            pageList = driver.find_elements_by_xpath('//*[@id="mainReplies"]/ul/li')
            pageNums = len(pageList)
            #print(pageNums)

            pageNum = driver.find_element_by_xpath('//*[@id="mainReplies"]/ul/li['+str(pageNums-1)+']').text
            #print(pageNum)
            print(u'评论共 '+pageNum+u' 页')

            currentPage = 1
            while currentPage <= pageNum:
                print('--------------')
                currentpageList = driver.find_elements_by_xpath('//*[@id="mainReplies"]/ul/li')
                currentpageNums = len(currentpageList)
                print(currentpageNums)

                print('当前是第 %d 页'%currentPage)
                a = driver.find_elements_by_xpath("//*[contains(@id,'tie-data')]")
                #print(a)

                for b in a:
                    if b.text.find(created_time) >= 0:
                        print(b.text)
                        c = b.get_attribute('id')
                        #print(c)
                        driver.find_element_by_xpath('//*[@id="'+c+'"]/div/ul/li[1]/a').click()
                        print('找到指定评论,点赞成功')
                        time.sleep(10)
                        driver.quit()


                #print(driver.find_element_by_xpath("//*[contains(@class,'postTime')]")).text

                target = driver.find_element_by_xpath('//*[@id="replyBody"]')
                driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="mainReplies"]/ul/li['+str(currentpageNums)+']/a').click()
                time.sleep(2)


                currentPage = currentPage+1





        except Exception as e:
            print (e)
        finally:
            print('---------我是分割线------------')
            driver.quit()


if __name__ == '__main__':
    #main('http://comment.news.163.com/news_shehui7_bbs/CT1GHQBT0001875P.html', u'2017-08-31 09:39:26','1')
    main('http://comment.news.163.com/news_shehui7_bbs/CT3L0KOI0001875P.html', '2017-08-31 13:06:36','1')

