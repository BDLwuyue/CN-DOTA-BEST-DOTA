import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import random

X=np.arange(0,5)
XX=np.arange(0,5,2)
hotnum=1000
greennum=1000
Q0=6054400000
v=0.0614
Q=v*Q0
r=3
m=0.00000414
n=-114.31
c=230
f=690
k=1
L=10
velocity=0.1
penalty=5
award=5
strategy=np.random.randint(0,2,size=(2,hotnum))
hotloc=np.random.uniform(0,L,size=(hotnum,2))
greenloc=np.random.uniform(0,L,size=(greennum,2))
dealpeople=np.zeros((len(X),2))
t0 = list(np.sort(np.random.uniform(0, Q, size=(1, hotnum- 1))[0]))
t0.insert(0, 0)
t0.append(Q)
t1 = []
for i in range(hotnum):
    t1.append(t0[i + 1] - t0[i])

t2 = list(np.sort(np.random.uniform(0, Q, size=(1, greennum- 1))[0]))
t2.insert(0, 0)
t2.append(Q)
t3 = []
for i in range(hotnum):
    t3.append(t2[i + 1] - t2[i])
quotagreen=t3
quotahot=t1
# fig = plt.figure()
# plt.scatter(hotloc[:,0],hotloc[:,1],c="r",s=20,marker="x",alpha=0.5)###marker="o\s\p\*\<\>\^\v\+"
# plt.scatter(greenloc[:,0],greenloc[:,1],c="g",s=20,marker="o",alpha=0.5)
# plt.show()
for i in X:
    print(i)
    bb=i
    ll=np.sum(strategy,axis=1)
    dealpeople[i]=ll
    hotlocup=copy.copy(hotloc)
    hotlocup[:,1]=np.add(hotloc[:,1],L)
    hotlocupright=np.add(hotloc,L)
    hotlocupleft=copy.copy(hotloc)
    hotlocupleft[:,1]=np.add(hotloc[:,1],L)
    hotlocupleft[:,0]=np.subtract(hotloc[:,0],L)
    hotlocdown=copy.copy(hotloc)
    hotlocdown[:,1]=np.subtract(hotloc[:,1],L)
    hotlocdownleft=np.subtract(hotloc,L)
    hotlocdownright=copy.copy(hotloc)
    hotlocdownright[:,1]=np.subtract(hotloc[:,1],L)
    hotlocdownright[:,0]=np.add(hotloc[:,0],L)
    hotlocright=copy.copy(hotloc)
    hotlocright[:,0]=np.add(hotloc[:,0],L)
    hotlocleft=copy.copy(hotloc)
    hotlocleft[:,0]=np.subtract(hotloc[:,0],L)
    greenlocup=copy.copy(greenloc)
    greenlocup[:,1]=np.add(greenloc[:,1],L)
    greenlocupright=np.add(greenloc,L)
    greenlocupleft=copy.copy(greenloc)
    greenlocupleft[:,1]=np.add(greenloc[:,1],L)
    greenlocupleft[:,0]=np.subtract(greenloc[:,0],L)
    greenlocdown=copy.copy(greenloc)
    greenlocdown[:,1]=np.subtract(greenloc[:,1],L)
    greenlocdownleft=np.subtract(greenloc,L)
    greenlocdownright=copy.copy(greenloc)
    greenlocdownright[:,1]=np.subtract(greenloc[:,1],L)
    greenlocdownright[:,0]=np.add(greenloc[:,0],L)
    greenlocright=copy.copy(greenloc)
    greenlocright[:,0]=np.add(greenloc[:,0],L)
    greenlocleft=copy.copy(greenloc)
    greenlocleft[:,0]=np.subtract(greenloc[:,0],L)
    distance_ghmindled=np.zeros((greennum,hotnum))#绿电横坐标，火电纵坐标
    distance_ghup=np.zeros((greennum,hotnum))
    distance_ghdown=np.zeros((greennum,hotnum))
    distance_ghleft=np.zeros((greennum,hotnum))
    distance_ghright=np.zeros((greennum,hotnum))
    distance_ghupright=np.zeros((greennum,hotnum))
    distance_ghupleft=np.zeros((greennum,hotnum))
    distance_ghdownright=np.zeros((greennum,hotnum))
    distance_ghdownleft=np.zeros((greennum,hotnum))
    for i in range(hotnum):
        distance_ghmindled[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotloc[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghup[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocup[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghdown[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocdown[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocleft[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocright[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghupright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocupright[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghupleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocupleft[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghdownright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocdownright[i],(hotnum,1)),greenloc)),axis=1))
        distance_ghdownleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocdownleft[i],(hotnum,1)),greenloc)),axis=1))
    distance_gh=np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(distance_ghmindled,distance_ghup),distance_ghdown),distance_ghleft),distance_ghright),distance_ghupright),distance_ghupleft),distance_ghdownright),distance_ghdownleft)
    distance_hhmindled=np.zeros((greennum,hotnum))#绿电横坐标，火电纵坐标
    distance_hhup=np.zeros((greennum,hotnum))
    distance_hhdown=np.zeros((greennum,hotnum))
    distance_hhleft=np.zeros((greennum,hotnum))
    distance_hhright=np.zeros((greennum,hotnum))
    distance_hhupright=np.zeros((greennum,hotnum))
    distance_hhupleft=np.zeros((greennum,hotnum))
    distance_hhdownright=np.zeros((greennum,hotnum))
    distance_hhdownleft=np.zeros((greennum,hotnum))
    for i in range(hotnum):
        distance_hhmindled[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotloc[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhup[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocup[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhdown[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocdown[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocleft[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocright[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhupright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocupright[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhupleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocupleft[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhdownright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocdownright[i],(hotnum,1)),hotloc)),axis=1))
        distance_hhdownleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(hotlocdownleft[i],(hotnum,1)),hotloc)),axis=1))
    distance_hh=np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(distance_hhmindled,distance_hhup),distance_hhdown),distance_hhleft),distance_hhright),distance_hhupright),distance_hhupleft),distance_hhdownright),distance_hhdownleft)
    distance_ggmindled=np.zeros((greennum,greennum))#绿电横坐标，火电纵坐标
    distance_ggup=np.zeros((greennum,greennum))
    distance_ggdown=np.zeros((greennum,greennum))
    distance_ggleft=np.zeros((greennum,greennum))
    distance_ggright=np.zeros((greennum,greennum))
    distance_ggupright=np.zeros((greennum,greennum))
    distance_ggupleft=np.zeros((greennum,greennum))
    distance_ggdownright=np.zeros((greennum,greennum))
    distance_ggdownleft=np.zeros((greennum,greennum))
    for i in range(hotnum):
        distance_ggmindled[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenloc[i],(greennum,1)),greenloc)),axis=1))
        distance_ggup[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocup[i],(greennum,1)),greenloc)),axis=1))
        distance_ggdown[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocdown[i],(greennum,1)),greenloc)),axis=1))
        distance_ggleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocleft[i],(greennum,1)),greenloc)),axis=1))
        distance_ggright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocright[i],(greennum,1)),greenloc)),axis=1))
        distance_ggupright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocupright[i],(greennum,1)),greenloc)),axis=1))
        distance_ggupleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocupleft[i],(greennum,1)),greenloc)),axis=1))
        distance_ggdownright[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocdownright[i],(greennum,1)),greenloc)),axis=1))
        distance_ggdownleft[i]=np.sqrt(np.sum(np.square(np.subtract(np.tile(greenlocdownleft[i],(greennum,1)),greenloc)),axis=1))
    distance_gg=np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(distance_ggmindled,distance_ggup),distance_ggdown),distance_ggleft),distance_ggright),distance_ggupright),distance_ggupleft),distance_ggdownright),distance_ggdownleft)
    distance_h= np.tril(distance_hh,-1)#下三角形###https://www.cnblogs.com/cymwill/p/7857456.html
    distance_g= np.tril(distance_gg,-1)

    field_gh=copy.copy(distance_gh)
    field_hh=copy.copy(distance_hh)
    field_gg=copy.copy(distance_gg)
    #####https://blog.csdn.net/qq_42393859/article/details/86524805?utm_medium=distribute.pc_aggpage_search_result.none-task-blog-2~all~first_rank_v2~rank_v25-2-86524805.nonecase&utm_term=python%20%E6%80%8E%E4%B9%88%E5%AF%B9%E7%9F%A9%E9%98%B5%E6%9F%90%E4%BA%9B%E5%85%83%E7%B4%A0%E6%9B%BF%E6%8D%A2
    field_gh[field_gh<=r]=1
    field_gh[field_gh>r]=0
    field_hh[field_hh==0]=r*2
    field_hh[field_hh<=r]=1
    field_hh[field_hh>r]=0
    field_gg[field_gg==0]=r*2
    field_gg[field_gg<=r]=1
    field_gg[field_gg>r]=0

    dealnum=int(np.sum(field_gh))
    l0=list(np.sort(np.random.uniform(0,Q,size=(1,dealnum-1))[0]))
    l0.insert(0,0)
    l0.append(Q)
    l1=[]
    for i in range(dealnum):
        l1.append(l0[i+1]-l0[i])
    deal=copy.copy(field_gh)
    l2=np.nonzero(deal)
    l3=np.dstack((l2[0],l2[1])).squeeze()
    for i in range(dealnum):
        deal[l3[i,0],l3[i,1]]=l1[i]
    earnhot=copy.copy(deal)
    earngreen=copy.copy(deal)
    dealhot=np.sum(deal,axis=1)
    dealgreen=np.sum(deal,axis=0)
    marginhot=np.subtract(dealhot,quotahot)
    margingreen=np.subtract(dealgreen,quotagreen)
    marginhot[marginhot>=0]=marginhot[marginhot>=0]*award
    marginhot[marginhot<0] = marginhot[marginhot<0] *penalty
    margingreen[margingreen>=0]=margingreen[margingreen>=0]*award
    margingreen[margingreen<0] = margingreen[margingreen<0] *penalty
    for i in l3:
        if strategy[0,i[0]]==0 and strategy[1,i[1]]==0:
            earnhot[i[0],i[1]]=-f*deal[i[0],i[1]]
            earngreen[i[0],i[1]]=0
        elif strategy[0,i[0]]==1 and strategy[1,i[1]]==1:
            earnhot[i[0],i[1]]=-(m*v*Q0+n)*deal[i[0],i[1]]-r
            earngreen[i[0],i[1]]=(m*v*Q0+n)*deal[i[0],i[1]]-c*deal[i[0],i[1]]-r
        elif strategy[0,i[0]]==1 and strategy[1,i[1]]==0:
            earnhot[i[0],i[1]]=-f*deal[i[0],i[1]]-r
            earngreen[i[0],i[1]]=0
        else:
            earnhot[i[0],i[1]]=-f*deal[i[0],i[1]]
            earngreen[i[0],i[1]]=-r
    totalearnhot=np.sum(earnhot,axis=1)
    totalearngreen=np.sum(earngreen,axis=0)
    totalhot=np.add(totalearnhot,marginhot)
    totalgreen = np.add(totalearngreen, margingreen)
    averearnhot=np.divide(totalhot,np.sum(field_gh,axis=1))
    averearngreen=np.divide(totalgreen,np.sum(field_gh,axis=0))
    l4=np.zeros((1,hotnum))[0]
    l5=np.zeros((1,greennum))[0]
    for i in range(hotnum):
        hotneighbor = field_hh[i]
        hotneighbori= np.nonzero(hotneighbor)[0]
        hotextractneighbori= random.choice(hotneighbori)
        if len(hotneighbori)==0:
            l4[i] = strategy[0, i]
        else:
            if random.random()<=(1/(1+np.exp((averearnhot[i]-averearnhot[hotextractneighbori])/k))):
                l4[i]=strategy[0,hotextractneighbori]
            else:
                l4[i]=strategy[0,i]
        greenneighbor = field_gg[i]
        greenneighbori= np.nonzero(greenneighbor)[0]
        greenextractneighbori= random.choice(greenneighbori)
        if len(greenneighbori)==0:
            l5[i] = strategy[1, i]
        else:
            if random.random()<=(1/(1+np.exp((averearngreen[i]-averearngreen[greenextractneighbori])/k))):
                l5[i]=strategy[1,greenextractneighbori]
            else:
                l5[i]=strategy[1,i]
    strategy[0]=l4
    strategy[1]=l5
    angle=np.random.uniform(-np.pi,np.pi,size=(2,hotnum))
    anglecos=np.multiply(np.sin(angle),v)
    anglesin=np.multiply(np.cos(angle),v)
    hotloc[:,0]=np.add(hotloc[:,0],anglecos[0])
    hotloc[:,1]=np.add(hotloc[:,1],anglesin[0])
    l6=np.where(hotloc>L)
    l8=np.where(hotloc<0)
    hotcopy=copy.copy(hotloc)
    for i in range(len(l6[0])):
        hotloc[l6[0][i],l6[1][i]]=hotcopy[l6[0][i],l6[1][i]]-L
    for i in range(len(l8[0])):
        hotloc[l8[0][i],l8[1][i]] = hotcopy[l8[0][i],l8[1][i]] + L
    greenloc[:,0]=np.add(greenloc[:,0],anglecos[1])
    greenloc[:,1]=np.add(greenloc[:,1],anglesin[1])
    l10=np.where(greenloc>L)
    l12=np.where(greenloc<0)
    greencopy=copy.copy(greenloc)
    for i in range(len(l10[0])):
        greenloc[l10[0][i],l10[1][i]]=greencopy[l10[0][i],l10[1][i]]-L
    for i in range(len(l12[0])):
        greenloc[l12[0][i],l12[1][i]] = greencopy[l12[0][i],l12[1][i]] +L
    if bb in XX:
        df0 = pd.DataFrame(hotloc)
        df0.to_excel('E:\\data\火电绿电\第二部分\奖惩火电位置第'+str(bb)+'轮.xls')
        df1 = pd.DataFrame(greenloc)
        df1.to_excel('E:\\data\火电绿电\第二部分\奖惩绿电位置第'+str(bb)+'轮.xls')
        df2=pd.DataFrame(strategy.T)
        df2.to_excel('E:\\data\火电绿电\第二部分\奖惩火电绿电策略第'+str(bb)+'轮.xls')

df3 = pd.DataFrame(dealpeople)
df3.to_excel('E:\\data\火电绿电\第二部分\奖惩火电绿电人数.xls')














