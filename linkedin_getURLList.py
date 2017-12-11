# coding=utf-8
from bs4 import BeautifulSoup

soup = BeautifulSoup(open('linkedin_list_hao_monica.html'), "html.parser")
r = soup.find_all('a',class_='mn-person-info__picture ember-view')
url = []
for i in r:
    # print i
    # print i['href']
    url.append('http://www.linkedin.com'+i['href'])

j = 1
print url
print len(url)



'''
jxm@hfm-phe.com            23957648jxm

https://www.linkedin.com/mynetwork/invite-connect/connections/
mary@hfm-phe.com           zq3856523

hao_monica@sina.com        monicafeng1990 
eva@hfm-phe.com            229911zzy!

'''