import numpy as np
from scipy import interpolate
import pylab as pl
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from matplotlib import axes
import pandas as pd
import os
##############################cd-cp部分#################
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd0\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=0.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=0.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd2\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cp\cpcd3\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=2",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=2",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

##############################cd-cp部分 无限制#################
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd0\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=0.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=0.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd2\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\无限制cd\cpcd3\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=2",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=2",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()



###################################################################
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd0\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=0.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=0.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd2\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=1.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cp\cpcd3\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=2",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_p}$ , ${C_d}$=2",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

##############################cd-cp部分 无限制#################
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd0\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=0.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=0.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd2\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1.5",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=1.5",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()
#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df02 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df04 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df06 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df08 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df09 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df010 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df011 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cpcd改\有限制cd\cpcd3\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df00.values/250)
# x=np.linspace(0,2,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df00.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df01.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df02.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df03.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df04.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df05.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=2",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df06.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df07.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df08.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df09.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df010.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df011.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ , ${C_p}$=2",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()
#############基础原始有限制内生
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.2000 ",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.4000 ",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.6000 ",font2)
# plt.legend()
# plt.show()

#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.8000 ",font2)
# plt.legend()
# plt.show()



# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.10000 ",font2)
# plt.legend()
# plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# # print(df30.values/250)
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values/250)[:-2000],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,(df31.values/250)[:-2000],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,(df32.values/250)[:-2000],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,(df36.values/250)[:-2000],lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df37.values/250)[:-2000],lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df38.values/250)[:-2000],lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df33.values/250)[:-2000],lw=1,label="H-RC with NT",color="red")
# plt.plot(x,(df34.values/250)[:-2000],lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,(df35.values/250)[:-2000],lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,(df39.values/250)[:-2000],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df310.values/250)[:-2000],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df311.values/250)[:-2000],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\监管部门惩罚.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生\监管部门奖励.xlsx',index_col=0))
#
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values)[:-2000],lw=1,label="Punishment",color="red")
# plt.plot(x,(df31.values)[:-2000],lw=1,label="Reward",color="olivedrab")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Reward and Punishment",font2)
# plt.legend()
# plt.show()





#############基础原始无限制内生
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.2000 ",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.4000 ",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.6000 ",font2)
# plt.legend()
# plt.show()

#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.8000 ",font2)
# plt.legend()
# plt.show()



# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.10000 ",font2)
# plt.legend()
# plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# # print(df30.values/250)
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values/250)[:-2000],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,(df31.values/250)[:-2000],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,(df32.values/250)[:-2000],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,(df36.values/250)[:-2000],lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df37.values/250)[:-2000],lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df38.values/250)[:-2000],lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df33.values/250)[:-2000],lw=1,label="H-RC with NT",color="red")
# plt.plot(x,(df34.values/250)[:-2000],lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,(df35.values/250)[:-2000],lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,(df39.values/250)[:-2000],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df310.values/250)[:-2000],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df311.values/250)[:-2000],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\监管部门惩罚.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生\监管部门奖励.xlsx',index_col=0))
#
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values)[:-2000],lw=1,label="Punishment",color="red")
# plt.plot(x,(df31.values)[:-2000],lw=1,label="Reward",color="olivedrab")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Reward and Punishment",font2)
# plt.legend()
# plt.show()



#############基础原始无限制内生1
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.2000 ",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.4000 ",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.6000 ",font2)
# plt.legend()
# plt.show()

#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.8000 ",font2)
# plt.legend()
# plt.show()



# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.10000 ",font2)
# plt.legend()
# plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# # print(df30.values/250)
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values/250)[:-2000],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,(df31.values/250)[:-2000],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,(df32.values/250)[:-2000],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,(df36.values/250)[:-2000],lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df37.values/250)[:-2000],lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df38.values/250)[:-2000],lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df33.values/250)[:-2000],lw=1,label="H-RC with NT",color="red")
# plt.plot(x,(df34.values/250)[:-2000],lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,(df35.values/250)[:-2000],lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,(df39.values/250)[:-2000],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df310.values/250)[:-2000],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df311.values/250)[:-2000],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\监管部门惩罚.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始无限制内生1\监管部门奖励.xlsx',index_col=0))
#
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values)[:-2000],lw=1,label="Punishment",color="red")
# plt.plot(x,(df31.values)[:-2000],lw=1,label="Reward",color="olivedrab")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Reward and Punishment",font2)
# plt.legend()
# plt.show()



#############基础原始有限制内生1
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.2000 ",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.4000 ",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.6000 ",font2)
# plt.legend()
# plt.show()

#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.8000 ",font2)
# plt.legend()
# plt.show()



# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.10000 ",font2)
# plt.legend()
# plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# # print(df30.values/250)
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values/250)[:-2000],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,(df31.values/250)[:-2000],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,(df32.values/250)[:-2000],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,(df36.values/250)[:-2000],lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df37.values/250)[:-2000],lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df38.values/250)[:-2000],lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df33.values/250)[:-2000],lw=1,label="H-RC with NT",color="red")
# plt.plot(x,(df34.values/250)[:-2000],lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,(df35.values/250)[:-2000],lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,(df39.values/250)[:-2000],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df310.values/250)[:-2000],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df311.values/250)[:-2000],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\监管部门惩罚.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始有限制内生1\监管部门奖励.xlsx',index_col=0))
#
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values)[:-2000],lw=1,label="Punishment",color="red")
# plt.plot(x,(df31.values)[:-2000],lw=1,label="Reward",color="olivedrab")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Reward and Punishment",font2)
# plt.legend()
# plt.show()




#############基础原始外生
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.2000 ",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.4000 ",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.6000 ",font2)
# plt.legend()
# plt.show()

#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.8000 ",font2)
# plt.legend()
# plt.show()



# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.10000 ",font2)
# plt.legend()
# plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df30.values/250)
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values/250)[:-2000],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,(df31.values/250)[:-2000],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,(df32.values/250)[:-2000],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,(df36.values/250)[:-2000],lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df37.values/250)[:-2000],lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df38.values/250)[:-2000],lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df33.values/250)[:-2000],lw=1,label="H-RC with NT",color="red")
# plt.plot(x,(df34.values/250)[:-2000],lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,(df35.values/250)[:-2000],lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,(df39.values/250)[:-2000],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df310.values/250)[:-2000],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df311.values/250)[:-2000],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()

#
# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\监管部门惩罚.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生\监管部门奖励.xlsx',index_col=0))
#
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values)[:-2000],lw=1,label="Punishment",color="red")
# plt.plot(x,(df31.values)[:-2000],lw=1,label="Reward",color="olivedrab")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Reward and Punishment",font2)
# plt.legend()
# plt.show()



#############基础原始外生1
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业位置第1999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业策略第1999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.2000 ",font2)
# plt.legend()
# plt.show()

# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业位置第3999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业策略第3999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.4000 ",font2)
# plt.legend()
# plt.show()


# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业位置第5999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业策略第5999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.6000 ",font2)
# plt.legend()
# plt.show()

#
# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业位置第7999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业策略第7999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.8000 ",font2)
# plt.legend()
# plt.show()



# df00= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df01 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df02= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df03 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df04= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df05 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# df06= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业位置第9999轮.xlsx',index_col=0))
# df07 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业策略第9999轮.xlsx',index_col=0))
# a00=np.where(df01.values==0)[0]
# b00=df00.values[a00,:]
# a01=np.where(df01.values==1)[0]
# b01=df00.values[a01,:]
# a02=np.where(df01.values==2)[0]
# b02=df00.values[a02,:]
# a10=np.where(df03.values==0)[0]
# b10=df02.values[a10,:]
# a11=np.where(df03.values==1)[0]
# b11=df02.values[a11,:]
# a12=np.where(df03.values==2)[0]
# b12=df02.values[a12,:]
#
# a20=np.where(df05.values==0)[0]
# b20=df04.values[a20,:]
# a21=np.where(df05.values==1)[0]
# b21=df04.values[a21,:]
# a22=np.where(df05.values==2)[0]
# b22=df04.values[a22,:]
#
# a30=np.where(df07.values==0)[0]
# b30=df06.values[a30,:]
# a31=np.where(df07.values==1)[0]
# b31=df06.values[a31,:]
# a32=np.where(df07.values==2)[0]
# b32=df06.values[a32,:]
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.scatter(b00[:,0],b00[:,1],label="H-FC with TN",color="r",s=20,marker="3")
# plt.scatter(b01[:,0],b01[:,1],label="H-FC with TP",color="g",s=20,marker="3")
# plt.scatter(b02[:,0],b02[:,1],label="H-FC with NT",color="b",s=20,marker="3")
#
# plt.scatter(b20[:,0],b20[:,1],label="L-FC with TN",color="r",s=20,marker="o")
# plt.scatter(b21[:,0],b21[:,1],label="L-FC with TP",color="g",s=20,marker="o")
# plt.scatter(b22[:,0],b22[:,1],label="L-FC with NT",color="b",s=20,marker="o")
#
# plt.scatter(b10[:,0],b10[:,1],label="H-RC with TN",color="r",s=20,marker="v")
# plt.scatter(b11[:,0],b11[:,1],label="H-RC with TP",color="g",s=20,marker="v")
# plt.scatter(b12[:,0],b12[:,1],label="H-RC with NT",color="b",s=20,marker="v")
#
# plt.scatter(b30[:,0],b30[:,1],label="L-RC with TN",color="r",s=20,marker="s")
# plt.scatter(b31[:,0],b31[:,1],label="L-RC with TP",color="g",s=20,marker="s")
# plt.scatter(b32[:,0],b32[:,1],label="L-RC with NT",color="b",s=20,marker="s")
# plt.title("Location-NO.10000 ",font2)
# plt.legend()
# plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# print(df30.values/250)
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values/250)[:-2000],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,(df31.values/250)[:-2000],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,(df32.values/250)[:-2000],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,(df36.values/250)[:-2000],lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df37.values/250)[:-2000],lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df38.values/250)[:-2000],lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df33.values/250)[:-2000],lw=1,label="H-RC with NT",color="red")
# plt.plot(x,(df34.values/250)[:-2000],lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,(df35.values/250)[:-2000],lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,(df39.values/250)[:-2000],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df310.values/250)[:-2000],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,(df311.values/250)[:-2000],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\监管部门惩罚.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\原始外生1\监管部门奖励.xlsx',index_col=0))
#
# x=np.arange(0,10000)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,(df30.values)[:-2000],lw=1,label="Punishment",color="red")
# plt.plot(x,(df31.values)[:-2000],lw=1,label="Reward",color="olivedrab")
# plt.ylabel("Proportion",font)
# plt.xlabel("Number of Evolution",font)
# plt.title("Reward and Punishment",font2)
# plt.legend()
# plt.show()

######################波动率无限制
# s=np.arange(0,10,0.5)
# fg=np.zeros((12,len(s)))
# for g in range(len(s)):
#     i=s[g]
#     print(i)
#     df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df3= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df6= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\未完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\未完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\未完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df9= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\未完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\未完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率\未完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     a0=np.mean(df0.values)
#     a1 = np.mean(df1.values)
#     a2 = np.mean(df2.values)
#     a3 = np.mean(df3.values)
#     a4 = np.mean(df4.values)
#     a5 = np.mean(df5.values)
#     a6 = np.mean(df6.values)
#     a7 = np.mean(df7.values)
#     a8 = np.mean(df8.values)
#     a9 = np.mean(df9.values)
#     a10 = np.mean(df10.values)
#     a11 = np.mean(df11.values)
#     fg[0,g]=a0
#     fg[1, g] = a1
#     fg[2, g] = a2
#     fg[3, g] = a3
#     fg[4,g] = a4
#     fg[5, g] = a5
#     fg[6, g] = a6
#     fg[7, g] = a7
#     fg[8, g] = a8
#     fg[9, g] = a9
#     fg[10, g] = a10
#     fg[11, g] = a11
# df = pd.DataFrame(fg)
# df.to_excel('E:\\data\火电绿电\第一部分\波动率.xlsx')

# dfdf=pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率.xlsx',index_col=0))
# ame=dfdf.values
# x=np.arange(0,10,0.5)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[0],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,ame[1],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,ame[2],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,ame[3],lw=1,label="H-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[4],lw=1,label="H-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[5],lw=1,label="H-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility ",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity - H type",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[6],lw=1,label="L-FC with NT",color="red")
# plt.plot(x,ame[7],lw=1,label="L-FC with TP",color="olivedrab")
# plt.plot(x,ame[8],lw=1,label="L-FC with TN",color="dodgerblue")
# plt.plot(x,ame[9],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[10],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[11],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity - L type",font2)
# plt.legend()
# plt.show()
########拟合
# f0=np.polyfit(x[:13],ame[0,:13], 3)
# y0vals=np.polyval(f0, x[:13])
# f1=np.polyfit(x[:13],ame[1,:13], 3)
# y1vals=np.polyval(f1, x[:13])
# f2=np.polyfit(x[:13],ame[2,:13], 3)
# y2vals=np.polyval(f2, x[:13])
# f6=np.polyfit(x[:13],ame[6,:13], 3)
# y6vals=np.polyval(f6, x[:13])
# f7=np.polyfit(x[:13],ame[7,:13], 3)
# y7vals=np.polyval(f7, x[:13])
# f8=np.polyfit(x[:13],ame[8,:13], 3)
# y8vals=np.polyval(f8, x[:13])
#
# f3=np.polyfit(x[:13],ame[3,:13], 3)
# y3vals=np.polyval(f3, x[:13])
# f4=np.polyfit(x[:13],ame[4,:13], 3)
# y4vals=np.polyval(f4, x[:13])
# f5=np.polyfit(x[:13],ame[5,:13], 3)
# y5vals=np.polyval(f5, x[:13])
# f9=np.polyfit(x[:13],ame[9,:13], 3)
# y9vals=np.polyval(f9, x[:13])
# f10=np.polyfit(x[:13],ame[10,:13], 3)
# y10vals=np.polyval(f10, x[:13])
# f11=np.polyfit(x[:13],ame[11,:13], 3)
# y11vals=np.polyval(f11, x[:13])
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x[:13],y0vals,lw=1,label="H-FC with NT",color="red")
# plt.plot(x[:13],y1vals,lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x[:13],y2vals,lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x[:13],y6vals,lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x[:13],y7vals,lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x[:13],y8vals,lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x[:13],y3vals,lw=1,label="H-RC with NT",color="red")
# plt.plot(x[:13],y4vals,lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x[:13],y5vals,lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x[:13],y9vals,lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x[:13],y10vals,lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x[:13],y11vals,lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-RC",font2)
# plt.legend()
# plt.show()

######################3波动率有限制
# s=np.arange(0,10,0.5)
# fg=np.zeros((12,len(s)))
# for g in range(len(s)):
#     i=s[g]
#     print(i)
#     df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df3= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df6= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\未完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\未完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\未完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df9= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\未完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\未完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\波动率有限制\未完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     a0=np.mean(df0.values)
#     a1 = np.mean(df1.values)
#     a2 = np.mean(df2.values)
#     a3 = np.mean(df3.values)
#     a4 = np.mean(df4.values)
#     a5 = np.mean(df5.values)
#     a6 = np.mean(df6.values)
#     a7 = np.mean(df7.values)
#     a8 = np.mean(df8.values)
#     a9 = np.mean(df9.values)
#     a10 = np.mean(df10.values)
#     a11 = np.mean(df11.values)
#     fg[0,g]=a0
#     fg[1, g] = a1
#     fg[2, g] = a2
#     fg[3, g] = a3
#     fg[4,g] = a4
#     fg[5, g] = a5
#     fg[6, g] = a6
#     fg[7, g] = a7
#     fg[8, g] = a8
#     fg[9, g] = a9
#     fg[10, g] = a10
#     fg[11, g] = a11
# df = pd.DataFrame(fg)
# df.to_excel('E:\\data\火电绿电\第一部分\波动率有限制.xlsx')

# dfdf=pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率有限制.xlsx',index_col=0))
# ame=dfdf.values
# x=np.arange(0,10,0.5)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[0],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,ame[1],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,ame[2],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,ame[3],lw=1,label="H-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[4],lw=1,label="H-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[5],lw=1,label="H-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility ",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity - H type",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[6],lw=1,label="L-FC with NT",color="red")
# plt.plot(x,ame[7],lw=1,label="L-FC with TP",color="olivedrab")
# plt.plot(x,ame[8],lw=1,label="L-FC with TN",color="dodgerblue")
# plt.plot(x,ame[9],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[10],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[11],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity - L type",font2)
# plt.legend()
# plt.show()
########拟合
# f0=np.polyfit(x,ame[0], 3)
# y0vals=np.polyval(f0, x)
# f1=np.polyfit(x,ame[1], 3)
# y1vals=np.polyval(f1, x)
# f2=np.polyfit(x,ame[2], 3)
# y2vals=np.polyval(f2, x)
# f6=np.polyfit(x,ame[6], 3)
# y6vals=np.polyval(f6, x)
# f7=np.polyfit(x,ame[7], 3)
# y7vals=np.polyval(f7, x)
# f8=np.polyfit(x,ame[8], 3)
# y8vals=np.polyval(f8, x)
#
# f3=np.polyfit(x,ame[3], 3)
# y3vals=np.polyval(f3, x)
# f4=np.polyfit(x,ame[4], 3)
# y4vals=np.polyval(f4, x)
# f5=np.polyfit(x,ame[5], 3)
# y5vals=np.polyval(f5, x)
# f9=np.polyfit(x,ame[9], 3)
# y9vals=np.polyval(f9, x)
# f10=np.polyfit(x,ame[10], 3)
# y10vals=np.polyval(f10, x)
# f11=np.polyfit(x,ame[11], 3)
# y11vals=np.polyval(f11, x)
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,y0vals,lw=1,label="H-FC with NT",color="red")
# plt.plot(x,y1vals,lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,y2vals,lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,y6vals,lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,y7vals,lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,y8vals,lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,y3vals,lw=1,label="H-RC with NT",color="red")
# plt.plot(x,y4vals,lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,y5vals,lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,y9vals,lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,y10vals,lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,y11vals,lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-RC",font2)
# plt.legend()
# plt.show()


#########################半径波动率无限制
# s=np.arange(1.5,10,0.5)
# fg=np.zeros((12,len(s)))
# for g in range(len(s)):
#     i=s[g]
#     print(i)
#     df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df3= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df6= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\未完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\未完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\未完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df9= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\未完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\未完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率\未完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     a0=np.mean(df0.values)
#     a1 = np.mean(df1.values)
#     a2 = np.mean(df2.values)
#     a3 = np.mean(df3.values)
#     a4 = np.mean(df4.values)
#     a5 = np.mean(df5.values)
#     a6 = np.mean(df6.values)
#     a7 = np.mean(df7.values)
#     a8 = np.mean(df8.values)
#     a9 = np.mean(df9.values)
#     a10 = np.mean(df10.values)
#     a11 = np.mean(df11.values)
#     fg[0,g]=a0
#     fg[1, g] = a1
#     fg[2, g] = a2
#     fg[3, g] = a3
#     fg[4,g] = a4
#     fg[5, g] = a5
#     fg[6, g] = a6
#     fg[7, g] = a7
#     fg[8, g] = a8
#     fg[9, g] = a9
#     fg[10, g] = a10
#     fg[11, g] = a11
# df = pd.DataFrame(fg)
# df.to_excel('E:\\data\火电绿电\第一部分\半径波动率.xlsx')

# dfdf=pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\半径波动率.xlsx',index_col=0))
# ame=dfdf.values
# x=np.arange(1.5,10,0.5)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[0],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,ame[1],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,ame[2],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,ame[3],lw=1,label="H-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[4],lw=1,label="H-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[5],lw=1,label="H-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility",font)
# plt.xlabel("Radius",font)
# plt.title("Radius - H type",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[6],lw=1,label="L-FC with NT",color="red")
# plt.plot(x,ame[7],lw=1,label="L-FC with TP",color="olivedrab")
# plt.plot(x,ame[8],lw=1,label="L-FC with TN",color="dodgerblue")
# plt.plot(x,ame[9],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[10],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[11],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility",font)
# plt.xlabel("Radius",font)
# plt.title("Radius - L type",font2)
# plt.legend()
# plt.show()
########拟合
# f0=np.polyfit(x,ame[0], 4)
# y0vals=np.polyval(f0, x)
# f1=np.polyfit(x,ame[1], 4)
# y1vals=np.polyval(f1, x)
# f2=np.polyfit(x,ame[2], 4)
# y2vals=np.polyval(f2, x)
# f6=np.polyfit(x,ame[6], 4)
# y6vals=np.polyval(f6, x)
# f7=np.polyfit(x,ame[7], 4)
# y7vals=np.polyval(f7, x)
# f8=np.polyfit(x,ame[8], 4)
# y8vals=np.polyval(f8, x)
#
# f3=np.polyfit(x,ame[3], 4)
# y3vals=np.polyval(f3, x)
# f4=np.polyfit(x,ame[4], 4)
# y4vals=np.polyval(f4, x)
# f5=np.polyfit(x,ame[5], 4)
# y5vals=np.polyval(f5, x)
# f9=np.polyfit(x,ame[9], 4)
# y9vals=np.polyval(f9, x)
# f10=np.polyfit(x,ame[10], 4)
# y10vals=np.polyval(f10, x)
# f11=np.polyfit(x,ame[11], 4)
# y11vals=np.polyval(f11, x)
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,y0vals,lw=1,label="H-FC with NT",color="red")
# plt.plot(x,y1vals,lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,y2vals,lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,y6vals,lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,y7vals,lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,y8vals,lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,y3vals,lw=1,label="H-RC with NT",color="red")
# plt.plot(x,y4vals,lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,y5vals,lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,y9vals,lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,y10vals,lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,y11vals,lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-RC",font2)
# plt.legend()
# plt.show()



#######################半径波动率有限制
# s=np.arange(1.5,10,0.5)
# fg=np.zeros((12,len(s)))
# for g in range(len(s)):
#     i=s[g]
#     print(i)
#     df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df3= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df6= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\未完成配额以传统能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\未完成配额以传统能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\未完成配额以传统能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     df9= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\未完成配额以可再生能源为主的电力企业不交易人数V'+str(i)+'.xlsx',index_col=0))
#     df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\未完成配额以可再生能源为主的电力企业与pool交易人数V'+str(i)+'.xlsx',index_col=0))
#     df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\波动率改\半径波动率有限制\未完成配额以可再生能源为主的电力企业与邻居交易人数V'+str(i)+'.xlsx',index_col=0))
#     a0=np.mean(df0.values)
#     a1 = np.mean(df1.values)
#     a2 = np.mean(df2.values)
#     a3 = np.mean(df3.values)
#     a4 = np.mean(df4.values)
#     a5 = np.mean(df5.values)
#     a6 = np.mean(df6.values)
#     a7 = np.mean(df7.values)
#     a8 = np.mean(df8.values)
#     a9 = np.mean(df9.values)
#     a10 = np.mean(df10.values)
#     a11 = np.mean(df11.values)
#     fg[0,g]=a0
#     fg[1, g] = a1
#     fg[2, g] = a2
#     fg[3, g] = a3
#     fg[4,g] = a4
#     fg[5, g] = a5
#     fg[6, g] = a6
#     fg[7, g] = a7
#     fg[8, g] = a8
#     fg[9, g] = a9
#     fg[10, g] = a10
#     fg[11, g] = a11
# df = pd.DataFrame(fg)
# df.to_excel('E:\\data\火电绿电\第一部分\半径波动率有限制.xlsx')

# dfdf=pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\半径波动率有限制.xlsx',index_col=0))
# ame=dfdf.values
# x=np.arange(1.5,10,0.5)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[0],lw=1,label="H-FC with NT",color="red")
# plt.plot(x,ame[1],lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,ame[2],lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,ame[3],lw=1,label="H-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[4],lw=1,label="H-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[5],lw=1,label="H-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility",font)
# plt.xlabel("Radius",font)
# plt.title("Radius - H type",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,ame[6],lw=1,label="L-FC with NT",color="red")
# plt.plot(x,ame[7],lw=1,label="L-FC with TP",color="olivedrab")
# plt.plot(x,ame[8],lw=1,label="L-FC with TN",color="dodgerblue")
# plt.plot(x,ame[9],lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[10],lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,ame[11],lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Volatility",font)
# plt.xlabel("Radius",font)
# plt.title("Radius - L type",font2)
# plt.legend()
# plt.show()
########拟合
# f0=np.polyfit(x,ame[0], 4)
# y0vals=np.polyval(f0, x)
# f1=np.polyfit(x,ame[1], 4)
# y1vals=np.polyval(f1, x)
# f2=np.polyfit(x,ame[2], 4)
# y2vals=np.polyval(f2, x)
# f6=np.polyfit(x,ame[6], 4)
# y6vals=np.polyval(f6, x)
# f7=np.polyfit(x,ame[7], 4)
# y7vals=np.polyval(f7, x)
# f8=np.polyfit(x,ame[8], 4)
# y8vals=np.polyval(f8, x)
#
# f3=np.polyfit(x,ame[3], 4)
# y3vals=np.polyval(f3, x)
# f4=np.polyfit(x,ame[4], 4)
# y4vals=np.polyval(f4, x)
# f5=np.polyfit(x,ame[5], 4)
# y5vals=np.polyval(f5, x)
# f9=np.polyfit(x,ame[9], 4)
# y9vals=np.polyval(f9, x)
# f10=np.polyfit(x,ame[10], 4)
# y10vals=np.polyval(f10, x)
# f11=np.polyfit(x,ame[11], 4)
# y11vals=np.polyval(f11, x)
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,y0vals,lw=1,label="H-FC with NT",color="red")
# plt.plot(x,y1vals,lw=1,label="H-FC with TP",color="olivedrab")
# plt.plot(x,y2vals,lw=1,label="H-FC with TN",color="dodgerblue")
# plt.plot(x,y6vals,lw=1,label="L-FC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,y7vals,lw=1,label="L-FC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,y8vals,lw=1,label="L-FC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,y3vals,lw=1,label="H-RC with NT",color="red")
# plt.plot(x,y4vals,lw=1,label="H-RC with TP",color="olivedrab")
# plt.plot(x,y5vals,lw=1,label="H-RC with TN",color="dodgerblue")
# plt.plot(x,y9vals,lw=1,label="L-RC with NT",color="orangered",linestyle='-.',alpha = 0.5)
# plt.plot(x,y10vals,lw=1,label="L-RC with TP",color="lawngreen",linestyle='-.',alpha = 0.5)
# plt.plot(x,y11vals,lw=1,label="L-RC with TN",color="powderblue",linestyle='-.',alpha = 0.5)
# plt.ylabel("Proportion",font)
# plt.xlabel("Velocity",font)
# plt.title("Velocity-fit-RC",font2)
# plt.legend()
# plt.show()



###############################pgpd无限制
# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe0\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_e}$",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_e}$",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()



# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe无限制\pgpe1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_g}$",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_g}$",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()


#######################################pgpe有限制

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe0\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_e}$",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_e}$",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()



# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe有限制\pgpe1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_g}$",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${P_g}$",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()


#################################################### 补充的

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\A\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\B\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\C\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()



# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\D\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$ and ${C_p}$",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()

#
# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# #
# # df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# #
# # df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# #
# # df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\成本差额\E\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# # x=np.linspace(0,3,30)
# # font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# # font2= {'family' : 'Times New Roman','weight' : 'normal'}
# # fig= plt.figure()
# # plt.rcParams['figure.figsize'] = (10.0, 6.0)
# # plt.rcParams['savefig.dpi'] = 1000 #图片像素
# # plt.rcParams['figure.dpi'] = 1000 #
# # plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# # plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# # plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# # plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# # plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# # plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# # plt.ylabel("Proportion",font)
# # plt.xlabel("${C_d}$ and ${C_p}$",font)
# # plt.title("H-FC and L-FC",font2)
# # plt.legend()
# # plt.show()
# # fig= plt.figure()
# # plt.rcParams['figure.figsize'] = (10.0, 6.0)
# # plt.rcParams['savefig.dpi'] = 1000 #图片像素
# # plt.rcParams['figure.dpi'] = 1000 #
# # plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# # plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# # plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# # plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# # plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# # plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# # plt.ylabel("Proportion",font)
# # plt.xlabel("${C_d}$ and ${C_p}$",font)
# # plt.title("H-RC and L-RC",font2)
# # plt.legend()
# # plt.show()

# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\e0f\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("e=0  ,  f",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("e=0  ,  f",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()




# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\ef\ef1\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,40)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("f=3  ,  e",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("e=0  ,  f",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cd\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$",font)
# plt.title("H-FC and L-FC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("${C_d}$",font)
# plt.title("H-RC and L-RC",font2)
# plt.legend()
# plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# #
# # df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# #
# # df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# #
# # df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# # df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# # df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\cp\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# # x=np.linspace(0,3,30)
# # font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# # font2= {'family' : 'Times New Roman','weight' : 'normal'}
# # fig= plt.figure()
# # plt.rcParams['figure.figsize'] = (10.0, 6.0)
# # plt.rcParams['savefig.dpi'] = 1000 #图片像素
# # plt.rcParams['figure.dpi'] = 1000 #
# # plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# # plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# # plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# # plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r",linestyle='--')
# # plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g",linestyle='--')
# # plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b",linestyle='--')
# # plt.ylabel("Proportion",font)
# # plt.xlabel("${C_p}$",font)
# # plt.title("H-FC and L-FC",font2)
# # plt.legend()
# # plt.show()
# # fig= plt.figure()
# # plt.rcParams['figure.figsize'] = (10.0, 6.0)
# # plt.rcParams['savefig.dpi'] = 1000 #图片像素
# # plt.rcParams['figure.dpi'] = 1000 #
# # plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r")
# # plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g")
# # plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b")
# # plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# # plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# # plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# # plt.ylabel("Proportion",font)
# # plt.xlabel("${C_p}$",font)
# # plt.title("H-RC and L-RC",font2)
# # plt.legend()
# # plt.show()


# df30= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df31 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df32 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df33 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df34 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df35 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df36 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df37 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df38 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df39 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df310 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df311 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\三个成本\c\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# x=np.linspace(0,3,30)
# font= {'family' : 'Times New Roman','weight' : 'ultralight','size':7,'style': 'italic'}
# font2= {'family' : 'Times New Roman','weight' : 'normal'}
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df30.values/250,lw=1,label="H-FC with NT",color="r")
# plt.plot(x,df31.values/250,lw=1,label="H-FC with TP",color="g")
# plt.plot(x,df32.values/250,lw=1,label="H-FC with TN",color="b")
# plt.plot(x,df33.values/250,lw=1,label="H-RC with NT",color="r",linestyle='--')
# plt.plot(x,df34.values/250,lw=1,label="H-RC with TP",color="g",linestyle='--')
# plt.plot(x,df35.values/250,lw=1,label="H-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("C",font)
# plt.title("H-FC and H-RC",font2)
# plt.legend()
# plt.show()
# fig= plt.figure()
# plt.rcParams['figure.figsize'] = (10.0, 6.0)
# plt.rcParams['savefig.dpi'] = 1000 #图片像素
# plt.rcParams['figure.dpi'] = 1000 #
# plt.plot(x,df36.values/250,lw=1,label="L-FC with NT",color="r")
# plt.plot(x,df37.values/250,lw=1,label="L-FC with TP",color="g")
# plt.plot(x,df38.values/250,lw=1,label="L-FC with TN",color="b")
# plt.plot(x,df39.values/250,lw=1,label="L-RC with NT",color="r",linestyle='--')
# plt.plot(x,df310.values/250,lw=1,label="L-RC with TP",color="g",linestyle='--')
# plt.plot(x,df311.values/250,lw=1,label="L-RC with TN",color="b",linestyle='--')
# plt.ylabel("Proportion",font)
# plt.xlabel("C",font)
# plt.title("L-FC and L-RC",font2)
# plt.legend()
# plt.show()




# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# b0=df0.values/250
# b1=df1.values/250
# b2=df2.values/250
# b3=df3.values/250
# b4=df4.values/250
# b5=df5.values/250
# b6=df6.values/250
# b7=df7.values/250
# b8=df8.values/250
# b9=df9.values/250
# b10=df10.values/250
# b11=df11.values/250
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



# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\火电绿电成本\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
# b0=df0.values/250
# b1=df1.values/250
# b2=df2.values/250
# b3=df3.values/250
# b4=df4.values/250
# b5=df5.values/250
# b6=df6.values/250
# b7=df7.values/250
# b8=df8.values/250
# b9=df9.values/250
# b10=df10.values/250
# b11=df11.values/250
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
#     plt.ylabel("${C_h}$",font)
#     plt.xlabel("${C_g}$",font)
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\CgCh'+i+'.png')

# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第一部分\\VR")
df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))

df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\VR\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
    plt.imshow(BB[i], cmap="rainbow",extent=[0,5,1,5],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
    plt.ylabel("radius",font)#hang
    plt.xlabel("velocity",font)#lie
    plt.colorbar(shrink=1)
    plt.title(BB2[i],font2)
    plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第一部分\VR\VR'+i+'.png')



# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第一部分\\EF")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\EF\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,4,0,4],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("e",font)#hang
#     plt.xlabel("f",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第一部分\EF\EF'+i+'.png')
#



# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第一部分\\pgpe")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     # print(i)
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
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第一部分\pgpe\pgpe'+i+'.png')




# os.makedirs("E:\\终生写论文\\王鹏宇_火电绿电配图\\第一部分\\cdcp")
# df0= pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df1 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df2 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df3 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df4 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df5 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df6 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\未完成配额以传统能源为主的电力企业不交易人数.xlsx',index_col=0))
# df7 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df8 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
#
# df9 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\未完成配额以可再生能源为主的电力企业不交易人数.xlsx',index_col=0))
# df10 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx',index_col=0))
# df11 = pd.DataFrame(pd.read_excel('E:\\data\火电绿电\第一部分\cdcp\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx',index_col=0))
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
#     # print(i)
#     # print(BB[i])
#     fig = plt.figure()
#     plt.rcParams['figure.figsize'] = (10.0, 6.0)
#     plt.rcParams['savefig.dpi'] = 1000 #图片像素
#     plt.rcParams['figure.dpi'] = 1000 #
#     plt.imshow(BB[i], cmap="rainbow",extent=[0,2,0,2],origin='lower',vmin=0, vmax=1,interpolation='kaiser')
#     plt.ylabel("${C_d}$",font)#hang
#     plt.xlabel("${C_p}$",font)#lie
#     plt.colorbar(shrink=1)
#     plt.title(BB2[i],font2)
#     plt.savefig('E:\\终生写论文\王鹏宇_火电绿电配图\第一部分\cdcp\cdcp'+i+'.png')