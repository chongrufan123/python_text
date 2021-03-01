###************************************************************************
	# File Name: code5_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月01日 星期一 16时31分37秒
  # notes: 将内容和数据分别保存
###***********************************************************************

class Mydes:
    def __init__(self, value, name):
        self.name = name
        super().__setattr__(name, value)
    def __get__(self, instance, owner):
        print('正在获取变量')
        return super().__getattribute__(self.name)
    def __set__(self, instance, value):
        print("正在修改变量")
        self.__dict__[self.name] = value
    def __delete__(self,instance):
        print('正在删除变量') 

class Test:
    x = Mydes(10, 'x')
