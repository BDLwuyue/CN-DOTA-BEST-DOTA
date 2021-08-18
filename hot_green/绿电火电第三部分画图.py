import numpy as np
from scipy import interpolate
import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pandas as pd
import os

# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第三部分\\差额")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,1,0,1],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${C_g}$",font)#hang
#     plt.xlabel("${C_h}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\差额\差额'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\与pool交易的人数.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\与邻居交易的人数.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\不交易人数.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\监管部门效用.xlsx',index_col=0))
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\不投资人数.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\投资火电人数.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\投资绿电人数.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\电力产量.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\绿电量.xlsx',index_col=0))
# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\差额\绿证数量需求.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# b21=df21.values
# b22=df22.values
# b23=df23.values
# b24=df24.values
# b25=df25.values
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "与pool交易的人数":b15,"与邻居交易的人数":b16,"不交易人数":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20,
#     "不投资人数":b21,"投资火电人数":b22,"投资绿电人数":b23,
#     "电力产量":b24,"绿电量":b25,"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#         "与pool交易的人数":"Number of TP","与邻居交易的人数":"Number of TN","不交易人数":"Number of NT",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory",
# "不投资人数":"Number of No Investment","投资火电人数":"Number of Investment in Traditional Energy","投资绿电人数":"Number of Investment in Renewable Energy",
# "电力产量":"Total Power Generation","绿电量":"Renewable Energy Generation",
#     "绿证价格":"Green Certificate Price","绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\差额\差额'+j+'.png')
# print("完成1")




# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第三部分\\pgpe")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\pgpe\pgpe'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\与pool交易的人数.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\与邻居交易的人数.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\不交易人数.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\监管部门效用.xlsx',index_col=0))
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\不投资人数.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\投资火电人数.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\投资绿电人数.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\电力产量.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿电量.xlsx',index_col=0))
# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿证数量需求.xlsx',index_col=0))
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# b21=df21.values
# b22=df22.values
# b23=df23.values
# b24=df24.values
# b25=df25.values
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "与pool交易的人数":b15,"与邻居交易的人数":b16,"不交易人数":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20,
#     "不投资人数":b21,"投资火电人数":b22,"投资绿电人数":b23,
#     "电力产量":b24,"绿电量":b25,"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#         "与pool交易的人数":"Number of TP","与邻居交易的人数":"Number of TN","不交易人数":"Number of NT",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory",
#      "不投资人数":"Number of No Investment","投资火电人数":"Number of Investment in Traditional Energy","投资绿电人数":"Number of Investment in Renewable Energy",
#      "电力产量":"Total Power Generation","绿电量":"Renewable Energy Generation","绿证价格":"Green Certificate Price",
#      "绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\pgpe\pgpe'+j+'.png')
# print("完成1")

# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pgpe\绿证数量需求.xlsx',index_col=0))
#
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"绿证价格":"Green Certificate Price",
#      "绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\pgpe\pgpe'+j+'.png')
# print("完成1")


# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第三部分\\VR")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\VR\VR'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\与pool交易的人数.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\与邻居交易的人数.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\不交易人数.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\监管部门效用.xlsx',index_col=0))
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\不投资人数.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\投资火电人数.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\投资绿电人数.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\电力产量.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\绿电量.xlsx',index_col=0))
#
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# b21=df21.values
# b22=df22.values
# b23=df23.values
# b24=df24.values
# b25=df25.values
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "与pool交易的人数":b15,"与邻居交易的人数":b16,"不交易人数":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20,
#     "不投资人数":b21,"投资火电人数":b22,"投资绿电人数":b23,
#     "电力产量":b24,"绿电量":b25}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#         "与pool交易的人数":"Number of TP","与邻居交易的人数":"Number of TN","不交易人数":"Number of NT",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory",
#      "不投资人数":"Number of No Investment","投资火电人数":"Number of Investment in Traditional Energy","投资绿电人数":"Number of Investment in Renewable Energy",
#      "电力产量":"Total Power Generation","绿电量":"Renewable Energy Generation"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\VR\VR'+j+'.png')
# print("完成1")
# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\VR\绿证数量需求.xlsx',index_col=0))
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"绿证价格":"Green Certificate Price",
#      "绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\VR\VR'+j+'.png')
# print("完成1")
#
# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第三部分\\EF")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\EF\EF'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\与pool交易的人数.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\与邻居交易的人数.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\不交易人数.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\监管部门效用.xlsx',index_col=0))
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\不投资人数.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\投资火电人数.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\投资绿电人数.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\电力产量.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\绿电量.xlsx',index_col=0))
#
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# b21=df21.values
# b22=df22.values
# b23=df23.values
# b24=df24.values
# b25=df25.values
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "与pool交易的人数":b15,"与邻居交易的人数":b16,"不交易人数":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20,
#     "不投资人数":b21,"投资火电人数":b22,"投资绿电人数":b23,
#     "电力产量":b24,"绿电量":b25}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#         "与pool交易的人数":"Number of TP","与邻居交易的人数":"Number of TN","不交易人数":"Number of NT",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory",
#      "不投资人数":"Number of No Investment","投资火电人数":"Number of Investment in Traditional Energy","投资绿电人数":"Number of Investment in Renewable Energy",
#      "电力产量":"Total Power Generation","绿电量":"Renewable Energy Generation"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\EF\EF'+j+'.png')
# print("完成1")
# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\EF\绿证数量需求.xlsx',index_col=0))
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"绿证价格":"Green Certificate Price",
#      "绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\EF\EF'+j+'.png')
# print("完成1")



# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第三部分\\pe")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\pe\pe'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\与pool交易的人数.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\与邻居交易的人数.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\不交易人数.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\监管部门效用.xlsx',index_col=0))
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\不投资人数.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\投资火电人数.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\投资绿电人数.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\电力产量.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\绿电量.xlsx',index_col=0))
#
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# b21=df21.values
# b22=df22.values
# b23=df23.values
# b24=df24.values
# b25=df25.values
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "与pool交易的人数":b15,"与邻居交易的人数":b16,"不交易人数":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20,
#     "不投资人数":b21,"投资火电人数":b22,"投资绿电人数":b23,
#     "电力产量":b24,"绿电量":b25}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#         "与pool交易的人数":"Number of TP","与邻居交易的人数":"Number of TN","不交易人数":"Number of NT",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory",
#      "不投资人数":"Number of No Investment","投资火电人数":"Number of Investment in Traditional Energy","投资绿电人数":"Number of Investment in Renewable Energy",
#      "电力产量":"Total Power Generation","绿电量":"Renewable Energy Generation"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\pe\pe'+j+'.png')
# print("完成1")
# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\pe\绿证数量需求.xlsx',index_col=0))
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"绿证价格":"Green Certificate Price",
#      "绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\pe\pe'+j+'.png')
# print("完成1")



# # os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第三部分\\投资效率4")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     plt.imshow(BB[i], cmap="rainbow",extent=[1,15,1,15],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${q_h-new}$",font)#hang
#     plt.xlabel("${q_g-new}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\投资效率4\投资效率'+i+'.png')
# print("完成0")
# df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\被迫进入pool.xlsx',index_col=0))
# df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\完成配额被迫进入pool.xlsx',index_col=0))
# df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\未完成配额被迫进入pool.xlsx',index_col=0))
# df15 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\与pool交易的人数.xlsx',index_col=0))
# df16 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\与邻居交易的人数.xlsx',index_col=0))
# df17 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\不交易人数.xlsx',index_col=0))
# df18 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\监管部门惩罚.xlsx',index_col=0))
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\监管部门奖励.xlsx',index_col=0))
# df20 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\监管部门效用.xlsx',index_col=0))
#
# b12=df12.values/500
# b13=df13.values/500
# b14=df14.values/500
# b15=df15.values
# b16=df16.values
# b17=df17.values
# b18=df18.values
# b19=df19.values
# b20=df20.values
# #
# #
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"被迫进入pool":b12,"完成配额被迫进入pool":b13,"未完成配额被迫进入pool":b14,
#     "与pool交易的人数":b15,"与邻居交易的人数":b16,"不交易人数":b17,
#     "监管部门惩罚":b18,"监管部门奖励":b19,"监管部门效用":b20}
# CC2={"被迫进入pool":"Forced with TP","完成配额被迫进入pool":"H type Forced with TP","未完成配额被迫进入pool":"L type Forced with TP",
#         "与pool交易的人数":"Number of TP","与邻居交易的人数":"Number of TN","不交易人数":"Number of NT",
#     "监管部门惩罚":"Regulatory Penalty Coefficient","监管部门奖励":"Regulatory Reward Coefficient","监管部门效用":"The Utility of the Regulatory"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[1,15,1,15],origin='lower',interpolation='kaiser')
#     plt.ylabel("${q_h-new}$",font)#hang
#     plt.xlabel("${q_g-new}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\投资效率4\投资效率'+j+'.png')
# print("完成1")

# df26 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\绿证价格.xlsx',index_col=0))
# df27 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\绿证数量供给.xlsx',index_col=0))
# df28 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\绿证数量需求.xlsx',index_col=0))
# b26=df26.values
# b27=df27.values
# b28=df28.values
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"绿证价格":b26,
#     "绿证数量供给":b27,"绿证数量需求":b28}
# CC2={"绿证价格":"Green Certificate Price",
#      "绿证数量供给":"Green Certificate Supply Quantity","绿证数量需求":"Green Certificate Required Quantity"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[1,15,1,15],origin='lower',interpolation='kaiser')
#     plt.ylabel("${q_h-new}$",font)#hang
#     plt.xlabel("${q_g-new}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\投资效率4\投资效率'+j+'.png')
# print("完成1")


# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\不投资人数.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\投资火电人数.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\投资绿电人数.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\电力产量.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第三部分\投资效率4\绿电量.xlsx',index_col=0))
#
# b21=df21.values
# b22=df22.values
# b23=df23.values
# b24=df24.values
# b25=df25.values
#
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# CC={"不投资人数":b21,"投资火电人数":b22,"投资绿电人数":b23,
#     "电力产量":b24,"绿电量":b25}
# CC2={"不投资人数":"Number of No Investment","投资火电人数":"Number of Investment in Traditional Energy","投资绿电人数":"Number of Investment in Renewable Energy",
#      "电力产量":"Total Power Generation","绿电量":"Renewable Energy Generation"}
# for j in CC:
#     print(j)
#     # print(BB[i])
#     fig1 = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(CC[j], cmap="rainbow",extent=[1,15,1,15],origin='lower',interpolation='kaiser')
#     plt.ylabel("${q_h-new}$",font)#hang
#     plt.xlabel("${q_g-new}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(CC2[j],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第三部分\投资效率4\投资效率'+j+'.png')
# print("完成1")


##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################

##################################################################################################################################
##################################################################################################################################
A=[str(i)+"kaka" for i in range(57)]
# A=["kaka"]
B=[", ${C_p}$=0",", ${C_p}$=0.5",", ${C_p}$=1",", ${C_p}$=1.5",", ${C_p}$=2",
   ", ${C_d}$=0",", ${C_d}$=0.5",", ${C_d}$=1",", ${C_d}$=1.5",", ${C_d}$=2",
   ", e=0",", e=0.5",", e=1",", e=1.5",", e=2",
   ", ${p_g}$=0",", ${p_g}$=0.5",", ${p_g}$=1",", ${p_g}$=1.5",", ${p_g}$=2",
   ", ${p_e}$=0 (${b_0}$)",", ${p_e}$=0.5 (${b_0}$)",", ${p_e}$=1 (${b_0}$)",", ${p_e}$=1.5 (${b_0}$)",", ${p_e}$=2 (${b_0}$)",
   ", ${q_h-new}$=1",", ${q_h-new}$=1.5",", ${q_h-new}$=2",", ${q_h-new}$=2.5",", ${q_h-new}$=3",
   ", ${q_g-new}$=1",", ${q_g-new}$=1.5",", ${q_g-new}$=2",", ${q_g-new}$=2.5",", ${q_g-new}$=3",
   ", f=0",", f=0.5",", f=1",", f=1.5",", f=2",
   ", ${C_g}$=0", ", ${C_g}$=0.5", ", ${C_g}$=1", ", ${C_g}$=1.5", ", ${C_g}$=2",
   ", ${C_h}$=0", ", ${C_h}$=0.5", ", ${C_h}$=1", ", ${C_h}$=1.5", ", ${C_h}$=2",
   ", f=0.2",", ${C_g}$=0.1",", ${C_h}$=0.1",", ${C_h}$=0.1",
   ", ${C_h}$=0.2",", ${C_g}$=0.3",", ${C_g}$=0.4"]
C=["\\0cp","\\0.5cp","\\1cp","\\1.5cp","\\2cp",
   "\\0cd","\\0.5cd","\\1cd","\\1.5cd","\\2cd",
   "\\0e","\\0.5e","\\1e","\\1.5e","\\2e",
   "\\0pg","\\0.5pg","\\1pg","\\1.5pg","\\2pg",
   "\\0pe","\\0.5pe","\\1pe","\\1.5pe","\\2pe",
   "\\1qhnew","\\1.5qhnew","\\2qhnew","\\2.5qhnew","\\3qhnew",
   "\\1qgnew","\\1.5qgnew","\\2qgnew","\\2.5qgnew","\\3qgnew",
   "\\0f","\\0.5f","\\1f","\\1.5f","\\2f",
   "\\0cg", "\\0.5cg", "\\1cg", "\\1.5cg", "\\2cg",
   "\\0ch", "\\0.5ch", "\\1ch", "\\1.5ch", "\\2ch",
   "\\0.2f","\\0.1cg","\\0.1ch","\\0.1ch2",
   "\\0.2ch","\\0.3cg","\\0.4cg"]
ti=56
d=1050
name=A[ti]
name2=B[ti]
name3=C[ti]

# name="kaka"
# name2=" "
# name3="原始"

df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门效用'+name+'.xlsx',index_col=0))
df110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门奖励'+name+'.xlsx',index_col=0))
df111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门惩罚'+name+'.xlsx',index_col=0))

df0 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量供给' + name + '.xlsx',index_col=0))
df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证价格' + name + '.xlsx',index_col=0))
df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量需求' + name + '.xlsx',index_col=0))
df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\被迫进入pool' + name + '.xlsx',index_col=0))
df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额被迫进入pool' + name + '.xlsx',index_col=0))
df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额被迫进入pool' + name + '.xlsx',index_col=0))

df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\不投资人数'+name+'.xlsx',index_col=0))
df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资绿电人数'+name+'.xlsx',index_col=0))
df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资火电人数'+name+'.xlsx',index_col=0))

x=np.arange(0,d)
font= {'family' : 'Times New Roman','weight' : 'ultralight','size':15,'style': 'italic'}
font2= {'family' : 'Times New Roman','weight' : 'normal','size':18}
fig,ax1 = plt.subplots()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df21.values, lw=1, label="Total Power Generation", color="r")
plt.plot(x,df22.values, lw=1, label="Renewable Power Generation", color="g")
plt.plot(x, 0.2*df21.values, lw=1, label="20% of total electricity", color="b",linestyle="--")
plt.ylabel("Yield", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("Power Generation" , font2)
plt.legend(fontsize="x-small")
ax2=ax1.twinx()
plt.plot(x, (df22.values/df21.values), lw=1, label="Proportion of Renewable Power", color="y",linestyle="--")
ax2.set_ylabel("Proportion", font)
plt.legend(loc=1,fontsize="x-small")
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Power GenerationAAA'+ name +'.png')
print("完成图0")
#
fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df111.values,lw=1,label="fine",color="r")
# plt.plot(x,df110.values,lw=1,label="reward",color="g")
# plt.ylabel("Proportion",font)
plt.xlabel("Evolution times"+name2,font)
plt.title("Fine",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Fine' + name + '.png')
print("完成图1")
#
fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df19.values,lw=1,label="utility",color="r")
plt.ylabel("utility",font)
plt.xlabel("Evolution times"+name2,font)
plt.title("Departmental utility",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Departmental utility' + name + '.png')
print("完成图2")

fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df00.values/500,lw=1,label="H-FC with NT",color="r")
plt.plot(x,df01.values/500,lw=1,label="H-FC with TP",color="g")
plt.plot(x,df02.values/500,lw=1,label="H-FC with TN",color="b")
plt.plot(x,df03.values/500,lw=1,label="H-RC with NT",color="r",linestyle='--')
plt.plot(x,df04.values/500,lw=1,label="H-RC with TP",color="g",linestyle='--')
plt.plot(x,df05.values/500,lw=1,label="H-RC with TN",color="b",linestyle='--')
plt.ylabel("Proportion",font)
plt.xlabel("Evolution times"+name2,font)
plt.title("H-FC and H-RC",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\H-FC and H-RC' + name + '.png')
print("完成图3")

fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df06.values/500,lw=1,label="L-FC with NT",color="r")
plt.plot(x,df07.values/500,lw=1,label="L-FC with TP",color="g")
plt.plot(x,df08.values/500,lw=1,label="L-FC with TN",color="b")
plt.plot(x,df09.values/500,lw=1,label="L-RC with NT",color="r",linestyle='--')
plt.plot(x,df010.values/500,lw=1,label="L-RC with TP",color="g",linestyle='--')
plt.plot(x,df011.values/500,lw=1,label="L-RC with TN",color="b",linestyle='--')
plt.ylabel("Proportion",font)
plt.xlabel("Evolution times"+name2,font)
plt.title("L-FC and L-RC",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\L-FC and L-RC' + name + '.png')
print("完成图4")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df00.values /500, lw=1, label="H-FC with NT", color="r")
plt.plot(x, df01.values /500, lw=1, label="H-FC with TP", color="g")
plt.plot(x, df02.values /500, lw=1, label="H-FC with TN", color="b")
plt.plot(x, df06.values /500, lw=1, label="L-FC with NT", color="r", linestyle='--')
plt.plot(x, df07.values /500, lw=1, label="L-FC with TP", color="g", linestyle='--')
plt.plot(x, df08.values /500, lw=1, label="L-FC with TN", color="b", linestyle='--')
plt.ylabel("Proportion", font)
plt.xlabel("Evolution times" +name2, font)
plt.title("H-FC and L-FC", font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\H-FC and L-FC' + name + '.png')
print("完成图5")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df03.values /500, lw=1, label="H-RC with NT", color="r")
plt.plot(x, df04.values /500, lw=1, label="H-RC with TP", color="g")
plt.plot(x, df05.values /500, lw=1, label="H-RC with TN", color="b")
plt.plot(x, df09.values / 500, lw=1, label="L-RC with NT", color="r", linestyle='--')
plt.plot(x, df010.values /500, lw=1, label="L-RC with TP", color="g", linestyle='--')
plt.plot(x, df011.values /500, lw=1, label="L-RC with TN", color="b", linestyle='--')
plt.ylabel("Proportion", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("H-RC and L-RC" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\H-RC and L-RC' + name + '.png')
print("完成图6")


fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df0.values, lw=1, label="Supply", color="r")
plt.plot(x, df2.values, lw=1, label="Demand", color="g")
# plt.ylabel("Proportion", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("Supply and demand of green certificate Market" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Supply and demand of green certificate Market' + name+ '.png')
print("完成图7")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df1.values, lw=1, label="Price", color="r")
plt.ylabel("Price", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("Price of green certificate Market" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Price of green certificate Market' + name + '.png')
print("完成图8")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df3.values /500, lw=1, label="Forced with TP", color="r")
plt.plot(x, df4.values /500, lw=1, label="H type Forced with TP", color="g")
plt.plot(x, df5.values /500, lw=1, label="L type Forced with TP", color="b")
plt.ylabel("Proportion", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("Forced with TP" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Forced with TP' + name + '.png')
print("完成图9")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df21.values, lw=1, label="Total Power Generation", color="r")
plt.plot(x,df22.values, lw=1, label="Renewable Power Generation", color="g")
# plt.ylabel("Proportion", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("Power Generation" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Power Generation' + name + '.png')
print("完成图10")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df23.values, lw=1, label="Number of No Investment", color="r")
plt.plot(x, df24.values, lw=1, label="Number of Investment in Renewable Energy", color="g")
plt.plot(x, df25.values, lw=1, label="Number of Investment in Traditional Energy", color="b")
plt.ylabel("Number", font)
plt.xlabel("Evolution times"+name2, font)
plt.title("Investment" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0311\\'+name3+'\Investment' + name + '.png')
print("完成图11")



print("第几次完成",ti)











###############################################****************************************************
# A=[str(i)+"kaka" for i in range(50)]
# # A=["kaka"]
# B=[", ${C_p}$=0",", ${C_p}$=0.5",", ${C_p}$=1",", ${C_p}$=1.5",", ${C_p}$=2",
#    ", ${C_d}$=0",", ${C_d}$=0.5",", ${C_d}$=1",", ${C_d}$=1.5",", ${C_d}$=2",
#    ", e=0",", e=0.5",", e=1",", e=1.5",", e=2",
#    ", ${p_g}$=0",", ${p_g}$=0.5",", ${p_g}$=1",", ${p_g}$=1.5",", ${p_g}$=2",
#    ", ${p_e}$=0 (${b_0}$)",", ${p_e}$=0.5 (${b_0}$)",", ${p_e}$=1 (${b_0}$)",", ${p_e}$=1.5 (${b_0}$)",", ${p_e}$=2 (${b_0}$)",
#    ", ${q_h-new}$=1",", ${q_h-new}$=1.5",", ${q_h-new}$=2",", ${q_h-new}$=2.5",", ${q_h-new}$=3",
#    ", ${q_g-new}$=1",", ${q_g-new}$=1.5",", ${q_g-new}$=2",", ${q_g-new}$=2.5",", ${q_g-new}$=3",
#    ", f=0",", f=0.5",", f=1",", f=1.5",", f=2",
#    ", ${C_g}$=0", ", ${C_g}$=0.5", ", ${C_g}$=1", ", ${C_g}$=1.5", ", ${C_g}$=2",
#    ", ${C_h}$=0", ", ${C_h}$=0.5", ", ${C_h}$=1", ", ${C_h}$=1.5", ", ${C_h}$=2"]
# C=["0cp","0.5cp","1cp","1.5cp","2cp",
#    "0cd","0.5cd","1cd","1.5cd","2cd",
#    "0e","0.5e","1e","1.5e","2e",
#    "0pg","0.5pg","1pg","1.5pg","2pg",
#    "0pe","0.5pe","1pe","1.5pe","2pe",
#    "1qhnew","1.5qhnew","2qhnew","2.5qhnew","3qhnew",
#    "1qgnew","1.5qgnew","2qgnew","2.5qgnew","3qgnew",
#    "0f","0.5f","1f","1.5f","2f",
#    "0cg", "0.5cg", "1cg", "1.5cg", "2cg",
#    "0ch", "0.5ch", "1ch", "1.5ch", "2ch"]
#
# d=1050
# for ti in range(45,50):
#    name=A[ti]
#    name2=B[ti]
#    name3=C[ti]
#
#    # name="kaka"
#    # name2=" "
#    # name3="原始"
#
#    df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门效用'+name+'.xlsx',index_col=0))
#    df110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门奖励'+name+'.xlsx',index_col=0))
#    df111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门惩罚'+name+'.xlsx',index_col=0))
#
#    x=np.arange(0,d)
#    font= {'family' : 'Times New Roman','weight' : 'ultralight','size':15,'style': 'italic'}
#    font2= {'family' : 'Times New Roman','weight' : 'normal','size':18}
#
#    fig= plt.figure()
#    plt.rcParams['figure.figsize'] = (10.0, 6.0)
#    plt.rcParams['savefig.dpi'] = 1000 #图片像素
#    plt.rcParams['figure.dpi'] = 1000 #
#    plt.plot(x,df111.values,lw=1,label="fine",color="r")
#    # plt.ylabel("Proportion",font)
#    plt.xlabel("Evolution times"+name2,font)
#    plt.title("Fine",font2)
#    plt.legend()
#    plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0301\\惩罚\\Fine' + name3 + '.png')
#    print("完成图",ti)
#
