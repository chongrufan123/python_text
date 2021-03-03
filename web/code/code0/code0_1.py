###************************************************************************
	# File Name: code0_1.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月03日 星期三 14时46分33秒
  # notes: 
###***********************************************************************

import urllib.request as urlreq
import chardet

ur = input("请输入URL: ")

responde = urlreq.urlopen(ur).read()
ma = chardet.detect(responde)
bian = ma['encoding']
print("该网页使用的编码是: %s" % bian)
