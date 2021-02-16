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
