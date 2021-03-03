###************************************************************************
	# File Name: code7_1.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月02日 星期二 18时35分43秒
  # notes: 
###***********************************************************************

import math

def isprime(number):
    for each in range(2, number//2 + 1):
        if number % each == 0:
            return False
        else:
            pass
    return True

def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

def MyDev(num):
    number = 1
    summ = 0
    while True:
        if is_prime(number):
            summ = summ + number
            yield summ
        number += 1
        if number >= num:
            break

for i in MyDev(2000000):
    print(i)
