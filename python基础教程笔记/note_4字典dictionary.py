# -*- coding: utf-8 -*-

#通过名字引用值的数据结构，映射mapping。字典中的值并没有特殊的顺序，但都是储存在一个特定的键里，键可以是数字，字符串，元组

#字典的使用
#用列表举例
names = ['Alice','John','Martin','Bryant']
numbers = ['12334','3456','5643','6789'] #电话号以及其他以0开头的数字应该表示成字符串，而不是整数，因为进制问题
print numbers[names.index('John')]
print names[numbers.index('5643')]

#创建和使用字典
phonebook = {'Alice':'1234','John':'3456','Bryant':'8907'} #'键'：'值'


##dict函数
#用dict创建字典的方法(dict并不是真正的函数，是一个类型，就像list,str)
#方法一
items = [('name','Gumby'),('age',42)] #这里42不加引号就是int，加引号就是string，两者都可以
d1 = dict(items)
print d1
print d1['name']
#方法二,关键字参数
d2 = dict(name = 'Gumby', age = 42, weight = 75)
print d2

#基字典方法
#clear清除字典中所有的项，无返回值
returned_value = d2.clear()
print d2
print returned_value

#copy 
#返回一个具有相同键-值对的新字典（浅复制）
x = {'name':'admin', 'machines':['foo','bar','baz']}
y = x.copy()
y['name'] = 'mlh'
y['machines'].remove('bar') 
print y
print x  #在副本中替换值时，原始字典不受影响，但在原地修改某个值时，原始字典也会改变
#deepcopy 复制其包含所有的值
from copy import deepcopy
d = {}
d['names'] = ['martin','john']
c = d.copy()
dc = deepcopy(d)
d['names'].append('cly')
print c
print dc

#fromkeys用给定的键建立新的字典，每个键默认对应的值为None
print {}.fromkeys(['name','age'])
print dict.fromkeys(['name','age'])
print dict.fromkeys(['name','age'],'(unknown)') #也可以自己提供默认值
#get更轻松的访问字典项的方法（查询）
d = {}
print d.get('name') #当访问字典中不存在的项时会得到None，还可以定义默认值，替换None
print d.get('name','N/A')
d['name'] = 'Eric'
print d.get('name') 

#has_key判断是否存在给出的键
d = {}
print d.has_key('name')
d['name'] = 'Eric'
print d.has_key('name')

#items and iteritems: items将所有的字典项以列表方式返回，但返回时无特殊顺序；iteritems返回的是一个迭代器对象，不是列表
d = {'title':'Python website', 'url':'http://www.python.org','spam':0}
print d.items()
it = d.iteritems()
print it
print list(it) #把（迭代器）iterator转换成list

#keys将字典中的键以列表的形式返回， iterkeys则返回针对键的迭代器

#pop用于获得对应于给定键的值，然后将这个键-值对从字典中移除
d = {'x':1,'y':2}
print d.pop('x')
print d

#popitem:类似于list.pop，但popitem弹出随机的项，因为字典中并没有’最后的元素‘的顺序的概念
d = {'title':'Python website', 'url':'http://www.python.org','spam':0}
print d.popitem()
print d

#setdefault类似于get,除此之外还可以在字典中不含有给定键的情况下设定相应的键值
d = {}
print d.setdefault('name','N/A')
print d
d['name'] = 'Gumby'
print d.setdefault('name','N/A')
print d     #当键不存在时，就会返回默认值并更新字典，若键存在，就返回对应值，但并不改变字典。

#update用于利用一个字典更新另一个字典
d = {
    'title':'Python website',
    'url':'http://www.python.org',
    'spam':0
}
x = {'title':'Python Language Website'}
d.update(x)
print d

#values和itervalues :前者返回字典中的值，后者返回值的迭代器
d = {1:1, 2:2, 3:3,4:1}
print d.values() #与键的返回列表不同的是，值的返回列表可以包含重复的元素
print d.keys() #返回键的列表




































