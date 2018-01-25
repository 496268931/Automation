# coding: utf-8
import json

import requests


def post(url, data):
    headers = {
        'Host': 'c.tieba.baidu.com',
        'User-Agent': 'bdtb for Android 9.2.8.0',
        'cookie': 'ka=open',
        'Accept-Encoding': 'gzip',
        'Content-Type': 'application/x-www-form-urlencoded',
        'net': '3',
        'Connection':'Keep-Alive'
    }

    r = requests.post(url, data=data, headers=headers)
    rr = json.loads(r.text.encode('utf-8'))
    print rr
    # print rr['error_msg']






if __name__ == '__main__':
    login_url = 'http://c.tieba.baidu.com/c/s/login'
    focus_url = 'http://c.tieba.baidu.com/c/c/forum/like'



    login = '_client_id=wappc_1516758378518_324&_client_type=2&_client_version=9.2.8.0&_phone_imei=861733039691369&bdusstoken=h4V0tncktDVTZpREoxNFJMfk1keHRHb0lGWVZJVFRNQVBod1R1Sm85ekhlWTlhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx%7ELd2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMfsZ1rH7Gdab1%7C&channel_id=&channel_uid=&cuid=B7F3B4D14F66911891315097968B9929%7C963196930337168&from=1008621x&model=Lenovo+K10e70&sign=42A137D1AB40176C908C6D4526BB6883&stErrorNums=1&stMethod=1&stMode=1&stSize=769&stTime=104&stTimesNum=1&stoken=3638a53a8c4bfa449323cf164a8d896ca79676df24ebe98d2b95b4e539a50dfa&timestamp=1516760263481&z_id=PR5lo-k4LYpIS4o6nj31TnFSbCagqWuTHHZ53hZrVCO4YJXvHMI0JouO2u4xHBL25I1SXnNG2yMamq7Lt2QZ7hw'
    focus = 'BDUSS=h4V0tncktDVTZpREoxNFJMfk1keHRHb0lGWVZJVFRNQVBod1R1Sm85ekhlWTlhQVFBQUFBJCQAAAAAAAAAAAEAAAB2kx%7ELd2lzZXdlYnNqZndiAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMfsZ1rH7Gdab1&_client_id=wappc_1516758378518_324&_client_type=2&_client_version=9.2.8.0&_phone_imei=861733039691369&cuid=B7F3B4D14F66911891315097968B9929%7C963196930337168&fid=1857518&forum_name=%E8%80%81%E5%B9%B4%E5%8A%A8%E7%94%BB&from=1008621x&kw=%E8%80%81%E5%B9%B4%E5%8A%A8%E7%94%BB&model=Lenovo+K10e70&sign=65D4A72FB79F72D673673581C7EADD0C&stErrorNums=1&stMethod=1&stMode=1&stSize=989&stTime=75&stTimesNum=1&st_type=detail_follow&stoken=3638a53a8c4bfa449323cf164a8d896ca79676df24ebe98d2b95b4e539a50dfa&tbs=30e96d6b2dba85121516760264&timestamp=1516760826453&user_id=3407844214&user_name=wisewebsjfwb&z_id=PR5lo-k4LYpIS4o6nj31TnFSbCagqWuTHHZ53hZrVCO4YJXvHMI0JouO2u4xHBL25I1SXnNG2yMamq7Lt2QZ7hw'

    post(focus_url, focus)