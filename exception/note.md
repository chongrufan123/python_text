# 异常处理


<!-- vim-markdown-toc Marked -->

* [异常类型](#异常类型)
* [try-except语句](#try-except语句)
* [try-finally语句](#try-finally语句)
* [raise 语句](#raise-语句)

<!-- vim-markdown-toc -->

## 异常类型

|常见异常|描述|
|:---:|:----|
|AssertionError|断言语句失败|
|AttributeError|尝试访问未知的对象属性|
|IndentationError|缩进错误|
|IndexError|索引超出序列的范围|
|KeyError|字典中查找一个不存在的关键字|
|NameError|尝试访问一个不存在的变量|
|OSError|操作系统的异常（例如打开一个不存在的文件）|
|OverflowError|数值运算超出数值|
|SyntaxError|语法错误|
|TypeError|不同类型间的无效操作|
|ZeroDivisionError|除数为0|

[详细异常表格](http://bbs.fishc.com/thread-45814-1-1.html)

## try-except语句

try:  
    检测范围  
except Exception[as reason]:  
    出现异常后的处理代码

后面加as reason在reason里存储异常的原因

同时捕获两种异常可以用元组

## try-finally语句

try:  
    检测范围  
except Exception[as reason]:  
    出现异常后的代码
finally:
    无论如何都会被执行的代码  

## raise 语句

引发异常

raise 异常名字(异常说明)
