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
##############################cd-cp部分#################
# A=["2cp","2cd","0cp","0cd","0e","2e","0pg","2pg","0pe","2pe"]
# B=[", ${C_p}$=2",", ${C_d}$=2",", ${C_p}$=0",", ${C_d}$=0",", e=0",", e=2",", ${p_g}$=0",", ${p_g}$=2",", ${p_e}$=0",", ${p_g}$=2"]
# # print(len(A))
# ti=9
# name=A[ti]
# name2=B[ti]
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
# df19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门效用'+name+'.xlsx',index_col=0))
# df110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门奖励'+name+'.xlsx',index_col=0))
# df111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门惩罚'+name+'.xlsx',index_col=0))
# # print(df00.values/250)
# x=np.arange(0,5000)
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
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Reward and Fine'+name+'.png')
# print("完成图1")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df19.values,lw=1,label="fine",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("Departmental utility",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Departmental utility'+name+'.png')
# print("完成图2")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/125,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/125,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/125,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/125,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/125,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/125,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-FC and H-RC'+name+'.png')
# print("完成图3")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/125,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/125,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/125,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/125,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/125,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/125,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times"+name2,font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\L-FC and L-RC'+name+'.png')
# print("完成图4")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df00.values / 125, lw=1, label="H-FC with NT", color="r")
# plt.plot(x, df01.values / 125, lw=1, label="H-FC with TP", color="g")
# plt.plot(x, df02.values / 125, lw=1, label="H-FC with TN", color="b")
# plt.plot(x, df06.values / 125, lw=1, label="L-FC with NT", color="r", linestyle='--')
# plt.plot(x, df07.values / 125, lw=1, label="L-FC with TP", color="g", linestyle='--')
# plt.plot(x, df08.values / 125, lw=1, label="L-FC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times" +name2, font)
# plt.title("H-FC and L-FC", font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-FC and L-FC' + name + '.png')
# print("完成图5")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df03.values / 125, lw=1, label="H-RC with NT", color="r")
# plt.plot(x, df04.values / 125, lw=1, label="H-RC with TP", color="g")
# plt.plot(x, df05.values / 125, lw=1, label="H-RC with TN", color="b")
# plt.plot(x, df09.values / 125, lw=1, label="L-RC with NT", color="r", linestyle='--')
# plt.plot(x, df010.values / 125, lw=1, label="L-RC with TP", color="g", linestyle='--')
# plt.plot(x, df011.values / 125, lw=1, label="L-RC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times"+name2, font)
# plt.title("H-RC and L-RC" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-RC and L-RC' + name + '.png')
# print("完成图6")
# print("第几次完成",ti)








# # A=["1次","2次","3次","4次","5次"]
# A=["大0次","大1次","大2次","大3次","大4次","大5次","大6次","大7次","大8次","大9次"]
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
#
#
# for i in range(len(A)):
#     name=A[i]
#     df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
#     df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
#     df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))
#
#     df12 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门效用'+name+'.xlsx',index_col=0))
#     df13 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门奖励'+name+'.xlsx',index_col=0))
#     df14 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门惩罚'+name+'.xlsx',index_col=0))
#
#     gdf00[:,i]=df0.values.reshape((1,350))[0]
#     gdf01[:, i] = df1.values.reshape((1,350))[0]
#     gdf02[:,i]=df2.values.reshape((1,350))[0]
#     gdf03[:, i] = df3.values.reshape((1,350))[0]
#     gdf04[:,i]=df4.values.reshape((1,350))[0]
#     gdf05[:, i] = df5.values.reshape((1,350))[0]
#     gdf06[:,i]=df6.values.reshape((1,350))[0]
#     gdf07[:, i] = df7.values.reshape((1,350))[0]
#     gdf08[:,i]=df8.values.reshape((1,350))[0]
#     gdf09[:, i] = df9.values.reshape((1,350))[0]
#     gdf010[:,i]=df10.values.reshape((1,350))[0]
#     gdf011[:, i] = df11.values.reshape((1,350))[0]
#     gdf012[:,i]=df12.values.reshape((1,350))[0]
#     gdf013[:, i] = df13.values.reshape((1,350))[0]
#     gdf014[:,i]=df14.values.reshape((1,350))[0]
#
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
#
#
# x=np.arange(0,350)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df111,lw=1,label="fine",color="r")
# plt.plot(x,df110,lw=1,label="reward",color="g")
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("Reward and Fine",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Reward and Fine.png')
# print("完成图1")
#
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df19,lw=1,label="utility",color="r")
# plt.ylabel("Proportion",font)
# plt.xlabel("Evolution times",font)
# plt.title("Departmental utility",font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Departmental utility.png')
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
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-FC and H-RC.png')
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
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\L-FC and L-RC.png')
# print("完成图4")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df00/ 125, lw=1, label="H-FC with NT", color="r")
# plt.plot(x, df01 / 125, lw=1, label="H-FC with TP", color="g")
# plt.plot(x, df02/ 125, lw=1, label="H-FC with TN", color="b")
# plt.plot(x, df06/ 125, lw=1, label="L-FC with NT", color="r", linestyle='--')
# plt.plot(x, df07/ 125, lw=1, label="L-FC with TP", color="g", linestyle='--')
# plt.plot(x, df08/ 125, lw=1, label="L-FC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times" , font)
# plt.title("H-FC and L-FC", font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-FC and L-FC.png')
# print("完成图5")
#
# fig = plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000  # 图片像素
# plt.rcParams['figure.dpi'] = 1000  #
# plt.plot(x, df03 / 125, lw=1, label="H-RC with NT", color="r")
# plt.plot(x, df04/ 125, lw=1, label="H-RC with TP", color="g")
# plt.plot(x, df05/ 125, lw=1, label="H-RC with TN", color="b")
# plt.plot(x, df09 / 125, lw=1, label="L-RC with NT", color="r", linestyle='--')
# plt.plot(x, df010 / 125, lw=1, label="L-RC with TP", color="g", linestyle='--')
# plt.plot(x, df011 / 125, lw=1, label="L-RC with TN", color="b", linestyle='--')
# plt.ylabel("Proportion", font)
# plt.xlabel("Evolution times", font)
# plt.title("H-RC and L-RC" , font2)
# plt.legend()
# plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-RC and L-RC.png')
# print("完成图6")
# print("第几次完成")





A=["大0次","大1次","大2次","大3次","大4次","大5次","大6次","大7次","大8次","大9次"]
# B=[" "," "," "," "," "," "," "," "," "," "]
# print(len(A))
# ti=9
# name=A[ti]
# name2=B[ti]
gdf00=np.zeros((350,len(A)))
gdf01=np.zeros((350,len(A)))
gdf02=np.zeros((350,len(A)))
gdf03=np.zeros((350,len(A)))
gdf04=np.zeros((350,len(A)))
gdf05=np.zeros((350,len(A)))
gdf06=np.zeros((350,len(A)))
gdf07=np.zeros((350,len(A)))
gdf08=np.zeros((350,len(A)))
gdf09=np.zeros((350,len(A)))
gdf010=np.zeros((350,len(A)))
gdf011=np.zeros((350,len(A)))
gdf012=np.zeros((350,len(A)))
gdf013=np.zeros((350,len(A)))
gdf014=np.zeros((350,len(A)))
gdf015=np.zeros((350,len(A)))
gdf016=np.zeros((350,len(A)))
gdf017=np.zeros((350,len(A)))
gdf018=np.zeros((350,len(A)))
gdf019=np.zeros((350,len(A)))
gdf020=np.zeros((350,len(A)))
for i in range(len(A)):
    name=A[i]
    ldf00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
    ldf01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
    ldf02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

    ldf03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
    ldf04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
    ldf05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

    ldf06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
    ldf07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
    ldf08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

    ldf09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx',index_col=0))
    ldf010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx',index_col=0))
    ldf011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx',index_col=0))

    ldf19 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门效用'+name+'.xlsx',index_col=0))
    ldf110 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门奖励'+name+'.xlsx',index_col=0))
    ldf111 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\监管部门惩罚'+name+'.xlsx',index_col=0))

    ldf0 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\绿证数量供给' + name + '.xlsx',index_col=0))
    ldf1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\绿证价格' + name + '.xlsx',index_col=0))
    ldf2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\绿证数量需求' + name + '.xlsx',index_col=0))
    ldf3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\被迫进入pool' + name + '.xlsx',index_col=0))
    ldf4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\完成配额被迫进入pool' + name + '.xlsx',index_col=0))
    ldf5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电2\第一部分\未完成配额被迫进入pool' + name + '.xlsx',index_col=0))
    gdf00[:,i]=ldf00.values.reshape((1,350))[0]
    gdf01[:, i] = ldf01.values.reshape((1,350))[0]
    gdf02[:,i]=ldf02.values.reshape((1,350))[0]
    gdf03[:, i] = ldf03.values.reshape((1,350))[0]
    gdf04[:,i]=ldf04.values.reshape((1,350))[0]
    gdf05[:, i] = ldf05.values.reshape((1,350))[0]
    gdf06[:,i]=ldf06.values.reshape((1,350))[0]
    gdf07[:, i] = ldf07.values.reshape((1,350))[0]
    gdf08[:,i]=ldf08.values.reshape((1,350))[0]
    gdf09[:, i] = ldf09.values.reshape((1,350))[0]
    gdf010[:,i]=ldf010.values.reshape((1,350))[0]
    gdf011[:, i] = ldf011.values.reshape((1,350))[0]
    gdf012[:,i]=ldf19.values.reshape((1,350))[0]
    gdf013[:, i] = ldf110.values.reshape((1,350))[0]
    gdf014[:,i]=ldf111.values.reshape((1,350))[0]
    gdf015[:,i]=ldf0.values.reshape((1,350))[0]
    gdf016[:,i]=ldf1.values.reshape((1,350))[0]
    gdf017[:,i]=ldf2.values.reshape((1,350))[0]
    gdf018[:,i]=ldf3.values.reshape((1,350))[0]
    gdf019[:,i]=ldf4.values.reshape((1,350))[0]
    gdf020[:,i]=ldf5.values.reshape((1,350))[0]
df00= np.mean(gdf00,axis=1)
df01 =np.mean(gdf01,axis=1)
df02 =np.mean(gdf02,axis=1)

df03 =np.mean(gdf03,axis=1)
df04 =np.mean(gdf04,axis=1)
df05 =np.mean(gdf05,axis=1)

df06 =np.mean(gdf06,axis=1)
df07 =np.mean(gdf07,axis=1)
df08 =np.mean(gdf08,axis=1)

df09 = np.mean(gdf09,axis=1)
df010 =np.mean(gdf010,axis=1)
df011 =np.mean(gdf011,axis=1)

df19 = np.mean(gdf012,axis=1)
df110 =np.mean(gdf013,axis=1)
df111 =np.mean(gdf014,axis=1)
df0 =np.mean(gdf015,axis=1)
df1 =np.mean(gdf016,axis=1)
df2 = np.mean(gdf017,axis=1)
df3 = np.mean(gdf018,axis=1)
df4 = np.mean(gdf019,axis=1)
df5 = np.mean(gdf020,axis=1)

# print(df00.values/250)
x=np.arange(0,350)
font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
font2= {'family' : 'Times New Roman','weight' : 'normal'}
fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df111,lw=1,label="fine",color="r")
plt.plot(x,df110,lw=1,label="reward",color="g")
plt.ylabel("Proportion",font)
plt.xlabel("Evolution times",font)
plt.title("Reward and Fine",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Reward and Fine.png')
print("完成图1")

fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df19,lw=1,label="utility",color="r")
plt.ylabel("Proportion",font)
plt.xlabel("Evolution times",font)
plt.title("Departmental utility",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Departmental utility.png')
print("完成图2")

fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df00/125,lw=1,label="H-FC with NT",color="r")
plt.plot(x,df01/125,lw=1,label="H-FC with TP",color="g")
plt.plot(x,df02/125,lw=1,label="H-FC with TN",color="b")
plt.plot(x,df03/125,lw=1,label="H-RC with NT",color="r",linestyle='--')
plt.plot(x,df04/125,lw=1,label="H-RC with TP",color="g",linestyle='--')
plt.plot(x,df05/125,lw=1,label="H-RC with TN",color="b",linestyle='--')
plt.ylabel("Proportion",font)
plt.xlabel("Evolution times",font)
plt.title("H-FC and H-RC",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-FC and H-RC.png')
print("完成图3")

fig= plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000 #图片像素
plt.rcParams['figure.dpi'] = 1000 #
plt.plot(x,df06/125,lw=1,label="L-FC with NT",color="r")
plt.plot(x,df07/125,lw=1,label="L-FC with TP",color="g")
plt.plot(x,df08/125,lw=1,label="L-FC with TN",color="b")
plt.plot(x,df09/125,lw=1,label="L-RC with NT",color="r",linestyle='--')
plt.plot(x,df010/125,lw=1,label="L-RC with TP",color="g",linestyle='--')
plt.plot(x,df011/125,lw=1,label="L-RC with TN",color="b",linestyle='--')
plt.ylabel("Proportion",font)
plt.xlabel("Evolution times",font)
plt.title("L-FC and L-RC",font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\L-FC and L-RC.png')
print("完成图4")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df00/ 125, lw=1, label="H-FC with NT", color="r")
plt.plot(x, df01/ 125, lw=1, label="H-FC with TP", color="g")
plt.plot(x, df02/ 125, lw=1, label="H-FC with TN", color="b")
plt.plot(x, df06/ 125, lw=1, label="L-FC with NT", color="r", linestyle='--')
plt.plot(x, df07/ 125, lw=1, label="L-FC with TP", color="g", linestyle='--')
plt.plot(x, df08/ 125, lw=1, label="L-FC with TN", color="b", linestyle='--')
plt.ylabel("Proportion", font)
plt.xlabel("Evolution times" , font)
plt.title("H-FC and L-FC", font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-FC and L-FC.png')
print("完成图5")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df03/ 125, lw=1, label="H-RC with NT", color="r")
plt.plot(x, df04/ 125, lw=1, label="H-RC with TP", color="g")
plt.plot(x, df05/ 125, lw=1, label="H-RC with TN", color="b")
plt.plot(x, df09/ 125, lw=1, label="L-RC with NT", color="r", linestyle='--')
plt.plot(x, df010/ 125, lw=1, label="L-RC with TP", color="g", linestyle='--')
plt.plot(x, df011/ 125, lw=1, label="L-RC with TN", color="b", linestyle='--')
plt.ylabel("Proportion", font)
plt.xlabel("Evolution times", font)
plt.title("H-RC and L-RC" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\H-RC and L-RC.png')
print("完成图6")


fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df0, lw=1, label="Supply", color="r")
plt.plot(x, df2, lw=1, label="Demand", color="g")
# plt.ylabel("Proportion", font)
plt.xlabel("Evolution times", font)
plt.title("Supply and demand of green certificate Market" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Supply and demand of green certificate Market.png')
print("完成图7")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df1, lw=1, label="Price", color="r")
plt.ylabel("Price", font)
plt.xlabel("Evolution times", font)
plt.title("Price of green certificate Market" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Price of green certificate Market.png')
print("完成图8")

fig = plt.figure()
plt.rcParams['figure.figsize'] = (10.0, 6.0)
plt.rcParams['savefig.dpi'] = 1000  # 图片像素
plt.rcParams['figure.dpi'] = 1000  #
plt.plot(x, df3/500, lw=1, label="Forced with TP", color="r")
plt.plot(x, df4/500, lw=1, label="H type Forced with TP", color="g")
plt.plot(x, df5/500, lw=1, label="L type Forced with TP", color="b")
plt.ylabel("Proportion", font)
plt.xlabel("Evolution times", font)
plt.title("Forced with TP" , font2)
plt.legend()
plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\新\第一部分\Forced with TP.png')
print("完成图9")