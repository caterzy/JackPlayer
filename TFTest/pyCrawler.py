# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'

from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

request = Request('https://www.torrentkitty.tv/search/')
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36')
response = urlopen(request)
print(response.read())

# html = urlopen("https://www.cnblogs.com/TsengYuen/archive/2012/04/12/2444177.html").read().decode('utf-8')
# print(html)