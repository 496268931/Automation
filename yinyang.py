#coding=utf-8
import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yinyangciqingshi.com/423.html')
# print r.content
soup = BeautifulSoup(r.content, "html.parser")
# print soup.find_all('div',id='contents')

for i in soup.find_all('div',id='contents'):

    print i.text
