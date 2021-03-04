###************************************************************************
	# File Name: test1.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月 4日  9:59:46
###***********************************************************************

import urllib.request as urlreq

response = urlreq.urlopen('http://placekitten.com/g/500/600')
cat_image = response.read()

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_image)



