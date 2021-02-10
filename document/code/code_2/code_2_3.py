def zhan(filename):
    f = open(filename)
    num = input('请输入显示的行数：')
    n = 0
    [num1, num2] = num.split(sep=':', maxsplit=1)
    if(num1 == ''):
        num1 = 0
    if(num2 == ''):
        num2 = 9999
    print(str(num1) +'\n'+ str(num2))
    line = []
    for eachline in  f:
        n += 1
        if (n >= int(num1)):
            line.append(eachline)
        if (n >= int(num2)):
            n -= 1
            break
    print("文件"+filename+'的钱'+str(n)+'的内容如下：')
    for each in line:
        print(each)

f = input('请输入要打开的文件')
zhan(f)

