# This Python file uses the following encoding: utf-8
__author__ = 'JackRao'

from bs4 import BeautifulSoup
import requests
import re
import sys

def CheckCount():
    fo = open("C:\Program Files (x86)\sys",'w+')
    fo.write('1')
    fo.close()

def Search(words):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Mobile Safari/537.36'
    }
    html = requests.get("https://www.torrentkitty.tv/search/"+words, headers = headers)
    html.encoding = 'utf-8'
    soup = BeautifulSoup(html.text, features='lxml')

    names = soup.find_all("td", {"class": 'name'})
    urls = soup.find_all("a", {"href": re.compile('magnet*')})
    # for name in names:
    #     print("名称:", name.get_text())
    for url in urls:
        print("link:",url['href'])

##CheckCount()
Search("snis-358")
##Search(sys.argv[1])
