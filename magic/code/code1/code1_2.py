class Nint(int):
    def __new__(self, sttr):
        if isinstance(sttr, str):
            self.a = 0
            for each in sttr:
                self.a += ord(each)
            return self.a
        else:
            return sttr
