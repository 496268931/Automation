# coding=utf-8
import random
import time
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


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






def zhidao_sign(driver):

    # login(driver, username, password)
    if driver.find_element_by_class_name('header-meta-attendance').find_element_by_tag_name('a').text != '已签到'.decode('utf-8'):
        print '未签到'
        driver.find_element_by_class_name('header-meta-attendance').find_element_by_tag_name('a').click()
        time.sleep(2)

        # 点击签到
        driver.find_element_by_id('sign-in-btn').click()
        time.sleep(2)
        # 点击关闭
        driver.find_element_by_class_name('close-layer').click()
        time.sleep(2)

        driver.refresh()
        time.sleep(2)

def zhidao_ask_question(driver, username, password, question1, question2):
    login(driver, username, password)

    driver.get('https://zhidao.baidu.com/ihome/homepage/recommendquestion')
    time.sleep(1)

    # 弹出礼物窗口
    if isElementExistByXPath("//a[contains(@class, 'mygift-btn')]", driver):
        print '领取礼物'
        driver.find_element_by_xpath("//a[contains(@class, 'mygift-btn')]").click()


    #签到
    zhidao_sign(driver)

    driver.find_element_by_id('ask-btn').click()
    time.sleep(10)

    driver.find_element_by_id('title-area').click()
    time.sleep(1)
    driver.find_element_by_id('title-area').clear()
    time.sleep(1)
    driver.find_element_by_id('title-area').send_keys(question1)
    time.sleep(1)

    driver.find_element_by_id('content-area').click()
    time.sleep(1)
    driver.find_element_by_id('content-area').clear()
    time.sleep(1)
    driver.find_element_by_id('content-area').send_keys(question2)
    time.sleep(1)


    if driver.find_element_by_id('phone').get_attribute('class').find('cb-status-on') >= 0:
        print '取消发短信'
        driver.find_element_by_id('phone').click()
        time.sleep(2)

    if driver.find_element_by_xpath("//li[contains(@class, 'offer-reward clearfix')]/div[1]/span").get_attribute('class').find('cb-status-on') >= 0:
        print '取消悬赏'
        driver.find_element_by_xpath("//li[contains(@class, 'offer-reward clearfix')]/div[1]/span").click()
        time.sleep(2)

    driver.find_element_by_id('submit-btn').click()
    time.sleep(10)

    zhidao_question_url = driver.current_url
    print zhidao_question_url
    return zhidao_question_url
    # https://zhidao.baidu.com/question/1866600782209937787.html
    # https://zhidao.baidu.com/question/1866600910027358547.html


def zhidao_answer_question(driver, zhidao_question_url, username2, password2, answer_word):

    # 登录另一个账号
    login(driver, username2, password2)


    driver.get('https://zhidao.baidu.com/ihome/homepage/recommendquestion')
    time.sleep(2)
    zhidao_sign(driver)

    driver.get(zhidao_question_url)
    time.sleep(1)

    driver.switch_to.frame(driver.find_element_by_id("ueditor_0"))

    driver.find_element_by_xpath('/html/body/p').click()
    time.sleep(5)


    driver.find_element_by_xpath('/html/body/p').send_keys(answer_word)
    time.sleep(2)

    driver.switch_to_default_content()
    time.sleep(5)

    driver.find_element_by_xpath('//*[@id="answer-editor"]/div[2]/a').click()
    time.sleep(5)

def zhidao_accept_answer(driver, zhidao_question_url, username, password):
    # 切换回提问账号
    login(driver, username, password)


    driver.get(zhidao_question_url)
    time.sleep(1)

    driver.find_element_by_xpath("//a[contains(@id, 'adopt-ask-')]").click()
    time.sleep(2)


def zhidao(username, password, username2, password2, question1, question2, answer_word):
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



    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # #提出问题
    # zhidao_question_url = zhidao_ask_question(driver, username, password, question1, question2)
    # driver.quit()
    # time.sleep(60)



    print '切换账号回答问题'
    driver = webdriver.Firefox()
    driver.maximize_window()
    zhidao_answer_question(driver, 'https://zhidao.baidu.com/question/437977126421837804.html', username2, password2, answer_word)
    # driver.quit()
    #
    #
    # print '再切换回提问账号 采纳并领取奖励'
    # driver = webdriver.Firefox()
    # driver.maximize_window()
    #
    # zhidao_accept_answer(driver, 'https://zhidao.baidu.com/question/437977126421837804.html', username, password)



if __name__ == '__main__':
    username = '18500346307'
    password = 'sjfwbznb'

    username2 = '18680663489'
    password2 = 'wiseR00t'

    question1 = u'电影"生化危机"系列讲的是什么'
    question2 = u'生化危机系列电影的相关信息'
    answer_word = u'《生化危机》系列电影改编自capcom游戏《生化危机》，由保罗·安德森执导，米拉·乔沃维奇主演。第一部《生化危机》于2002' \
                  u'年上映，先后推出了《生化危机：启示录》（2004年）、《生化危机：灭绝》（2007）、《生化危机：战神再生》（2010年）、《生化危机：惩罚》（2012年），《生化危机：终章》（2017年）为该系列电影终结篇。[1]2017年5月，德国康斯坦丁影业确认将重启《生化危机》系列，并计划制作六部电影。[2] '
    zhidao(username, password, username2, password2, question1, question2, answer_word)