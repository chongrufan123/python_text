###************************************************************************
	# File Name: code2_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月04日 星期四 14时25分20秒
  # notes: 
###***********************************************************************

import urllib.request as urlreq
from bs4 import BeautifulSoup as BS

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
url = 'http://baike.baidu.com/view/284853.htm'
url = urlreq.Request(url, {}, head)
respond = urlreq.urlopen(url)
baike = respond.read().decode('utf-8')

with open('url_baike.txt', 'w') as f:
    f.write(baike)
