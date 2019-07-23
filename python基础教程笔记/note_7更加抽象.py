# -*- coding: utf-8 -*-

#创建自己的对象

#多态：多种形式，即使不知道变量所引用的对象类型，也能对其进行操作
#封装： 可以不关心对象是如何构建的而直接进行使用
#继承：从其他类调用某种方法

##类和类型
#类，就是一种对象，所有的对象都属于某一个类，称为类的实例
#鸟类是百灵鸟类的超类（superclass)，百灵鸟类是鸟类的子类（subclass）
#创建自己的类:
__metaclass__ = type #赋值语句，确定使用新式类 

class Person:  #person就是该类的名字

    def setName(self,name):
        self.name = name

    def getName(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s. " % self.name

foo = Person()
foo.setName('Luke Skywalker')
print foo.greet()  
print foo.name
#self是对于对象自身的引用
         