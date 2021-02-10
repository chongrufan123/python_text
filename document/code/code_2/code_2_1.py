def contrst(filename1, filename2):
    f1 = open(filename1)
    f2 = open(filename2)
    n = 0
    num = []
    line = 0
    for each_line1 in f1:
        line += 1
        if f2.readline() != each_line1:
            n += 1
            num.append(line)
    f1.close()
    f2.close()
    print('两个文件共有['+ str(n) +'处不同：')
    for each in num:
        print('第' +str(each)+'行不一样')

filename1 = input('第一个')
filename2 = input('第二个')
contrst(filename1, filename2)
