#coding=utf-8
import uuid

import random

import socket
import threading
import time
import os


from appium import webdriver


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
        # print '%d 被占用' % port
        return True
    except:
        # print '%d 未被占用' % port
        return False

def getFreePort():

    while True:
        random_port = random.randrange(4723,5000)

        if not IsOpen('127.0.0.1', random_port) and not IsOpen('127.0.0.1', random_port + 1) :


            return random_port





def findAndKill():
    os.popen('tasklist /fi "imagename eq 360MobileMgr.exe"').read().decode('gbk')
    os.popen('taskkill /F /IM 360MobileMgr.exe').read().decode('gbk')
    os.popen('tasklist /fi "imagename eq adb.exe"').read().decode('gbk')
    os.popen('taskkill /F /IM adb.exe').read().decode('gbk')


    # print os.popen('tasklist /fi "imagename eq 360MobileMgr.exe"').read().decode('gbk')
    # print os.popen('taskkill /F /IM 360MobileMgr.exe').read().decode('gbk')
    # print os.popen('tasklist /fi "imagename eq adb.exe"').read().decode('gbk')
    # print os.popen('taskkill /F /IM adb.exe').read().decode('gbk')


def install_deviceInfoList():
    findAndKill()


    # adb_result = execCmd('adb devices').split('\n')
    # # print adb_result
    #
    # adb_result.pop(0)
    # adb_result.pop(0)
    # adb_result.pop(0)
    # adb_result.pop()
    # adb_result.pop()
    #
    # print adb_result
    deviceInfoList = []

    # deviceInfoList = [{'desired_cap': {'deviceName': '03d61be113b3d502', 'unicodeKeyboard': 'True', 'udid': '03d61be113b3d502', 'resetKeyboard': 'True', 'platformVersion': '4.4.2', 'appPackage': 'com.sina.weibo', 'platformName': 'Android', 'appActivity': 'com.sina.weibo.SplashActivity'}, 'deviceID': '03d61be113b3d502', 'port': '4973'}, {'desired_cap': {'deviceName': '461dcf4', 'unicodeKeyboard': 'True', 'udid': '461dcf4', 'resetKeyboard': 'True', 'platformVersion': '4.4.2', 'appPackage': 'com.sina.weibo', 'platformName': 'Android', 'appActivity': 'com.sina.weibo.SplashActivity'}, 'deviceID': '461dcf4', 'port': '4854'}]


    # for i in range(len(adb_result)):
    #     deviceInfoList.append({'deviceID':adb_result[i].split('\t')[0]})
    # print deviceInfoList


    deviceInfoList.append({'deviceID':'461dcf4'})

    for i in range(len(deviceInfoList)):
        deviceInfoList[i]['port'] = str(getFreePort())
    # print deviceInfoList


    for i in range(len(deviceInfoList)):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.2'
        desired_caps['deviceName'] = deviceInfoList[i]['deviceID']
        desired_caps['udid'] = deviceInfoList[i]['deviceID']
        desired_caps['appPackage'] = 'com.huajiao'
        desired_caps['appActivity'] = 'com.huajiao.cover.CoverActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        deviceInfoList[i]['desired_cap'] = desired_caps
    # print desired_caps
    # print deviceInfoList[i]
    # print deviceInfoList
    return deviceInfoList





# 参照，对花椒无用
# def praiseWeibo(current_deviceInfo, mblogid):
#     driver = webdriver.Remote('http://localhost:' + current_deviceInfo['port'] + '/wd/hub', current_deviceInfo['desired_cap'])
#     time.sleep(10)
#
#     # os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am start -n com.sina.weibo/.feed.DetailWeiboActivity -d sinaweibo://detail?mblogid=' + mblogid)
#     # time.sleep(3)
#     while True:
#         if isElementExist('com.sina.weibo:id/liked', driver):
#
#             driver.find_element_by_id('com.sina.weibo:id/liked').click()
#             time.sleep(2)
#             break
#         time.sleep(1)
#         # print 1

def huajiao(current_deviceInfo, nickName, text):
    driver = webdriver.Remote('http://localhost:' + current_deviceInfo['port'] + '/wd/hub', current_deviceInfo['desired_cap'])
    time.sleep(10)

    # os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am start -n com.sina.weibo/.feed.DetailWeiboActivity -d sinaweibo://detail?mblogid=' + mblogid)
    # time.sleep(3)

    # 点击搜索框
    while True:
        if isElementExist('com.huajiao:id/explore_search_btn', driver):

            driver.find_element_by_id('com.huajiao:id/explore_search_btn').click()
            time.sleep(2)
            break
        time.sleep(1)
        # print 1

    # 输入用户名
    driver.find_element_by_id('com.huajiao:id/edit_keyword').clear()
    time.sleep(1)
    driver.find_element_by_id('com.huajiao:id/edit_keyword').send_keys(nickName)
    time.sleep(1)
    # 点击搜索
    driver.find_element_by_id('com.huajiao:id/btn_search').click()
    time.sleep(1)
    # 通过昵称查找
    # while True:
    #     if isElementExist('com.huajiao:id/search_item_user_name', driver):
    #         if driver.find_element_by_id('com.huajiao:id/search_item_user_name').text == nickName:
    #             print 123
    #             driver.find_element_by_id('com.huajiao:id/search_item_user_name').click()
    #             print 123
    #         else:
    #             print '没有相关用户,退出'
    #             os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.huajiao')
    #             return
    #         break
    #     else:
    #
    #         print '未找到，重复尝试'
    #         time.sleep(1)
    #         driver.find_element_by_id('com.huajiao:id/btn_search').click()
    #     time.sleep(1)
    # 通过uuid查找   点击头像
    while True:
        if isElementExist('com.huajiao:id/header_iv', driver):
            driver.find_element_by_id('com.huajiao:id/header_iv').click()
            # if driver.find_element_by_id('com.huajiao:id/header_iv').text == nickName:
            #     print 123
            #     driver.find_element_by_id('com.huajiao:id/header_iv').click()
            #     print 123
            # else:
            #     print '没有相关用户,退出'
            #     os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.huajiao')
            #     return
            break
        else:

            print '未找到，重复尝试'
            time.sleep(1)
            driver.find_element_by_id('com.huajiao:id/btn_search').click()
        time.sleep(1)


    # 点击私信
    while True:
        if isElementExist('com.huajiao:id/sixin_btn', driver):
            driver.find_element_by_id('com.huajiao:id/sixin_btn').click()
            time.sleep(2)
            print '已点击私信'
            break
        time.sleep(1)


    driver.find_element_by_id('com.huajiao:id/chatactivity_edittext_input').clear()
    time.sleep(2)
    driver.find_element_by_id('com.huajiao:id/chatactivity_edittext_input').send_keys(text)
    time.sleep(2)

    driver.find_element_by_id('com.huajiao:id/chatactivity_button_send').click()
    time.sleep(2)

    os.system('adb -s ' + current_deviceInfo['deviceID'] +' shell am force-stop com.huajiao')
    time.sleep(2)


def main():
    sixinText = '您好，在花椒平台报名青年电影A计划的选手，我们将您的资料和视频上传到了微信官方平台。请您扫码加我们的官方微信号18516862403，验证信息以 花椒+真实姓名 的形式发送。登录微信官方平台，账号密码都是自己的手机号。选手可以关注青年电影A计划微信公众号，点击 我要报名 ，直接登录查看。注意:不需要注册。希望选手尽快联系我们'

    string = '257475,291,1061,149137476,美热阿依,18337376263,0,0,2017/12/11 22:26,2017/12/11 22:26,女,学生,152,46,19,河南,河南师范大学+++257493,291,1061,109743104,代恒霞,18754991585,0,0,2017/12/12 1:53,2017/12/12 1:53,女,自由职业,163,60,34,山东临沂,无+++257507,291,1061,60178293,瑶瑶,13405760269,0,0,2017/12/12 9:57,2017/12/12 9:57,女,化妆,165,120,22,湖南的,我是化妆的+++257530,291,1061,120330595,陈盈盈,18259578763,0,0,2017/12/12 14:33,2017/12/12 14:33,女,学生,162,50,19,福建,福建商学院+++257535,291,1061,100102393,许传来,17624098065,0,0,2017/12/12 16:03,2017/12/12 16:03,男,外卖员,177c?m,55kg,25,辽宁沈阳,饿了么+++257607,291,1061,150713955,赵小童,17685259363,0,0,2017/12/13 13:31,2017/12/13 13:31,女,学生,162,50,17,贵州,学生+++257640,291,1061,99686013,黄志斌,13249298034,0,0,2017/12/13 19:53,2017/12/13 19:53,男,学生,175cm,55kg,20,广东,学校+++257672,291,1061,71995523,王晨伟,15735503056,0,0,2017/12/13 23:51,2017/12/13 23:51,男,IT,188,65,25,上海,上海兢鑫软件+++257676,291,1061,94501290,盛思嘉,18501617421,0,0,2017/12/14 0:08,2017/12/14 0:08,女,学生,169,54,20,上海,曼彻斯特大学+++257709,291,1061,150567073,李政,18679459867,0,0,2017/12/14 10:25,2017/12/14 10:25,男,学生,177,130,20,南昌,江西科技学院+++257715,291,1061,73967698,曾青,13138219921,0,0,2017/12/14 12:07,2017/12/14 12:07,女,一名全职主播,1.58cm,44kg,18,珠海,一名全职主播+++257732,291,1061,131346292,吴国平,18976864147,0,0,2017/12/14 15:46,2017/12/14 15:46,男,主播,175,120,25,海口,无+++257768,291,1061,108684620,陈宝莹,13312070386,0,0,2017/12/14 20:07,2017/12/14 20:07,女,学生,165,50,19,天津,无+++257791,291,1061,25391166,张志颖,13309238182,0,0,2017/12/14 22:49,2017/12/14 22:49,男,歌手,174,68,38,郑州,曲艺团+++257792,291,1061,150878866,罗圆红,13873663297,0,0,2017/12/14 23:17,2017/12/14 23:17,女,作业员,155,45,20,苏州,三星半导体+++257803,291,1061,21482417,魏高峰,17703770372,0,0,2017/12/15 2:38,2017/12/15 2:38,男,演员 后期剪辑,168cm,110kg,18,安阳,传媒公司+++257814,291,1061,150965612,祁青山,15887284357,0,0,2017/12/15 8:41,2017/12/15 8:41,男,学生,170,43,15,云南省楚雄州元谋县,学生+++257831,291,1061,134021617,王欢,15135360403,0,0,2017/12/15 11:15,2017/12/15 11:15,女,理发店学徒,156,67,24,山西省临汾市霍州市,无+++257839,291,1061,35750215,孙金峰,18766112841,0,0,2017/12/15 12:03,2017/12/15 12:03,男,学生,180,60,19,济南,无+++257872,291,1061,134526529,刘文杰,15949816816,0,0,2017/12/15 17:56,2017/12/15 17:56,女,实习生,170,60,19,青岛,青岛有米街市商贸有限公+++257900,291,1061,149674580,瑞拉,13570846206,0,0,2017/12/15 22:59,2017/12/15 22:59,女,普通上班族,150cm,58kg,20,湖南,东莞乌沙+++257993,291,1061,34671037,赵颖孩,15752735676,0,0,2017/12/16 21:06,2017/12/16 21:06,女,学生,167,44,14,大理,祥华+++258063,291,1061,150837279,毛建蕾,15022635565,0,0,2017/12/17 19:01,2017/12/17 19:01,女,公务员,168,50,22,天津,武清区东蒲洼街道办事处+++258122,291,1061,150283534,魏金财,15159796001,0,0,2017/12/18 16:48,2017/12/18 16:48,男,自己卖水果,160,103,21,福建省泉州市南安市,创+++258144,291,1061,90418767,樊炎华,18295080796,0,0,2017/12/18 21:39,2017/12/18 21:39,女,学生  艺考生,1米64,65,17,宁夏银川,宁夏艺术职业学院+++258266,291,1061,23588615,刘金雨,15131177205,0,0,2017/12/20 5:13,2017/12/20 5:13,女,主播,167,50,21,河北省石家庄,花椒平台+++258270,291,1061,80391736,魏嘉锐,18732091797,0,0,2017/12/20 8:46,2017/12/20 8:46,女,学生,170,60,20,河北邯郸,无'


    string_list = string.split('+++')
    uuidlist = []
    for i in string_list:
        uuidlist.append(i.split(',')[3])
    print uuidlist
    print len(uuidlist)

    # uuidlist=['58340720','58340720','58340720']



    for i in uuidlist:
        print '---------------------分割线------------------------------'
        print "all over %s" % time.ctime()
        try:

            print i
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


            huajiao(deviceInfoList[0],i,sixinText.decode('utf-8'))

            time.sleep(3)
            print '本次结束'

        #一个手机发花椒私信，不需要线程
        # task_threads = []
        # for j in range(len(deviceInfoList)):
        #
        #     # driver = webdriver.Remote('http://localhost:' + deviceInfo[j]['port'] + '/wd/hub', deviceInfo[j]['desired_cap'])
        #
        #     current_deviceInfo = deviceInfoList[j]
        #     print current_deviceInfo
        #
        #     # thread = threading.Thread(target=praiseWeibo,args=(current_deviceInfo,'4173987502094550'))
        #     # thread = threading.Thread(target=commentWeibo,args=(current_deviceInfo, taskurl, check_task(get_mac_address(), task_type)['data']['content']))
        #     # thread = threading.Thread(target=sendWeibo,args=(current_deviceInfo, u'今天天气不错'))
        #
        #     thread = threading.Thread(target=huajiao,args=(current_deviceInfo, uuid, sixinText))
        #
        #     task_threads.append(thread)
        #
        #     print '第 %d 个设备的线程组装完毕' %(j+1)
        # print '所有线程组装完毕，开始作业'
        #
        #
        #
        #
        # for current_thread in task_threads:
        #
        #     current_thread.start()
        #     print '当前线程启动'
        #
        # current_thread.join()



        except Exception as e:
            print e
            continue


if __name__ == '__main__':


    main()

