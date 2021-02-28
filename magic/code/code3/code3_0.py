###************************************************************************
	# File Name: code3_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月27日 星期六 21时56分34秒
###***********************************************************************

import time as t
class MyTimer:
    def __init__(self):
        self.timer = []
        self.dan = ['年', '月', '日', '小时', '分钟', '秒']
        self.jiewei = [12, 31, 24, 60, 60]
        self.laster = '还未开始计时'
        self.begin = []

    def __str__(self):
        return self.laster

    __repr__ = __str__

    def __add__(self, other):
        laaster = '统共运行了'
        addd = []
        for each in range(6):
            addd.append(self.timer[each] + other.timer[each])
            if addd[each]:
                laaster = laaster + str(addd[each]) + self.dan[each]
        return laaster

    def start(self):
        self.begin = t.localtime()
        self.laster = ('计时还没有结束')
        print('现在开始计时')

    def stop(self):
        if self.begin == []:
            print('请先按开始键')
        else:
            self.end = t.localtime()
            self._calu()
            print('现在计时结束')

    def _calu(self):
        self.timer = []
        self.laster = '总共运行了'
        for each in range(6):
            self.timer.append(self.end[each] - self.begin[each])
            if self.timer[each] < 0:
                self.timer[each] = self.jiewei[each - 1] + self.timer[each]
                for eeach in range(1, each+1):
                    if self.timer[each - eeach]:
                        self.timer[each - eeach] -= 1
                        break
        for each in range(6):
            if self.timer[each]:
                self.laster = self.laster + str(self.timer[each] ) + self.dan[each]
        self.begin = 0
        self.end = 0
