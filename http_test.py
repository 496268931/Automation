#coding=utf-8

import requests
import json


title = '羞羞的铁拳'
title1 = u'羞羞的铁拳'
print(type(title))
print(type(title1))

actors = ['沈腾', '马丽', '艾伦', '田雨 ', '薛皓文', '黄才伦', '常远']
print ''.join(actors)
print type(''.join(actors))
print(type(actors))
print(json.dumps(actors, ensure_ascii=False))
print(type(json.dumps(actors, ensure_ascii=False)))
minScore = 7
maxScore = 10
prototypes = {'唐人街探案': '56442c2b4f3854a2007db4d5', '夏洛特烦恼': '56442bd94f3854a2007db483',
              '一念天堂': '56442c2e4f3854a2007db4d6'}
print(type(prototypes))
print(json.dumps(prototypes, ensure_ascii=False))
print(type(json.dumps(prototypes, ensure_ascii=False)))
#
# print json.dumps(actors, ensure_ascii=False)
# print type(json.dumps(actors, ensure_ascii=False))
# time.sleep(1000)
count = 2

url = "http://47.93.113.175:9000/generate/comment"
payload = {'title': title, 'actors': json.dumps(actors, ensure_ascii=False), 'maxScore': maxScore, 'minScore': minScore,
           'prototypes': json.dumps(prototypes, ensure_ascii=False),
           'count': count}
# r = requests.post(url, data=payload)
# r = requests.post('http://httpbin.org/post', data=payload)
# r = requests.post('http://www.gongjuji.net', data=payload)
# print(r.text)
