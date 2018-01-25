# -*- coding: utf-8 -*-
import base64
import requests
import json

from com.aliyun.api.gateway.sdk.util import showapi

print('send data....')
'''无用
#第一种写法
# f = open('showapi.png', 'rb')
# b_64 = base64.b64encode(f.read())
# # print b_64
# f.close()
'''
# 第二种写法
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

'''
# 调用阿里云的接口，现在已经无法充值
# picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
# driver.save_screenshot(picName)
# time.sleep(1)
#
# # 裁切图片
# img = Image.open(picName)
#
# region = (1095, 208, 1169, 240)
# cropImg = img.crop(region)
#
# # 保存裁切后的图片
# picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(
#     datetime.datetime.now())) + '.png'
# cropImg.save(picNameCut)
# time.sleep(2)

# 进行验证码验证
f = open('showapi.png', 'rb')
b_64 = base64.b64encode(f.read())
# print b_64
f.close()
req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode",
                             "4e5510e696c748ca8d5033dd595bfbbc")
json_res = req.addTextPara("typeId", "3040") \
    .addTextPara("img_base64", b_64) \
    .addTextPara("convert_to_jpg", "1") \
    .post()

print (json_res)    #<type 'str'>
# print type(json_res)
# "{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"edj3\",\"ret_code\":0,\"Id\":\"42b38146-3495-4cd7-9544-26531bc48e3c\"}}"

result = json.loads(str(json_res[1:-1]).replace('\\', ''))
yanzhengma = result['showapi_res_body']['Result']
print yanzhengma
'''