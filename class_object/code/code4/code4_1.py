class Stack:
    def __init__(self):
        self.sta = []
    def isEmpty(self):
        if self.sta == []:
            return True
        else:
            return False
    def push(self, x):
        self.sta.append(x)
    def pop(self):
        self.top = self.sta.pop()
        return self.top
    def top(self):
        try:
            self.ttop = self.sta[len(self.sta) - 1]
            print(str(self.ttop))
        except IndexError:
            print("栈空")
    def bottom(self):
        try:
            print(self.sta[0])
        except IndexError:
            print("栈空")
        
