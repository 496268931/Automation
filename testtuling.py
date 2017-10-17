# -*- coding: utf-8 -*-
import json

import requests

def getText():
    url = 'http://www.tuling123.com/openapi/api'
    data = {'key':'c572878ae4774d8f94ae14a59b39562c','info':'豆瓣','loc':'北京市中关村',
        'userid':'496268931@qq.com'}

    x = requests.post(url=url, data=data)
    text = json.loads(x.text)['text']
    print text
    return text

def getKeyWord():

    url1 = 'http://fileload.datagrand.com:8080/ner'
    data1 = {'text':'U英伦对决[星星][星星][星星][半星]，成龙大哥余威不减，依然领跑假期档[笑而不语]#虎啸数据#','types':'person,location,org'}

    x1 = requests.post(url=url1, data=data1)
    print x1.text
    for i in json.loads(x1.text)['person']:
        print i

def getkey():
    url = 'http://bosonnlp.com/analysis/ner?category=&sensitivity=5'
    data = {'data' :'#白夜追凶# ' \
                  '昨日完结，心里空空荡荡的，肯定不只虎啸君有这种感觉！简直想向全世界安利这部剧，上线几集通过口碑发酵俨然已成爆款，悬念丛生，情节上乘，演员爆发力高，每个镜头都是干货！豆瓣为此贡献了9.1高分，讨论量持续高涨，#潘粤明# 为此也赢来了事业的第二春！不说了！虎啸君要再刷一遍！...全文： http://m.weibo.cn/5664409818/4162138677134197 ​'}
    x = requests.post(url=url, data=data)
    print x.text


if __name__ == '__main__':
    # getText()
    # getKeyWord()
    # getkey()
    # z = [1]
    # if z:
    #     print 123
    # else:
    #     print 234
    # File: readline-example-3.py
    file = open(u"F:\\影视剧字幕语料库(www.shareditor.com)\\subtitle.corpus")
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            print line
            # pass # do something