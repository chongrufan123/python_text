###************************************************************************
	# File Name: code4_2.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月28日 星期日 16时39分11秒
###***********************************************************************

class Counter:
    def __init__(self):
        self.counter = 0
    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        self.__dict__[] += 1
    def __delattr__(self, name):
        self.counter -= 1
        super().__delattr__(name)
