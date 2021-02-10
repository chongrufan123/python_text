### 打开文件
open(file, mode, )
#### 打开格式
r   只读  
w   以写入的方式打开  
x   如果文件存在，使用这个格式出现异常  
a   写入方式，如果文件存在，在末尾追加
b   二进制打开  
t   文本模式打开  
'+'   可读写模式  
U   通用换行符支持  

#### 文件对象方法
f.close()   关闭文件  

f.read(size=-1)     从文件中读取size个字符

f.readline()        以写入模式打开

f.tell()            告诉现在指针在哪里

f.seek(offset, from)    文件中移动指针，从from偏移offset个字节（1代表当前位置，2代表末尾）

f.write(str)        将字符串str写入文件

f.writelines(seq)           向文件写入字符串序列seq，seq是一个可迭代对象
   
