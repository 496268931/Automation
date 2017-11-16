#coding=utf-8

import os, re

# execute command, and return the output
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

# 获取计算机MAC地址和IP地址
if __name__ == '__main__':
    # cmd = 'netstat -aon|findstr 4723'
    # result = execCmd(cmd).replace('\n','')
    # print result
    #
    #
    # result = re.sub(' +', ' ', result).split(' ')
    # print result
    # port = result[-1]
    # print port
    #
    # result1 = execCmd('tasklist|findstr '+port).replace('\n','')
    # result1 = re.sub(' +', ' ', result1).split(' ')
    # print result1
    #
    #
    # result2 = execCmd('tasklist /fi "imagename eq node.exe"')
    # print result2.decode('gbk')
    # kill = execCmd('taskkill -t -f /pid '+port)
    #
    # print kill.decode('gbk')


    start = 'start /b D:\\ProgramFiles\\appium\\Appium\\node.exe D:\\ProgramFiles\\appium\\Appium\\node_modules\\appium\\lib\\server\\main.js --address 127.0.0.1 --port 4723  --bootstrap-port 4780'

    execCmd(start)