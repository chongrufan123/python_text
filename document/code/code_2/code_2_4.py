def exchange(filename):
    f = open(filename)
    name_old = input('原来的：')
    name_new = input('替换成：')
    chun = []
    n = 0
    for each_line in f:
        if name_old in  each_line:
            n += 1
            each_line = each_line.replace(name_old, name_new)
        chun.append(each_line)
    print('文件中共有' +str(n) + '个' + name_old)
    pan = input('确定吗:[yes/no]')
    f.close()
    if(pan == 'yes'):
        f = open(filename, 'w')
        
        f.writelines(chun)
        f.close()


fil = input('输入文件名')
exchange(fil)
            
            

