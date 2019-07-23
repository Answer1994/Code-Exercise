# -*- coding: utf-8 -*-

#基本字符串操作（所有标准的序列操作对字符串同样适用如索引，分片，乘法成员资格，长度，最值，但字符串是不可变的，所以不能进行分片赋值）

#字符串格式化
formation = 'hello,%s,%s,enough fpr ya?'
values = ('world','hot')
print formation%values

#find用于在较长字符串中查找子字符串

#join用于添加元素
seq = ['1','2','3','4','5'] #这里不能用seq=[1,2,3,4,5]因为需要添加的元素必须是字符串
sep = '+'
print sep.join(seq)
#lower返回字符串的小写字母版
name = 'Gumby'
names = ['gumby','smith','jones']
if name.lower() in names: print 'Found it!'
#与lowerx相反的是title
#capwords 正确的首字母大写的标题
import string
print string.capwords("that's all, folks")

#replace 替换
print 'this is a test'.replace('is','eez')

#split将字符串分割成序列
print '1+2+3+4'.split('+')
print 'using the default'.split()

#strip返回去除两侧（不包括内部）空格的字符串
print '        internal withespace is kept       '.strip()
print '*** SPAM*for*everyone!!!***'.strip(' *!') #strip也可以去除指定的字符，但只能去除两侧的

#translate替换
from string import maketrans #转换表
table = maketrans('cs','kz')
print 'this is an increadible test'.translate(table)














