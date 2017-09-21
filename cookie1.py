# coding=utf-8
import json

import requests

# cookies = {'bid': '0HZ8w7vIzDU', 'dbcl2': '"121892422:7k+dHEvklKs"'}
# testurl='http://www.douban.com/people/71263652/'
# s=requests.get(testurl, cookies=cookies)
# print s.status_code
# print s.text

# accountId = '18513199891'
# password = '1qaz2wsx'
import time
from selenium import webdriver

platform = '豆瓣'
# cookies = None
# cookiesStr = json.JSONEncoder().encode(cookies) #dict转str
# #print type(cookiesStr)
# testurl ='http://114.215.170.176:4000/add-account'
# data = {'accountId': accountId, 'password': password, "platform": platform, 'data': cookiesStr}
# s=requests.post(testurl, data=data)
# print s.text
# print s.status_code

# testurl = 'http://114.215.170.176:4000/get-account'
# req = requests.get(testurl, params = {'platform': platform})  #json字符串
# r = json.JSONDecoder().decode(req.text)   #json转成dict
# rr = json.JSONDecoder().decode(r['data']['data'])
# print req.text
# print type(req.text)    #<type 'unicode'>
# print r
# print type(r)   #<type 'dict'>
# print r['data']['data']
# print type(r['data']['data'])   #<type 'unicode'>
# print rr
# print type(rr)  #<type 'dict'>
# print isinstance(rr, dict)  #True
# print rr['bid']
# print rr['dbcl2']#


# cookies = {'dbcl2': '"121892422:7k+sdf"'}
# testurl = 'http://114.215.170.176:4000/update-account'
# req = requests.post(testurl, data={'accountId': '18513199891', 'password': '1qaz2wsx', 'platform': '豆瓣', 'data': json.JSONEncoder().encode(cookies)})
# print req.text


# driver = webdriver.Chrome()
# driver.get('https://movie.douban.com/subject_search?search_text=2017&cat=1002&start=105')
# driver.delete_all_cookies()
# # driver.maximize_window()
# # time.sleep(2)
# cookies = {'dbcl2': '"121892422:K4ZBC0dF8Kg"'}
# response=requests.get('https://movie.douban.com/subject_search?search_text=2017&cat=1002&start=105', cookies=cookies)
# print response.status_code
# print response.text
# # driver.add_cookie({'name': 'bid', 'value': cookies['bid']})
# driver.add_cookie({'name': 'dbcl2', 'value': cookies['dbcl2']})
# time.sleep(1)
# driver.refresh()


# response=requests.get('http://114.215.170.176:4000/check-task', params={'clientId': '218.241.214.234', 'taskTypes': '712'})
# print response.text
# #{"result":"ok","data":null}
# print json.JSONDecoder().decode(response.text)['data']
# print json.JSONDecoder().decode(response.text)['data']['taskUrl']

# response=requests.post('http://114.215.170.176:4000/report-task', data={'clientId': '218.241.214.234', 'taskId': '59c0e0154c0410386ce37cfd', 'status': '0'})
# print response.text

response=requests.get('http://114.215.170.176:4000/check-task', params={'clientId':  '218.241.214.234', 'taskTypes': '712'})
print response.text