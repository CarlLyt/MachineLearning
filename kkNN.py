# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:20:52 2018

@author: Administrator
"""
from numpy import *
import operator

def CreatDataSet():
    group = array([[1.0, 1.1],[1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ["A","A","B","B"]
    return group, labels

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]                      
    diffMat = tile(inX, (dataSetSize,1)) - dataSet   
     """
     # 0  1  2 ... 代表矩阵维度，例如shape[0]代表计算第一维数据的长度
     #tile(a, reps) 是矩阵重复，代表讲a重复reps
     #这里的reps是重复(dataSetSize,1)看下面的
     >>> a = np.array([0,1,2])
     >>> a
     array([0, 1, 2])     //这是示例的原始数据
                                                                                
     >>> np.tile(a,(1,1,1))  //这里是3维的重复，当作参照物进行对比
     array([[[0, 1, 2]]])
                                                        
                                                        
     >>> np.tile(a,(2,1,1)   //每一对[]代表一维的数据  （2，1，1）先从2开始
    //故从最外面的[]开始，将剩下的2倍
    array([[[0, 1, 2]],
                                                        
          [[0, 1, 2]]])
    
    
    >>> np.tile(a,(1,1,2))    //每一对[]代表一维的数据  （1，1，2）先从1开始
    //故进入最外面的[]开始，1倍
    //再进入外面的[]开始，1倍
    //最后进入最里面面的[]开始，2倍
    array([[[0, 1, 2, 0, 1, 2]]])
                                                        
    >>> np.tile(a,(1,2,1))
    array([[[0, 1, 2],
            [0, 1, 2]]])
    """
                                                        
                                                        
    sqDiffMat = diffMat ** 2                        
    """
    这是矩阵数乘，矩阵对应每个元素平方   np.dot(A，B)才是真正意义的矩阵乘法
    """
    sqDistances = sqDiffMat.sum(axis = 1)   
    """
  >>> np.sum([[0,1,2],[2,1,3],[1,2,3]],axis=0)  axis=0
  从第一个[]进入，计算里面的的矩阵数值，符合矩阵加法
  array([3, 4, 8])
                                                
  
  >>> np.sum([[0,1,2],[2,1,3],[1,2,3]],axis=1)
  进入到第二个[]，计算里面的数值，现在都是一维数据，直接满足加法
  array([3, 6, 6])
  >>>

"""
    distances = sqDistances ** 0.5   
    """
    矩阵数开方
    """
    sorteDistIndicies = distances.argsort()
    """
    按照数值的从小 到 大  的顺序，将标签返回
    """
    classCount = {}
    
    for i in range(k):
        voteIlabel = labels[sorteDistIndicies[i]]
        
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
        
        
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    
    return sortedClassCount[0][0]
