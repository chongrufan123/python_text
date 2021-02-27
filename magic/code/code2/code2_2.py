###************************************************************************
	# File Name: code2_2.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月27日 星期六 16时44分33秒
###***********************************************************************

class Nstr(str):
    def __add__(self, other):
        a = 0
        b = 0
        for each in self:
            a += ord(each)
        for each in other:
            b += ord(each)
        return a + b

    def __sub__(self, other):
        a = 0
        b = 0
        for each in self:
            a += ord(each)
        for each in other:
            b += ord(each)
        return a - b
    
    def __mul__(self, other):
        a = 0
        b = 0
        for each in self:
            a += ord(each)
        for each in other:
            b += ord(each)
        return a * b

    def __truediv__(self, other):
        a = 0
        b = 0
        for each in self:
            a += ord(each)
        for each in other:
            b += ord(each)
        return a / b

    def __floordiv__(self, other):
        a = 0
        b = 0
        for each in self:
            a += ord(each)
        for each in other:
            b += ord(each)
        return a // b
