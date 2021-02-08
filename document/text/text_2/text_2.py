
def chao(p, boy, girl):
    str1 = "boy_" + str(p) + ".txt"
    fb1 = open(str1,'w')
    str2 = "girl_" + str(p) + ".txt"
    fb2 = open(str2,'w')
    fb1.writelines(boy)
    fb2.writelines(girl)
    p+=1
    fb1.close
    fb2.close
    return p

def file(filename):
    f = open(filename)
    p = 1
    boy = []
    girl = []

    for each_line in f:
        if each_line[:6] != '======':
            (role, line_spoken) = each_line.split(':', 1)
            if role == '小甲鱼':
                boy.append(line_spoken)
            if role == '小客服':
                girl.append(line_spoken)
        else:
            p = chao(p, boy, girl) 
            boy = []
            girl = []
    chao(p, boy, girl) 
    print(p)
    f.close()
file('record.txt')
