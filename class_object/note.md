# 类和对象

<!-- vim-markdown-toc Marked -->

* [OO的特征](#oo的特征)
* [继承](#继承)
    * [调用未绑定的父类方法](#调用未绑定的父类方法)
    * [使用super函数](#使用super函数)
    * [多重继承](#多重继承)

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

