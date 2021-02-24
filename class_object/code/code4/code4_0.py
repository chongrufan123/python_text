class C:
    count = 0
    def __init__(self):
        C.count+=1
    def __del__(self):
        C.count-=1
