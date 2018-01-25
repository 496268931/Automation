# -*- coding: utf-8 -*-
import requests
import re
from lxml import etree


def login_baidu(user, password):
    # get之后获得cookies
    session.get('http://www.baidu.com')
    session.get('https://passport.baidu.com/v2/api/?login')
    # 带着cookies访问，获取token
    token_data = session.get('https://passport.baidu.com/v2/api/?getapi&tpl=mn&apiver=v3').text
    token = re.findall(r'"token" : "(.*?)"', token_data)[0]
    print token_data
    print(token)

    # 构造headers
    headers = {
        'Host': 'passport.baidu.com',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'h-CN,zh;q=0.8,en;q=0.6'
    }

    # 构造POST data
    data = {
        "token": token,
        "tpl": "mn",
        "loginmerge": True,
        "username": user,
        "password": password
    }

    login = session.post('https://passport.baidu.com/v2/api/?login', data=data, headers=headers)
    print login
    print session.cookies
    if 'BDUSS' in session.cookies:
        print("登录成功")
    else:
        print("登录失败")

    web_data = session.get('http://www.baidu.com').text
    page = etree.HTML(web_data)
    my_name = page.xpath(u'//span[@class="user-name"]/text()')
    print(my_name)


if __name__ == '__main__':
    # 构造一个会话，用来跨请求保存cookie
    session = requests.Session()
    user = '18500346307'
    password = 'sjfwbznb'
    login_baidu(user, password)

