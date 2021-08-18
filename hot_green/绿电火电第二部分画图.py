import numpy as np
from scipy import interpolate
import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pandas as pd
import os
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,10,1.5,10],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("Radius",font)
#     plt.xlabel("Velocity",font)
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\VR'+i+'.png')

# CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
#     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
#     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,10,1.5,10],origin='lower',interpolation='kaiser')
#     plt.ylabel("Radius",font)
#     plt.xlabel("Velocity",font)
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\VR'+j+'.png')





# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp2\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# # for i in BB:
# #     # print(i)
# #     # print(BB[i])
# #     fig = plt.figure()
# #     plt.rcParams['figure.figsize'] = (10.0, 6.0)
# #     plt.rcParams['savefig.dpi'] = 1000 #图片像素
# #     plt.rcParams['figure.dpi'] = 1000 #
# #     plt.imshow(BB[i], cmap="rainbow",extent=[0,3,0,3],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
# #     plt.ylabel("${C_d}$",font)
# #     plt.xlabel("${C_p}$",font)
# #     plt.colorbar(shrink=1)
# #     plt.title(BB2[i],font2)
# #     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\cdcp2'+i+'.png')
#
# # CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
# #     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
# #     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# # CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
# #     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
# #     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# # for j in CC:
# #     # print(i)
# #     # print(BB[i])
# #     fig = plt.figure()
# #     plt.rcParams['figure.figsize'] = (10.0, 6.0)
# #     plt.rcParams['savefig.dpi'] = 1000 #图片像素
# #     plt.rcParams['figure.dpi'] = 1000 #
# #     plt.imshow(CC[j], cmap="rainbow",extent=[0,3,0,3],origin='lower',interpolation='kaiser')
# #     plt.ylabel("${C_d}$", font)
# #     plt.xlabel("${C_p}$", font)
# #     plt.colorbar(shrink=1)
# #     plt.title(CC2[j],font2)
# #     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\cdcp2'+j+'.png')


# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\cdcp\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,2,0,2],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${C_d}$",font)
#     plt.xlabel("${C_p}$",font)
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\cdcp'+i+'.png')

# CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
#     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
#     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,3,0,3],origin='lower',interpolation='kaiser')
#     plt.ylabel("${C_d}$", font)
#     plt.xlabel("${C_p}$", font)
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\cdcp'+j+'.png')






# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\第二部分\pe\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,5,0,5],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${b_0}$",font)
#     plt.xlabel("${b_1}$",font)
#     my_x_ticks =np.arange(0,5,0.5)
#     plt.xticks(my_x_ticks,("50","100","150","200","250","300","350","400","450","500"))
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\pe'+i+'.png')

# CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
#     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
#     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,5,0,5],origin='lower',interpolation='kaiser')
#     plt.ylabel("${b_0}$", font)
#     plt.xlabel("${b_1}$", font)
#     my_x_ticks =np.arange(0,5,0.5)
#     plt.xticks(my_x_ticks,("50","100","150","200","250","300","350","400","450","500"))
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\pe'+j+'.png')






# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,3,0,3],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("e",font)
#     plt.xlabel("f",font)
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\ef'+i+'.png')

# CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
#     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
#     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,3,0,3],origin='lower',interpolation='kaiser')
#     plt.ylabel("e", font)
#     plt.xlabel("f", font)
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\ef'+j+'.png')





# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\新建文件夹\ef2\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,3,0,3],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("e",font)
#     plt.xlabel("f",font)
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\ef2'+i+'.png')

# CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
#     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
#     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,3,0,3],origin='lower',interpolation='kaiser')
#     plt.ylabel("e", font)
#     plt.xlabel("f", font)
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\ef2'+j+'.png')





# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pg\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,3,0,3],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${p_e}$",font)
#     plt.xlabel("${p_g}$",font)
#     my_y_ticks =np.linspace(0,3,9)
#     plt.yticks(my_y_ticks,("${b_0}$=1,${b_1}$=250","${b_0}$=2,${b_1}$=250","${b_0}$=3,${b_1}$=250","${b_0}$=1,${b_1}$=350","${b_0}$=2,${b_1}$=350","${b_0}$=3,${b_1}$=350","${b_0}$=1,${b_1}$=450","${b_0}$=2,${b_1}$=450","${b_0}$=3,${b_1}$=450"))
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\pg'+i+'.png')

# CC={"被迫进入pool":df12.values/800,"完成配额被迫进入pool":df13.values/800,"未完成配额被迫进入pool":df14.values/800,
#     "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
#     "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,3,0,3],origin='lower',interpolation='kaiser')
#     plt.ylabel("${p_e}$", font)
#     plt.xlabel("${p_g}$", font)
#     my_y_ticks = np.linspace(0, 3, 9)
#     plt.yticks(my_y_ticks, (
#     "${b_0}$=1,${b_1}$=250", "${b_0}$=2,${b_1}$=250", "${b_0}$=3,${b_1}$=250", "${b_0}$=1,${b_1}$=350",
#     "${b_0}$=2,${b_1}$=350", "${b_0}$=3,${b_1}$=350", "${b_0}$=1,${b_1}$=450", "${b_0}$=2,${b_1}$=450",
#     "${b_0}$=3,${b_1}$=450"))
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\ef2'+j+'.png')





# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\A\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# x=np.arange(0,250)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b0,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,b1,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,b2,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,b6,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,b7,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,b8,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\传统能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b3,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,b4,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,b5,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,b9,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,b10,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,b11,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\清洁能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df12.values/800,lw=1,label="Forced with TP",color="r")
# plt.plot(x,df13.values/800,lw=1,label="H type Forced with TP",color="g")
# plt.plot(x,df14.values/800,lw=1,label="L type Forced with TP",color="b")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Forced",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\被迫.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df15.values,lw=1,label="Green Certificate Price",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Price",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证价格.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df16.values,lw=1,label="Green Certificate Supply Quantity",color="r")
# plt.plot(x,df17.values,lw=1,label="Green Certificate Required Quantity",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Quantity in Pool",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证供给需求.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df18.values,lw=1,label="Regulatory Penalty Coefficient",color="r")
# plt.plot(x,df19.values,lw=1,label="Regulatory Reward Coefficient",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Regulatory Coefficient",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\奖励惩罚系数.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df20.values,lw=1,label="The Utility of the Regulatory",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("The Utility of the Regulatory",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\监管部门效用.png')



# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\B\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# x=np.arange(0,250)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b0,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,b1,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,b2,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,b6,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,b7,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,b8,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\传统能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b3,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,b4,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,b5,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,b9,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,b10,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,b11,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\清洁能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df12.values/800,lw=1,label="Forced with TP",color="r")
# plt.plot(x,df13.values/800,lw=1,label="H type Forced with TP",color="g")
# plt.plot(x,df14.values/800,lw=1,label="L type Forced with TP",color="b")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Forced",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\被迫.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df15.values,lw=1,label="Green Certificate Price",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Price",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证价格.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df16.values,lw=1,label="Green Certificate Supply Quantity",color="r")
# plt.plot(x,df17.values,lw=1,label="Green Certificate Required Quantity",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Quantity in Pool",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证供给需求.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df18.values,lw=1,label="Regulatory Penalty Coefficient",color="r")
# plt.plot(x,df19.values,lw=1,label="Regulatory Reward Coefficient",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Regulatory Coefficient",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\奖励惩罚系数.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df20.values,lw=1,label="The Utility of the Regulatory",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("The Utility of the Regulatory",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\监管部门效用.png')



# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\C\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# x=np.arange(0,250)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b0,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,b1,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,b2,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,b6,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,b7,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,b8,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\传统能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b3,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,b4,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,b5,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,b9,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,b10,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,b11,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\清洁能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df12.values/800,lw=1,label="Forced with TP",color="r")
# plt.plot(x,df13.values/800,lw=1,label="H type Forced with TP",color="g")
# plt.plot(x,df14.values/800,lw=1,label="L type Forced with TP",color="b")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Forced",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\被迫.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df15.values,lw=1,label="Green Certificate Price",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Price",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证价格.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df16.values,lw=1,label="Green Certificate Supply Quantity",color="r")
# plt.plot(x,df17.values,lw=1,label="Green Certificate Required Quantity",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Quantity in Pool",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证供给需求.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df18.values,lw=1,label="Regulatory Penalty Coefficient",color="r")
# plt.plot(x,df19.values,lw=1,label="Regulatory Reward Coefficient",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Regulatory Coefficient",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\奖励惩罚系数.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df20.values,lw=1,label="The Utility of the Regulatory",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("The Utility of the Regulatory",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\监管部门效用.png')



# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\D\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# x=np.arange(0,250)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b0,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,b1,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,b2,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,b6,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,b7,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,b8,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\传统能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b3,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,b4,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,b5,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,b9,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,b10,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,b11,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\清洁能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df12.values/800,lw=1,label="Forced with TP",color="r")
# plt.plot(x,df13.values/800,lw=1,label="H type Forced with TP",color="g")
# plt.plot(x,df14.values/800,lw=1,label="L type Forced with TP",color="b")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Forced",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\被迫.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df15.values,lw=1,label="Green Certificate Price",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Price",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证价格.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df16.values,lw=1,label="Green Certificate Supply Quantity",color="r")
# plt.plot(x,df17.values,lw=1,label="Green Certificate Required Quantity",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Quantity in Pool",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证供给需求.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df18.values,lw=1,label="Regulatory Penalty Coefficient",color="r")
# plt.plot(x,df19.values,lw=1,label="Regulatory Reward Coefficient",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Regulatory Coefficient",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\奖励惩罚系数.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df20.values,lw=1,label="The Utility of the Regulatory",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("The Utility of the Regulatory",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\监管部门效用.png')


# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\单图\F\监管部门效用.xlsx',index_col=0))
#
# b0=df0.values/200
# b1=df1.values/200
# b2=df2.values/200
# b3=df3.values/200
# b4=df4.values/200
# b5=df5.values/200
# b6=df6.values/200
# b7=df7.values/200
# b8=df8.values/200
# b9=df9.values/200
# b10=df10.values/200
# b11=df11.values/200
# x=np.arange(0,250)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b0,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,b1,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,b2,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,b6,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,b7,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,b8,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\传统能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,b3,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,b4,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,b5,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,b9,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,b10,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,b11,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\清洁能源.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df12.values/800,lw=1,label="Forced with TP",color="r")
# plt.plot(x,df13.values/800,lw=1,label="H type Forced with TP",color="g")
# plt.plot(x,df14.values/800,lw=1,label="L type Forced with TP",color="b")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Forced",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\被迫.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df15.values,lw=1,label="Green Certificate Price",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Price",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证价格.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df16.values,lw=1,label="Green Certificate Supply Quantity",color="r")
# plt.plot(x,df17.values,lw=1,label="Green Certificate Required Quantity",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Green Certificate Quantity in Pool",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\绿证供给需求.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df18.values,lw=1,label="Regulatory Penalty Coefficient",color="r")
# plt.plot(x,df19.values,lw=1,label="Regulatory Reward Coefficient",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Regulatory Coefficient",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\奖励惩罚系数.png')
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df20.values,lw=1,label="The Utility of the Regulatory",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("The Utility of the Regulatory",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\监管部门效用.png')










# # os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第二部分\\差额")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# b0=df0.values/125
# b1=df1.values/125
# b2=df2.values/125
# b3=df3.values/125
# b4=df4.values/125
# b5=df5.values/125
# b6=df6.values/125
# b7=df7.values/125
# b8=df8.values/125
# b9=df9.values/125
# b10=df10.values/125
# b11=df11.values/125
#
font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,1,0,1],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${C_g}$",font)#hang
#     plt.xlabel("${C_h}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\差额\差额'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\差额\监管部门效用.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "绿证价格":b15,"绿证数量供给":b16,"绿证数量需求":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,1,0,1],origin='lower',interpolation='kaiser')
#     plt.ylabel("${C_g}$",font)#hang
#     plt.xlabel("${C_h}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\差额\差额'+j+'.png')
# print("完成1")



# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第二部分\\pgpe")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# b0=df0.values/125
# b1=df1.values/125
# b2=df2.values/125
# b3=df3.values/125
# b4=df4.values/125
# b5=df5.values/125
# b6=df6.values/125
# b7=df7.values/125
# b8=df8.values/125
# b9=df9.values/125
# b10=df10.values/125
# b11=df11.values/125
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,2,0,2],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${p_g}$",font)#hang
#     plt.xlabel("${p_e}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\pgpe\pgpe'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pgpe\监管部门效用.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "绿证价格":b15,"绿证数量供给":b16,"绿证数量需求":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,2,0,2],origin='lower',interpolation='kaiser')
#     plt.ylabel("${p_g}$",font)#hang
#     plt.xlabel("${p_e}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\pgpe\pgpe'+j+'.png')
# print("完成1")




# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第二部分\\VR")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# b0=df0.values/125
# b1=df1.values/125
# b2=df2.values/125
# b3=df3.values/125
# b4=df4.values/125
# b5=df5.values/125
# b6=df6.values/125
# b7=df7.values/125
# b8=df8.values/125
# b9=df9.values/125
# b10=df10.values/125
# b11=df11.values/125
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,5,1,5],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("radius",font)#hang
#     plt.xlabel("velocity",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\VR\VR'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\VR\监管部门效用.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "绿证价格":b15,"绿证数量供给":b16,"绿证数量需求":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,5,1,5],origin='lower',interpolation='kaiser')
#     plt.ylabel("radius",font)#hang
#     plt.xlabel("velocity",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\VR\VR'+j+'.png')
# print("完成1")




# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第二部分\\EF")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# b0=df0.values/125
# b1=df1.values/125
# b2=df2.values/125
# b3=df3.values/125
# b4=df4.values/125
# b5=df5.values/125
# b6=df6.values/125
# b7=df7.values/125
# b8=df8.values/125
# b9=df9.values/125
# b10=df10.values/125
# b11=df11.values/125
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,5,0,5],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("e",font)#hang
#     plt.xlabel("f",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\EF\EF'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\EF\监管部门效用.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "绿证价格":b15,"绿证数量供给":b16,"绿证数量需求":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,5,0,5],origin='lower',interpolation='kaiser')
#     plt.ylabel("e",font)#hang
#     plt.xlabel("f",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\EF\EF'+j+'.png')
# print("完成1")




# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第二部分\\pe")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# b0=df0.values/125
# b1=df1.values/125
# b2=df2.values/125
# b3=df3.values/125
# b4=df4.values/125
# b5=df5.values/125
# b6=df6.values/125
# b7=df7.values/125
# b8=df8.values/125
# b9=df9.values/125
# b10=df10.values/125
# b11=df11.values/125
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
#     "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
#     "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
#     "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
# BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
#     "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
#     "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
#     "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
# for i in BB:
#     print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,2,0,2],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${b_0}$",font)#hang
#     plt.xlabel("${b_1}$",font)
#     my_x_ticks =np.arange(0,2,0.2)
#     plt.xticks(my_x_ticks,("50","100","150","200","250","300","350","400","450","500"))
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\pe\pe'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\pe\监管部门效用.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "绿证价格":b15,"绿证数量供给":b16,"绿证数量需求":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,2,0,2],origin='lower',interpolation='kaiser')
#     plt.ylabel("${b_0}$", font)  # hang
#     plt.xlabel("${b_1}$", font)
#     my_x_ticks = np.arange(0, 2, 0.2)
#     plt.xticks(my_x_ticks, ("50", "100", "150", "200", "250", "300", "350", "400", "450", "500"))
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\pe\pe'+j+'.png')
# print("完成1")




# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第二部分\\cdcp")
df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

b0=df0.values/125
b1=df1.values/125
b2=df2.values/125
b3=df3.values/125
b4=df4.values/125
b5=df5.values/125
b6=df6.values/125
b7=df7.values/125
b8=df8.values/125
b9=df9.values/125
b10=df10.values/125
b11=df11.values/125

font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
font2= {'family' : 'Times New Roman','weight' : 'normal'}
BB={"完成配额以传统能源为主的电力企业不交易人数":b0,"完成配额以传统能源为主的电力企业与pool交易人数":b1,"完成配额以传统能源为主的电力企业与邻居交易人数":b2,
    "完成配额以可再生能源为主的电力企业不交易人数":b3,"完成配额以可再生能源为主的电力企业与pool交易人数":b4,"完成配额以可再生能源为主的电力企业与邻居交易人数":b5,
    "未完成配额以传统能源为主的电力企业不交易人数":b6,"未完成配额以传统能源为主的电力企业与pool交易人数":b7,"未完成配额以传统能源为主的电力企业与邻居交易人数":b8,
    "未完成配额以可再生能源为主的电力企业不交易人数":b9,"未完成配额以可再生能源为主的电力企业与pool交易人数":b10,"未完成配额以可再生能源为主的电力企业与邻居交易人数":b11}
BB2={"完成配额以传统能源为主的电力企业不交易人数":"H-FC with NT","完成配额以传统能源为主的电力企业与pool交易人数":"H-FC with TP","完成配额以传统能源为主的电力企业与邻居交易人数":"H-FC with TN",
    "完成配额以可再生能源为主的电力企业不交易人数":"H-RC with NT","完成配额以可再生能源为主的电力企业与pool交易人数":"H-RC with TP","完成配额以可再生能源为主的电力企业与邻居交易人数":"H-RC with TN",
    "未完成配额以传统能源为主的电力企业不交易人数":"L-FC with NT","未完成配额以传统能源为主的电力企业与pool交易人数":"L-FC with TP","未完成配额以传统能源为主的电力企业与邻居交易人数":"L-FC with TN",
    "未完成配额以可再生能源为主的电力企业不交易人数":"L-RC with NT","未完成配额以可再生能源为主的电力企业与pool交易人数":"L-RC with TP","未完成配额以可再生能源为主的电力企业与邻居交易人数":"L-RC with TN"}
for i in BB:
    print(i)
    # print(BB[i])
    fig = plt.figure()
    plt.rcParams['figure.figsize'] = (10.0, 6.0)
    plt.rcParams['savefig.dpi'] = 1000 #图片像素
    plt.rcParams['figure.dpi'] = 1000 #
    plt.imshow(BB[i], cmap="rainbow",extent=[0,2,0,2],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
    plt.ylabel("${C_d}$",font)#hang
    plt.xlabel("${C_p}$",font)#lie
    plt.colorbar(shrink=1)
    plt.title(BB2[i],font2)
    plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\cdcp\cdcp'+i+'.png')
print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\绿证数量供给.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\绿证数量需求.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\监管部门效用.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "绿证价格":b15,"绿证数量供给":b16,"绿证数量需求":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,2,0,2],origin='lower',interpolation='kaiser')
#     plt.ylabel("${C_d}$",font)#hang
#     plt.xlabel("${C_p}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\cdcp\cdcp'+j+'.png')
# print("完成1")






# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\绿证价格.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\绿证数量供给.xlsx',index_col=0))
#
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第二部分\cdcp\监管部门效用.xlsx',index_col=0))
#
# b15=df15.values
# b16=df16.values
#
# b18=df18.values
# b19=df19.values
# b20=df20.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"绿证价格":b15,"绿证数量供给":b16,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[0,2,0,2],origin='lower',interpolation='kaiser')
#     plt.ylabel("${C_d}$",font)#hang
#     plt.xlabel("${C_p}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第二部分\cdcp\cdcp'+j+'.png')
# print("完成1")