###************************************************************************
	# File Name: code4_1.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月28日 星期日 16时37分02秒
###***********************************************************************

class Demo:
    def __getattr__(self, name):
        print('FishC')

