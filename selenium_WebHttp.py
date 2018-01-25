# coding=utf-8
import json
import random

import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

'''
{
    "no":0,
    "error":"",
    "data":{
        "errno":0,
        "errmsg":"success",
        "sign_version":2,
        "is_block":0,
        "finfo":{
            "forum_info":{
                "forum_id":689,
                "forum_name":"篮球"
            },
            "current_rank_info":{
                "sign_count":25882
            }
        },
        "uinfo":{
            "user_id":3407844214,
            "is_sign_in":1,
            "user_sign_rank":25882,
            "sign_time":1516610933,
            "cont_sign_num":1,
            "total_sign_num":1,
            "cout_total_sing_num":1,
            "hun_sign_num":0,
            "total_resign_num":0,
            "is_org_name":0
        }
    }
}


{
    "no":1101,
    "error":"亲，你之前已经签过了",
    "data":""
}
'''
keywords = ['韩雪', '李小璐', '张天爱', '马苏', '迪丽热巴', '赵丽颖', '江疏影', '秦岚', '关晓彤', '张歆艺', '杨幂',
            'angelababy', '郑爽', '张钧甯', '刘亦菲', '蒋欣', '刘诗诗', '范冰冰', '唐嫣', '林心如', '章子怡', '古力娜扎',
            '柳岩', '景甜', '李沁', '周冬雨', '高圆圆', '佟丽娅', '杨紫', '宋茜', '刘涛', '陈乔恩', '杨蓉', '林志玲', '郭碧婷',
            '郭采洁', '刘萌萌', '唐艺昕', '阚清子', '戚薇', '张馨予', '王丽坤', '林允儿', '李冰冰', '邓家佳', '娄艺潇', '袁姗姗',
            '王珞丹', '毛晓彤', '陈紫函', '姚晨', '闫妮', '韩庚', '马天宇', '黄子韬', '演员马可', '陈学冬', '鹿晗', '盛一伦',
            '汪东城', '贾乃亮', '胡歌', '蒋劲夫', '吴亦凡', '王俊凯', '刘昊然', '易烊千玺', '周星驰', '刘德华', '杨洋', '李易峰',
            '王凯', '张艺兴', '黄晓明', '吴磊', '黄渤', '王源', '成龙', '谢霆锋', '吴京', '陈伟霆', '郑恺', '陈晓', '李晨',
            '陈赫', '邓超', '林更新', '冯绍峰', '王宝强', '杜淳', '徐峥', '陈坤', '霍建华', '彭于晏', '张翰', '孙艺洲', '郭德纲',
            '吉克隽逸', '张韶涵', '王菲', '邓紫棋', 'hebe', '那英', '张靓颖', 'selina', '蔡依林', '李宇春', '弦子',
            '曲婉婷', '杨钰莹', '莫文蔚', 'by2', '孙燕姿', '梁静茹', '黄丽玲', '周杰伦', '张杰', 'vae', '汪峰', '王力宏',
            '薛之谦', '郑龙华', 'tfboys', '林俊杰', '华晨宇', '陈奕迅', '潘玮柏', '陈小春', '汪苏泷', '杨宗纬', '李玉刚',
            '大张伟', '萧敬腾', '张学友', '林宥嘉', '电影', '电影票房', '最新电影', '电影资源共享', '香港电影', '中国电影', '好看的电影',
            '电影截图', '科幻电影', '恐怖电影', '高清电影资源', '微电影', '经典电影', '银河电影联盟', '世界电影票房', '电影推荐', '图解电影',
            '泰国电影', '动漫电影', '热门电影分享', '电影圈', '免费电影分享', '小清新电影', '北美票房榜', '新电影票房', '动画电影', '电视剧',
            '古装电视剧', '剧', '日剧', '韩剧', '泰剧', '美剧', '广播剧', '网剧', '网络剧', '爱奇艺综艺', '真人秀', '韩国综艺',
            '综艺', '综艺玩很大', '综艺大热门', '综艺满天星', '动漫', '后宫动漫', '动漫头像', '腐女动漫', '动漫图片', '动漫群',
            '日本动漫', '手绘动漫', '天津动漫', '动漫美图', '好看的动漫', '治愈动漫', '动漫情侣头像', '动漫资源', '动漫壁纸', '贴动漫频道',
            '动漫手绘', '动漫歌曲', '动漫情头', '动漫男头', '动画', '国产动画', '哔哩哔哩动画', '国产动漫', '漫画', '暴走漫画', '飒漫画',
            '动漫音乐', '音乐', '欧美音乐', '纯音乐', '无损音乐', '轻音乐', '古典音乐', '网易云音乐', '原创音乐', '背景音乐', '流行音乐',
            '读书', '读书笔记', '小说', '言情小说', 'yy小说吧', '小说推荐', '微小说', '穿越小说', '炫舞小说', '小说吧', '玄幻小说',
            '原创小说', '校园小说', '好看的言情小说', '恐怖小说', '虐心小说', '轻小说', 'bl小说', '最小说', '网络小说']
def add_account(user_id, accountId, password, platform, cookies):
    # accountId = '18500346307'
    # password = 'sjfwbznb'
    # platform = '百度王'
    #cookies = {u'bottleBubble': u'1', u'TIEBA_USERTYPE': u'181e5540159a7ef38f29bd1d', u'BDUSS': u'l2MnRVVmlkLWJibXRVa3hSU1dBSi1EZVI4THhTUi0xb35jd0xreU55flRIWTVhQVFBQUFBJCQAAAAAAAAAAAEAAAARVwvOu6LQpbjnNjY2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANOQZlrTkGZaZF', u'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948': u'1516671175', u'BAIDUID': u'5316C65D3395F32DF1B7B3C9BEEC18D2:FG=1', u'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948': u'1516671189', u'TIEBAUID': u'69f9537a8d22b677ddfeb3db', u'FP_UID': u'6c21b2b922cf1f23b31b91b20da79736', u'STOKEN': u'2552a3439dd8d7a202885d0f99c155de994f3ef402a0e9d9cce361299570ba65'}

    cookiesStr = json.JSONEncoder().encode(cookies) #dict转str
    # cookiesStr = json.dumps(cookies)

    # print cookiesStr
    # print type(cookiesStr)
    #print type(cookiesStr)  #str


    url ='http://114.215.170.176:4000/add-account'
    data = {'area': user_id, 'accountId': accountId, 'password': password, "platform": platform,
            'data': cookiesStr}
    s=requests.post(url, data=data)
    print s.text

def update_cookies(user_id, accountId, password, platform, current_cookie):
    url = 'http://114.215.170.176:4000/update-account'
    req = requests.post(url, data={'accountId': accountId, 'password': password, 'platform':
        platform, 'area': user_id, 'data': json.JSONEncoder().encode(current_cookie)})
    print req.text

def get_account(platform):
    url = 'http://114.215.170.176:4000/get-account'
    req = requests.get(url, params = {'platform': platform})  #json字符串

    #print type(req.text) #<type 'unicode'>
    r = json.JSONDecoder().decode(req.text)   #将获取的结果转成dict   #<type 'dict'>
    return r

def get_newCookies(username, password):
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.delete_all_cookies()

    login(driver, username, password)

    cookie= driver.get_cookies()
    print cookie
    '''
    cookie
    
    [{u'domain': u'.tieba.baidu.com', u'secure': False, u'value': u'8ffe8aebd28ada7bc9fcc6e6', u'expiry': 1609430399, u'path': u'/', u'httpOnly': False, u'name': u'TIEBA_USERTYPE'}, {u'domain': u'.baidu.com', u'secure': False, u'value': u'0CB7ACDFCF652857B5C250A44135C52A:FG=1', u'expiry': 1548151178, u'path': u'/', u'httpOnly': False, u'name': u'BAIDUID'}, {u'domain': u'tieba.baidu.com', u'secure': False, u'value': u'1', u'expiry': 9223372036854776000L, u'path': u'/', u'httpOnly': False, u'name': u'bottleBubble'}, {u'domain': u'.baidu.com', u'secure': False, u'value': u'b2d237f7fe14534791ad39c438b4ec80', u'expiry': 2556057600L, u'path': u'/', u'httpOnly': False, u'name': u'FP_UID'}, {u'domain': u'.baidu.com', u'secure': False, u'value': u'lpGeS1oaElGfm9GVk5-bkVIMVMzUFVFRmRUMXlxcDVCUlhGc2RxaThVZ1lRNDFhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABi2ZVoYtmVaY', u'expiry': 1775815192, u'path': u'/', u'httpOnly': True, u'name': u'BDUSS'}, {u'domain': u'.tieba.baidu.com', u'secure': False, u'value': u'8a1847a7f2b74cd44d80e9be9fed1b04a4e0bd216784987a8a708412dcc1b951', u'expiry': 1519207192, u'path': u'/', u'httpOnly': True, u'name': u'STOKEN'}, {u'domain': u'.tieba.baidu.com', u'secure': False, u'value': u'e56b4cc77a1677e7f0eb2890', u'expiry': 1609430399, u'path': u'/', u'httpOnly': False, u'name': u'TIEBAUID'}, {u'domain': u'.tieba.baidu.com', u'secure': False, u'value': u'1516615179', u'expiry': 1548151193, u'path': u'/', u'httpOnly': False, u'name': u'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948'}, {u'domain': u'.tieba.baidu.com', u'secure': False, u'value': u'1516615193', u'expiry': 9223372036854776000L, u'path': u'/', u'httpOnly': False, u'name': u'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948'}, {u'domain': u'tieba.baidu.com', u'secure': False, u'value': u'1', u'expiry': 9223372036854776000L, u'path': u'/', u'httpOnly': False, u'name': u'3407844214_FRSVideoUploadTip'}, {u'domain': u'tieba.baidu.com', u'secure': False, u'value': u'1', u'expiry': 1603015195, u'path': u'/', u'httpOnly': False, u'name': u'rpln_guide'}]
    
    
    '''

    cookies = {}
    for i in cookie:
        cookies[i['name']]=i['value']
    # print cookies
    '''
    cookies
    
    {u'bottleBubble': u'1', u'TIEBA_USERTYPE': u'45a1bae3e3f2eb6441e23019', u'BDUSS': u'HBvM3RlTFZqYUp6Q3hTd3hhSlNQOHFxcy1mQ2h3Tk1xOGFVQmpiOEZKVkZHbzVhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEWNZlpFjWZaW', u'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948': u'1516670264', u'BAIDUID': u'8C34BC867A1638092435F920AABA2CD1:FG=1', u'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948': u'1516670279', u'TIEBAUID': u'e56b4cc77a1677e7f0eb2890', u'FP_UID': u'deed4da9f38280539d9c9fc546d2e4cf', u'STOKEN': u'6a4ad1b9623dc04e653b552aa8fb236363db1914d1e8747fc37ee8c9e7dabaf2'}
    '''
    return cookies


def isElementExistById(element, driver):
    flag = True

    try:
        driver.find_element_by_id(element)
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
# def getTBS(keyword):
#     r = requests.get('https://tieba.baidu.com/f?kw=' + keyword)
#     res = r.text
#     # print res
#
#     soup = BeautifulSoup(res, "html.parser")
#     soups = soup.find_all('script')
#     for i in soups:
#         if i.getText().find(u'// 页面的基本信息')>=0:
#             xyz = i.getText().encode('utf-8')
#             # print i.getText()
#     s = xyz.replace(" ","").strip()
#
#     print s
#     print '-------------'
#     tbs = s[s.find("'tbs'")+7:s.find("'tbs'")+33]
#     print tbs
#     return tbs

def sign(cookie, keyword):
    # 不需要登录即可获取tbs
    r = requests.get('https://tieba.baidu.com/f?kw=' + keyword + '&ie=utf-8&fr=search')
    res = r.text
    # print res

    soup = BeautifulSoup(res, "html.parser")
    soups = soup.find_all('script')
    for i in soups:
        if i.getText().find(u'// 页面的基本信息')>=0:
            text = i.getText().encode('utf-8')
            # print i.getText()

    text_all = text.split(';')
    tbs = text_all[0][text_all[0].find('tbs')+7:text_all[0].find('"    }')]
    tieba_id = text_all[3][text_all[3].find('id')+5:text_all[3].find(',')]
    print tbs
    print tieba_id


    headers = {
        'Host': 'tieba.baidu.com',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36",
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Cookie': cookie,
        'X-Requested-With':'XMLHttpRequest',
        'Referer': 'http://tieba.baidu.com'
    }
    # tbs = getTBS(keyword)
    data = {'ie':'utf-8','kw':keyword,'fr':'search','tbs':tbs}

    r = requests.post('https://tieba.baidu.com/sign/add', data=data, headers=headers)
    # print r.text
    # print r.content
    # print type(r.text.encode('utf-8'))  <type 'str'>


    rr = json.loads(r.text.encode('utf-8'))
    print rr

    if rr['error'] != '':
        print rr['error']

    if rr['data'] != '':
        print rr['data']['errmsg']

    random_wait_time = random.randint(5, 10)
    # print random_wait_time
    time.sleep(random_wait_time)
    print '----------本次签到结束----------'

def focus(cookie):


    headers = {
        'Host': 'tieba.baidu.com',
        'origin': 'http://tieba.baidu.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': cookie,
        'X-Requested-With': 'XMLHttpRequest',
        'Referer': 'http://tieba.baidu.com'
    }
    for keyword in keywords:
        # 需要登录获取tbs
        # 关注时，cookie必须是网页实际的，不能通过selenium获取，且tbs也是登陆之后才有效
        r = requests.get('https://tieba.baidu.com/f?kw=' + keyword, cookies=cookie_strTodict(cookie))
        res = r.text
        # print res

        soup = BeautifulSoup(res, "html.parser")
        soups = soup.find_all('script')
        for i in soups:
            if i.getText().find(u'// 页面的基本信息')>=0:
                text = i.getText().encode('utf-8')
                # print i.getText()

        text_all = text.split(';')
        tbs = text_all[0][text_all[0].find('tbs')+7:text_all[0].find('"    }')]
        tieba_id = text_all[3][text_all[3].find('id')+5:text_all[3].find(',')]
        # print tbs
        # print tieba_id

        # data = {'fid': 2458, 'uid': 'wisewebsjfwb', 'fname':keyword, 'tbs': tbs}
        data = {'fid': tieba_id, 'fname':keyword, 'tbs': tbs}
        rrr = requests.post('http://tieba.baidu.com/f/like/commit/add', data=data, headers=headers)
        print rrr.text,keyword



def cookie_strTodict(cookie):
    # cookie = 'TIEBA_USERTYPE=75e4e6f4b6b39a6f8e3a8458; BAIDUID=ABEF6BA56A1240C733DA4596FC3F615C:FG=1; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1516587980; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1516608345; TIEBAUID=e56b4cc77a1677e7f0eb2890; bottleBubble=1; FP_UID=7e028bf8b0dc29ef886f6c27e50be8b8; BDUSS=UtKZWQ2RDFKc1RkWHhkZHJ6MEtVZW9DNmZRSm5RbDVyOGpXbzlqZXdyeloySXhhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANlLZVrZS2VaN; STOKEN=d44cc7ac344435f66aa4df36e2bf8f7f63f1e17eaa771737121ab69effc8f756; rpln_guide=1; 3407844214_FRSVideoUploadTip=1; showCardBeforeSign=1'
    list = cookie.split(';')
    cookies = {}
    # for i in list:
    # print i
    for line in list:   #按照字符：进行划分读取
        #其设置为1就会把字符串拆分成2份
        name,value=line.strip().split('=',1)
        cookies[name]=value  #为字典cookies添加内容
    # print cookies
    return cookies
def cookie_dictTostr(cookie):
    # 发送http请求需先处理cookie
    current_cookies = []
    for key,value in cookie.items():
        current_cookies.append(key + '=' + value)

    current_cookies = ';'.join(current_cookies)
    print current_cookies
    return current_cookies

if __name__ == '__main__':

    # cookies = {'bottleBubble': '1', 'TIEBA_USERTYPE': '7feb3d5e00d5b6d500319bcb', 'BDUSS': 'nNuVEN2bjEwbXhBM0haVm84eHIzZndzd3RuN1ZjOWtBVXJMUlh2UXhsYnRaNDlhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO3aZ1rt2mdaM', '3407844214_FRSVideoUploadTip': '1', 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948': '1516755679', 'BAIDUID': '81DC03428A81AB9F0511B9E71EDDAE0F:FG=1', 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948': '1516755695', 'TIEBAUID': 'e56b4cc77a1677e7f0eb2890', 'FP_UID': 'd8a253c55dfe37428a8038ed5f901492', 'STOKEN': '4c55c9c011241a60def8cdd43df5dc425259c802b05a488e74ab8ddc8e3e9121'}
    #
    # r = requests.get('https://tieba.baidu.com/f?ie=utf-8&kw=篮球&fr=search')
    # print r.text
    # time.sleep(10000)
    # username = '18500346307'
    # password = 'sjfwbznb'
    #
    # username2 = '18680663489'
    # password2 = 'wiseR00t'




    accountInfo = get_account('百度王')
    user_id = accountInfo['data']['area']
    nickName = accountInfo['data']['nickName']
    username = accountInfo['data']['accountId']
    password = accountInfo['data']['password']

    print user_id
    print nickName
    print username
    print password

    if type(accountInfo['data']['data']) == dict:
        print type(accountInfo['data']['data'])
        get_cookies = accountInfo['data']['data']
    elif type(accountInfo['data']['data']) == unicode:
        print type(accountInfo['data']['data'])
        get_cookies = json.loads(str(accountInfo['data']['data']))

    print get_cookies   #dict
    print '开始签到'
    for keyword in keywords:
        print keyword
        sign(cookie_dictTostr(get_cookies), keyword)

    # cookie = 'abc'
    # sign(cookie, '明星')



    # wisewebsjfwb_cookie = 'BAIDUID=8B57102E68EC847D4A79A6FB3ED3F808:FG=1; BIDUPSID=8B57102E68EC847D4A79A6FB3ED3F808; PSTM=1505097142; TIEBA_USERTYPE=7b398ec204291e1ac0e68834; bdshare_firstime=1505276453115; bottleBubble=1; 963363010_FRSVideoUploadTip=1; 2805889111_FRSVideoUploadTip=1; wise_device=0; __cfduid=df71fb196be52e9135ba14a49c61ef6651508743877; FP_LASTTIME=1510535215666; H_WISE_SIDS=102572_104487_119593_116520_106370_119047_120762_120136_110776_118942_118879_118868_118842_118826_118802_107312_120774_118969_117580_117328_117237_120635_117436_120610_120590_121034_120944_118966_119968_117553_120482_119962_119945_120850_120852_120071_120840_116408_110085_120503_120861; H_PS_PSSID=1446_21095_17001_20927; 3407844214_FRSVideoUploadTip=1; baidu_broswer_setup_wisewebsjfwb=0; rpln_guide=1; MCITY=-131%3A; BDSFRCVID=4X_sJeC62wp99O5AjHhjrFH7lSUUOTnTH6aICTE47vBENP9kJ03NEG0PDf8g0Ku-MJflogKK0mOTHvoP; H_BDCLCKID_SF=fRKf_I0ytKvDj6rnbnJHh4bH-UnLetJXf2uJa4OF5l8-hljayj5PDU_gDp63bf57JKJ-XD3_bpcxOKQpyqnky5FYhtnMK5c8-2TGKpON3KJmqJL9bT3v5DuSQ-oi2-biWbRL2MbdbJ7mbC_mD68he5bWepb3-4oX5-oDQ6rJabC3HqccKU6qLT5Xh-JDL5on0mOdXCo-3qPbDb5oyp5U-p0njxQA0DrOymovaC8h-t82snOGWxonDh8L2a7MJUntKDbrbx3O5hvvhb6O3M7-hpOhDG8Dt6FHJbus3JF8-PTMjb7kqROqbbQH-UIsLRQJ-2Q-5KL-3-5FefKGLJbmMx0XQ4Af2UkfJCj2oMbdJJjzfl59e-oUKM4bbHQuq4T7LeTxoUJhMInJhhvq-47cqJ_ebPRiJPr9QgbqWMtLtD-2MIDCjTK3KbF3MMnXetcJMInQsJO8fhoOjPO_bf--DlIsW-6vtxoeaJnwQqQdJbR4VtO2MUnxy5K_yt7B3qjjtacX0MTGW45RJxOHQT3mQMrbbN3i-4jiagv3Wb3cWKJV8UbS54nme6jXDGAOtjFJf5c0QTrV-RTBjjrnhPF3MKufKP6-35KHbCJrbxbt0R7pERR4QxAbh-LjbNQvQq37JD6AQtbIfPTUfM7-yhoijnIn54oxJpODBRbMopvaKtTqODOvbURvD-ug3-7q2h8EtJuHVIPKfC-3fRTxq4raMJFtqxby26nuMjTeaJ5nJDohDhRh3-5NQMPRKl5lBTbQ5CJMoxn4QpP-HqT45MDW2f03Bn57LlkfMebqKl0MLPjYbb0xynoD2tLPDUnMBMPjamOnaPQOLIFbMC_Cej0Men8Qqxvy2tbJbCvKWRK8Kb7VbIbyBnbkbfJBDlJjq6c9Jm6Bann_-qQ1MnRb3qoc3-C7yajKBxJn3RPfLqoNBftBjpFxDUTpQT8rQMDOK5Oib4juaJQsab3vOIJzXpO1544rexbH55uJJRkO_MK; baidu_broswer_setup_虎啸哥666=0; TIEBAUID=e56b4cc77a1677e7f0eb2890; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1516601322,1516675116,1516682967,1516686753; BDUSS=mFaWUY4MVVvMngzeFA5bTNudVc4N3dOdWxod09FZE5MWUtiNlUzN3VPcHZZbzVhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAG~VZlpv1WZab; STOKEN=a65fb6f781bf25cd7d96da16897f2e750226e060032369b1c548ff7abaad4aba; PSINO=1; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1516690195'
    # focus(wisewebsjfwb_cookie)





    # time.sleep(10000)


    # print '开始获取新cookie'
    # get_cookies = get_newCookies('18500346307', 'sjfwbznb')
    # print get_cookies
    #
    # update_cookies('3407844214', '18500346307', 'sjfwbznb', '百度王', get_cookies)
    #
    # res = requests.get('https://tieba.baidu.com/f?ie=utf-8&kw=篮球&fr=search',cookies=get_cookies).text
    # # print res
    #
    # soup = BeautifulSoup(res, "html.parser")
    # soups = soup.find_all('script')
    # for i in soups:
    #     if i.getText().find('3407844214')>=0:
    #         # print i
    #         print '该cookie可用'






    # driver = webdriver.Firefox()
    # driver.maximize_window()
    # driver.get('http://tieba.baidu.com/f?kw=网剧&fr=index')
    # for key,value in get_cookies.items():
    #     driver.add_cookie({'name': key, 'value': value})
    #     print key
    #     time.sleep(1)
    #
    # driver.refresh()

    # time.sleep(10000)



