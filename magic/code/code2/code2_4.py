###************************************************************************
	# File Name: code2_4.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年02月27日 星期六 17时18分04秒
###***********************************************************************

class Word(str):
    def __lt__(self, other):
        self = self.split(' ', 1)[0]
        other = other.split(' ', 1)[0]
        if(len(self) < len(other)):
            return True
        else:
            return False

    def __le__(self, other):
        self = self.split(' ', 1)[0]
        other = other.split(' ', 1)[0]
        if(len(self) <= len(other)):
            return True
        else:
            return False

    def __eq__(self, other):
        self = self.split(' ', 1)[0]
        other = other.split(' ', 1)[0]
        if(len(self) == len(other)):
            return True
        else:
            return False

    def __ne__(self, other):
        self = self.split(' ', 1)[0]
        other = other.split(' ', 1)[0]
        if(len(self) != len(other)):
            return True
        else:
            return False

    def __gt__(self, other):
        self = self.split(' ', 1)[0]
        other = other.split(' ', 1)[0]
        if(len(self) > len(other)):
            return True
        else:
            return False

    def __ge__(self, other):
        self = self.split(' ', 1)[0]
        other = other.split(' ', 1)[0]
        if(len(self) >= len(other)):
            return True
        else:
            return False

