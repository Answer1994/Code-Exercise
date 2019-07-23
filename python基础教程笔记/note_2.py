# -*- coding: utf-8 -*-

#数据结构  序列：列表和元组 （列表可以修改，元组不可以）
martin = ['Kevin Martin', 42] #列表的各个元素通过逗号分隔，写在方括号中
john = ['John Smith', 50]
database = [martin, john]
print database

# 通用序列操作：索引indexing，分片sliceing,加adding，乘multiplying,等
#indexing
greeting = 'hello'
print greeting[0] #正数索引时第一个位置为0，负数索引时，最后一个位置为-1
#直接对返回结果进行索引
fourth = raw_input('Year: ')[3]
print fourth

#sliceing
numbers = [1,2,3,4,5,6,7,8,9,10]
print numbers[3:6]  #前包后不包
print numbers[0:1]
print numbers[-3:]
print numbers[:5]
print numbers[0:10:2] #第三个数2指步长，意思就是从开始，每隔一个数做选择
print numbers[::4]
print numbers[::-2] #步长不能为0，但可以为负数，即从右到左提取元素
print numbers[8:3:-1]

#序列相加
num = [1,2,3] + [4,5,6]
'hello' + 'world'
#[1,2,3] + 'hello'  # 字符串和列表是无法相加的

#乘法
print 'python '*5
print [42]*10

# None 是Python的一个内建值，指“这里什么也没有”
sequence = [None]*10 #初始化一个长度为10的列表
print sequence

#成员资格，用于检查某个值是否在序列中
# 'p' in python

# 长度，最值
numbers = [100,34,456]
print len(numbers)
print max(numbers)
print min(numbers)

# list函数 (适用于所有类型的序列)
print list('hello') 

#基本的列表操作
  #元素赋值
x = [1,1,1]
x[1] = 2
print x
  #元素删除
names = ['alice','john','martin','david']
del names[2]
print names
  #分片赋值（可以使用与原序列不等长的序列将分片替换）
name = list('Prel')
name[1:] = list('ython')
print name

numbers = [1,5]
numbers[1:1] = [2,3,4]
print numbers
names[2:] = ['mike','kobe']
print names

numbers[1:4] = [] #通过分片赋值来删除元素,等于del numbers[1:4] 
print numbers


#列表方法
#append用于在列表末尾增加新的对象
lst = [1,2,3]
lst.append(4)
print lst
#count统计元素出现次数
T = ['to','be','or','not','to','be']
print T.count('to')
#extend可以在列表的末尾一次性追加另一个序列中的多个值
a = [1,2,3]
b = [4,5,6]
a.extend(b)
print a
a + b #a.extend(b)方法是修改了原序列a， 而a + b则是构建了另外一个新序列
#index索引，用于从列表中找出某个值第一个匹配的索引位置
knights = ['we','are','the','knights','who','say','ni']
print knights.index('who')
#insert用于将对象插入到列表
numbers = [1,2,3,5,6,7]
numbers.insert(3,4)#(位置，对象)
print numbers
#pop移除列表中的一个元素（默认为最后一个）并返回该元素值
x = [1,2,3]
x.pop()
x.pop(0)#移除第一个元素
x.append(x.pop())#保持不变
#remove用于移除列表中某个值的第一个匹配项
T.remove('be')
#reverse元素反向存放
x.reverse()
print x
#sort用于在原位置对列表进行排序
y = [4,6,1,7,9,3,11]
y.sort()
print y
#sort函数改变列表但不返回值，原有列表已改变排序，想得到排序的和原有的都保留，
#不能用m = y.sort()这种方法，应该先先把y的副本赋值给m，再对m进行排序
y = [4,6,1,7,9,3,11]
m = y[:]#这里不能写m = y
m.sort()
print y
print m
#获得已排序的副本的另一种方法
y = [4,6,1,7,9,3,11]
n = sorted(y)
print n
#sorted函数可以用于任何序列，但总是返回一个列表
#sort方法的两个参数
#x.sort(key = len)是根据长度排序，x.sort(reverse = True)则是进行反向排序

#元组（不可变序列）
#实现一个值的元组，值后必须加上一个逗号
#3*（40+2）
#3*（40+2，）

















































