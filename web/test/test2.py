###************************************************************************
	# File Name: test2.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月04日 星期四 13时14分26秒
  # notes: 获得当前的ip地址
###***********************************************************************

import urllib.request as urlreq

url = 'http://www.whatismyip.com.tw'

respond = urlreq.urlopen(url)
html = respond.read().decode('utf-8')

print(html)
input()
