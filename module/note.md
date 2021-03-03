---------------------------------------------------------------------------
	 File Name: note.md
	 Author: Fan Chongru
	 Mail: chongrufan123@gmail.com
	 Created Time: 2021年03月03日 星期三 11时56分21秒
   notes: 
 --------------------------------------------------------------------------

<!-- vim-markdown-toc Marked -->

* [模块](#模块)
    * [命名空间](#命名空间)
    * [模块的导入](#模块的导入)
    * [if __name__ = '__main__'](#if-__name__-=-'__main__')
    * [搜索路径](#搜索路径)
    * [package包](#package包)
    * [内置模块](#内置模块)

<!-- vim-markdown-toc -->
# 模块
每一个程序就是模块

## 命名空间
函数前面要加上模块名如hello.hi()

## 模块的导入
-   import 文件名
-   from 模块名 import 函数名  
    然后之后就只要输入函数名就可以
-   import 模块名 as 别名  
    相当于给模块起个别名, 之后调用只打别名就可以

## if __name__ = '__main__'
当在主程序中调用__name__时返回__main__  
当在某一个模块中调用__name__时返回模块名  
所以在模块中调用
```
if __name__ == '__main__':
    程序体
//当当前程序作为主程序调用时执行下面的语句
```

## 搜索路径
```
import sys
sys.path
得到python模块导入的路径
['', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '/home/pi/.local/lib/python3.7/site-packages', '/usr/local/lib/python3.7/dist-packages', '/usr/lib/python3/dist-packages']
一般是放在site-packages文件中
```
当模块在python模块导入的路径或者本路径中时可以成功导入

## package包
1.  创建一个文件夹, 用来存放相关的模块, 文件夹的名字即为包的名字
2.  在文件夹中创建__init__.py的模块文件, 内容可以为空
3.  将相关的模块放入文件夹

当需要导入包的模块时
```
import 包名.模块名
```

## 内置模块
当要学习一个模块时可以先导入他
```
import 模块名
```
然后查看他的doc文档
```
print(模块名.__doc__)
```
然后看看他们函数
```
dir(模块名)
```
如果有__all__属性的话, __all__里面的方法和属性是作者希望我们调用的, 可以查看
```
模块名.__all__
```
当你全部导入模块的时候
```
from 模块名 import *
```
导入的将是__all__中的模块  
__file__函数提供了源代码的位置
```
模块名.__file__
```


