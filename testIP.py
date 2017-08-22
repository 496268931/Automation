# -*- coding: utf-8 -*-
import random
import urllib2
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
            req = urllib2.Request(url,headers=header)
            res = urllib2.urlopen(req).read()
            soup = BeautifulSoup(res,'html.parser')
            ips = soup.findAll('tr')
            for x in range(1, len(ips)):
                ip = ips[x]
                tds = ip.findAll("td")
                ip_temp = tds[1].contents[0]+"\t"+tds[2].contents[0]
                proxy.append(ip_temp)

        except:
            continue
    #print(proxy)
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
            res = urllib.urlopen(url,proxies=proxy_temp).read()
            #print(res)
            f.write(proxy_host+'\n')
            proxy_list.append(proxy_host)
            #print proxy[i]  #106.59.230.200	8118
            print proxy_host#106.59.230.200:8118
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

    getOneIP(validateIp(getProxyIp()))