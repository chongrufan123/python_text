# 文件
<!-- vim-markdown-toc Marked -->

* [打开文件](#打开文件)
    * [打开格式](#打开格式)
    * [文件对象方法](#文件对象方法)
* [os模块中的关于文件的函数](#os模块中的关于文件的函数)
* [os.path模块中函数](#os.path模块中函数)
* [pickle 以二进制文件的形式保存对象](#pickle-以二进制文件的形式保存对象)

<!-- vim-markdown-toc -->

## 打开文件
open(file, mode, )
### 打开格式
r   只读  
w   以写入的方式打开  
x   如果文件存在，使用这个格式出现异常  
a   写入方式，如果文件存在，在末尾追加
b   二进制打开  
t   文本模式打开  
'+'   可读写模式  
U   通用换行符支持  

### 文件对象方法
f.close()   关闭文件  

f.read(size=-1)     从文件中读取size个字符

f.readline()        以写入模式打开

f.tell()            告诉现在指针在哪里

f.seek(offset, from)    文件中移动指针，从from偏移offset个字节（1代表当前位置，2代表末尾）

f.write(str)        将字符串str写入文件

f.writelines(seq)           向文件写入字符串序列seq，seq是一个可迭代对象
   
## os模块中的关于文件的函数

|函数名|功能|
|:---:|:----|
|gitcwd()|返回当前工作目录|
|chdir(pash)|改变工作目录|
|listdir(pash='.')|列出目录中的文件|
|mkdir(pash)|创建当前目录|
|makedirs(pash)|创建多级目录|
|remove(pash)|删除文件|
|rmdir(pash)|删除空目录|
|removedirs(pash)|递归删除空目录|
|rename(old, new)|将文件old更换为new|
|system(command)|运行系统命令|
|curdir|指代当前目录|
|pardir|指代上一级目录|
|sep|输出操作系统的路经分隔符|
|name|当前操作系统|
|linesep|当前平台使用的行终止符|


## os.path模块中函数

|函数名|功能|
|:---:|:----|
|basename(path)|去掉目录路径，单独返回文件名|
|dirname(path)|去掉文件名，返回路径|
|split(path)|分割文件名和路径，返回元组|
|splitext(path)|分离文件名和扩展名|
|getsize(file)|返回文件的尺寸，单位字节|
|getatime(file)|返回最近访问时间|
|getctime(file)|返回文件创建时间|
|getmtime(file)|返回文件的最近修改时间|
|time.gmtime()|换算时间为英国时间|
|time.localtime()|换算时间为北京时间|
|下面函数返回True或Fulse|
|exists(path)|判断路径是否存在|
|isabs(path)|判断指定路径是否是绝对路径|
|isdir(path)|判断指定路径是否是相对路径|
|isfile(path)|判断是否是一个文件|

## pickle 以二进制文件的形式保存对象

- 要用wb形式打开写入文件
- 一般来说pickle文件后缀是.pkl
- pickle.dump(对象,文件) 将对象放入文件
- pickle.load(文件) 将文件内的对象读取出来
- 打开pickle文件一般用rb形式
