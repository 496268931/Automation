# coding=utf-8
import os

import re

import datetime
import requests
import json
import base64

import time

from PIL import Image
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from com.aliyun.api.gateway.sdk.util import showapi


def login(username, password):
    username = base64.b64encode(username.encode('utf-8')).decode('utf-8')
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    loginURL = r'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)'
    session = requests.Session()
    print session
    res = session.post(loginURL, data = postData)
    print res
    jsonStr = res.content.decode('gbk')
    print jsonStr
    info = json.loads(jsonStr)
    print info

    if info["retcode"] == "0":
        print("登录成功")
        # 把cookies添加到headers中，必须写这一步，否则后面调用API失败
        cookies = session.cookies.get_dict()
        print cookies
        print type(cookies)

        # cookies = [key + "=" + value for key, value in cookies.items()]
        # cookies = "; ".join(cookies)
        # print cookies
        # print type(cookies)

        session.headers["cookie"] = cookies

    else:
        print("登录失败，原因： %s" % info["reason"])

    print session

    return cookies

def main():
    cookies = login('dcu1234947@sina.cn', 'vadjnrwa1701u')
    response=requests.get('http://weibo.com/', cookies=cookies)
    print response.text
    driver = webdriver.Firefox()
    driver.get(r'https://weibo.com')
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="loginname"]')).click()
    driver.delete_all_cookies()
    for k, v in cookies.iteritems():
        print "dict[%s]=" % k, v
        driver.add_cookie({'name': k, 'value': v})
    time.sleep(2)
    driver.refresh()
    time.sleep(2)


    # driver = webdriver.Firefox()
    # driver.get(r'https://weibo.com/')
    # driver.delete_all_cookies()
    # #driver.maximize_window()
    # print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="loginname"]')).click()
    # print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # #driver.find_element_by_xpath('//*[@id="loginname"]').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="loginname"]').clear()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="loginname"]').send_keys('kva84723526@sina.cn')
    # time.sleep(2)
    #
    #
    #
    # driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').click()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').clear()
    # time.sleep(1)
    # driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys('EO1iRkiNLBPy')
    # time.sleep(2)
    #
    #
    #
    # if driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/a/img').is_displayed():
    #     # 如果存在验证码图片
    #     print('有验证码')
    #
    #     picName = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
    #     driver.save_screenshot(picName)
    #     time.sleep(1)
    #
    #     # 裁切图片
    #     img = Image.open(picName)
    #
    #     region = (1005, 236, 1105, 270)
    #     cropImg = img.crop(region)
    #
    #     # 保存裁切后的图片
    #     picNameCut = os.path.abspath('.') + '\\' + re.sub(r'[^0-9]', '', str(datetime.datetime.now())) + '.png'
    #     cropImg.save(picNameCut)
    #     time.sleep(2)
    #
    #     # 进行验证码验证
    #     f = open(picNameCut, 'rb')
    #     b_64 = base64.b64encode(f.read())
    #     f.close()
    #     req = showapi.ShowapiRequest("http://ali-checkcode.showapi.com/checkcode", "4e5510e696c748ca8d5033dd595bfbbc")
    #     json_res = req.addTextPara("typeId", "3050") \
    #         .addTextPara("img_base64", b_64) \
    #         .addTextPara("convert_to_jpg", "1") \
    #         .post()
    #
    #     # print ('1')
    #     # print ('json_res data is:', json_res)
    #     print (json_res)
    #     json_res
    #     # str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"
    #
    #
    #
    #     result = json.loads(str(json_res[1:-1]).replace('\\', ''))
    #     yanzhengma = result['showapi_res_body']['Result']
    #
    #     print yanzhengma
    #     time.sleep(2)
    #
    #
    #     driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').click()
    #     time.sleep(1)
    #     driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').clear()
    #     time.sleep(1)
    #     driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[3]/div/input').send_keys(yanzhengma)
    #     time.sleep(2)
    #
    #     os.remove(picName)
    #     time.sleep(1)
    #     os.remove(picNameCut)
    #     time.sleep(1)
    #
    #
    #
    # driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    # time.sleep(15)
    #
    #
    # cook = driver.get_cookies()
    # print cook
    # for i in cook:
    #
    #     print i['name'] + '=' + i['value']
    #
    # driver.quit()
    # driver = webdriver.Firefox()
    # driver.get(r'https://weibo.com')
    #
    # print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    # WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="loginname"]')).click()
    # print('本次评论开始时间： '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #
    # driver.delete_all_cookies()
    # for j in cook:
    #
    #     driver.add_cookie({'name': j['name'], 'value': j['value']})
    #
    #
    #
    # driver.refresh()
    # cook1 = driver.get_cookies()
    # print cook1
    # for k in cook1:
    #
    #     print k['name'] + '=' + k['value']


if __name__ == '__main__':
    #main()
    # for i in range(1,200):
    #     r = requests.get('http://www.toutiao.com/i6445080545176060429/')
    #     #print r.text
    #     print i
    #     print r.status_code

    pattern = re.compile(r'\d+')
    result = re.match(pattern, 'a31b2c3d4')
    if result:
        print result.group()
    else:
        print result    #None

    print re.search(pattern, 'a31b2c3d4').group()
    print re.split(pattern, 'a1b2c3d4')