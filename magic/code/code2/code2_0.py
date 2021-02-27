###************************************************************************
	# File Name: code2_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月27日 星期六 15时42分27秒
###***********************************************************************

class Nstr(str):
    def __sub__(self, other):
        self = self.replace(other, '')
        return self
