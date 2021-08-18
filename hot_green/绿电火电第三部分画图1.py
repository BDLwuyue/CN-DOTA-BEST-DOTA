import numpy as np
from scipy import interpolate
import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pandas as pd
import os
import time

# import pandas as pd
# df0 = pd.DataFrame(pd.read_excel('E:\\data\文件名.xlsx', index_col=0))
# #第一列数据就是
# df0.values[:,0]
# #第二列数据就是
# df0.values[:,1]
# #冒号表示每一行
##############################cd-cp部分#################
# A=[str(i)+"ame" for i in range(40)]
# B=[", ${C_p}$=0",", ${C_p}$=0.5",", ${C_p}$=1",", ${C_p}$=1.5",", ${C_p}$=2",
#    ", ${C_d}$=0",", ${C_d}$=0.5",", ${C_d}$=1",", ${C_d}$=1.5",", ${C_d}$=2",
#    ", e=0",", e=0.5",", e=1",", e=1.5",", e=2",
#    ", ${p_g}$=0",", ${p_g}$=0.5",", ${p_g}$=1",", ${p_g}$=1.5",", ${p_g}$=2",
#    ", ${p_e}$=0 (${b_0}$)",", ${p_e}$=0.5 (${b_0}$)",", ${p_e}$=1 (${b_0}$)",", ${p_e}$=1.5 (${b_0}$)",", ${p_e}$=2 (${b_0}$)",
#    ", ${q_h-new}$=1",", ${q_h-new}$=1.5",", ${q_h-new}$=2",", ${q_h-new}$=2.5",", ${q_h-new}$=3",
#    ", ${q_g-new}$=1",", ${q_g-new}$=1.5",", ${q_g-new}$=2",", ${q_g-new}$=2.5",", ${q_g-new}$=3",
#    ", f=0",", f=0.5",", f=1",", f=1.5",", f=2"]
# C=["\\0cp","\\0.5cp","\\1cp","\\1.5cp","\\2cp",
#    "\\0cd","\\0.5cd","\\1cd","\\1.5cd","\\2cd",
#    "\\0e","\\0.5e","\\1e","\\1.5e","\\2e",
#    "\\0pg","\\0.5pg","\\1pg","\\1.5pg","\\2pg",
#    "\\0pe","\\0.5pe","\\1pe","\\1.5pe","\\2pe",
#    "\\1qhnew","\\1.5qhnew","\\2qhnew","\\2.5qhnew","\\3qhnew",
#    "\\1qgnew","\\1.5qgnew","\\2qgnew","\\2.5qgnew","\\3qgnew",
#    "\\0f","\\0.5f","\\1f","\\1.5f","\\2f"]
# ti=40
# d=1050
# name=A[ti]
# name2=B[ti]
# name3=C[ti]
#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门效用'+name+'.xlsx',index_col=0))
# df110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门奖励'+name+'.xlsx',index_col=0))
# df111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门惩罚'+name+'.xlsx',index_col=0))
#
# df0 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量供给' + name + '.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证价格' + name + '.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量需求' + name + '.xlsx',index_col=0))
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\被迫进入pool' + name + '.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额被迫进入pool' + name + '.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额被迫进入pool' + name + '.xlsx',index_col=0))
#
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
# df23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\不投资人数'+name+'.xlsx',index_col=0))
# df24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资绿电人数'+name+'.xlsx',index_col=0))
# df25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资火电人数'+name+'.xlsx',index_col=0))
#
# x=np.arange(0,d)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df111.values,lw=1,label="fine",color="r")
# plt.plot(x,df110.values,lw=1,label="reward",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("Reward and Fine",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Reward and Fine' + name + '.png')
# print("完成图1")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df19.values,lw=1,label="utility",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("Departmental utility",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Departmental utility' + name + '.png')
# print("完成图2")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/500,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/500,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/500,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/500,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/500,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/500,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\H-FC and H-RC' + name + '.png')
# print("完成图3")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/500,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/500,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/500,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/500,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/500,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/500,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\L-FC and L-RC' + name + '.png')
# print("完成图4")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df00.values / 500, lw=1, label="H-FC with NT", color="r")
# plt.plot(x, df01.values / 500, lw=1, label="H-FC with TP", color="g")
# plt.plot(x, df02.values / 500, lw=1, label="H-FC with TN", color="b")
# plt.plot(x, df06.values / 500, lw=1, label="L-FC with NT", color="r", linestyle='--')
# plt.plot(x, df07.values / 500, lw=1, label="L-FC with TP", color="g", linestyle='--')
# plt.plot(x, df08.values / 500, lw=1, label="L-FC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times" +name2, font)
# plt.title("H-FC and L-FC", font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\H-FC and L-FC' + name + '.png')
# print("完成图5")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df03.values / 500, lw=1, label="H-RC with NT", color="r")
# plt.plot(x, df04.values / 500, lw=1, label="H-RC with TP", color="g")
# plt.plot(x, df05.values / 500, lw=1, label="H-RC with TN", color="b")
# plt.plot(x, df09.values / 500, lw=1, label="L-RC with NT", color="r", linestyle='--')
# plt.plot(x, df010.values / 500, lw=1, label="L-RC with TP", color="g", linestyle='--')
# plt.plot(x, df011.values / 500, lw=1, label="L-RC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("H-RC and L-RC" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\H-RC and L-RC' + name + '.png')
# print("完成图6")
#
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df0.values, lw=1, label="Supply", color="r")
# plt.plot(x, df2.values, lw=1, label="Demand", color="g")
# # plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Supply and demand of green certificate Market" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Supply and demand of green certificate Market' + name+ '.png')
# print("完成图7")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df1.values, lw=1, label="Price", color="r")
# plt.ylabel("Price", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Price of green certificate Market" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Price of green certificate Market' + name + '.png')
# print("完成图8")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df3.values /500, lw=1, label="Forced with TP", color="r")
# plt.plot(x, df4.values /500, lw=1, label="H type Forced with TP", color="g")
# plt.plot(x, df5.values /500, lw=1, label="L type Forced with TP", color="b")
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Forced with TP" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Forced with TP' + name + '.png')
# print("完成图9")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df21.values, lw=1, label="Total Power Generation", color="r")
# plt.plot(x,df22.values, lw=1, label="Renewable Power Generation", color="g")
# # plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Power Generation" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Power Generation' + name + '.png')
# print("完成图10")
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df23.values, lw=1, label="Number of No Investment", color="r")
# plt.plot(x, df24.values, lw=1, label="Number of Investment in Renewable Energy", color="g")
# plt.plot(x, df25.values, lw=1, label="Number of Investment in Traditional Energy", color="b")
# plt.ylabel("Number", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Investment" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0120第三部分'+name3+'\Investment' + name + '.png')
# print("完成图11")
# print("第几次完成",ti)





# A=["gg"]
# # B=[" "," "," "," "," "," "," "," "," "," "]
# # print(len(A))
# # ti=9
# # name=A[ti]
# # name2=B[ti]
# dd=1050
# gdf00=np.zeros((dd,len(A)))
# gdf01=np.zeros((dd,len(A)))
# gdf02=np.zeros((dd,len(A)))
# gdf03=np.zeros((dd,len(A)))
# gdf04=np.zeros((dd,len(A)))
# gdf05=np.zeros((dd,len(A)))
# gdf06=np.zeros((dd,len(A)))
# gdf07=np.zeros((dd,len(A)))
# gdf08=np.zeros((dd,len(A)))
# gdf09=np.zeros((dd,len(A)))
# gdf010=np.zeros((dd,len(A)))
# gdf011=np.zeros((dd,len(A)))
# gdf012=np.zeros((dd,len(A)))
# gdf013=np.zeros((dd,len(A)))
# gdf014=np.zeros((dd,len(A)))
# gdf015=np.zeros((dd,len(A)))
# gdf016=np.zeros((dd,len(A)))
# gdf017=np.zeros((dd,len(A)))
# gdf018=np.zeros((dd,len(A)))
# gdf019=np.zeros((dd,len(A)))
# gdf020=np.zeros((dd,len(A)))
# gdf021=np.zeros((dd,len(A)))
# gdf022=np.zeros((dd,len(A)))
# gdf023=np.zeros((dd,len(A)))
# gdf024=np.zeros((dd,len(A)))
# gdf025=np.zeros((dd,len(A)))
#
# for i in range(len(A)):
#     name=A[i]
#     ldf00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门效用'+name+'.xlsx',index_col=0))
#     ldf110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门奖励'+name+'.xlsx',index_col=0))
#     ldf111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门惩罚'+name+'.xlsx',index_col=0))
#
#     ldf0 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量供给' + name + '.xlsx',index_col=0))
#     ldf1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证价格' + name + '.xlsx',index_col=0))
#     ldf2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量需求' + name + '.xlsx',index_col=0))
#     ldf3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\被迫进入pool' + name + '.xlsx',index_col=0))
#     ldf4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额被迫进入pool' + name + '.xlsx',index_col=0))
#     ldf5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额被迫进入pool' + name + '.xlsx',index_col=0))
#
#     ldf21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
#     ldf22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
#     ldf23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\不投资人数'+name+'.xlsx',index_col=0))
#     ldf24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资绿电人数'+name+'.xlsx',index_col=0))
#     ldf25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资火电人数'+name+'.xlsx',index_col=0))
#     gdf00[:,i]=ldf00.values.reshape((1,dd))[0]
#     gdf01[:, i] = ldf01.values.reshape((1,dd))[0]
#     gdf02[:,i]=ldf02.values.reshape((1,dd))[0]
#     gdf03[:, i] = ldf03.values.reshape((1,dd))[0]
#     gdf04[:,i]=ldf04.values.reshape((1,dd))[0]
#     gdf05[:, i] = ldf05.values.reshape((1,dd))[0]
#     gdf06[:,i]=ldf06.values.reshape((1,dd))[0]
#     gdf07[:, i] = ldf07.values.reshape((1,dd))[0]
#     gdf08[:,i]=ldf08.values.reshape((1,dd))[0]
#     gdf09[:, i] = ldf09.values.reshape((1,dd))[0]
#     gdf010[:,i]=ldf010.values.reshape((1,dd))[0]
#     gdf011[:, i] = ldf011.values.reshape((1,dd))[0]
#     gdf012[:,i]=ldf19.values.reshape((1,dd))[0]
#     gdf013[:, i] = ldf110.values.reshape((1,dd))[0]
#     gdf014[:,i]=ldf111.values.reshape((1,dd))[0]
#     gdf015[:,i]=ldf0.values.reshape((1,dd))[0]
#     gdf016[:,i]=ldf1.values.reshape((1,dd))[0]
#     gdf017[:,i]=ldf2.values.reshape((1,dd))[0]
#     gdf018[:,i]=ldf3.values.reshape((1,dd))[0]
#     gdf019[:,i]=ldf4.values.reshape((1,dd))[0]
#     gdf020[:,i]=ldf5.values.reshape((1,dd))[0]
#     gdf021[:,i]=ldf21.values.reshape((1,dd))[0]
#     gdf022[:,i]=ldf22.values.reshape((1,dd))[0]
#     gdf023[:,i]=ldf23.values.reshape((1,dd))[0]
#     gdf024[:,i]=ldf24.values.reshape((1,dd))[0]
#     gdf025[:,i]=ldf25.values.reshape((1,dd))[0]
# df00= np.mean(gdf00,axis=1)
# df01 =np.mean(gdf01,axis=1)
# df02 =np.mean(gdf02,axis=1)
#
# df03 =np.mean(gdf03,axis=1)
# df04 =np.mean(gdf04,axis=1)
# df05 =np.mean(gdf05,axis=1)
#
# df06 =np.mean(gdf06,axis=1)
# df07 =np.mean(gdf07,axis=1)
# df08 =np.mean(gdf08,axis=1)
#
# df09 = np.mean(gdf09,axis=1)
# df010 =np.mean(gdf010,axis=1)
# df011 =np.mean(gdf011,axis=1)
#
# df19 = np.mean(gdf012,axis=1)
# df110 =np.mean(gdf013,axis=1)
# df111 =np.mean(gdf014,axis=1)
# df0 =np.mean(gdf015,axis=1)
# df1 =np.mean(gdf016,axis=1)
# df2 = np.mean(gdf017,axis=1)
# df3 = np.mean(gdf018,axis=1)
# df4 = np.mean(gdf019,axis=1)
# df5 = np.mean(gdf020,axis=1)
# df21 = np.mean(gdf021,axis=1)
# df22 = np.mean(gdf022,axis=1)
# df23 = np.mean(gdf023,axis=1)
# df24 = np.mean(gdf024,axis=1)
# df25 = np.mean(gdf025,axis=1)
# x=np.arange(0,dd)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df111,lw=1,label="fine",color="r")
# plt.plot(x,df110,lw=1,label="reward",color="g")
# # plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("Reward and Fine",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Reward and Fine.png')
# print("完成图1")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df19,lw=1,label="utility",color="r")
# # plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("Departmental utility",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Departmental utility.png')
# print("完成图2")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00/500,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01/500,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02/500,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03/500,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04/500,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05/500,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\H-FC and H-RC.png')
# print("完成图3")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06/500,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07/500,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08/500,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09/500,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010/500,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011/500,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\L-FC and L-RC.png')
# print("完成图4")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df00/500, lw=1, label="H-FC with NT", color="r")
# plt.plot(x, df01/500, lw=1, label="H-FC with TP", color="g")
# plt.plot(x, df02/500, lw=1, label="H-FC with TN", color="b")
# plt.plot(x, df06/500, lw=1, label="L-FC with NT", color="r", linestyle='--')
# plt.plot(x, df07/500, lw=1, label="L-FC with TP", color="g", linestyle='--')
# plt.plot(x, df08/500, lw=1, label="L-FC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times" , font)
# plt.title("H-FC and L-FC", font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\H-FC and L-FC.png')
# print("完成图5")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df03/ 500, lw=1, label="H-RC with NT", color="r")
# plt.plot(x, df04/ 500, lw=1, label="H-RC with TP", color="g")
# plt.plot(x, df05/ 500, lw=1, label="H-RC with TN", color="b")
# plt.plot(x, df09/ 500, lw=1, label="L-RC with NT", color="r", linestyle='--')
# plt.plot(x, df010/ 500, lw=1, label="L-RC with TP", color="g", linestyle='--')
# plt.plot(x, df011/ 500, lw=1, label="L-RC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("H-RC and L-RC" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\H-RC and L-RC.png')
# print("完成图6")
#
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df0, lw=1, label="Supply", color="r")
# plt.plot(x, df2, lw=1, label="Demand", color="g")
# # plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("Supply and demand of green certificate Market" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Supply and demand of green certificate Market.png')
# print("完成图7")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df1, lw=1, label="Price", color="r")
# plt.ylabel("Price", font)
# plt.xlabel("Evolution times", font)
# plt.title("Price of green certificate Market" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Price of green certificate Market.png')
# print("完成图8")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df3/500, lw=1, label="Forced with TP", color="r")
# plt.plot(x, df4/500, lw=1, label="H type Forced with TP", color="g")
# plt.plot(x, df5/500, lw=1, label="L type Forced with TP", color="b")
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("Forced with TP" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Forced with TP.png')
# print("完成图9")

# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df21, lw=1, label="Total Power Generation", color="r")
# plt.plot(x,df22, lw=1, label="Renewable Power Generation", color="g")
# # plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("Power Generation" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Power Generation.png')
# print("完成图10")
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df23, lw=1, label="Number of No Investment", color="r")
# plt.plot(x, df24, lw=1, label="Number of Investment in Renewable Energy", color="g")
# plt.plot(x, df25, lw=1, label="Number of Investment in Traditional Energy", color="b")
# plt.ylabel("Number", font)
# plt.xlabel("Evolution times", font)
# plt.title("Investment" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Investment.png')
# print("完成图11")
# print("第几次完成")








#
# A=["大1次","大2次","大3次","大4次","大5次"]
# # B=[" "," "," "," "," "," "," "," "," "," "]
# # print(len(A))
# # ti=9
# # name=A[ti]
# # name2=B[ti]
# gdf00=np.zeros((350,len(A)))
# gdf01=np.zeros((350,len(A)))
# gdf02=np.zeros((350,len(A)))
# gdf03=np.zeros((350,len(A)))
# gdf04=np.zeros((350,len(A)))
# gdf05=np.zeros((350,len(A)))
# gdf06=np.zeros((350,len(A)))
# gdf07=np.zeros((350,len(A)))
# gdf08=np.zeros((350,len(A)))
# gdf09=np.zeros((350,len(A)))
# gdf010=np.zeros((350,len(A)))
# gdf011=np.zeros((350,len(A)))
# gdf012=np.zeros((350,len(A)))
# gdf013=np.zeros((350,len(A)))
# gdf014=np.zeros((350,len(A)))
# gdf015=np.zeros((350,len(A)))
# gdf016=np.zeros((350,len(A)))
# gdf017=np.zeros((350,len(A)))
# gdf018=np.zeros((350,len(A)))
# gdf019=np.zeros((350,len(A)))
# gdf020=np.zeros((350,len(A)))
# gdf021=np.zeros((350,len(A)))
# gdf022=np.zeros((350,len(A)))
# gdf023=np.zeros((350,len(A)))
# gdf024=np.zeros((350,len(A)))
# gdf025=np.zeros((350,len(A)))
#
# for i in range(len(A)):
#     name=A[i]
#     ldf00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     ldf010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     ldf011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     ldf19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门效用'+name+'.xlsx',index_col=0))
#     ldf110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门奖励'+name+'.xlsx',index_col=0))
#     ldf111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\监管部门惩罚'+name+'.xlsx',index_col=0))
#
#     ldf0 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量供给' + name + '.xlsx',index_col=0))
#     ldf1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证价格' + name + '.xlsx',index_col=0))
#     ldf2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿证数量需求' + name + '.xlsx',index_col=0))
#     ldf3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\被迫进入pool' + name + '.xlsx',index_col=0))
#     ldf4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\完成配额被迫进入pool' + name + '.xlsx',index_col=0))
#     ldf5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\未完成配额被迫进入pool' + name + '.xlsx',index_col=0))
#
#     ldf21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
#     ldf22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
#     ldf23 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\不投资人数'+name+'.xlsx',index_col=0))
#     ldf24 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资绿电人数'+name+'.xlsx',index_col=0))
#     ldf25 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\投资火电人数'+name+'.xlsx',index_col=0))
#     gdf00[:,i]=ldf00.values.reshape((1,350))[0]
#     gdf01[:, i] = ldf01.values.reshape((1,350))[0]
#     gdf02[:,i]=ldf02.values.reshape((1,350))[0]
#     gdf03[:, i] = ldf03.values.reshape((1,350))[0]
#     gdf04[:,i]=ldf04.values.reshape((1,350))[0]
#     gdf05[:, i] = ldf05.values.reshape((1,350))[0]
#     gdf06[:,i]=ldf06.values.reshape((1,350))[0]
#     gdf07[:, i] = ldf07.values.reshape((1,350))[0]
#     gdf08[:,i]=ldf08.values.reshape((1,350))[0]
#     gdf09[:, i] = ldf09.values.reshape((1,350))[0]
#     gdf010[:,i]=ldf010.values.reshape((1,350))[0]
#     gdf011[:, i] = ldf011.values.reshape((1,350))[0]
#     gdf012[:,i]=ldf19.values.reshape((1,350))[0]
#     gdf013[:, i] = ldf110.values.reshape((1,350))[0]
#     gdf014[:,i]=ldf111.values.reshape((1,350))[0]
#     gdf015[:,i]=ldf0.values.reshape((1,350))[0]
#     gdf016[:,i]=ldf1.values.reshape((1,350))[0]
#     gdf017[:,i]=ldf2.values.reshape((1,350))[0]
#     gdf018[:,i]=ldf3.values.reshape((1,350))[0]
#     gdf019[:,i]=ldf4.values.reshape((1,350))[0]
#     gdf020[:,i]=ldf5.values.reshape((1,350))[0]
#     gdf021[:,i]=ldf21.values.reshape((1,350))[0]
#     gdf022[:,i]=ldf22.values.reshape((1,350))[0]
#     gdf023[:,i]=ldf23.values.reshape((1,350))[0]
#     gdf024[:,i]=ldf24.values.reshape((1,350))[0]
#     gdf025[:,i]=ldf25.values.reshape((1,350))[0]
#
# j=4
# name2=A[j]
# df00= gdf00[:,j]
# df01 = gdf01[:,j]
# df02 = gdf02[:,j]
#
# df03 = gdf03[:,j]
# df04 = gdf04[:,j]
# df05 = gdf05[:,j]
#
# df06 = gdf06[:,j]
# df07 = gdf07[:,j]
# df08 = gdf08[:,j]
#
# df09 = gdf09[:,j]
# df010 = gdf010[:,j]
# df011 = gdf011[:,j]
#
# df19 =  gdf012[:,j]
# df110 = gdf013[:,j]
# df111 = gdf014[:,j]
# df0 = gdf015[:,j]
# df1 = gdf016[:,j]
# df2 =  gdf017[:,j]
# df3 =  gdf018[:,j]
# df4 =  gdf019[:,j]
# df5 =  gdf020[:,j]
# df21 = gdf021[:,j]
# df22 =gdf022[:,j]
# df23 = gdf023[:,j]
# df24 =gdf024[:,j]
# df25 =gdf025[:,j]
# x=np.arange(0,350)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df111,lw=1,label="fine",color="r")
# plt.plot(x,df110,lw=1,label="reward",color="g")
# # plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("Reward and Fine",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Reward and Fine'+name2+'.png')
# print("完成图1")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df19,lw=1,label="utility",color="r")
# # plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("Departmental utility",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Departmental utility'+name2+'.png')
# print("完成图2")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00/125,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01/125,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02/125,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03/125,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04/125,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05/125,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\H-FC and H-RC'+name2+'.png')
# print("完成图3")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06/125,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07/125,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08/125,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09/125,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010/125,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011/125,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\L-FC and L-RC'+name2+'.png')
# print("完成图4")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df00/ 125, lw=1, label="H-FC with NT", color="r")
# plt.plot(x, df01/ 125, lw=1, label="H-FC with TP", color="g")
# plt.plot(x, df02/ 125, lw=1, label="H-FC with TN", color="b")
# plt.plot(x, df06/ 125, lw=1, label="L-FC with NT", color="r", linestyle='--')
# plt.plot(x, df07/ 125, lw=1, label="L-FC with TP", color="g", linestyle='--')
# plt.plot(x, df08/ 125, lw=1, label="L-FC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times" , font)
# plt.title("H-FC and L-FC", font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\H-FC and L-FC'+name2+'.png')
# print("完成图5")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df03/ 125, lw=1, label="H-RC with NT", color="r")
# plt.plot(x, df04/ 125, lw=1, label="H-RC with TP", color="g")
# plt.plot(x, df05/ 125, lw=1, label="H-RC with TN", color="b")
# plt.plot(x, df09/ 125, lw=1, label="L-RC with NT", color="r", linestyle='--')
# plt.plot(x, df010/ 125, lw=1, label="L-RC with TP", color="g", linestyle='--')
# plt.plot(x, df011/ 125, lw=1, label="L-RC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("H-RC and L-RC" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\H-RC and L-RC'+name2+'.png')
# print("完成图6")
#
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df0, lw=1, label="Demand", color="r")
# plt.plot(x, df2, lw=1, label="Supply", color="g")
# # plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("Supply and demand of green certificate Market" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Supply and demand of green certificate Market'+name2+'.png')
# print("完成图7")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df1, lw=1, label="Price", color="r")
# plt.ylabel("Price", font)
# plt.xlabel("Evolution times", font)
# plt.title("Price of green certificate Market" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Price of green certificate Market'+name2+'.png')
# print("完成图8")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df3/500, lw=1, label="Forced with TP", color="r")
# plt.plot(x, df4/500, lw=1, label="H type Forced with TP", color="g")
# plt.plot(x, df5/500, lw=1, label="L type Forced with TP", color="b")
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("Forced with TP" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Forced with TP'+name2+'.png')
# print("完成图9")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df21, lw=1, label="Total Power Generation", color="r")
# plt.plot(x,df22, lw=1, label="Renewable Power Generation", color="g")
# # plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("Power Generation" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Power Generation'+name2+'.png')
# print("完成图10")
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df23, lw=1, label="Number of No Investment", color="r")
# plt.plot(x, df24, lw=1, label="Number of Investment in Traditional Energy", color="g")
# plt.plot(x, df25, lw=1, label="Number of Investment in Renewable Energy", color="b")
# plt.ylabel("Number", font)
# plt.xlabel("Evolution times", font)
# plt.title("Investment" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第三部分\Investment'+name2+'.png')
# print("完成图11")
# print("第几次完成")














# A=[str(i)+"kaka" for i in range(40)]
# B=[", ${C_p}$=0",", ${C_p}$=0.5",", ${C_p}$=1",", ${C_p}$=1.5",", ${C_p}$=2",
#    ", ${C_d}$=0",", ${C_d}$=0.5",", ${C_d}$=1",", ${C_d}$=1.5",", ${C_d}$=2",
#    ", e=0",", e=0.5",", e=1",", e=1.5",", e=2",
#    ", ${p_g}$=0",", ${p_g}$=0.5",", ${p_g}$=1",", ${p_g}$=1.5",", ${p_g}$=2",
#    ", ${p_e}$=0 (${b_0}$)",", ${p_e}$=0.5 (${b_0}$)",", ${p_e}$=1 (${b_0}$)",", ${p_e}$=1.5 (${b_0}$)",", ${p_e}$=2 (${b_0}$)",
#    ", ${q_h-new}$=1",", ${q_h-new}$=1.5",", ${q_h-new}$=2",", ${q_h-new}$=2.5",", ${q_h-new}$=3",
#    ", ${q_g-new}$=1",", ${q_g-new}$=1.5",", ${q_g-new}$=2",", ${q_g-new}$=2.5",", ${q_g-new}$=3",
#    ", f=0",", f=0.5",", f=1",", f=1.5",", f=2"]
# C=["0cp","0.5cp","1cp","1.5cp","2cp",
#    "0cd","0.5cd","1cd","1.5cd","2cd",
#    "0e","0.5e","1e","1.5e","2e",
#    "0pg","0.5pg","1pg","1.5pg","2pg",
#    "0pe","0.5pe","1pe","1.5pe","2pe",
#    "1qhnew","1.5qhnew","2qhnew","2.5qhnew","3qhnew",
#    "1qgnew","1.5qgnew","2qgnew","2.5qgnew","3qgnew",
#    "0f","0.5f","1f","1.5f","2f"]
#
# d=1000
# for ti in range(40):
#     if ti>30 and ti<=40:
#         name=A[ti]
#         name2=B[ti]
#         name3=C[ti]
#
#         df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
#         df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
#
#         x=np.arange(0,d)
#         font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
#         font2= {'family' : 'Times New Roman','weight' : 'normal'}
#
#         fig,ax1 = plt.subplots()
#         plt.rcParams['figure.figsize'] = (10.0, 6.0)
#         plt.rcParams['savefig.dpi'] = 1000  # 图片像素
#         plt.rcParams['figure.dpi'] = 1000  #
#         plt.plot(x, df21.values[50:], lw=1, label="Total Power Generation", color="r")
#         plt.plot(x,df22.values[50:], lw=1, label="Renewable Power Generation", color="g")
#         plt.plot(x, 0.2*df21.values[50:], lw=1, label="20% of total electricity", color="b",linestyle="--")
#         plt.ylabel("Yield", font)
#         plt.xlabel("Evolution times"+name2, font)
#         plt.title("Power Generation" , font2)
#         plt.legend(fontsize="x-small")
#         ax2=ax1.twinx()
#         plt.plot(x, (df22.values/df21.values)[50:], lw=1, label="Proportion of Renewable Power", color="y",linestyle="--")
#         ax2.set_ylabel("Proportion", font)
#         plt.legend(loc=1,fontsize="x-small")
#         plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0228\\Power Generation' + name3 + '.png')
#         print(ti)


# A=[str(i)+"kaka" for i in range(40)]
# # A=["kaka"]
# B=[", ${C_p}$=0",", ${C_p}$=0.5",", ${C_p}$=1",", ${C_p}$=1.5",", ${C_p}$=2",
#    ", ${C_d}$=0",", ${C_d}$=0.5",", ${C_d}$=1",", ${C_d}$=1.5",", ${C_d}$=2",
#    ", e=0",", e=0.5",", e=1",", e=1.5",", e=2",
#    ", ${p_g}$=0",", ${p_g}$=0.5",", ${p_g}$=1",", ${p_g}$=1.5",", ${p_g}$=2",
#    ", ${p_e}$=0 (${b_0}$)",", ${p_e}$=0.5 (${b_0}$)",", ${p_e}$=1 (${b_0}$)",", ${p_e}$=1.5 (${b_0}$)",", ${p_e}$=2 (${b_0}$)",
#    ", ${q_h-new}$=1",", ${q_h-new}$=1.5",", ${q_h-new}$=2",", ${q_h-new}$=2.5",", ${q_h-new}$=3",
#    ", ${q_g-new}$=1",", ${q_g-new}$=1.5",", ${q_g-new}$=2",", ${q_g-new}$=2.5",", ${q_g-new}$=3",
#    ", f=0",", f=0.5",", f=1",", f=1.5",", f=2"]
# C=["\\0cp","\\0.5cp","\\1cp","\\1.5cp","\\2cp",
#    "\\0cd","\\0.5cd","\\1cd","\\1.5cd","\\2cd",
#    "\\0e","\\0.5e","\\1e","\\1.5e","\\2e",
#    "\\0pg","\\0.5pg","\\1pg","\\1.5pg","\\2pg",
#    "\\0pe","\\0.5pe","\\1pe","\\1.5pe","\\2pe",
#    "\\1qhnew","\\1.5qhnew","\\2qhnew","\\2.5qhnew","\\3qhnew",
#    "\\1qgnew","\\1.5qgnew","\\2qgnew","\\2.5qgnew","\\3qgnew",
#    "\\0f","\\0.5f","\\1f","\\1.5f","\\2f"]
# ti=3
# d=1050
# name=A[ti]
# name2=B[ti]
# name3=C[ti]
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
#
# x=np.arange(0,1050)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':15,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal','size':18}
#
# fig,ax1 = plt.subplots()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df21.values, lw=1, label="Total Power Generation", color="r")
# plt.plot(x,df22.values, lw=1, label="Renewable Power Generation", color="g")
# plt.plot(x, 0.2*df21.values, lw=1, label="20% of total electricity", color="b",linestyle="--")
# plt.ylabel("Yield", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Power Generation" , font2)
# plt.legend(fontsize="x-small")pip
# ax2=ax1.twinx()
# plt.plot(x, (df22.values/df21.values), lw=1, label="Proportion of Renewable Power", color="y",linestyle="--")
# ax2.set_ylabel("Proportion", font)
# plt.legend(loc=1,fontsize="x-small")
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0228\\'+name3+'\Power GenerationAAA'+ name +'.png')

# A=["kaAka"]
# ti=0
# d=1050
# name=A[ti]
# name2=" "
# name3="原始"
# df21 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx',index_col=0))
# df22 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx',index_col=0))
#
# x=np.arange(0,1050)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':15,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal','size':18}
#
# fig,ax1 = plt.subplots()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df21.values, lw=1, label="Total Power Generation", color="r")
# plt.plot(x,df22.values, lw=1, label="Renewable Power Generation", color="g")
# plt.plot(x, 0.2*df21.values, lw=1, label="20% of total electricity", color="b",linestyle="--")
# plt.ylabel("Yield", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("Power Generation" , font2)
# plt.legend(fontsize="x-small")
# ax2=ax1.twinx()
# plt.plot(x, (df22.values/df21.values), lw=1, label="Proportion of Renewable Power", color="y",linestyle="--")
# ax2.set_ylabel("Proportion", font)
# plt.legend(loc=1,fontsize="x-small")
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\\0228\\'+name3+'\Power GenerationAAA'+ name +'.png')