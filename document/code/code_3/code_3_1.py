import os

file_dict = {}
all_file = os.listdir('.')
for each in all_file:
    file_dict[each] = os.path.getsize(each)
for name,size in file_dict.items():
    print('该文件'+str(name)+'的大小为'+str(size))
