#coding=utf-8
import requests
import json


title = '芳华'
actors = ['黄轩', '苗苗', '钟楚曦']
print(type(actors))

minScore = 7
maxScore = 10
prototypes = {'烽火芳菲': '59a79ae180ffbf169b327d7f', '密战': '56ebc5960c0c25fa083cf420'}
print(type(prototypes))

count = 100

url = "http://47.93.113.175:9000/generate/comment"
payload = {'title': title, 'actors': json.dumps(actors, ensure_ascii=False), 'maxScore': maxScore, 'minScore': minScore,
           'prototypes': json.dumps(prototypes, ensure_ascii=False),
           'count': count}
r = requests.post(url, data=payload)
print(r.text)
