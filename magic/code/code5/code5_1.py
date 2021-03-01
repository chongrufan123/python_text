###************************************************************************
	# File Name: code5_1.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月01日 星期一 17时13分51秒
  # notes: 
###***********************************************************************
import time

class Record:
    def __init__(self, value, name):
        self.name = name
        self.value = value
    def __get__(self,instance, owner):
        f = open("record.txt",'a')
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        date = str(self.name) + '变量于'+ date + '被读取' + str(self.name) + '=' + str(self.value) + '\n'
        f.writelines(date)
        f.close()
        return self.value
    def __set__(self, instance, value):
        f = open("record.txt",'a')
        date = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        date = str(self.name) + '变量于'+ date + '被修改' + str(self.name) + '=' + str(value) + '\n'
        f.writelines(date)
        f.close()
        self.value = value

class Test:
    x = Record(10, 'x')
    y = Record(8.8, 'y')

