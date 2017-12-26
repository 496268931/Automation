#coding=utf-8
import uuid

import requests

import  utf8Togbk

import base64
import json
import random
import re
import socket
import threading
import time
import os
import datetime
from PIL import Image
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from com.aliyun.api.gateway.sdk.util import showapi

# PATH=lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
#desired_caps['app'] = PATH('E:\\虎啸\\appiumTest\\CalculatorSuper.apk')



# execute command, and return the output
def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac
def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()

    return text


def isElementExist(element, driver):
    flag = True

    try:
        driver.find_element_by_id(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag
#open=被占用
def IsOpen(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        print '%d 被占用' % port
        return True
    except:
        print '%d 未被占用' % port
        return False

def getFreePort():

    while True:
        # random_port = random.randrange(4723,5000)
        random_port = random.randrange(10000,65535)
        if not IsOpen('127.0.0.1', random_port) and not IsOpen('127.0.0.1', random_port + 1):


            return random_port





def findAndKill():

    # result1 = execCmd('tasklist /fi "imagename eq 360MobileMgr.exe"')
    # print result1.decode('gbk')
    # kill1 = execCmd('taskkill /F /IM 360MobileMgr.exe')
    # print kill1.decode('gbk')
    #
    # result2 = execCmd('tasklist /fi "imagename eq node.exe"')
    # print result2.decode('gbk')
    # kill2 = execCmd('taskkill /F /IM node.exe')
    # print kill2.decode('gbk')
    #
    # result3 = execCmd('tasklist /fi "imagename eq adb.exe"')
    # print result3.decode('gbk')
    # kill3 = execCmd('taskkill /F /IM adb.exe')
    # print kill3.decode('gbk')

    print os.popen('tasklist /fi "imagename eq 360MobileMgr.exe"').read().decode('gbk')
    print os.popen('taskkill /F /IM 360MobileMgr.exe').read().decode('gbk')
    # print os.popen('tasklist /fi "imagename eq node.exe"').read().decode('gbk')
    # print os.popen('taskkill /F /IM node.exe').read().decode('gbk')
    print os.popen('tasklist /fi "imagename eq adb.exe"').read().decode('gbk')
    print os.popen('taskkill /F /IM adb.exe').read().decode('gbk')


def install_deviceInfoList():

    while True:
        findAndKill()
        time.sleep(2)
        if os.popen('tasklist /fi "imagename eq 360MobileMgr.exe"').read().decode('gbk').find(
                u'信息: 没有运行的任务匹配指定标准。') >= 0 and os.popen(
                'tasklist /fi "imagename eq adb.exe"').read().decode('gbk').find(
                u'信息: 没有运行的任务匹配指定标准。') >= 0:
            print '没有占据端口的程序'
            break

    adb_result = execCmd('adb devices').split('\n')
    print adb_result
    # for i in adb_result:
    #
    #     if not i.endswith('\tdevice'):
    #         adb_result.remove(i)
    #     else:
    #         if i.endswith(r'*'):
    #             adb_result.remove(i)
    # print adb_result
    adb_result.pop(0)
    adb_result.pop(0)
    adb_result.pop(0)
    adb_result.pop()
    adb_result.pop()

    print adb_result
    # time.sleep(11111)

    deviceInfoList = []

    # deviceInfoList = [{'desired_cap': {'deviceName': '03d61be113b3d502', 'unicodeKeyboard': 'True', 'udid': '03d61be113b3d502', 'resetKeyboard': 'True', 'platformVersion': '4.4.2', 'appPackage': 'com.sina.weibo', 'platformName': 'Android', 'appActivity': 'com.sina.weibo.SplashActivity'}, 'deviceID': '03d61be113b3d502', 'port': '4973'}, {'desired_cap': {'deviceName': '461dcf4', 'unicodeKeyboard': 'True', 'udid': '461dcf4', 'resetKeyboard': 'True', 'platformVersion': '4.4.2', 'appPackage': 'com.sina.weibo', 'platformName': 'Android', 'appActivity': 'com.sina.weibo.SplashActivity'}, 'deviceID': '461dcf4', 'port': '4854'}]


    for i in range(len(adb_result)):
        deviceInfoList.append({'deviceID':adb_result[i].split('\t')[0]})
    print deviceInfoList


    for i in range(len(deviceInfoList)):
        deviceInfoList[i]['port'] = str(getFreePort())
    print deviceInfoList


    for i in range(len(deviceInfoList)):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = deviceInfoList[i]['deviceID']
        desired_caps['udid'] = deviceInfoList[i]['deviceID']
        desired_caps['appPackage'] = 'com.sina.weibo'
        desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        deviceInfoList[i]['desired_cap'] = desired_caps
    # print desired_caps
    # print deviceInfoList[i]
    print deviceInfoList
    return deviceInfoList



def login(driver, username, password):
    #登录按钮
    #WebDriverWait(driver, 20).until(lambda x: x.find_element_by_id('com.sina.weibo:id/titleSave')).click()
    WebDriverWait(driver, 60).until(lambda x: x.find_element_by_accessibility_id('我的资料')).click()
    time.sleep(2)

    if isElementExist('com.sina.weibo:id/btn_login', driver):
        print '未登录状态'
        driver.find_element_by_id('com.sina.weibo:id/btn_login').click()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').send_keys(username)
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').send_keys(password)
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/bnLogin').click()
        time.sleep(10)
        if True:
            if driver.find_element_by_id('com.sina.weibo:id/iv_access_image').is_displayed():# 如果存在验证码图片
                i = 0
                while i < 6:
                    print('有验证码')
                    print(i)

                    picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
                    driver.get_screenshot_as_file(picName)
                    time.sleep(1)

                    # 裁切图片
                    img = Image.open(picName)

                    region = (120, 567, 420, 647)
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
                    json_res = req.addTextPara("typeId", "3040") \
                        .addTextPara("img_base64", b_64) \
                        .addTextPara("convert_to_jpg", "1") \
                        .post()

                    # print ('1')
                    # print ('json_res data is:', json_res)
                    print (json_res)
                    json_res
                    # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

                    result = json.loads(str(json_res[1:-3]).replace('\\', ''))
                    yanzhengma = result['showapi_res_body']['Result']


                    print(yanzhengma)

                    time.sleep(1)

                    os.remove(picName)
                    time.sleep(1)
                    os.remove(picNameCut)
                    time.sleep(1)

                    driver.find_element_by_id('com.sina.weibo:id/et_input').click()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').clear()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').send_keys(yanzhengma)
                    time.sleep(3)

                    #点击登录
                    driver.find_element_by_name('确定').click()
                    time.sleep(5)

                    if not isElementExist('com.sina.weibo:id/iv_access_image', driver):
                        print '验证码输入正确'
                        break
    else:
        print '已登录状态'
        driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/accountContent').click()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/exitAccountContent').click()
        time.sleep(2)

        driver.find_element_by_name('确定').click()
        time.sleep(2)

        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etLoginUsername').send_keys(username)
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').clear()
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/etPwd').send_keys(password)
        time.sleep(2)
        driver.find_element_by_id('com.sina.weibo:id/bnLogin').click()
        time.sleep(10)
        if True:
            if driver.find_element_by_id('com.sina.weibo:id/iv_access_image').is_displayed():# 如果存在验证码图片
                i = 0
                while i < 6:
                    print('有验证码')
                    print(i)

                    picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
                    driver.get_screenshot_as_file(picName)
                    time.sleep(1)

                    # 裁切图片
                    img = Image.open(picName)

                    region = (120, 567, 420, 647)
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
                    json_res = req.addTextPara("typeId", "3040") \
                        .addTextPara("img_base64", b_64) \
                        .addTextPara("convert_to_jpg", "1") \
                        .post()

                    # print ('1')
                    # print ('json_res data is:', json_res)
                    print (json_res)
                    json_res
                    # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

                    result = json.loads(str(json_res[1:-3]).replace('\\', ''))
                    yanzhengma = result['showapi_res_body']['Result']


                    print(yanzhengma)

                    time.sleep(1)

                    os.remove(picName)
                    time.sleep(1)
                    os.remove(picNameCut)
                    time.sleep(1)

                    driver.find_element_by_id('com.sina.weibo:id/et_input').click()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').clear()
                    time.sleep(1)
                    driver.find_element_by_id('com.sina.weibo:id/et_input').send_keys(yanzhengma)
                    time.sleep(3)

                    #点击登录
                    driver.find_element_by_name('确定').click()
                    time.sleep(5)

                    if not isElementExist('com.sina.weibo:id/iv_access_image', driver):
                        print '验证码输入正确'
                        break


    print '登录成功'
    time.sleep(15)


def sendWeibo(current_deviceInfo, text):
    # driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver = webdriver.Remote('http://localhost:' + current_deviceInfo['port'] + '/wd/hub', current_deviceInfo['desired_cap'])
    time.sleep(10)

    # login(driver, '17018036531', 'asd55333')

    #WebDriverWait(driver, 30).until(lambda x: x.find_element_by_accessibility_id('打开发布面板')).click()

    while True:
        if isElementExist('com.sina.weibo:id/plus_icon', driver):

            driver.find_element_by_id('com.sina.weibo:id/plus_icon').click()
            time.sleep(2)
            break
        time.sleep(1)



    #点击文字 发微博
    driver.find_element_by_id('com.sina.weibo:id/composer_item_text').click()
    time.sleep(3)
    driver.find_element_by_id('com.sina.weibo:id/sv_element_container').clear()
    time.sleep(2)
    driver.find_element_by_id('com.sina.weibo:id/sv_element_container').send_keys(text)
    time.sleep(2)

    driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
    time.sleep(2)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.sina.weibo')
    time.sleep(2)




def forwardWeibo(current_deviceInfo, mblogid, text):
    driver = webdriver.Remote('http://localhost:' + current_deviceInfo['port'] + '/wd/hub', current_deviceInfo['desired_cap'])
    time.sleep(10)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am start -n com.sina.weibo/.feed.DetailWeiboActivity -d sinaweibo://detail?mblogid=' + mblogid)
    time.sleep(3)

    while True:
        if isElementExist('com.sina.weibo:id/forward', driver):

            driver.find_element_by_id('com.sina.weibo:id/forward').click()
            time.sleep(2)
            break
        time.sleep(1)


    driver.find_element_by_id('com.sina.weibo:id/edit_view').send_keys(text)
    time.sleep(2)
    driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
    time.sleep(2)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.sina.weibo')
    time.sleep(2)


def commentWeibo(current_deviceInfo, mblogid, text):

    driver = webdriver.Remote('http://localhost:' + current_deviceInfo['port'] + '/wd/hub', current_deviceInfo['desired_cap'])
    time.sleep(10)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am start -n com.sina.weibo/.feed.DetailWeiboActivity -d sinaweibo://detail?mblogid=' + mblogid)
    time.sleep(3)

    while True:
        if isElementExist('com.sina.weibo:id/comment', driver):

            driver.find_element_by_id('com.sina.weibo:id/comment').click()
            time.sleep(2)
            break
        time.sleep(1)



    driver.find_element_by_id('com.sina.weibo:id/edit_view').send_keys(text)
    time.sleep(2)
    driver.find_element_by_id('com.sina.weibo:id/titleSave').click()
    time.sleep(2)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.sina.weibo')
    time.sleep(2)

def praiseWeibo(current_deviceInfo, mblogid):
    driver = webdriver.Remote('http://localhost:' + current_deviceInfo['port'] + '/wd/hub', current_deviceInfo['desired_cap'])
    time.sleep(10)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am start -n com.sina.weibo/.feed.DetailWeiboActivity -d sinaweibo://detail?mblogid=' + mblogid)
    time.sleep(3)
    while True:
        if isElementExist('com.sina.weibo:id/liked', driver):

            driver.find_element_by_id('com.sina.weibo:id/liked').click()
            time.sleep(2)
            break
        time.sleep(1)
        # print 1


    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.sina.weibo')
    time.sleep(2)

# t1 = threading.Thread(target=sendWeibo,args=(webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1),))
# threads.append(t1)
# t2 = threading.Thread(target=sendWeibo,args=(webdriver.Remote('http://localhost:4730/wd/hub', desired_caps2),))
# threads.append(t2)




def check_task(clientId, taskTypes):
    response=requests.get('http://114.215.170.176:4000/check-task', params={'clientId': clientId,
                                                                  'taskTypes': taskTypes})
    print '任务信息: '

    # print response.text
    # return response.text
    print json.JSONDecoder().decode(response.text)
    return json.JSONDecoder().decode(response.text)

def report_task(clientId, taskId, status):
    response=requests.post('http://114.215.170.176:4000/report-task', data={'clientId': clientId, 'taskId': taskId, 'status': status})
    # print '上报结果: '
    # print response.text
    return response.text

def main():
    # driver1 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps1)
    # sendWeibo(driver1)

    # print 22222222222
    # driver2 = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps2)
    # sendWeibo(driver2)


    # start1 = 'start /b D:\\ProgramFiles\\appium\\Appium\\node.exe ' \
    #          'D:\\ProgramFiles\\appium\\Appium\\node_modules\\appium\\lib\\server\\main.js ' \
    #          '--address 127.0.0.1 --port ' + deviceInfoList[0]['port'] + '  --bootstrap-port 4780'
    # start2 = 'start /b D:\\ProgramFiles\\appium\\Appium\\node.exe D:\\ProgramFiles\\appium\\Appium\\node_modules\\appium\\lib\\server\\main.js --address 127.0.0.1 --port ' + \
    #          deviceInfoList[1]['port'] + '  --bootstrap-port 4781'
    # print deviceInfoList[0]['port']
    # print deviceInfoList[1]['port']
    # t_appiums = []
    # t_appium1 = threading.Thread(target=execCmd,args=(start1,))
    # t_appiums.append(t_appium1)
    # t_appium2 = threading.Thread(target=execCmd,args=(start2,))
    # t_appiums.append(t_appium2)

    # url = 'http://192.168.10.174:4000/add-account'
    # data = {'accountId': '17018036531', 'password': 'asd55333', 'platform': 'appium_微博',
    #         'data': {"access_token": "2.00rbAAAHzfFy9C0049e8db2e135HhC", "remind_in": "2651530",
    #                  "expires_in": 8888888, "uid": "6412932171", "isRealName": "true"}}
    # s = requests.post(url, data=data)
    # print s.text

    # info = get_account('豆瓣')
    # print '账号信息: '
    # print info


    # time.sleep(11111)
    try:
        task_type = checkTask['data']['type']
        weibo_rid = checkTask['data']['taskUrl']
        taskId = checkTask['data']['_id']
        timeInterval = checkTask['data']['param']['timeInterval']
        # content = checkTask['data']['content'] 循环取
        count = checkTask['data']['title']['count']
        print u'任务类型为: ' + str(task_type)
        print u'本次任务为: ' + weibo_rid
        print u'任务ID为: ' +taskId
        print u'时间间隔为: ' + timeInterval
        # print u'任务语料为: ' + content
        print u'任务数量为: ' + str(count)







        deviceInfoList = install_deviceInfoList()

        t_startAppiums = []
        for j in range(len(deviceInfoList)):
            start = 'start /b D:\\ProgramFiles\\appium\\Appium\\node.exe D:\\ProgramFiles\\appium\\Appium\\node_modules\\appium\\lib\\server\\main.js --address 127.0.0.1 --port ' + deviceInfoList[j]['port'] + '  --bootstrap-port ' + str(int(deviceInfoList[j]['port']) + 1)
            t_startAppiums.append(threading.Thread(target=execCmd,args=(start,)))


        for t in t_startAppiums:
            t.setDaemon(True)
            t.start()
        # x.join()
        #启动需要时间，必须等待一段时间
        time.sleep(10*len(t_startAppiums))
        print 'appium服务已启动'

        task_threads = []
        for j in range(len(deviceInfoList)):

            # driver = webdriver.Remote('http://localhost:' + deviceInfo[j]['port'] + '/wd/hub', deviceInfo[j]['desired_cap'])

            current_deviceInfo = deviceInfoList[j]
            print current_deviceInfo

            # thread = threading.Thread(target=praiseWeibo,args=(current_deviceInfo,'4173987502094550'))
            # thread = threading.Thread(target=commentWeibo,args=(current_deviceInfo, taskurl, check_task(get_mac_address(), task_type)['data']['content']))
            # thread = threading.Thread(target=sendWeibo,args=(current_deviceInfo, u'今天天气不错'))

            if task_type ==3000:
                print '发送微博'
                thread = threading.Thread(target=sendWeibo,args=(current_deviceInfo, check_task(get_mac_address(), task_type)['data']['content']))
            elif task_type == 3001:
                print '转发微博'
                thread = threading.Thread(target=forwardWeibo,args=(current_deviceInfo, weibo_rid, check_task(get_mac_address(), task_type)['data']['content']))
            elif task_type == 3002:
                print '评论微博'
                thread = threading.Thread(target=commentWeibo,args=(current_deviceInfo, weibo_rid, check_task(get_mac_address(), task_type)['data']['content']))
            elif task_type == 3003:
                print '点赞微博'
                thread = threading.Thread(target=praiseWeibo,args=(current_deviceInfo,weibo_rid))

            task_threads.append(thread)

            print '第 %d 个设备的线程组装完毕' %(j+1)
        print '所有线程组装完毕，开始作业'

        # driver2 = webdriver.Remote('http://localhost:4724/wd/hub', desired_caps2)
        # time.sleep(10)

        # thread2 = threading.Thread(target=praiseWeibo,args=(driver2,desired_caps2['udid']))
        # threads.append(thread2)



        for current_thread in task_threads:

            current_thread.start()
            print '当前线程启动'

        current_thread.join()


        # c_count = 1
        # while c_count < count:
        #     report_task(get_mac_address(), taskId, '1')
        #     c_count = c_count + 1
        #
        # print report_task(get_mac_address(), taskId, '1')
    except Exception as e:
        print e


if __name__ == '__main__':
    # 4173987502094550
    clientId = get_mac_address()
    print clientId


    checkTask = check_task(clientId, '3003')

    if checkTask['data'] is None:
        weibo_rid = None
        print '当前没有可执行任务'

    else:
        main()
    print "all over %s" % time.ctime()


    # url ='http://localhost:4000/add-account'
    # data = {'accountId': '17018031242', 'password': 'asd55333', "platform": '微博评论',
    #         'data': {"access_token": "2.00OjhGzGzfFy9C54e9588685M6183E", "remind_in": "2633070", "expires_in": 2633070, "uid": "6399751552", "isRealName": "true"}}
    # s=requests.post(url, data=data)
    # print s.text

    # time.sleep(11111)
