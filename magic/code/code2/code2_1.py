###************************************************************************
	# File Name: code2_1.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月27日 星期六 15时47分38秒
###***********************************************************************

class Nstr(str):
    def __lshift__(self, other):
        return self[other:] + self[:other]
    def __rshift__(self, other):
        return self[-other:] + self[:-other]
