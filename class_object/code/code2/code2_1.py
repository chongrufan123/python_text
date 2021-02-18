import random

class Tor():
    def __init__(self):
        self.torx = random.randint(0, 10)
        self.tory = random.randint(0, 10)
        self.life = 100
    def speedl(self, speed, dirction):
        if dirction == 0:
            self.torx = self.torx - speed
        if dirction == 1:
            self.tory = self.tory - speed
        if dirction == 2:
            self.tory = self.tory + speed
        if dirction == 3:
            self.torx = self.torx + speed
        
    def move(self):
        direction = random.randint(0,3)
        speed = random.randint(1,2)
        self.speedl(speed, direction)
        self.life -= 1
        if(self.torx < 0):
            self.torx = 0 - self.torx
        if(self.tory < 0):
            self.tory = 0 - self.tory
        if(self.tory > 10):
            self.tory = 20 - self.tory
        if(self.torx > 10):
            self.torx = 20 - self.torx

        
        

class Fish():
    def __init__(self):
        self.torx = random.randint(0, 10)
        self.tory = random.randint(0, 10)
    def speedl(self, dirction):
        if dirction == 0:
            self.torx = self.torx - 1
        if dirction == 1:
            self.tory = self.tory - 1
        if dirction == 2:
            self.tory = self.tory + 1
        if dirction == 3:
            self.torx = self.torx + 1
        
    def move(self):
        direction = random.randint(0,3)
        self.speedl(direction)
        if(self.torx < 0):
            self.torx = 0 - self.torx
        if(self.tory < 0):
            self.tory = 0 - self.tory
        if(self.tory > 10):
            self.tory = 20 - self.tory
        if(self.torx > 10):
            self.torx = 20 - self.torx

gui = Tor()
fish = []
for each in range(10):
    fish.append(Fish())
i = 0
while(1):
    i += 1
    if gui.life <= 0:
        print('乌龟的生命值已经为0')
        print('共移动了%d次' %i)
        break
    if len(fish) <= 0:
        print('鱼被完全吃完')
        print('共移动了%d次' %i)
        break

    for each in range(0, len(fish)):
        try:
            if gui.torx == fish[each].torx and gui.tory == fish[each].tory:
                gui.life += 20
                fish.pop(each)
        except IndexError:
            pass
    for each in range(0, len(fish)):
        fish[each].move()
    gui.move()
