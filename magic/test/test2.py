###************************************************************************
	# File Name: test2.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月28日 星期日 17时10分22秒
###***********************************************************************

class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)
class Fahre:
    def __get__(self, instance, owner):
        return instance.cel * 1.8 + 32

    def __set__(self, instance, value):
        instance.cel = (instance - 32) / 1.8
class Temper:
   cel = Celsius() 
   fah = Fahre()
        
