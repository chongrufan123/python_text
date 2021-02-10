import os


type_dict = {}
lei = []
filename = os.listdir('.')
for aech in filename:
    if os.path.isdir(aech):
        type_dict.setdefault('文件夹', 0)
        type_dict['文件夹'] += 1
    else:
        n2 = os.path.splitext(aech)[1]
        type_dict.setdefault(n2, 0)
        type_dict[n2] += 1
for each_type in type_dict.keys():
    print('该文件夹下共有类型为【%s】的文件 %d 个' % (each_type, type_dict[each_type]))
