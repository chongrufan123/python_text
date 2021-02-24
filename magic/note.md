# 魔法方法


<!-- vim-markdown-toc Marked -->

* [构造和折构](#构造和折构)

<!-- vim-markdown-toc -->

## 构造和折构
- __init__(self[, ...])
对象初始化时进行调用
- __new__(cls[, ...])
当继承的父类的方法不可改变时可以重写new方法,在init方法之前调用  
是调用的第一个方法
```
class CapStr(str):
    def __new__(cls, string):
        string = string.upper() //式string变成大写
        return str.__new__(cls, string)
```
- __del__(self)
当所有指向该类的对象都del之后触发该方法
