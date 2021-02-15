import pickle

def file_put(boy, gril, n):
    file_name_boy = 'boy' +str(n) + '.txt' 
    file_name_gril = 'gril' +str(n) +'.txt'
    pickle_file_boy = open(file_name_boy, 'wb')
    pickle_file_gril = open(file_name_gril, 'wb')
    pickle.dump(boy, pickle_file_boy)
    pickle.dump(gril, pickle_file_gril)
    pickle_file_boy.close()
    pickle_file_gril.close()


file_txt = open('record.txt', 'r')
boy = []
gril = []
n = 1
for each_line in file_txt:
    if(each_line[:5] != '====='):
        [name, story] = each_line.split(':', 1)
        if(name == '小甲鱼'):
            boy.append(story)
        else:
            gril.append(story)
    else:
        file_put(boy,gril, n)
        n += 1
        boy = []
        gril = []
file_put(boy, gril, n)

