import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import random

episodes = 10
act=np.arange(0,1,0.1)
load=5
ame=np.zeros((episodes-load,10))
for episode in range(episodes):
    print(episode)
    ind=np.random.randint(0,10,size=(1,10))[0]
    print(ind)
    if episode>=load:
        for i in range(len(ind)):
            v=ind[i]
            ame[episode-load,i]=act[v]
print(ame)
##基本参数设定

# def plane():
#     pass
# #定义周期性边界
# def distance(g,x,y):
#     pass
# #定义距离计算函数
#
#
# def field(x):
#     pass
# #定义小于半径的邻居是谁
#
# #主循环
# for turn in X:
#    #计算距离矩阵
#    #计算各节点周围的邻居节点
#    #策略更新
#    #移动
#
#
#
# #
