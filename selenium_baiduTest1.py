# -*- coding: utf8 -*-
# author: hrwhisper
# blog  : hrwhisper.me
# date  : 2015.5.3

import requests
import urllib
import urllib2
import re
import cookielib

class baiduLogin:
    url_token = 'https://passport.baidu.com/v2/api/?getapi&tpl=pp&apiver=v3&tt=1426660772709&class=login&logintype=basicLogin&callback=bd__cbs__hif73f'
    url_login = 'https://passport.baidu.com/v2/api/?login'
    url_tieba = 'http://tieba.baidu.com/f/like/mylike?v=1387441831248'
    s = requests.Session()

    def startLogin(self,username,password):
        #urllib2.install_opener(self.opener)
        postData = {
            'username' : username,
            'password' : password,
            'token' : self.getToken(),
            'charset' : 'UTF-8',
            'apiver' : 'v3',
            'isPhone' : 'false',
            'tpl' : 'tb',
            'u' : 'https://passport.baidu.com/',
            'staticpage' : 'https://passport.baidu.com/static/passpc-account/html/v3Jump.html',
            'callback' : 'parent.bd__pcbs__ra48vi'
        }

        myhead={
            'Host': 'passport.baidu.com',
            'Referer': 'https://passport.baidu.com/v2/?login',
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36'  ,
        }
        self.s.post(self.url_login,data=postData,headers=myhead)


    def getToken(self):
        r = self.s.get(u'http://www.baidu.com/')
        r = self.s.get(self.url_token)
        #取个别名并且从分组中取出token
        token = re.search(u'"token" : "(?P<token>.*?)"',r.text)
        print token.group('token')
        return token.group('token')

    def getMyTieBa(self):
        tieba = self.s.get(self.url_tieba)
        tieba.encoding = 'gbk'
        print tieba.text

username = '18500346307'
password = 'sjfwbznb'
baidu = baiduLogin()
baidu.startLogin(username, password)
baidu.getMyTieBa()