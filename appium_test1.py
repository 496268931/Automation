#coding=utf-8

import os, re

# execute command, and return the output
import random
import socket


def execCmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text

# write "data" to file-filename
def writeFile(filename, data):
    f = open(filename, "w")
    f.write(data)
    f.close()

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
# 获取计算机MAC地址和IP地址
if __name__ == '__main__':
    cmd = 'netstat -aon|findstr 4850'
    result = execCmd(cmd).replace('\n','')
    print result


    result = re.sub(' +', ' ', result).split(' ')
    print result
    port = result[-1]
    print port

    result1 = execCmd('tasklist|findstr '+port).replace('\n','')
    result1 = re.sub(' +', ' ', result1).split(' ')
    print result1


    result2 = execCmd('tasklist /fi "imagename eq node.exe"')
    print result2.decode('gbk')

    # kill = execCmd('taskkill -t -f /pid '+port)
    #
    # print kill.decode('gbk')


    #---------------------------------------
    # udids = [{'deviceName':'03d61be113b3d502','port':'4723'},    {'deviceName':'461dcf4','port':'4724'}]
    #
    # for i in range(len(udids)):
    #     print i
    #     desired_caps = {}
    #     desired_caps['platformName'] = 'Android'
    #     desired_caps['platformVersion'] = '4.4.2'
    #     desired_caps['deviceName'] = udids[i]['deviceName']
    #     desired_caps['udid'] = udids[i]['deviceName']
    #     desired_caps['appPackage'] = 'com.sina.weibo'
    #     desired_caps['appActivity'] = 'com.sina.weibo.SplashActivity'
    #     desired_caps['unicodeKeyboard'] = 'True'
    #     desired_caps['resetKeyboard'] = 'True'
    #     print desired_caps
    #     udids[i]['desired_cap'] = desired_caps
    #     print udids[i]
        #---------------------------------------


    # start = 'start /b D:\\ProgramFiles\\appium\\Appium\\node.exe D:\\ProgramFiles\\appium\\Appium\\node_modules\\appium\\lib\\server\\main.js --address 127.0.0.1 --port 4723  --bootstrap-port 4780'
    #
    # execCmd(start)
    print 123
    cmd = 'adb devices'
    result = execCmd(cmd).split('\n')
    print result
    print type(result)
    print result.pop(0)
    print result.pop()
    print result.pop()
    print result
    print 123

    # x = random.randrange(4723,5000)
    # print x
    IsOpen('127.0.0.1',4865)
