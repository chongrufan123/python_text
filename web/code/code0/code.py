###************************************************************************
	# File Name: code.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月04日 星期四 14时13分44秒
  # notes: 
###***********************************************************************

from bs4 import BeautifulSoup as BS

fishc = BS(open("url_1.html"))
print(fishc.prettify())
