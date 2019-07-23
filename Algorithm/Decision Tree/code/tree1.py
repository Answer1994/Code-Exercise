# -*- coding: utf-8 -*

'''
使用ID3决策树算法预测销量高低
from 《Python数据挖掘与分析实战》P94
copyed by Answer in 2018/11/17
'''
import pandas as pd 
from sklearn.tree import DecisionTreeClassifier as DTC 


#读取数据
filename = '../data/sales_data.xls'
names = ['weather','weekends','promation','sales']
data = pd.read_excel(filename, index_col = u'序号',names = names)   #行列重命名
'''
terminal命令行输入下列代码查看数据
首先进入tree1.py的目录，再输入python3
import tree1
data = tree1.data
data.head()
data.describe()

from imp import reload  
reload(tree1)   (tree1代码修改后再运行需要reload)
'''

#转换数据类别
data[data == u'好'] = 1
data[data == u'是'] = 1
data[data == u'高'] = 1
data[data != 1] = -1

x = data.iloc[:,:3].as_matrix().astype(int)
y = data.iloc[:,3].as_matrix().astype(int)

dtc = DTC(criterion = 'entropy') #基于信息熵，建立决策树模型
dtc.fit(x,y) #训练模型

#导入相关函数，可视化决策树
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
x = pd.DataFrame(x)
with open('tree.dot','w') as f:
  f = export_graphviz(dtc, feature_names = x.columns,out_file = f)


'''
 在terminal命令行输入下列命令将dot文件转换为PDF，png文件
 dot -Tpdf tree.dot -o tree.pdf
 dot -Tpng tree.dot -o tree.png
 '''
 

