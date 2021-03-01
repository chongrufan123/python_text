###************************************************************************
	# File Name: code6.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月01日 星期一 19时27分47秒
  # notes: 
###***********************************************************************

class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value
        self.count[key] = 0

    def __delitem__(self, key):
        del self.values[key]
        self._dicmove(key)

    def counter(self, index):
        return self.count[index]

    def append(self, other):
        self.values.append(other)
        self.count[len(self.values) - 1] = 0

    def pop(self):
        self.values.pop()
        self.count.popitem()

    def remove(self, value):
        for each in range(len(self.values)):
            if self.values[each] == value:
                self.values.remove(value)
                break
        self._dicmove(each)

    def _dicmove(self, key):
        for each in range(len(self.count)):
            if each == key:
                del self.count[key]
            elif each > key:
                val = self.count[each]
                del self.count[each]
                self.count[each - 1] = val

    def insert(self, index, value):
        self.values.insert(index, value)
        self._decins(index)

    def _decins(self, index):
        for each in range(len(self.count)):
            each = len(self.count) - each -1
            if each >= index:
                val = self.count[each]
                del self.count[each]
                self.count[each + 1] = val
                if (each) == index:
                    self.count[index] = 0
                    break

    def clear(self):
        self.values.clear()
        self.count.clear()

    def reverse(self):
        self.values.reverse()
        for each in range(len(self.values)//2):
            val = self.count[each]
            self.count[each] = self.count[len(self.values) - 1]
            self.count[len(self.values) - 1] = val
