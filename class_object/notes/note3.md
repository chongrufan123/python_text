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
