###************************************************************************
	# File Name: test.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月03日 星期三 13时02分01秒
  # notes: 
###***********************************************************************

# const 模块就是这道题要求我们自己写的
# const 模块用于让 Python 支持常量操作
import const

const = const.Const()
const.NAME = "FishC"
print(const.NAME)

try:
    # 尝试修改常量
    const.NAME = "FishC.com"
    print('111')
except TypeError as Err:
    print(Err)

try:
    # 变量名需要大写
    const.name = "FishC"
    print('222')
except TypeError as Err:
    print(Err)
