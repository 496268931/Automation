#coding=utf-8
import json

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yinyangciqingshi.com/423.html')
# print r.content
soup = BeautifulSoup(r.content, "html.parser")
# print soup.find_all('div',id='contents')

# for i in soup.find_all('div',id='contents'):
#
#     print i.text
a= '沈腾'
actor = ['沈腾','马丽','艾伦']
act = ['a','b','c']
print actor[0]
print actor
print act
print a

def report_task(clientId, taskId, status):
    response = requests.post('http://114.215.170.176:4000/report-task',
                             data={'clientId': clientId, 'taskId': taskId, 'status': status})
    # print '上报结果: '
    print response.text
    return response.text

num = 0
while num < 2:
    report_task("xxx", '5a3b0c01c2a90c20ac1c6c54', 1)
    num = num + 1




r = requests.get('http://localhost:4000/check-task?clientId=qweqwe&taskTypes=3005')
res = json.loads(r.text)
print r.text
print r.content
print res
print 123456
print res['data']
for i in res['data']['param']['actors']:
    print i
print res['data']['_id']