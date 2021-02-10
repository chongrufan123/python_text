def zhan(filename):
    f = open(filename)
    num = input('请输入显示的行数：')
    n = 0
    line = []
    for eachline in  f:
        n += 1
        if (n > int(num)):
            n -= 1
            break
        else:
            line.append(eachline)
    print("文件"+filename+'的钱'+str(n)+'的内容如下：')
    for each in line:
        print(each)

f = input('请输入要打开的文件')
zhan(f)

