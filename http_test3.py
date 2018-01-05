#coding=utf-8
import requests
import json

# _id = "5a3b0c01c2a90c20ac1c6c29"
# userId = "5a154d06693818312043d94b"
# createTime = "2017-12-20T16:35:24+08:00"
# updateTime = "2017-12-20T16:35:24+08:00"
#
# title = '羞羞的铁拳'
# actors = json.dumps(["沈腾", "马丽", "艾伦", "田雨 ", "薛皓文", "黄才伦", "常远"])
# minScore = '1'
# maxScore = '10'
# prototypes = json.dumps({"唐人街探案": "56442c2b4f3854a2007db4d5", "夏洛特烦恼": "56442bd94f3854a2007db483"})
# count = '5'
#
# url = "http://47.93.113.175:9000/generate/comment"
# payload = {'_id': _id,
#            'userId': userId,
#            'title': title,
#            'actors': json.dumps(actors, ensure_ascii=False),
#            'maxScore': maxScore,
#            'minScore': minScore,
#            'prototypes': json.dumps(prototypes, ensure_ascii=False),
#            'count': count}
# r = requests.post(url, data=payload)
# print(r.text)

prototypes = {"唐人街探案": "56442c2b4f3854a2007db4d5", "夏洛特烦恼": "56442bd94f3854a2007db483"}
print list(prototypes.keys())
print list(prototypes.values())
print prototypes