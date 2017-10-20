# -*- coding: utf-8 -*-
import random
import urllib2

import requests
from bs4 import BeautifulSoup
import urllib
import socket

User_Agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
header = {}
header['User-Agent'] = User_Agent

''''' 
获取所有代理IP地址 
'''
def getProxyIp():
    proxy = []
    for i in range(1,2):
        try:
            url = 'http://www.xicidaili.com/nn/'+str(i)
            # req = urllib2.Request(url,headers=header)
            # res = urllib2.urlopen(req).read()
            r = requests.get(url=url, headers=header).text
            soup = BeautifulSoup(r,'html.parser')
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")

                # print tds[8].contents[0]

                if tds[8].contents[0].find(u'天')>=0:
                    if int(tds[8].contents[0][0:len(tds[8].contents[0])-1])>20:
                        ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]
                        proxy.append(ip_temp)

        except:
            continue
    for i in proxy:
        print i
    print(proxy)
    print '------------------'
    return proxy

''''' 
验证获得的代理IP地址是否可用 
'''
def validateIp(proxy):
    proxy_list = []
    url = "http://ip.chinaz.com/getip.aspx"
    f = open("ip.txt","w")
    socket.setdefaulttimeout(3)
    for i in range(0, len(proxy)):
        try:
            ip = proxy[i].strip().split("\t")
            proxy_host = "http://"+ip[0]+":"+ip[1]
            proxy_temp = {"http":proxy_host}
            #res = urllib.urlopen(url,proxies=proxy_temp).read()
            res = requests.get(url,proxies=proxy_temp).text
            #print(res)
            f.write(proxy_host[7:]+'\n')    #120.78.15.63:80
            proxy_list.append(proxy_host)
            #print proxy[i]  #106.59.230.200	8118
            print proxy_host    #http://120.78.15.63:80
        except Exception,e:
            continue
    f.close()
    print('over')
    return proxy_list

def getOneIP(proxy_list):
    proxy_ip = random.sample(proxy_list, 1)
    ip = {'http': ''.join(proxy_ip)}
    print(ip)
    return ip



if __name__ == '__main__':
    #proxy = getProxyIp()

    #validateIp(proxy)
    # x = u'23123天'
    # print len(x)
    # if x.find(u'天')>=0:
    #
    #     y = int(x[0:len(x)-1])
    #     print(y)
    #     print(type(y))

    getOneIP(validateIp(getProxyIp()))

