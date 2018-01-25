# coding=utf-8
import json

from pip._vendor.requests.sessions import Session

global username, password, token
username = '18500346307'
password = 'sjfwbznb'
s = Session()


# python2.x与python3.x差别非常大
# 过去使用urllib，urllib2，现在使用request包

def showCookie(cookies):
    for i in cookies:
        print(i)
        i.domain = '*'
    print('*' * 20)


# 第一步，访问百度，获取cookie百度ID
s.get("http://www.baidu.com")
# 第二步，访问密码网页，获取token，此页面返回一个json串。后面的参数不同返回的结果不同，抓包之后，尝试着删除了许多没用的参数
resp = s.get("https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3")
# json.dumps可以识别包含单引号的json串，json.loads却不能
t = json.loads(resp.text.replace('\'', '\"'))
print t
token = t['data']['token']
print token
# 第三步，提交表单。经过测试，只有下面五个数据是必需的
data = {
    "token": token,
    "tpl": "tb",
    "loginmerge": True,
    "username": username,
    "password": password
}
resp = s.post("https://passport.baidu.com/v2/api/?login", data)
print resp.text
print resp.status_code