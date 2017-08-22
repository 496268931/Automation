# coding=utf-8
import time
import requests
import uuid
import logging
from selenium import webdriver
import sys

#import ZZZautoReview_gewala
import ZZZautoReview_qiy
import ZZZautoReview_youku

reload(sys)
sys.setdefaultencoding('utf-8')

def get_mac_address():
    node = uuid.getnode()
    mac = uuid.UUID(int=node).hex[-12:]
    return mac

# 整体是一个大的循环体
'''参数配置'''
class ClientParam():
    # 基本的参数
    name = 'wy'
    clientId = get_mac_address()
    # apiURL = 'http://127.0.0.1:3000'
    apiURL = 'http://114.215.170.176:4000'
    sleep = 1
    #taskTypes = '111,911,112'
    taskTypes = '512,412'
    # taskTypes = '911'

    routeCheckTask = '/check-task'
    routeReportTask = '/report-task'





'''格瓦拉刷量'''
def gewaraAttention(task,args):
    url = task['taskUrl']
    data={
        'movieId':task['param']['movieId']
    }
    headers=task['param']['headers']
    print(data)
    print(headers)
    print(url)

    sleep=3
    return requestPost(url,data,headers,sleep)

'''浏览网网页'''
def browsePage(task,args):
    try:
        seconds = args.sleep

        if(task['taskUrl']):
            # driver = webdriver.Chrome()
            driver = webdriver.Firefox()
            # driver = webdriver.Safari()
            driver.get(task['taskUrl'])
            if (task['param'] != None and task['param']['timeInterval'] != None):
                # if(type(task['param']['timeInterval']) is types.IntType ):
                seconds = int(task['param']['timeInterval'])
                print(seconds)
            time.sleep(seconds)
            driver.quit()
            return {
                'status': 1
            }
        else:
            return {
                'status':0
            }
    except:
        return {
            'status': 0,
            'message':'出现异常'
        }


'''请求链接 get'''
def requestPage(task,args):
    try:
        seconds=args.sleep
        if (task['param'] != None and task['param']['timeInterval'] != None and task['param']['timeInterval'] != 'NaN'):
            # if(type(task['param']['timeInterval']) is types.IntType ):
            seconds = int(task['param']['timeInterval'])
            print(seconds)
        time.sleep(seconds)
        if(task['taskUrl']):
            result = requests.get(url=task['taskUrl'])
            print(result.status_code);
            if result.status_code==200:
                return {
                    'status': 1
                }
            else:
                return {
                    'status': 0
                }
        else:
            return {
                'status':0,
                'message': 'taskUrl 为空'
            }
    except Exception as e:
        logging.exception(e)
        return {
            'status': 0,
            'message': '出现异常'
        }
'''post 请求网页'''
def requestPost(url,data,headers,sleep):
    try:
        seconds = sleep
        time.sleep(seconds)
        result = requests.post(url=url,headers=headers,data=data)
        if result.status_code == 200:
            return {
                'status': 1
            }
        else:
            return {
                'status': 0
            }
    except Exception as e:
        logging.exception(e)
        return {
            'status': 0,
            'message': '出现异常'
        }
'''get 请求网页'''
def requestGet(url,params,headers,cookies,sleep):
    try:
        seconds = sleep
        time.sleep(seconds)
        result = requests.get(url,headers=headers,params=params,cookies=cookies)
        if result.status_code == 200:
            return {
                'status': 1
            }
        else:
            return {
                'status': 0
            }
    except Exception as e:
        logging.exception(e)
        return {
            'status': 0,
            'message': '出现异常'
        }

# 组成部分包括：配置参数

def checkTask(args):
    try:
        params = {'name': args.name, 'clientId': args.clientId, 'taskTypes': args.taskTypes}
        result = requests.get(url=args.apiURL + args.routeCheckTask, params=params).json()
        print(result)
        if result['result']=='ok':
            print(result['data'])
            return result['data']
        else:
            return None
    except:
        return None



def reportTask(report, task,args):
    params = {
        'clientId':args.clientId,
        'taskId':task['_id'],
        'status':report['status']
        # 'message':report['message']
    }
    print(params)
    result = requests.post(url=args.apiURL + args.routeReportTask,
                           data=params);
    print(result.text)

def runTask(task,args):
    print(task)
    if (task['type'] == 111):
        return browsePage(task, args)
    elif (task['type'] == 412):
        return autoReview(task)
    elif (task['type'] == 512):
        return autoReview(task)
    elif (task['type'] == 911):
        return gewaraAttention(task, args)
    elif (task['type'] == 112):
        return requestPage(task, args)
    else:
        return {
            'status': 0
        }
def runTask1(task):
    print(task)
    if (task['type'] != None):
        return autoReview(task)

    else:
        return {
            'status': 0
        }
def autoReview(task):
    try:
        if(task['type'] == 412):
            ZZZautoReview_youku.main(task['taskUrl'],task['account']['accountId'], task['account']['password'],task['content'])

            return {
                'status': 1
            }
        elif(task['type'] == 512):
            ZZZautoReview_qiy.main(task['taskUrl'],task['account']['accountId'], task['account']['password'],task['content'])

            return {
                'status': 1
            }


        else:
            return {
                'status':0
            }
    except:
        return {
            'status': 0,
            'message':'出现异常'
        }

def main():
    args = ClientParam()
    # 执行次数
    sum = 0
    while True:
        time.sleep(args.sleep)
        sum += 1
        print("第 %d 次" % (sum))
        task = checkTask(args)

        if task==None:
            continue

        print('-----参数信息-----')
        print(task['taskUrl'])
        print(task['content'])
        print(task['account']['accountId'])
        # print(task['account']['password'])
        print('-----参数信息-----')
        report = runTask1(task)
        #report = runTask(task,args)
        reportTask(report, task,args)

        time.sleep(float(task['param']['timeInterval']))

        # task =  checkTask(args)

        # report = runTask(task)

        # reportTask(report,args)



if __name__ == '__main__':
    print('启动')
    main()

    # msg = """
    # Usage:
    # Training:
    #     python3 gen_lyrics.py 0
    # Sampling:
    #     python3 gen_lyrics.py 1
    # """
    # if len(sys.argv) == 2:
    #     infer = int(sys.argv[-1])
    #     print('--Sampling--' if infer else '--Training--')
#         main(infer)
# else:
#     print(msg)
#     sys.exit(1)

