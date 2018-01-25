# coding=utf-8
import requests

s = requests.Session()
a = s.get('http://www.baidu.com')
b =s.get('https://passport.baidu.com/v2/api/?login')
print
print b.text