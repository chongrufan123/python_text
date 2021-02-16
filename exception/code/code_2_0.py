import random

secret = random.randint(1,10)
print('------------------我爱鱼C工作室------------------')
try:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
except (NameError, EOFError, KeyboardInterrupt):
    guess = secret
try:
    if(guess != secret):
        guess = int(temp)
except (ValueError, EOFError, KeyboardInterrupt, NameError):
    print("请输入数字哦")
    guess = 'a'
                                    
while (guess != secret or guess == 'a'):
    try:
        temp = input("哎呀，猜错了，请重新输入吧：")
    except (EOFError,KeyboardInterrupt):
        break
    try:
        guess = int(temp)
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
    except (ValueError, EOFError, KeyboardInterrupt):
        print("请输入数字哦")
    finally:
        print('------')
print("游戏结束，不玩啦^_^")

