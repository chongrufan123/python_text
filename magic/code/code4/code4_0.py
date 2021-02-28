###************************************************************************
	# File Name: code4_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月28日 星期日 16时26分54秒
###***********************************************************************

class C:
    def __getattr__(self, name):
        print('该属性不存在')
