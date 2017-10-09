# coding=utf-8
import base64
import json
import random
import time

import datetime

import re

import os

import requests
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

def add_account(accountId, password, platform, cookies):
    # accountId = '18513199891'
    # password = '1qaz2wsx'
    # platform = '豆瓣'
    #cookies = {'bid': '0HZ8w7vIzDU', 'dbcl2': '"121892422:7k+dHEvklKs"'}

    cookiesStr = json.JSONEncoder().encode(cookies) #dict转str
    #print type(cookiesStr)  #str
    url ='http://114.215.170.176:4000/add-account'
    data = {'accountId': accountId, 'password': password, "platform": platform, 'data': cookiesStr}
    s=requests.post(url, data=data)
    print s.text


def get_account(platform):
    url = 'http://114.215.170.176:4000/get-account'
    req = requests.get(url, params = {'platform': platform})  #json字符串

    #print type(req.text) #<type 'unicode'>
    r = json.JSONDecoder().decode(req.text)   #将获取的结果转成dict   #<type 'dict'>


    return r
def update_cookies(accountId, password, current_cookie):
    url = 'http://114.215.170.176:4000/update-account'
    req = requests.post(url, data={'accountId': accountId, 'password': password, 'platform': '豆瓣', 'data': json.JSONEncoder().encode(current_cookie)})
    print req.text

def check_task(clientId, taskTypes):
    response=requests.get('http://114.215.170.176:4000/check-task', params={'clientId': clientId, 'taskTypes': taskTypes})
    print '任务信息: '
    # print response.text
    # return response.text
    print json.JSONDecoder().decode(response.text)
    return json.JSONDecoder().decode(response.text)
    #{"result":"ok","data":null}
    #{u'count': 10, u'status': 0, u'updateTime': u'2017-09-19T02:30:00.627Z', u'title': u'\u7329\u7329', u'failTasks': 0, u'userId': u'5992d65f753bb474afad6294', u'reportTasks': 0, u'param': {u'timeInterval': u'10'}, u'createTime': u'2017-09-19T02:30:00.627Z', u'__v': 0, u'checkTasks': 5, u'_id': u'59c08128a1f0cd1feb506ee5', u'type': 712, u'taskUrl': u'https://movie.douban.com/subject/25808075/?from=showing'}

def report_task(clientId, taskId, status):
    response=requests.post('http://114.215.170.176:4000/report-task', data={'clientId': clientId, 'taskId': taskId, 'status': status})
    print response.text

def check_comment_task(clientId, taskTypes):
    pass

def main(text=u'推荐大家看看', keyword = 2017, pageNum = 1):
    for xyz in range(1, 401):

        try:
            # 格式化成2016-03-20 11:45:39形式
            print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            print xyz
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
            info = get_account('豆瓣')
            print '账号信息: '
            print info
            accountId = info['data']['accountId']
            password = info['data']['password']
            clientId = info['data']['ipAddress']
            print accountId
            print password
            print clientId

            checkTask = check_task(clientId, '712')#这里的clientId随便写，但是要有

            taskId = None
            print taskId
            content = None
            print content
            timeInterval = None
            print timeInterval

            if checkTask['data'] is None:
                taskurl = None
                print '当前没有可执行任务'
            else:
                taskurl = checkTask['data']['taskUrl']
                taskId = checkTask['data']['_id']
                timeInterval = checkTask['data']['param']['timeInterval']
                content = checkTask['data']['content']
                print u'本次任务为: ' + taskurl
                print u'任务ID为: ' +taskId
                print u'时间间隔为: ' + timeInterval
                print u'任务语料为: ' +content
            if None == taskurl:
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
                    taskurl = 'https://movie.douban.com/subject_search?search_text='+str(keyword)+'&cat=1002&start='+randompage
                    driver.get(taskurl)
                    time.sleep(2)
                    print taskurl
                    time.sleep(2)





                    currentClassName = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]').get_attribute('class')
                    print currentClassName
                    #每个页面内链接个数
                    linknum=len(driver.find_elements_by_xpath("//div[contains(@class, '"+ currentClassName+"')]"))
                    print '当前页面链接数为 %d'%linknum
                    num = random.choice(range(1, linknum+1))
                    print '随机选择第 %d 个'%num
                    time.sleep(2)

                    j = 0
                    for link in driver.find_elements_by_tag_name("a"):
                        #link.get_attribute("href")  是 unicode
                        if None != link.get_attribute("href") and link.get_attribute(
                            "href") != '#' and str(link.get_attribute("href").encode('utf-8')).find(
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


                                    print(u'点击当前链接: '+ link.get_attribute("href"))
                                    time.sleep(2)
                                    link.click()
                                    time.sleep(3)

                                    break





                elif int(pageNum) != int(1) and int(pageNum) <= pageMax:
                    print '进入指定的第 %s 页'%pageNum
                    pageNum = str(15*(int(pageNum)-1))
                    taskurl = 'https://movie.douban.com/subject_search?search_text='+str(keyword)+'&cat=1002&start='+pageNum
                    driver.get(taskurl)
                    time.sleep(2)
                    print taskurl
                    time.sleep(2)





                    currentClassName = driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div[1]/div[1]').get_attribute('class')
                    print currentClassName
                    #每个页面内链接个数
                    linknum=len(driver.find_elements_by_xpath("//div[contains(@class, '"+ currentClassName+"')]"))
                    print '当前页面链接数为 %d'%linknum
                    num = random.choice(range(1, linknum+1))
                    print '随机选择第 %d 个'%num
                    time.sleep(2)

                    j = 0
                    for link in driver.find_elements_by_tag_name("a"):
                        #link.get_attribute("href")  是 unicode
                        if None != link.get_attribute("href") and link.get_attribute(
                                "href") != '#' and str(link.get_attribute("href").encode('utf-8')).find(
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


                                    print(u'点击当前链接: '+ link.get_attribute("href"))
                                    time.sleep(2)
                                    link.click()
                                    time.sleep(3)

                                    break







                else:
                    print '输入页码有误，退出'

            else:
                driver = webdriver.Firefox()
                driver.get(taskurl)
                driver.maximize_window()
                time.sleep(2)




            driver.delete_all_cookies()


            #cookies = json.JSONDecoder().decode(info['data']['data'])


            #取cookies
            #将json转化成dict
            json_string = json.dumps(info['data']['data'])
            get_cookies = json.loads(json_string)
            #print type(cookies) #<type 'dict'>
            print '取到的cookie为: '
            print get_cookies
            #cookies = {'bid': '0HZ8w7vIzDU', 'dbcl2': '"121892422:7k+dHEvklKs"'}

            response=requests.get(taskurl, cookies=get_cookies)
            time.sleep(1)
            if response.text.find('<li class="nav-user-account">') >= 0:
                print '取到的cookie可用'
                #driver.add_cookie({'name': 'bid', 'value': cookies['bid']})
                driver.add_cookie({'name': 'dbcl2', 'value': get_cookies['dbcl2']})
                time.sleep(1)
                driver.refresh()
                time.sleep(2)
                print u'该cookie的用户名为: ' + driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/ul/li[2]/a/span[1]').text


            else:
                print '取到的cookie不可用，进行实际登陆操作'
                #点击登录
                driver.find_element_by_xpath('//*[@id="db-global-nav"]/div/div[1]/a[1]').click()
                time.sleep(2)

                driver.find_element_by_xpath('//*[@id="email"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="email"]').clear()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="email"]').send_keys(accountId)
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="password"]').click()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="password"]').clear()
                time.sleep(1)
                driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
                time.sleep(2)

                #下次记住我
                #driver.find_element_by_xpath('//*[@id="remember"]').click()
                #time.sleep(1)


                if isElementExist('//*[contains(@class, "captcha_image")]', driver):

                    # 如果存在验证码图片
                    print('有验证码')

                    picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
                    driver.save_screenshot(picName)
                    time.sleep(1)

                    # 裁切图片
                    img = Image.open(picName)

                    region = (559, 266, 809, 308)
                    cropImg = img.crop(region)

                    # 保存裁切后的图片
                    picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
                    cropImg.save(picNameCut)
                    time.sleep(2)

                    # 进行验证码验证
                    f = open(picNameCut, 'rb')
                    b_64 = base64.b64encode(f.read())
                    f.close()
                    req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode", "4e5510e696c748ca8d5033dd595bfbbc")
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

                    os.remove(picName)
                    time.sleep(2)
                    os.remove(picNameCut)
                    time.sleep(2)

                    driver.find_element_by_xpath('//*[@id="lzform"]/div[7]/input').click()
                    time.sleep(10)


                else:
                    #if isElementExist("//*[contains(@id, 'lzform')]", driver):
                    print('无验证码')
                    driver.find_element_by_xpath('//*[@id="lzform"]/div[6]/input').click()
                    time.sleep(10)

                print driver.get_cookies()
                # for cookie in driver.get_cookies():
                #     print "%s == %s" % (cookie['name'], cookie['value'])
                for i in range(0, len(driver.get_cookies())):

                    if 'dbcl2' == driver.get_cookies()[i]['name']:

                        y = driver.get_cookies()[i]['value']
                    #print y
                current_cookie = {'dbcl2': y}
                print '本次成功登陆的cookie为: '
                print current_cookie

                print '需要更新cookie'
                update_cookies(accountId, password, current_cookie)
                print '更新cookie成功'






            target = driver.find_element_by_xpath('//*[@id="comments-section"]/div[1]/a/span')
            driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
            time.sleep(2)




            #点击评论
            driver.find_element_by_xpath('//*[@id="comments-section"]/div[1]/a/span').click()
            time.sleep(2)
            #点击五星
            driver.find_element_by_xpath('//*[@id="star5"]').click()
            time.sleep(2)





            if None != content:
                driver.find_element_by_xpath('//*[@id="comment"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="comment"]').clear()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="comment"]').send_keys(content)
                time.sleep(2)
            else:
                #当前页面电影评论数
                commentNum=len(driver.find_elements_by_xpath("//div[contains(@class, 'comment-item')]"))
                if isElementExist('//*[@id="following-comments"]', driver):
                    commentNum = commentNum - 1

                if commentNum > 0:

                    random_comment = random.choice(range(1, commentNum+1))

                    print '当前页面短评数为 %d 随机选择第 %d 个'%(commentNum, random_comment)
                    copytext = driver.find_element_by_xpath('//*[@id="hot-comments"]/div['+str(random_comment)+']/div/p').text

                    text = copytext
                    time.sleep(2)

                    print text
                    time.sleep(2)
                else:
                    print u'当前页面没有评论，采用默认评论：'+text


                driver.find_element_by_xpath('//*[@id="comment"]').click()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="comment"]').clear()
                time.sleep(2)
                driver.find_element_by_xpath('//*[@id="comment"]').send_keys(text)
                time.sleep(2)



            driver.find_element_by_xpath('//*[@id="submits"]/span/input').click()
            time.sleep(10)





            if None != taskId:
                print '上报任务成功结果:'
                report_task(clientId, taskId, '1')
                time.sleep(2)

            print('本次评论成功，结束时间为： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            driver.quit()


            if None == timeInterval:
                timeInterval = random.choice(range(1, 2))
                print '技能CD： '+ str(timeInterval) + '小时'
                time.sleep(timeInterval*1200)
            else:
                print '技能CD： '+ str(timeInterval) + '秒'
                time.sleep(int(timeInterval))



        except Exception as e:
            print e
            driver.quit()
            if None != taskId:
                print '上报任务失败结果:'
                report_task(clientId, taskId, '0')


        finally:
            print('---------我是分割线------------')



if __name__ == '__main__':
    main()