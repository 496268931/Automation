# coding=utf-8
import time
from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get('http://tieba.baidu.com/f?kw=网剧&fr=index')
    driver.maximize_window()
    time.sleep(2)

    driver.delete_all_cookies()
    print('开始登录')
    # chg_field = driver.find_element_by_class_name('pass-login-tab').find_element_by_class_name('account-title')
    # chg_field.click()
    #
    # name_field = driver.find_element_by_id('TANGRAM__PSP_4__userName')
    # name_field.send_keys('18500346307')
    # passwd_field = driver.find_element_by_id('TANGRAM__PSP_4__password')
    # passwd_field.send_keys('sjfwbznb')
    # login_button = driver.find_element_by_id('TANGRAM__PSP_4__submit')
    # login_button.click()
    # time.sleep(20)

    cookies = [{'domain': '.tieba.baidu.com', 'secure': False, 'value': '5c40c0e6bf7849e212d68f26',
                'expiry': 1609430399, 'path': '/', 'httpOnly': False, 'name': 'TIEBA_USERTYPE'},
               {'domain': '.baidu.com', 'secure': False,
                'value': '6861AE77AFAA42A76EAE4FEE3785669F:FG=1', 'expiry': 1547610462, 'path': '/',
                'httpOnly': False, 'name': 'BAIDUID'},
               {'domain': 'tieba.baidu.com', 'secure': False, 'value': '1',
                'expiry': 9223372036854776000L, 'path': '/', 'httpOnly': False,
                'name': 'bottleBubble'}, {'domain': '.baidu.com', 'secure': False,
                                          'value': 'c06c4d1483cb2fc3a15e87c74be49b27',
                                          'expiry': 2556057600L, 'path': '/', 'httpOnly': False,
                                          'name': 'FP_UID'},
               {'domain': '.baidu.com', 'secure': False,
                'value': 'JpeUdYOHloOWhuVzQ2TUNnbDVSNDRPWTdWNC1XYVRmeGhQOUNGRVd1M3FBb1ZhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOp1XVrqdV1aek',
                'expiry': 1775274474, 'path': '/', 'httpOnly': True, 'name': 'BDUSS'},
               {'domain': '.tieba.baidu.com', 'secure': False,
                'value': '5ae6397058461898795ce76173221e1fd73369351ff021078449f071c51fd117',
                'expiry': 1518666475, 'path': '/', 'httpOnly': True, 'name': 'STOKEN'},
               {'domain': '.tieba.baidu.com', 'secure': False, 'value': 'e56b4cc77a1677e7f0eb2890',
                'expiry': 1609430399, 'path': '/', 'httpOnly': False, 'name': 'TIEBAUID'},
               {'domain': '.tieba.baidu.com', 'secure': False, 'value': '1516074463',
                'expiry': 1547610479, 'path': '/', 'httpOnly': False,
                'name': 'Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948'},
               {'domain': '.tieba.baidu.com', 'secure': False, 'value': '1516074479',
                'expiry': 9223372036854776000L, 'path': '/', 'httpOnly': False,
                'name': 'Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948'}]
    # for i in cookies:
    #     print i
    #     for key,value in i.items():
    #         print key,value
    #         driver.add_cookie({'name': key, 'value': str(value)})
    #     time.sleep(1)
    driver.add_cookie({'name': 'BDUSS', 'value':
        '8zOHlhZ0c3bHBwNFlJaFhTR2JmSzZMa1FOZHhGTm82Qy11d2h2OHBnfndOWVZhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx~Ld2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPCoXVrwqF1aOU'})
    time.sleep(2)
    driver.refresh()
    time.sleep(2)

    cookie= driver.get_cookies()
    print cookie

if __name__ == '__main__':
    main()