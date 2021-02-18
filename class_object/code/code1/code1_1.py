class Rectangle():
    def __init__(self):
        self.lenth = 5
        self.width = 4

    def setRect(self):
        self.lenth = float(input("lenth:"))
        self.width = float(input("width:"))
    def getRect(self):
        print('这个矩形的长是%.2f, 宽是%.2f' % (self.lenth, self.width))

    def getArea(self):
        print('这个矩形的面积是%.4f' % (self.lenth * self.width))

