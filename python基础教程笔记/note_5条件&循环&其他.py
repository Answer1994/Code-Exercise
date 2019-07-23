# -*- coding: utf-8 -*-

###条件、循环和其他语句

## more about print

#使用逗号输出,以打印多个表达式
print 1,2,3   #注意print并不能构成一个元组
print (1,2,3)
name = 'John'
saluation = 'Mr.'
greeting = 'hello,'
print greeting,saluation,name
#若greeting字符串不带逗号，则
greeting = 'hello'
print greeting + ',',saluation,name
#在结尾处加上一个逗号，那么接下来的语句就会与前一条语句打印在同一行
print 'hello,',
print 'world!'
##more about import
#从模块中导入函数，可以用import somemodule 或者 from somemodule import somefunction, anotherfunction, yetanotherfunction 或者
#from somemodule import *(当从给定的模块导入所有功能时)，同样还可以为模块提供别名以区别不同模块下的同名函数，例：
import math as foobar
print foobar.sqrt(4)
from math import sqrt as foobar #也可以为函数提供别名
print foobar(4)


##赋值魔法

#序列解包
values = 1,2,3
print values
x,y,z = values
print x
#序列解包允许函数返回一个一个以上的值并打包成元组，以popitem为例
scound = {'name':'Robin','girlfriend':'martin'}
key, value = scound.popitem()
print key
print value
print key,value

#链式赋值 chained assignment 是将同一个赋值给多个变量的捷径
# x = y = somefunction
#or x = somefunction
#   x = y 
#但上面的与下面的不一定等价
# x = somefunction
# y = somefunction

#增量赋值
x = 2
x += 1  # x = x + 1
x *= 2  # x = x * 2
print x

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print fnord


##语句块：缩排的乐趣；语句块是在条件为真时执行或者执行多次的一组语句


##条件和条件语句

#布尔值
print True
print False
print True == 1
print False == 0
print True + False + 42

#if and else
name = raw_input("what's your name?")
if name.endswith('Gumby'):
    print 'Hello, Mr.Gumby'
else:
    print 'Hello, stranger'  #注意if 和else语句要以冒号结尾

#elif (else if)
num = input('Enter a number:')
if num > 0:
    print 'The number is positive'
elif num < 0 :
    print 'The number is negative'
else:
    print 'The numner is zero'

#嵌套代码块
name = raw_input("what's your name?")
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print 'Hello, Mr.Gumby'
    elif name.startswith('Mrs.'):
        print 'Hello, Mrs.Gumby'
    else:
        print 'Hello, Gumby'
else:
    print 'Hello, stranger' 

#更复杂的条件
#    python中的比较运算符
#  表达式              描述
#  x == y            等于
#  x < y             小于
#  x > y             大于
#  x >= y            大于等于
#  x <= y            小于等于
#  x != y            不等于
#  x is y            x和y是同一个对象
#  x is not y        x和y不是同一个对象 
#  x in y            x是y的成员
#  x not in y        x不是y的成员
x = y = [1,2,3]
z = [1,2,3]
print x == y
print x is y
print x is z #这里是false是因为is判定的是同一性而不是相等性，x和z并没有绑定在同一个列表 
x = [1,2,3]
y = [2,1]
print x is not y
del x[2]
y.reverse()
print x == y
print x is y
#字符串和序列的比较
print 'alpha' < 'beta'
print [1,2] < [2,1]
#布尔运算符 and, or, not
number = input('Enter a number between 1 and 10:')
if number <= 10 and number >= 1:
    print 'Great!'
else:
    print 'Wrong!'

#断言 assert与其让程序在晚些时候崩溃，不如在出错时直接崩溃
#assert类似于检查点，在确保某个条件一定为真时才正常工作
#age = -1
#assert 0 < age < 100, 'the age must be realistic'
#注意上面两行的代码如果运行的话，那么程序运行到这里就会停止，下面的程序不会再运行，因为上述条件为False
age = 10
assert 0 < age < 100, 'the age must be realistic'

##循环

#while循环
x = 1
while x <= 100:
    print x
    x += 1

#for循环   (能用for循环，尽量不用while循环)
numbers = [0,1,2,3,4,5,6,7]
for number in numbers:
    print number

print range(10) #range函数默认下限为0
print range(1,10,2)
for number in range(1,38):
    print number

#循环遍历字典元素
d = {'x':1, 'y':2, 'z':3}
for key in d:
    print key,'correspond to', d[key]

for key, value in d.items():
    print key, 'correspond to', value

#一些迭代（循环）工具
#并行迭代：同时迭代两个序列
names = ['ame','beth','george','domn']
ages = [12,45,32,102]
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old'
#或者用内建的zip函数并行迭代
print zip(names, ages)
for name,age in zip(names,ages):  #在循环中解包元组
    print name, 'is', 'age', 'years old'

print zip(range(5), xrange(1000000)) #zip可以应付不等长序列， xrange类似于range，但是xrange一次只创建一个数
#编号迭代

#跳出循环
#break
from math import sqrt
for n in range(99,0,-1):
    root = sqrt(n)
    if root == int(root):
        print n 
        break
#continue:结束当前迭代，跳到下一循环的开始
#while True/break习语  ??????
#循环中的else语句：
from math import sqrt
for n in range(99,81,-1):
    root = sqrt(n)
    if root == int(root):
        print n
        break
else:
    print "Didn't find it!"


##list comprehension列表推导式 ：利用其它列表创建新列表，类似于for循环
print [x*x for x in range(10)]
print [x*x for x in range(10) if x % 3 == 0]
print [(x,y) for x in range(3) for y in range(3)]   #注：range函数的上限是取不到的
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print result

girls = ['alice','bernice','clarie']
boys = ['chirs','answer','bob']
print [b + '+' + g for b in boys for g in girls if b[0]==g[0]]


##pass,del,exec
#pass占位符，即在代码块中缺少代码，就先用pass，这样程序依旧可以先测试
if name == 'martin':
    print 'welcome!'
elif name == 'john':
    #还没完。。。。
    pass
elif name == 'James':
    print 'Access Denied'
#使用del删除
x = ['hello','world']
y = x
y[1] = 'python'
print x
del x
print y   #x删除后，y依旧存在
#使用exec和eval执行和求值字符串
print eval(raw_input('Enter an arithmetic expression:'))







































