# -*- coding: utf-8 -*-
import base64
import requests
import json

print('send data....')

#第一种写法
# f = open('showapi.png', 'rb')
# b_64 = base64.b64encode(f.read())
# # print b_64
# f.close()
#第二种写法
with open('showapi.png', 'rb') as f:
    b_64 = base64.b64encode(f.read())


showapi_appid="49831"  #替换此值
showapi_sign="46325613a25244d6ac8a87835e3ba8c2"   #替换此值
url="http://route.showapi.com/184-5"


data = {'showapi_appid': showapi_appid, 'showapi_sign': showapi_sign, 'img_base64': b_64,
       'typeId': "3040", 'convert_to_jpg': "1"}


try:

    response = requests.post(url,data=data)
except Exception as e:
    print(e)
result = response.text.decode('utf-8')
print result
result_json = json.loads(result)
print result_json['showapi_res_body']['Result']