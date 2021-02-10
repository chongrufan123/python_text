def writefile(filename):
    f = open(filename, 'w')
    print('请输入内容【单独输入:w】保存退出')
    while(1):
        str1 = input()
        if(str1 == ':w'):
            f.close()
            break
        f.write(str1 + '\n')
    
filen = input("请输入文件名：")
writefile(filen)
