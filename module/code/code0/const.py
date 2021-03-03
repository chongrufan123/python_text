###************************************************************************
	# File Name: const.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月03日 星期三 12时45分46秒
  # notes: 
###***********************************************************************

class Const:
    def __init__(self):
        super().__setattr__(self.namelist, [])

    def __getattr__(self, name):
        raise NameError(正在访问一个不存在的变量)

    def __getattribute__(self, name):
        return super().__getattribute__(self.name)

    def __setattr__(self, name, value):
        print(self.namelist)
        print(name)
        if name.isupper():
            if name not in namelist:
                self.namelist.append(name)
                self.name = value
            else:
                raise TypeError(常量无法更改)
        else:
            raise TypeError(常量名称请用大写)


