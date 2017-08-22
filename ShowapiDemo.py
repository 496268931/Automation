# -*- coding: utf-8 -*-
from com.aliyun.api.gateway.sdk.util import showapi
import json
import base64


#get
req=showapi.ShowapiRequest(  "请求地址，比如http://ali-weather.showapi.com/area-to-weather","appcode"   )
json_res=req.addTextPara("para1_name","para1_value")\
   .addTextPara("para2_name","para2_value")\
   .addTextPara("para3_name","para3_value")\
   .get()
# #最后如果是post提交则换成.post()
print ('json_res data is:', json_res)



#post form
# f=open(r'c:\a.jpg','rb')
# b_64=base64.b64encode(f.read())
# f.close()
# req=showapi.ShowapiRequest( "请求地址，比如http://ali-checkcode.showapi.com/checkcode","appcode" )
# json_res= req.addTextPara("typeId","3040")\
#     .addTextPara("img_base64",b_64)\
#     .addTextPara("convert_to_jpg","1")\
#     .post()
# print ('json_res data is:', json_res)

