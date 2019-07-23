# -*- coding: utf-8 -*-

print "hello, world"
#获取用户输入 raw_input （单独的input规定输入的必须是标准的Python可读的）
#name = raw_input("waht is your name?")
#print "hello," + name + "!"
#print "I am a super man" + " and " + "123456789"
#取余数的运算符 %
print 10%3
#乘方函数,绝对值函数
print pow(2,3)
print abs(-19)
#导入模块
import math
math.floor(32.9)
print math.floor(32.9)
math.ceil(32.9)
print math.sqrt(16)
from math import sqrt #从模块直接调用函数后不用再加前缀
print sqrt(9)
import cmath #处理复数
cmath.sqrt(-1)
print cmath.sqrt(-1)


print 123 #这里123是数值，可以单独打印
print "hello" #hello是字符串，要打印的话要加双引号或者单引号
print "hello " + "123"#因为字符串和数字是不可以连接在一起的，所以打印时可以在数字上加引号
temp = 42
print "the tempature is " + repr(temp) #这里使用repr将Python值转换为字符串,也可以用str或者反引号
#str和repr都是把值转化为字符串，str让字符串更容易阅读，repr则把结果字符串转化为合法的Python表达式
print '''this is a very long string,
it continues here''' #跨行时用三个引号代替普通引号
print 'hello, \
world' #用反斜线跨行，反斜线也可以用来转义


##input 和 raw_input的区别
#input会假设用户输入的是合法的Python表达式，Python中输入字符串必须加引号，
#raw_input会把所有输入当做原始数据，然后将其放入字符串中
name  = input("what's your name?")  #这里的输入必须加引号
print 'hello' + name + '!'
name  = raw_input("what's your name?")  #这里的输入不用加引号
print 'hello ' + name + '!'

























