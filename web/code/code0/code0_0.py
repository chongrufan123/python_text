###************************************************************************
	# File Name: code0_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月03日 星期三 14时43分43秒
  # notes: 
###***********************************************************************

import urllib.request as urlrt
fishc = urlrt.urlopen("http://www.fishc.com")
print(fishc.read(300))
