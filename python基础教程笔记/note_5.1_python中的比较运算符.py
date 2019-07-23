# -*- coding: utf-8 -*-

#p    ython中的比较运算符

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
