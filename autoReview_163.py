# coding=utf-8
from selenium import webdriver

import time

from com.aliyun.api.gateway.sdk.util import showapi

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

driver = webdriver.Firefox()
# driver  = webdriver.Chrome()

# driver.get("http://comment.news.163.com/news2_bbs/CPISM0FT000189FH.html")
driver.get("http://comment.news.163.com/news2_bbs/CPMT4G4F0001899N.html")

driver.maximize_window()
time.sleep(2)
print('wait')
# driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部
# driver.switch_to.frame('iframe')

##############################################################

# 点击登录
driver.find_element_by_xpath('/html/body/div[8]/div[1]/div[1]/div[1]/div[1]/a').click()
time.sleep(2)

# 将页面滚动条拖到底部
# js = "var q=document.body.scrollTop=100000"
js = "var q=document.documentElement.scrollTop=10000"


#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
def isElementExist(element):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag


'''
exist=True
i=0
while exist:

    if isElementExist('//*[@id="YT-ytaccount"]'):#找到登录框
        #exist=False
        print('登录框')
        break
    driver.execute_script(js)
    i+=1
    print(i)
'''

# 输入账号密码
if isElementExist('//*[@id="loginForm"]/p[1]/input'):
    # driver.switch_to.frame('login_frame')


    # 输入账号
    # driver.find_element_by_xpath('//*[@id="YT-normalLogin"]/div[1]/label/span[1]').clear()
    driver.find_element_by_xpath('//*[@id="quickPostLogin"]/label[1]/input').send_keys("i493735")
    # 输入密码
    # driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/div/div[2]/div/p').clear()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="quickPostLogin"]/label[2]/input').send_keys("aaafff")
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="quickPostLogin"]/div/a').click()
    time.sleep(2)

'''
    #截图验证码并进行剪裁           下面的是判断验证码输入框是否存在，如果不行，换成前面的登录按钮
    if isElementExist('//*[@id="dologin"]'):

        driver.switch_to.frame('x-URS-iframe1500343362826.9832')

        picName=os.path.abspath('.')+'\\'+re.sub(r'[^0-9]','',str(datetime.datetime.now()))+'.png'
        driver.save_screenshot(picName)
        time.sleep(1)


        #裁切图片
        img = Image.open(picName)
        region = (73,110,220,160)
        cropImg = img.crop(region)

        #保存裁切后的图片
        picNameCut=os.path.abspath('.')+'\\'+re.sub(r'[^0-9]','',str(datetime.datetime.now()))+'.png'
        cropImg.save(picNameCut)
        time.sleep(2)


        #进行验证码验证
        f=open(picNameCut,'rb')
        b_64=base64.b64encode(f.read())
        f.close()
        req=showapi.ShowapiRequest(  "http://ali-checkcode.showapi.com/checkcode","4e5510e696c748ca8d5033dd595bfbbc"   )
        json_res=req.addTextPara("typeId","3040") \
            .addTextPara("img_base64",b_64) \
            .addTextPara("convert_to_jpg","1") \
            .post()

        #print ('1')
        #print ('json_res data is:', json_res)
        print (json_res)
        json_res
        #str="{\"showapi_res_code\":0,\"showapi_res_error\":\"\",\"showapi_res_body\":{\"Result\":\"28ht\",\"ret_code\":0,\"Id\":\"adb1c363-d566-48a6-820e-55859428599d\"}}"

        int=json_res.find('Result')
        yanzhengma=json_res[int+11:int+15]
        print(yanzhengma)

        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[1]').send_keys(yanzhengma[0:1])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[2]').send_keys(yanzhengma[1:2])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[3]').send_keys(yanzhengma[2:3])
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/div/div/input[4]').send_keys(yanzhengma[3:4])
        time.sleep(1)

        driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div/div/a[2]').click()

'''

driver.find_element_by_xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div[1]/a').click()  # 快速发帖
time.sleep(2)
# 输入评论
driver.find_element_by_xpath('//*[@id="quickPostBody"]').clear()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="quickPostBody"]').send_keys("养狗要有责任心，对狗狗要负责任".decode())
# 打印评论内容
print(driver.find_element_by_xpath('//*[@id="quickPostBody"]').get_attribute('value'))
# 马上发表
driver.find_element_by_xpath('//*[@id="quickPostForm"]/div/a').click()
time.sleep(2)

print('end')


# driver.quit()
