# -*- coding: utf-8 -*-

##创建函数

#callable判断是否可调用
import math
x = 1
y = math.sqrt
print callable(x)    #Ccallable用于判断是否是函数
print callable(y)
#定义函数def
def hello(name):
    return 'Hello, '+ name + '!'
print hello('world')
print hello('gumby')
#记录函数：解释函数可以用#，也可以用文档字符串
def square(x):
    'Calculates the square of the number x.'
    return x*x
print square.__doc__  #访问文档字符串的方法； __doc__是函数属性
#关键字参数和位置参数
#之前的参数都是未知参数，关键字参数可以帮助设定默认值
def hello(greeting = 'hello', name = 'world'):
    print '%s, %s !' % (greeting, name)
print hello()
print hello('Greetings')
print hello(name = 'John')


##递归：调用或者引用自身的意思
#阶乘
def factorial(n):  #原版本
    result = n
    for i in range(1,n):
        result *= i
    return result
print factorial(9)

def factorial(n):  #递归版本
    if n ==1:
        return 1
    else:
        return n*factorial(n-1)
print factorial(11)

#幂
def power(x,n):  #原版本
    result = 1
    for i in range(n):
        result *= x
    return result
print power(3,4)

def power(x,n):
    if n== 0:
        return 1
    else:
        return x * power(x, n-1)
print power(4,5)










