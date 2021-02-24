# 类和对象

<!-- vim-markdown-toc Marked -->

* [OO的特征](#oo的特征)
* [继承](#继承)
    * [调用未绑定的父类方法](#调用未绑定的父类方法)
    * [使用super函数](#使用super函数)
    * [多重继承](#多重继承)
* [组合](#组合)
* [绑定](#绑定)
* [BIF](#bif)
* [备注](#备注)

<!-- vim-markdown-toc -->
## OO的特征

1. 封装  
对外隐藏对象的工作细节

2. 继承
子类自动共享父类之间的数据和方法的机制

3. 多态
可以对不同类的对象调用相同的方法，产生不同的结果

## 继承

class DerivedClassName(BaseClassName)  
       子类             父类/基类

子类和父类相同定义的方法，子类会把父类覆盖掉  

### 调用未绑定的父类方法  
 在方法中加入 BaseClassName.__init__(self)

### 使用super函数

 super().__init__()

### 多重继承

class Derive(Base1, Base2, Base3...)

## 组合
把一个不是很有继承关系的class搞在一起
```
class Fish:
    def __init__(self, x):
        self.num = x
class Turtle:
    def __init__(self, x):
        self.num = x
class poll:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)
    def print_num(self):
        print(self.turtle.num, self.fish.num)
```
## 绑定
python要有实例概念才可以被调用,也就是在类的函之下要调用函数本身

## BIF
- issubclass(class, classinfo)
检查class是否为classinfo的子类
1. 自身会被认为是自身的子类
2. classinfo可以是一个元组，然后看看class是不是其中一个的子类
- isinstance(object, classinfo)
检查object是否是classinfo的实例对象
1. class可以是一个元组
2. 继承于子类的实例对象同样可以被认为是该父类的实例对象
- hasattr(object, name)
检测object中name属性是否存在
- getattr(object, name[, default]))
获取object中name属性的值，如果name不存在抛出异常，但是如果有设置defaule，将返回default
- setattr(object, name, value)
新在objext中生成一个name,并赋值为value
- delattr(object, name)
在object中删除name属性,如果不存在的话抛出错误
- property(fget, fset, fdel)
## 备注
- __init__特殊方法不能返回除了none之外的任何对象
- 属性名和方法相同会覆盖掉


