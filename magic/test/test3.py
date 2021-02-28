###************************************************************************
	# File Name: test3.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月28日 星期日 20时02分21秒
###***********************************************************************

class MyDes:
        def __get__(self, instance, owner):
                print("getting...")

class Test:
    a = MyDes()
    x = a
