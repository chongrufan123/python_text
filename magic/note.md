# 魔法方法


<!-- vim-markdown-toc Marked -->

* [构造和折构](#构造和折构)
* [算数运算的魔法方法](#算数运算的魔法方法)
    * [算术运算](#算术运算)
    * [反运算](#反运算)
    * [赋值运算](#赋值运算)
    * [一元操作符](#一元操作符)
    * [比较操作符](#比较操作符)
    * [静态方法](#静态方法)
* [鸭子类型](#鸭子类型)
* [访问属性](#访问属性)
* [描述符](#描述符)
* [容器类型](#容器类型)
* [迭代器](#迭代器)
* [生成器](#生成器)
    * [协同程序](#协同程序)
* [备注](#备注)

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

## 算数运算的魔法方法
```
divmod()    //生成一个元组,前面放整除结果,后面放余数
```
### 算术运算
|魔法方法|作用|符号|
|:---|:---|:---|
|__add__(self, other)|定义加法行为|+|
|__sub__(self, other)|定义减法行为|-|
|__mul__(self, other)|定义乘法行为|*|
|__truediv__(self, other)|定义真除法行为|/|
|__floordiv__(self, other)|定义整数除法行为|//|
|__mod__(self, other)|定义取模行为|%|
|__divmod__(self, other)|定义当被divmod()调用的行为|divmod()|
|__pow__(self, other[, modulo])|定义当被power()调用的行为|**|
|__lshift__(self, other)|定义按位左移位|\<\<|
|__rshift__(self, other)|定义按位右移位|\>\>|
|__and__(self, other)|定义按位与|&|
|__xor__(self, other)|定义按位异或|^|
|__or__(self, other)|定义按位或|\||

### 反运算
运算过程中后面的那个数,当第一个运算符没有定义时采用第二个运算符的反运算进行运算

|魔法方法|作用|符号|
|:---|:---|:---|
|__radd__(self, other)|定义加法行为|+|
|__rsub__(self, other)|定义减法行为|-|
|__rmul__(self, other)|定义乘法行为|*|
|__rtruediv__(self, other)|定义真除法行为|/|
|__rfloordiv__(self, other)|定义整数除法行为|//|
|__rmod__(self, other)|定义取模行为|%|
|__rdivmod__(self, other)|定义当被divmod()调用的行为|divmod()|
|__rpow__(self, other)|定义当被power()调用的行为|**|
|__rlshift__(self, other)|定义按位左移位|\<\<|
|__rrshift__(self, other)|定义按位右移位|\>\>|
|__rand__(self, other)|定义按位与|&|
|__rxor__(self, other)|定义按位异或|^|
|__ror__(self, other)|定义按位或|\||

### 赋值运算
自己的一些行为

|魔法方法|作用|符号|
|:---|:---|:---|
|__iadd__(self, other)|定义加法行为|+=|
|__isub__(self, other)|定义减法行为|-=|
|__imul__(self, other)|定义乘法行为|*=|
|__itruediv__(self, other)|定义真除法行为|/=|
|__ifloordiv__(self, other)|定义整数除法行为|//=|
|__imod__(self, other)|定义取模行为|%=|
|__ipow__(self, other[, modulo])|定义当被power()调用的行为|**=|
|__ilshift__(self, other)|定义按位左移位|\<\<=|
|__irshift__(self, other)|定义按位右移位|\>\>=|
|__iand__(self, other)|定义按位与|&=|
|__ixor__(self, other)|定义按位异或|^=|
|__ior__(self, other)|定义按位或|\|=|

### 一元操作符
|魔法方法|作用|符号|
|:---|:---|:---|
|__pos__(self)|定义正号|+x|
|__neg__(self)|定义负号|-x|
|__abs__(self)|定义绝对值|abs()|
|__invert__(self)|定义按位求反|~x|

### 比较操作符
|魔法方法|作用|符号|
|:---|:---|:---|
|__lt__(self, other)|定义小于号|\<|
|__le__(self, other)|定义小于等于号|\<=|
|__eq__(self, other)|定义等于号|==|
|__ne__(self, other)|定义不等号|!=|
|__gt__(self, other)|定义大于号|\>|
|__ge__(self, other)|定义大于等于号|\>=|

### 静态方法
当类中的属性前面没有self时就是静态方法,不会绑定在实例对象上,只会在类中生成一次  

当类中的方法要成为静态方法,需要在前面加上
```
@staticmethod   #表示static()是静态方法
```
## 鸭子类型
> 当看到一只鸟走起来像鸭子, 游泳起来像鸭子, 叫起来也像鸭子, 那么这只鸟就可以被称为鸭子  

只要两个类, 他们在函数中被调用的方法和属性相同的话, 他们都可以被调用

## 访问属性
|魔法方法|作用|
|:---|:---|
|__getattr__(self, name)|定义当用户试图访问一个不存在的属性时|
|__getattribute__(self, name)|定义该属性被访问时|
|__setattr__(self, name, value)|定义当一个属性被设置时|
|__delattr__(self, name)|定义当一个属性被删除时|

## 描述符
就是将某种特殊类型的类的实例指派给另一个类的属性
|魔法方法|作用|
|:---|:---|
|__get__(self, instance, owner)|用于访问属性|
|__set__(self, instance, value)|在属性分配操作中调用|
|__delete__(self, instance)|控制删除操作|

self是描述符所在的类的实例, instance是被指派的类的实例, owner是被指派的类

## 容器类型
|魔法方法|作用|
|:---|:---|
|__len__(self)|定义当len()被调用时的行为|
|__getitem__(self, key)|定义获取容器指定元素的行为,相当于self[key]|
|__setitem__(self, key, value)|定义设置容器中指定元素的行为,类似self[key]=value|
|__delitem__(self,key)|定义删除容器中指定元素的行为|
|__iter__(self)|定义当迭代容器中的元素时的行为|
|__reversed__(self)|定义当被reversed()调用时的行为|
|__contains__(self, item)|定义当使用成员测试符(in or not in)时的行为|

## 迭代器
```
iter()  //构建迭代器
next()  //依次输出迭代器的内容
```

## 生成器
```
yield
```
到达yield之后程序自动被挂起, 并返回yield后面的值, 下一次会接着下一个yield继续走  
最大的作用是可以保留现场, 下次执行函数直接从上次结束的地方开始

### 协同程序
可以运行的的独立函数调用, 函数在此暂停或挂起, 并在需要的时候从程序离开的地方继续或重新开始

## 备注
1. 类的属性名和方法名不能相同
2. super对象没有__getattr__()对象
