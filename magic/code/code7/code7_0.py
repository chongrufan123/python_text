###************************************************************************
	# File Name: code7_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月02日 星期二 18时28分02秒
  # notes: 
###***********************************************************************

def MyRev(aa):
    bb = list(aa)
    while True:
        yield bb.pop()
        if bb == []:
            break

for i in MyRev("FishC"):
    print(i,  end='')
