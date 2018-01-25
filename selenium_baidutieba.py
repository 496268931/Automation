# coding=utf-8
import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

tieba_UrlList = [

    'http://tieba.baidu.com/f?kw=网剧&fr=index',
    'http://tieba.baidu.com/f?kw=游戏&fr=index',
    'http://tieba.baidu.com/f?kw=音乐&fr=index',
    'http://tieba.baidu.com/f?kw=动漫&fr=index',
    'http://tieba.baidu.com/f?kw=电视剧&fr=index',
    'http://tieba.baidu.com/f?kw=影视&fr=index',
    'http://tieba.baidu.com/f?kw=明星&fr=index',
    'http://tieba.baidu.com/f?kw=电影&fr=index',
    'http://tieba.baidu.com/f?kw=韩雪',
    'http://tieba.baidu.com/f?kw=李小璐',
    'http://tieba.baidu.com/f?kw=张天爱',
    'http://tieba.baidu.com/f?kw=马苏',
    'http://tieba.baidu.com/f?kw=迪丽热巴',
    'http://tieba.baidu.com/f?kw=赵丽颖',
    'http://tieba.baidu.com/f?kw=江疏影',
    'http://tieba.baidu.com/f?kw=秦岚',
    'http://tieba.baidu.com/f?kw=关晓彤',
    'http://tieba.baidu.com/f?kw=张歆艺',
    'http://tieba.baidu.com/f?kw=杨幂',
    'http://tieba.baidu.com/f?kw=angelababy',
    'http://tieba.baidu.com/f?kw=郑爽',
    'http://tieba.baidu.com/f?kw=张钧甯',
    'http://tieba.baidu.com/f?kw=刘亦菲',
    'http://tieba.baidu.com/f?kw=蒋欣',
    'http://tieba.baidu.com/f?kw=刘诗诗',
    'http://tieba.baidu.com/f?kw=范冰冰',
    'http://tieba.baidu.com/f?kw=唐嫣',
    'http://tieba.baidu.com/f?kw=林心如',
    'http://tieba.baidu.com/f?kw=章子怡',
    'http://tieba.baidu.com/f?kw=古力娜扎',
    'http://tieba.baidu.com/f?kw=柳岩',
    'http://tieba.baidu.com/f?kw=景甜',
    'http://tieba.baidu.com/f?kw=李沁',
    'http://tieba.baidu.com/f?kw=周冬雨',
    'http://tieba.baidu.com/f?kw=高圆圆',
    'http://tieba.baidu.com/f?kw=佟丽娅',
    'http://tieba.baidu.com/f?kw=杨紫',
    'http://tieba.baidu.com/f?kw=宋茜',
    'http://tieba.baidu.com/f?kw=刘涛',
    'http://tieba.baidu.com/f?kw=陈乔恩',
    'http://tieba.baidu.com/f?kw=杨蓉',
    'http://tieba.baidu.com/f?kw=林志玲',
    'http://tieba.baidu.com/f?kw=郭碧婷',
    'http://tieba.baidu.com/f?kw=郭采洁',
    'http://tieba.baidu.com/f?kw=刘萌萌',
    'http://tieba.baidu.com/f?kw=唐艺昕',
    'http://tieba.baidu.com/f?kw=阚清子',
    'http://tieba.baidu.com/f?kw=戚薇',
    'http://tieba.baidu.com/f?kw=张馨予',
    'http://tieba.baidu.com/f?kw=王丽坤',
    'http://tieba.baidu.com/f?kw=林允儿',
    'http://tieba.baidu.com/f?kw=李冰冰',
    'http://tieba.baidu.com/f?kw=邓家佳',
    'http://tieba.baidu.com/f?kw=娄艺潇',
    'http://tieba.baidu.com/f?kw=袁姗姗',
    'http://tieba.baidu.com/f?kw=王珞丹',
    'http://tieba.baidu.com/f?kw=毛晓彤',
    'http://tieba.baidu.com/f?kw=陈紫函',
    'http://tieba.baidu.com/f?kw=姚晨',
    'http://tieba.baidu.com/f?kw=闫妮'

]

tieba_content = ['你们有见过这么整齐的十五个字吗',
           '这么整齐的十五个字人家最喜欢了',
           '他们都说打出十五字才是最标准的',
           '我也没办法因为我要打十五个字啊',
           '我说了多少次了不要只打十五个字',
           '你们那些十五字神马的完全弱爆了',
           '都怪吧主删我贴所以我只能到处逛',
           '为了经验我没办法只能遇贴就灌水',
           '灌水也要讲技术保证句句是十五字',
           '如今发帖有困难整不好就被删贴了',
           '我也没办法吧主他老是删我帖子啊',
           '只能够这样用十五字来混混经验了',
           '用十五字混经验的有谁比我厉害呢',
           '有前排就要占没前排也要灌一下水',
           '有前排不占或者不灌水是会后悔的',
           '无论是多么无聊的帖子我都会去的',
           '因为为了一句话万一这贴子火了呢',
           '句句十五个字有哪个高手能超越呢'
           ]
def getHttpIP():
    i = 0
    isDaili = 0
    while i < 6:
        r = requests.get('http://121.42.227.3:3838/getIp?clientId=123456')
        res = r.text

        if res != 'null\r\n':
            print '取到IP'

            proxies = {"http": "http://" + res.replace('\r\n', '')}
            testRes = requests.get('http://httpbin.org/ip', proxies=proxies)

            if None != testRes.text:
                print testRes.text
                isDaili = 1
                break
        print '未取到Ip'
        time.sleep(10)
        i = i + 1

    print res.replace('\r\n', ''), isDaili
    return res.replace('\r\n', ''), isDaili
def isElementExistById(element, driver):
    flag = True

    try:
        driver.find_element_by_id(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag

def isElementExistByXPath(element, driver):
    flag = True

    try:
        driver.find_element_by_xpath(element)
        return flag

    except:
        flag = False
        # driver.execute_script(js)
        return flag
def login(driver, username, password):

    driver.get('http://tieba.baidu.com/f?kw=网剧&fr=index')
    time.sleep(2)

    # 点击登录
    # WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a')).click()
    # 点击签到
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath('//*[@id="signstar_wrapper"]/a')).click()
    time.sleep(1)
    # 使用账号密码登录
    WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath("//*[contains(@class, 'login-username')]")).click()
    time.sleep(1)

    if isElementExistById('TANGRAM__PSP_9__userName', driver):
        print 9
        driver.find_element_by_id('TANGRAM__PSP_9__userName').click()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_9__userName').clear()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_9__userName').send_keys(username)
        time.sleep(1)

        driver.find_element_by_id('TANGRAM__PSP_9__password').click()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_9__password').clear()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_9__password').send_keys(password)
        time.sleep(1)

        # 点击登录
        driver.find_element_by_id('TANGRAM__PSP_9__submit').click()
        time.sleep(2)
    elif isElementExistById('TANGRAM__PSP_5__userName', driver):
        print 5
        driver.find_element_by_id('TANGRAM__PSP_5__userName').click()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_5__userName').clear()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_5__userName').send_keys(username)
        time.sleep(1)

        driver.find_element_by_id('TANGRAM__PSP_5__password').click()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_5__password').clear()
        time.sleep(1)
        driver.find_element_by_id('TANGRAM__PSP_5__password').send_keys(password)
        time.sleep(1)

        # 点击登录
        driver.find_element_by_id('TANGRAM__PSP_5__submit').click()
        time.sleep(2)
    time.sleep(10)




def tieba_sign(driver):
    try:
        # login(driver, username, password)

        for url in tieba_UrlList:
            print url
            driver.get(url)
            # j_signbtn sign_btn_bright j_cansign
            # j_signbtn signstar_signed
            time.sleep(2)




            if driver.find_element_by_id('j_head_focus_btn').get_attribute('class')!='focus_btn cancel_focus':
                print '该账号未关注本贴吧，点击关注'
                driver.find_element_by_id('j_head_focus_btn').click()
                time.sleep(2)
                if isElementExistByXPath("//a[contains(@class, 'dialogJclose')]", driver):
                    print '点击关注后，关掉弹出的小窗口'
                    driver.find_element_by_xpath("//a[contains(@class, 'dialogJclose')]").click()
                    time.sleep(2)

            while driver.find_element_by_xpath("//*[contains(@class, 'j_signbtn sign')]").get_attribute('title')=='签到'.decode('utf-8'):

                print driver.find_element_by_xpath("//*[contains(@class, 'j_signbtn sign')]").get_attribute('title')

                # 两次才能点上
                WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath("//*[contains(@class, 'j_signbtn sign')]")).click()
                time.sleep(1)
                WebDriverWait(driver, 30).until(lambda x: x.find_element_by_xpath("//*[contains(@class, 'j_signbtn sign')]")).click()
                time.sleep(1)
                driver.refresh()


                time.sleep(2)
                if driver.find_element_by_xpath("//*[contains(@class, 'j_signbtn sign')]").get_attribute('title')=='签到完成'.decode('utf-8'):
                    print driver.find_element_by_xpath("//*[contains(@class, 'j_signbtn sign')]").get_attribute('title')
                    break



            random_wait_time = random.randint(450, 750)
            print random_wait_time
            time.sleep(random_wait_time)
            print '----------本次签到结束----------'
        print '----------所有签到结束----------'


    except Exception as e:
        print e

    finally:
        print('---------我是分割线------------')

def tieba_review(driver):
    try:
        # login(driver, username, password)

        random_url = random.choice(tieba_UrlList)
        print random_url
        driver.get(random_url)

        random_all_tiezi = driver.find_elements_by_css_selector("[class=' j_thread_list clearfix']")
        # print random_all_tiezi
        print len(random_all_tiezi)

        random_one_url = random.choice(random_all_tiezi).find_element_by_xpath("//div[contains(@class, 't_con cleafix')]/div[2]/div[1]/div[1]/a").get_attribute('href')
        print random_one_url

        # https://tieba.baidu.com/p/5517149983可评论
        # http://tieba.baidu.com/p/5222335273不可评论
        driver.get(random_one_url)
        time.sleep(2)

        target = driver.find_element_by_id('ueditor_replace')
        driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去

        time.sleep(2)


        #有些贴吧是需要等级达到一定程度才能评论
        if isElementExistByXPath("//div[contains(@class, 'tb_poster_info poster_warning')]", driver):
            print driver.find_element_by_xpath("//div[contains(@class, 'tb_poster_info poster_warning')]").text
        else:

            print '可评论'
            time.sleep(1)
            driver.execute_script("var aaa=$('.tb_poster_placeholder').hide()")
            time.sleep(2)
            print 'js处理结束'

            target.click()
            time.sleep(1)
            target.clear()
            time.sleep(1)
            target.send_keys(random.choice(tieba_content).decode('utf-8'))
            time.sleep(2)
            driver.find_element_by_xpath("//a[contains(@class, 'j_submit poster_submit')]").click()
            time.sleep(5)
        time.sleep(10)


    except Exception as e:
        print e

    finally:
        print('---------我是分割线------------')








def tieba(username, password):
    # httpIp, isDaili = getHttpIP()
    # ip_ip = httpIp.split(":")[0]
    # ip_port = int(httpIp.split(":")[1])
    #
    # # 123.56.154.24:5818
    #
    # profile = webdriver.FirefoxProfile()
    # profile.set_preference('network.proxy.type', isDaili)
    # profile.set_preference('network.proxy.http', ip_ip)
    # profile.set_preference('network.proxy.http_port', ip_port)  # int
    # profile.update_preferences()
    # driver = webdriver.Firefox(firefox_profile=profile)

    driver = webdriver.Firefox()
    driver.maximize_window()
    login(driver, username, password)
    tieba_sign(driver)
    print '1111111111111111111111111111111111111111111111111111111111111111111111111111111111111'
    time.sleep(100000)
    tieba_review(driver)


    # driver.quit()




if __name__ == '__main__':
    username = '18500346307'
    password = 'sjfwbznb'

    username2 = '18680663489'
    password2 = 'wiseR00t'

    tieba(username, password)



    star = ['韩雪','李小璐','张天爱','马苏','迪丽热巴','赵丽颖','江疏影','秦岚','关晓彤','张歆艺','杨幂','angelababy','郑爽','张钧甯','刘亦菲','蒋欣','刘诗诗','范冰冰','唐嫣','林心如','章子怡','古力娜扎','柳岩','景甜','李沁','周冬雨','高圆圆','佟丽娅','杨紫','宋茜','刘涛','陈乔恩','杨蓉','林志玲','郭碧婷','郭采洁','刘萌萌','唐艺昕','阚清子','戚薇','张馨予','王丽坤','林允儿','李冰冰','邓家佳','娄艺潇','袁姗姗','王珞丹','毛晓彤','陈紫函','姚晨','闫妮']