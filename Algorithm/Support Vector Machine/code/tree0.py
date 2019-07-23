# -*- coding: utf-8 -*

'''
SVMs
resource:http://sklearn.apachecn.org/cn/0.19.0/modules/svm.html#svm
'''

from sklearn import svm
X = [[0,0],[1,1]]
y = [0,1]
clf = svm.SVC()
clf.fit(X,y)

clf.predict([[2.,2.]])

clf.support_vectors_    #获取支持向量
