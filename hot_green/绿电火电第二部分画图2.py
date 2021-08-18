import numpy as np
from scipy import interpolate
import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pandas as pd
import os


# path="\\火电绿电2\\min\\第二部分\\cdcp\\"
# path2="\\零一二五\\第二部分\\cdcp\\"
# zen=[0,2,0,2]
# yl="${C_d}$"
# xl="${C_p}$"
# sh=0.8
# sh1=1


# path="\\火电绿电2\\min\\第二部分\\chcg\\"
# path2="\\零一二五\\第二部分\\chcg\\"
# zen=[0,2,0,2]
# yl="${C_h}$"
# xl="${C_g}$"
# sh=0.8
# sh1=1
#
# #
# path="\\火电绿电2\\min\\第二部分\\ef\\"
# path2="\\零一二五\\第二部分\\ef\\"
# zen=[0,2,0,2]
# yl="e"
# xl="f"
# sh=0.8
# sh1=1

# path="\\火电绿电2\\min\\第二部分\\pgpe\\"
# path2="\\零一二五\\第二部分\\pgpe\\"
# zen=[0,2,0,2]
# yl="${p_g}$"
# xl="${p_e}$"
# sh=0.8
# sh1=1
#
#
# path="\\火电绿电2\\min\\第二部分\\vr\\"
# path2="\\零一二五\\第二部分\\vr\\"
# zen=[0,5,1,5]
# yl="radius"
# xl="velocity"
# sh=0.65
# sh1=0.85
# path="\\火电绿电2\\min\\第二部分\\pe\\"
# path2="\\零一二五\\第二部分\\pe\\"
# zen=[0,2,0,2]
# yl="${b_1}$"
# xl="${b_0}$"
# sh=0.8
# sh1=1

# path="\\火电绿电2\\min\\第二部分\\pgpe\\"
# path2="\\零一二五\\第二部分\\pgpe\\"
# zen=[0,2,0,2]
# yl="${p_g}$"
# xl="${p_e}$ (${b_0}$)"
# sh=0.8
# sh1=1


path="\\火电绿电2\\min\\第二部分\\vr\\"
path2="\\零一二五\\第二部分\\vr\\"
zen=[0,5,1,5]
yl="Radius"
xl="Velocity"
sh=0.65
sh1=0.85

#
# df0= pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.rcParams['figure.figsize'] = (6.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=zen,origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel(yl,font)
#     plt.xlabel(xl,font)
#     # my_y_ticks =np.arange(0,2,0.5)
#     # plt.yticks(my_y_ticks,("50","200","350","500"))
#     plt.colorbar(shrink=sh)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图'+path2+i+'.png')

# nu="完成配额以传统能源为主的电力企业不交易人数"
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (6.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.imshow(BB[nu], cmap="rainbow",extent=zen,origin='lower',vmin=0, vmax=1,interpolation='kaiser')
# plt.ylabel(yl,font)
# plt.xlabel(xl,font)
# # my_y_ticks =np.arange(0,2,0.5)
# # plt.yticks(my_y_ticks,("50","200","350","500"))
# plt.colorbar(shrink=sh1)
# plt.title(BB2[nu],font2)
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图'+path2+nu+'.png')

df12 = pd.DataFrame(pd.read_excel('E:\\data'+path+'被迫进入pool.xlsx',index_col=0))
df13 = pd.DataFrame(pd.read_excel('E:\\data'+path+'完成配额被迫进入pool.xlsx',index_col=0))
df14 = pd.DataFrame(pd.read_excel('E:\\data'+path+'未完成配额被迫进入pool.xlsx',index_col=0))
df15 = pd.DataFrame(pd.read_excel('E:\\data'+path+'绿证价格.xlsx',index_col=0))
df16 = pd.DataFrame(pd.read_excel('E:\\data'+path+'绿证数量供给.xlsx',index_col=0))
df17 = pd.DataFrame(pd.read_excel('E:\\data'+path+'绿证数量需求.xlsx',index_col=0))
df18 = pd.DataFrame(pd.read_excel('E:\\data'+path+'监管部门惩罚.xlsx',index_col=0))
df19 = pd.DataFrame(pd.read_excel('E:\\data'+path+'监管部门奖励.xlsx',index_col=0))
df20 = pd.DataFrame(pd.read_excel('E:\\data'+path+'监管部门效用.xlsx',index_col=0))
font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
font2= {'family' : 'Times New Roman','weight' : 'normal'}
CC={"被迫进入pool":df12.values/500,"完成配额被迫进入pool":df13.values/500,"未完成配额被迫进入pool":df14.values/500,
    "绿证价格":df15.values,"绿证数量供给":df16.values,"绿证数量需求":df17.values,
    "监管部门惩罚":df18.values,"监管部门奖励":df19.values,"监管部门效用":df20.values}
CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
    "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity",
    "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (6.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=zen,origin='lower',interpolation='kaiser')
#     plt.ylabel(yl,font)
#     plt.xlabel(xl,font)
#     # my_y_ticks =np.arange(0,2,0.5)
#     # plt.yticks(my_y_ticks,("50","200","350","500"))
#     plt.colorbar(shrink=sh)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图'+path2+j+'.png')

mu="被迫进入pool"
fig = plt.figure()
plt.rcParams['figure.figsize'] = (6.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.imshow(CC[mu], cmap="rainbow",extent=zen,origin='lower',interpolation='kaiser')
plt.ylabel(yl,font)
plt.xlabel(xl,font)
# my_y_ticks =np.arange(0,2,0.5)
# plt.yticks(my_y_ticks,("50","200","350","500"))
plt.colorbar(shrink=sh1)
plt.title(CC2[mu],font2)
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图'+path2+mu+'.png')