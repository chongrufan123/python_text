class Piao:
    def __init__(self):
        self.price = 100
    def buy(self):
        time = input("时间是平日还是周末:")
        if time == '周末':
            self.price = 120
        adult = int(input("成人的数量是:"))
        children = int(input("儿童的数量是:"))
        print("门票的总价格是%d" % (adult * self.price + children *
            self.price/2))
