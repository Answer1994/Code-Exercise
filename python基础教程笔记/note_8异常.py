# -*- coding: utf-8 -*-

#异常

#Python内建命名空间的exceptions模块可以找到内建异常
import exceptions
print dir(exceptions)

#自定义异常类

#try/except语句：
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except ZeroDivisionError:
    print "The second number can't be zero!"
except TypeError:
    print "That wasn't a number, was it?"
#用一个块捕捉两个异常:
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except (ZeroDivisionError, TypeError, NameError):
    print 'Your numbers were bogus...'

#捕捉对象:在except子句中访问异常对象本身
try:
    x = input('Enter the first number:')
    y = input('Enter the second number:')
    print x/y
except (ZeroDivisionError, TypeError), e:
    print e
#万事大吉
while True:
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')
        value = x/y
        print 'x/y is', value
    except:
        print 'Invalid input. Please try again.'
    else:
        break

#finally子句：用于可能的异常后进行清理
try:
    1/0
except NameError:
    print 'Unknown variable'
else:
    print 'That went well'
finally:
    print 'Cleaning up.'

#如果知道某段代码可能出现异常，又不希望程序以堆栈跟踪的形式终止，那么就用try/except
#或者try/finally处理；有时使用if/else会比try/except要好
















