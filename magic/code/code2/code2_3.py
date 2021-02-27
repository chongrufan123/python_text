###************************************************************************
	# File Name: code2_3.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月27日 星期六 17时03分05秒
###***********************************************************************

class Count:
    def __init__(self, *arg):
        canshu = ''
        if len(arg) == 0:
            print('并没有传入参数')
            return
        for each in arg:
            canshu = canshu + '  ' + str(each)
        print('传入%d个参数, 分别是:' % len(arg) , end = ' ')
        print(canshu)
