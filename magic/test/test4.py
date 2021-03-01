###************************************************************************
	# File Name: test4.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月01日 星期一 19时03分51秒
  # notes: 
###***********************************************************************

class Mylist:
    def __init__(self, *a):
        self.a = a
        self.dict = dict.fromkeys(a, 0)
    def __len__(self):
        return len(self.a)
    def __getitem__(self, key):
        key = self.a[key]
        self.dict[key] += 1 
        return key
    def getval(self, key):
        key = self.a[key]
        return self.dict[key]


