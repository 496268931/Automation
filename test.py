# -*- coding: utf-8 -*
import os

import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

import ZZZautoReview_163
import ZZZautoReview_gewala
import ZZZautoReview_qiy
import ZZZautoReview_sohu
import ZZZautoReview_youku

'''
projectName='Mate 8'
filename="../"+projectName+"_PicsDetectedResults_" + re.sub(r'[^0-9]','',str(datetime.datetime.now())) + '.xml'
print filename
filename="../"+projectName+"_PicsDetectedResults_" + re.sub(r'[^0-9]','',str(datetime.datetime.now())) + '.xml'

print filename

h=float(input('请输入你的身高：'))
w=float(input('请输入你的体重：'))
bmi=(w/(h*h))
if bmi<18.5:
    print('体重过轻！')
elif bmi<=25:
    print('体重正常！')
elif bmi<=28:
    print('体重过重！')
elif bmi<=32:
    print('体重肥胖！')
else:
    print('体重严重肥胖！！！')


print os.path.abspath('.')

print os.path.abspath('..')

s='1'
n=int(s)
print n


import urllib2
url = "http://api.tianma168.com/tm/Login?uName=tianma8888&pWord=123456789"
req = urllib2.Request(url)
#print req
res_data = urllib2.urlopen(req)
res = res_data.read()
token = res[0:res.index('&')]
print res
print token
'''

#ZZZautoReview_youku.main('http://v.youku.com/v_show/id_XMjkxMzk0OTIyNA==.html?spm=a2htv.20009910.m_86821.5~5!2~5~5!2~A','17097352190', 'abc17097352190',u'超级无敌喜欢这部剧')
#ZZZautoReview_qiy.main('http://www.iqiyi.com/v_19rr769c4s.html#vfrm=3-2-0-0', '15011335008','my0316WY','超级无敌喜欢这部剧啊啊啊啊啊啊'.decode())
#ZZZautoReview_163.main('http://comment.news.163.com/news2_bbs/CPMT4G4F0001899N.html','i493735',
# 'aaafff',u'养狗要有责任心，对狗狗要负责任')
#ZZZautoReview_sohu.main('http://www.sohu.com/a/160145302_467279', 'mkt45196@sina.cn',
# 'faCTpTN5ukQy', u'文章讲的非常好，就是要紧跟时尚，享受生活')
#ZZZautoReview_gewala.main('http://www.gewara.com/movie/315849910', '17031511791',
# 'abc17031511791', u'像吴京这样努力的人，必然会成功的')
'''
import time
# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

'''
