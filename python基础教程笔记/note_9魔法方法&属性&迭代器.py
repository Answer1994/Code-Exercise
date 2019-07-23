# -*- coding: utf-8 -*-


#魔法方法：
#类似于__future__，即在名称前后加上两个下划线
__metaclass__ = type #为了保证类是新型的，要把该赋值语句放在模块的最开始


##构造方法：类似于init的初始化方法，但一个对象被创建后，会立即调用构造方法
#在Python中创建构造方法只需要把方法的名字改造为魔法版本
class Foobar():
    def __init__(self):
        self.somevar = 42
f = Foobar()
print f.somevar

class Foobar():
    def __init__(self,value = 42):
        self.somevar = value
f = Foobar()  #不使用参数
print f.somevar
f = Foobar("this is an argument")  #使用参数
print f.somevar
#在所有魔法方法中，__init__最常用

#类B和它的超类A，B可以从A那里继承行为方式
class A(): #这里A后面可以不加括号
    def hello(self):
        print "Hello, I'm A"
class B(A):      
    pass
a = A()
b = B()
print a.hello
print b.hello   #A定义了hello方法，被B继承
#B类也能重写hello这个方法，但会造成不同的结果
class B(A):
    def hello(self):
       print "Hello, i'm B"
b = B()
print b.hello()

#如果一个类的构造方法被重写，则需要调用超类的构造方法，负责对象可能不会被初始化。例：
class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'
b = Bird()
print b.eat()
print b.eat()

class  SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
sb = SongBird()
print sb.sing()

try:  
    print sb.eat() 
except AttributeError, e:
    print e 
#这里会出现异常，因为SongBird中，构造方法被重写，但新的构造方法没有任何关于初始化hungry的特性的代码。
#为了使SongBird调用Bird的构造方法，可以调用超类构造方法的未绑定版本，也可以用super函数。
#调用未绑定的超类构造方法
class SongBird1(Bird):
    def __init__(self):
        Bird.__init__(self) #多加入了这一行
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
sb1 = SongBird1()
print sb1.sing()
print sb1.eat()
print sb1.eat()
#使用super函数
class  SongBird2(Bird):
    def __init__(self):
        super(SongBird2, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
sb2 = SongBird2()
print sb2.sing()
print sb2.eat()
print sb2.eat()

    

            
    








































