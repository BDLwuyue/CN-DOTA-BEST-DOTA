import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import random



Total_rounds=50
powerinterval=10
photointerval=25
Ygnum=50
Ngnum=50
Yhnum=50
Nhnum=50
Ynum=Ygnum+Yhnum
Nnum=Ngnum+Nhnum
Ynum_list=np.arange(Ynum)
Nnum_list=np.arange(Nnum)
Bii=10#投资轮次
X=np.arange(0,Total_rounds)
XX=np.arange(powerinterval,Total_rounds,powerinterval)#监管力度变化
XX2=np.arange(photointerval-1,Total_rounds+photointerval-1,photointerval)#瞬时快照
department_utility=np.zeros((1,len(X)))[0]
departmentsign=np.zeros((1,len(X)))[0]
Ee=np.zeros((1,len(X)))[0]
Ff=np.zeros((1,len(X)))[0]

green_quota_upper=0.4
green_quota=0.3
green_quota_lower=0.2
hot_quota_upper=0.2
hot_quota=0.1
hot_quota_lower=0
quota=np.array([hot_quota]*Yhnum+[green_quota]*Ygnum)
Yh_ratio=np.random.uniform(hot_quota,hot_quota_upper,size=(1,Yhnum))[0]
Yg_ratio=np.random.uniform(green_quota,green_quota_upper,size=(1,Ygnum))[0]
Nh_ratio=np.random.uniform(hot_quota_lower,hot_quota,size=(1,Nhnum))[0]
Ng_ratio=np.random.uniform(green_quota_lower,green_quota,size=(1,Ngnum))[0]
Yh_produce=np.random.uniform(10,50,size=(1,Yhnum))[0]
Yg_produce=np.random.uniform(10,50,size=(1,Ygnum))[0]
Nh_produce=np.random.uniform(10,50,size=(1,Nhnum))[0]
Ng_produce=np.random.uniform(10,50,size=(1,Ngnum))[0]



def cost_gpg(x):
    c=1
    return c
def cost_gph(x):
    c=1
    return c
def cost_hpg(x):
    c=1
    return c
def cost_hph(x):
    c=1
    return c
def pe(x):
    f=1
    return f
def Cd(x):
    c=2*x
    return c
def Cp(x):
    if x<=0:
        c=0
    else:
        c=1
    return c
def Cplist(x):
    x[x<=0]=0
    x[x>0]=1
    return x
pg=2
ph=1.5
a=0.5
W=30
e=0.4
f=0.5
L=10
r=3
K=10
K2=10
K3=10
C=5
velocity=0.01
powerchange=0.01
Cnew=10
newinvesthot=1
newinvestgreen=1
newinvest=0
Y_strategy=np.random.randint(0,2,size=(1,Ynum))[0]
N_strategy=np.random.randint(0,2,size=(1,Nnum))[0]
Yloc=np.random.uniform(0,L,size=(Ynum,2))
Nloc=np.random.uniform(0,L,size=(Nnum,2))



def ef(c0,c1,cty):
    no1=np.random.choice(cty)
    no2=np.random.choice(cty)##(+,+)=1;(+,-)=2;(-,+)=3;(-,-)=4
    if no1<=0 and no2<=0:
        why=4
    elif no1>=0 and no2>=0:
        why=1
    elif no1>=0 and no2<=0:
        why=2
    else:
        why=3
    x0=c0+no1
    x1=c1+no2
    s0=np.maximum(0,np.minimum(x0,1))
    s1=np.maximum(0,np.minimum(x1,1))
    return s0,s1,why

def plane(x):
    up=copy.copy(x)
    up[:,1]=np.add(x[:,1],L)
    upright=np.add(x,L)
    upleft=copy.copy(x)
    upleft[:,1]=np.add(x[:,1],L)
    upleft[:,0]=np.subtract(x[:,0],L)
    down=copy.copy(x)
    down[:,1]=np.subtract(x[:,1],L)
    downleft=np.subtract(x,L)
    downright=copy.copy(x)
    downright[:,1]=np.subtract(x[:,1],L)
    downright[:,0]=np.add(x[:,0],L)
    right=copy.copy(x)
    right[:,0]=np.add(x[:,0],L)
    left=copy.copy(x)
    left[:,0]=np.subtract(x[:,0],L)
    xiao8=[x,up,down,left,right,upright,upleft,downright,downleft]
    return xiao8

def boundary(x):
    x[x>10]=x[x>10]-10
    x[x<0]=x[x<0]+10
    return x


def distance(g,x,y):
    mindled=np.linalg.norm((g[0][x]-y),axis=1)
    up = np.linalg.norm((g[1][x]-y),axis=1)
    down = np.linalg.norm((g[2][x]-y),axis=1)
    left =np.linalg.norm((g[3][x]-y),axis=1)
    right =np.linalg.norm((g[4][x]-y),axis=1)
    upright = np.linalg.norm((g[5][x]-y),axis=1)
    upleft =np.linalg.norm((g[6][x]-y),axis=1)
    downright = np.linalg.norm((g[7][x]-y),axis=1)
    downleft =np.linalg.norm((g[8][x]-y),axis=1)
    f=np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(mindled,up),down),left),right),upright),upleft),downright),downleft)
    return f

def pairlist(x):
    linshi = copy.copy(x)
    pair = np.zeros((Ynum, 2))
    unfold = np.arange(Ynum * Nnum)
    fold = unfold.reshape(Ynum, Nnum)
    for i in range(Ynum):
        try:
            reshap_p=linshi.reshape(1,Ynum*Nnum)[0]
            Want_delete=np.random.choice(unfold ,p=reshap_p)
            rowdelete=np.where(fold==Want_delete)[0][0]#Y的编号
            columndelete=np.where(fold==Want_delete)[1][0]#N的编号
            pair0=np.array([rowdelete,columndelete])
            pair[i]=pair0
            linshi[rowdelete,:]=0
            linshi[:,columndelete]=0
            linshi=linshi/(np.sum(linshi))
        except:
            pair[i]=np.array([99999,99999])
    return pair

def field(x):
    cc=copy.copy(x)
    cc[cc==0]=r*100000
    cc[cc<=r]=1
    cc[cc>r]=0
    return cc

def greenbook(x,q1,q2):
    inpool=np.zeros((1,Ynum))[0]
    dog0=copy.copy(Ynum_list)
    for i in range(Ynum):
        jiu=x[i]
        jiu0=int(jiu[0])
        jiu1=int(jiu[1])
        if jiu0!=99999:
            np.delete(dog0, jiu0)
            if Y_strategy[jiu0]==1 and N_strategy[jiu1]==1:
                inpool[i]=np.maximum((q1[jiu0]-q2[jiu1]),0)
            else:
                inpool[i]=q1[jiu0]
        else:
            inpool[i]=0
    inpool[dog0]=q1[dog0]
    return np.sum(inpool)

def costame(x,a0,a1,a2,a3):
    cost0=copy.copy(x)
    cost1 = copy.copy(x)
    cost2 = copy.copy(x)
    cost3 = copy.copy(x)
    cost0[x[x<Yhnum]]=cost_hpg(a0[x[x<Yhnum]])
    cost0[x[x>Yhnum]] = cost_gpg(a0[x[x>Yhnum]])
    cost1[x[x<Yhnum]]=cost_hph(a1[x[x<Yhnum]])
    cost1[x[x>Yhnum]]=cost_gph(a1[x[x>Yhnum]])
    cost2[x[x<Nhnum]]=cost_hpg(a2[x[x<Nhnum]])
    cost2[x[x>Nhnum]] = cost_gpg(a2[x[x>Nhnum]])
    cost3[x[x<Nhnum]]=cost_hph(a3[x[x<Nhnum]])
    cost3[x[x>Nhnum]]=cost_gph(a3[x[x>Nhnum]])
    return cost0,cost1,cost2,cost3
Ygdeal=np.zeros((len(X),1))
Yhdeal=np.zeros((len(X),1))
Ngdeal=np.zeros((len(X),1))
Nhdeal=np.zeros((len(X),1))
Ytime_utility = np.zeros((len(X), Ynum))
Ntime_utility = np.zeros((len(X), Nnum))
CNnewlist = np.zeros((len(X), Nnum))
CYnewlist = np.zeros((len(X), Nnum))
Y_ratio = np.append(Yh_ratio, Yg_ratio)
N_ratio = np.append(Nh_ratio, Ng_ratio)
Y_produce = np.append(Yh_produce, Yg_produce)
N_produce = np.append(Nh_produce, Ng_produce)
TimeYg_producehot=np.zeros((len(X),Ygnum))
TimeYg_producegreen=np.zeros((len(X),Ygnum))
TimeYh_producehot=np.zeros((len(X),Yhnum))
TimeYh_producegreen=np.zeros((len(X),Yhnum))
TimeNg_producehot=np.zeros((len(X),Ngnum))
TimeNg_producegreen=np.zeros((len(X),Ngnum))
TimeNh_producehot=np.zeros((len(X),Nhnum))
TimeNh_producegreen=np.zeros((len(X),Nhnum))
for turn in X:
    Nbuy = (quota - N_ratio) * N_produce
    Nsellgreen = N_ratio * N_produce
    Nsellhot = (1 - N_ratio) * N_produce
    Ysell = (Y_ratio - quota) * Y_produce
    Ysellgreen = quota * Y_produce
    Ysellhot = (1 - Y_ratio) * Y_produce
    RY = a * Y_ratio * Y_produce
    RN = a * N_ratio * N_produce
    EEY = (Y_ratio - hot_quota) * Y_produce
    ZZN = (green_quota - N_ratio) * N_produce
    EY = e *EEY
    ZN= f *ZZN
    TimeYg_producehot[turn]=(1-Y_ratio[Ygnum:])*Y_produce[Ygnum:]
    TimeYg_producegreen[turn] =(Y_ratio[Ygnum:])*Y_produce[Ygnum:]
    TimeYh_producehot[turn] = (1-Y_ratio[:Yhnum])*Y_produce[:Yhnum]
    TimeYh_producegreen[turn] =(Y_ratio[:Yhnum])*Y_produce[:Yhnum]
    TimeNg_producehot[turn] =(1-N_ratio[Ngnum:])*N_produce[Ngnum:]
    TimeNg_producegreen[turn]=(N_ratio[Ngnum:])*N_produce[Ngnum:]
    TimeNh_producehot[turn] =  (1-N_ratio[:Nhnum])*N_produce[:Nhnum]
    TimeNh_producegreen[turn] = (N_ratio[:Nhnum])*N_produce[:Nhnum]
    print(turn)
    bb=turn
    bb2=turn
    YNdistancematrix=np.zeros((Ynum,Nnum))
    NNdistancematrix=np.zeros((Nnum,Nnum))
    YYdistancematrix=np.zeros((Ynum,Ynum))
    for i in range(Ynum):
        YNdistancematrix[i]=distance(plane(Yloc),i,Nloc)
    for i in range(Nnum):
        NNdistancematrix[i]=distance(plane(Nloc),i,Nloc)
    for i in range(Ynum):
        YYdistancematrix[i]=distance(plane(Yloc),i,Yloc)
    YYfield=field(YYdistancematrix)
    YNfield=field(YNdistancematrix)
    NNfield=field(NNdistancematrix)
    NNdistancematrix_inverse=(1./NNdistancematrix)
    NNdistancematrix_inverse[np.isinf(NNdistancematrix_inverse)]=0
    NNlinshimatrix=NNdistancematrix_inverse*NNfield
    YYdistancematrix_inverse=(1./YYdistancematrix)
    YYdistancematrix_inverse[np.isinf(YYdistancematrix_inverse)]=0
    YYlinshimatrix=YYdistancematrix_inverse*YYfield
    YNprobmatrix=((1./YNdistancematrix)*YNfield)/(np.sum((1./YNdistancematrix)*YNfield))
    # print(YNfield)
    # print(np.where(YNfield[0]==1)[0])
    YNpairlist=pairlist(YNprobmatrix)
    green=greenbook(YNpairlist, Y_produce, N_produce)
    price=pe(green)
    Y_utility=np.zeros((1,Ynum))[0]
    N_utility=np.zeros((1,Nnum))[0]
    fgnb0 = copy.copy(Ynum_list)
    fgnb1 = copy.copy(Nnum_list)
    for i in range(Ynum):
        bjiu=YNpairlist[i]
        bjiu0=int(bjiu[0])
        bjiu1=int(bjiu[1])
        if bjiu0!=99999:
            np.delete(fgnb0, bjiu0)
            np.delete(fgnb1, bjiu1)
            if bjiu0 < Yhnum:
                cost0 = cost_hpg(Ysellgreen[bjiu0])
                cost1 = cost_hph(Ysellhot[bjiu0])
            else:
                cost0 = cost_gpg(Ysellgreen[bjiu0])
                cost1 = cost_gph(Ysellhot[bjiu0])
            if bjiu1 < Nhnum:
                cost2 = cost_hpg(Nsellgreen[bjiu1])
                cost3 = cost_hph(Nsellhot[bjiu1])
            else:
                cost2 = cost_gpg(Nsellgreen[bjiu1])
                cost3 = cost_gph(Nsellhot[bjiu1])
            if Y_strategy[bjiu0]==1 and N_strategy[bjiu1]==1:
                Y_utility[bjiu0]=pg*Ysellgreen[bjiu0]-price*Ysell[bjiu0]-cost0+ph*Ysellhot[bjiu0]-cost1-Cd(YNdistancematrix[bjiu0,bjiu1])/2-Cp((Ysell[bjiu0]-Nbuy[bjiu1]))+EY[bjiu0]
                N_utility[bjiu1]=pg*Nsellgreen[bjiu1]-price*Nbuy[bjiu1]-cost2+ph*Nsellhot[bjiu1]-cost3-Cd(YNdistancematrix[bjiu0,bjiu1])/2-Cp((Nbuy[bjiu1]-Ysell[bjiu0]))-ZN[bjiu1]
            elif Y_strategy[bjiu0]==1 and N_strategy[bjiu1]==0:
                Y_utility[bjiu0]=pg*Ysellgreen[bjiu0]-price*Ysell[bjiu0]-cost0+ph*Ysellhot[bjiu0]-cost1-Cd(YNdistancematrix[bjiu0,bjiu1])-Cp(Ysell[bjiu0])+EY[bjiu0]
                N_utility[bjiu1]=pg*Nsellgreen[bjiu1]-price*Nbuy[bjiu1]-cost2+ph*Nsellhot[bjiu1]-cost3-Cp(Nbuy[bjiu1])-ZN[bjiu1]
            elif Y_strategy[bjiu0]==0 and N_strategy[bjiu1]==1:
                Y_utility[bjiu0]=pg*Ysellgreen[bjiu0]-price*Ysell[bjiu0]-cost0+ph*Ysellhot[bjiu0]-cost1-Cp(Ysell[bjiu0])+EY[bjiu0]
                N_utility[bjiu1]=pg*Nsellgreen[bjiu1]-price*Nbuy[bjiu1]-cost2+ph*Nsellhot[bjiu1]-cost3-Cd(YNdistancematrix[bjiu0,bjiu1])-Cp(Nbuy[bjiu1])-ZN[bjiu1]
            else:
                Y_utility[bjiu0]=pg*Ysellgreen[bjiu0]-price*Ysell[bjiu0]-cost0+ph*Ysellhot[bjiu0]-cost1-Cp(Ysell[bjiu0])+EY[bjiu0]
                N_utility[bjiu1]=pg*Nsellgreen[bjiu1]-price*Nbuy[bjiu1]-cost2+ph*Nsellhot[bjiu1]-cost3-Cp(Nbuy[bjiu1])-ZN[bjiu1]
    Y_utility[fgnb0]=pg*Ysellgreen[fgnb0]-price*Ysell[fgnb0]-costame(fgnb0,Ysellgreen,Ysellhot,Nsellgreen,Nsellhot)[0]+ph*Ysellhot[fgnb0]-costame(fgnb0,Ysellgreen,Ysellhot,Nsellgreen,Nsellhot)[1]-Cplist(Ysell[fgnb0])+EY[fgnb0]
    N_utility[fgnb1]=pg*Nsellgreen[fgnb1]-price*Nbuy[fgnb1]-costame(fgnb0,Ysellgreen,Ysellhot,Nsellgreen,Nsellhot)[2]+ph*Nsellhot[fgnb1]-costame(fgnb0,Ysellgreen,Ysellhot,Nsellgreen,Nsellhot)[3]-Cplist(Nbuy[fgnb1])-ZN[fgnb1]
    copyY_strategy=copy.copy(Y_strategy)
    copyN_strategy=copy.copy(N_strategy)
    for i in range(Ynum):
        cjiu=NNlinshimatrix[i]
        if np.all(cjiu==0)==False:
            cjiu_p=cjiu/np.sum(cjiu)
            ineighbor=np.random.choice(Nnum_list,p=cjiu_p)
            if random.random()<=(1/(1+np.exp((N_utility[i]-N_utility[ineighbor])/K))):
                N_strategy[i]=copyN_strategy[ineighbor]
            else:
                N_strategy[i] = copyN_strategy[i]
        else:
            N_strategy[i] = copyN_strategy[i]
        djiu=YYlinshimatrix[i]
        if np.all(djiu==0)==False:
            djiu_p=djiu/np.sum(djiu)
            ineighbor0=np.random.choice(Ynum_list,p=djiu_p)
            if random.random()<=(1/(1+np.exp((Y_utility[i]-Y_utility[ineighbor0])/K))):
                Y_strategy[i]=copyY_strategy[ineighbor0]
            else:
                Y_strategy[i] = copyY_strategy[i]
        else:
            Y_strategy[i] = copyY_strategy[i]

    Ytime_utility[turn]=Y_utility
    Ntime_utility[turn]=N_utility
    copyY_produce=copy.copy(Y_produce)
    copyN_produce=copy.copy(N_produce)
    copyY_ratio=copy.copy(Y_ratio)
    copyN_ratio=copy.copy(N_ratio)
    if turn>=Bii:
        nji=np.arange(4)
        for i in range(Ynum):
            investpoint=np.where(CYnewlist[:turn,i])
            nearinvestpoint=np.where(CYnewlist[(turn - Bii):turn,i])
            if len(investpoint)==0:
                itypeU = np.mean(Ytime_utility[(turn - Bii):turn, i])
                iNneighbor = np.where(YNfield[i] == 1)[0]
                iYneighbor = np.where(YYfield[i] == 1)[0]
                itypeNh = np.mean(Ntime_utility[(turn - Bii):turn, iNneighbor[iNneighbor < Nhnum]])
                itypeNg = np.mean(Ntime_utility[(turn - Bii):turn, iNneighbor[iNneighbor >= Nhnum]])
                itypeYh = np.mean(Ytime_utility[(turn - Bii):turn, iYneighbor[iYneighbor < Yhnum]])
                itypeYg = np.mean(Ytime_utility[(turn - Bii):turn, iYneighbor[iYneighbor >= Yhnum]])
                if i < Yhnum:
                    if np.random.choice(nji) == 0:  ##Yh-Nh
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeNh) / K3))):
                            Y_produce[i] = copyY_produce[i] + newinvesthot
                            Y_ratio[i] = (1 - (((1 - copyY_ratio[i]) * copyY_produce[i] + newinvesthot) / (
                                        copyY_produce[i] + newinvesthot)))
                            CYnewlist[turn, i] = Cnew
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                    elif np.random.choice(nji) == 1:  ##Yh-Ng
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeNg) / K3))):
                            Y_produce[i] = copyY_produce[i] + newinvestgreen
                            Y_ratio[i] = (copyY_ratio[i] * copyY_produce[i] + newinvestgreen) / (
                                        copyY_produce[i] + newinvestgreen)
                            CYnewlist[turn, i] = Cnew
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                    elif np.random.choice(nji) == 2:  ##Yh-Yh
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeYh) / K3))):
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                    else:  ##Yh-Yg
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeYg) / K3))):
                            Y_produce[i] = copyY_produce[i] + newinvestgreen
                            Y_ratio[i] = (copyY_ratio[i] * copyY_produce[i] + newinvestgreen) / (
                                        copyY_produce[i] + newinvestgreen)
                            CYnewlist[turn, i] = Cnew
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                else:
                    if np.random.choice(nji) == 0:  ##Yg-Nh
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeNh) / K3))):
                            Y_produce[i] = copyY_produce[i] + newinvesthot
                            Y_ratio[i] = (1 - (((1 - copyY_ratio[i]) * copyY_produce[i] + newinvesthot) / (
                                        copyY_produce[i] + newinvesthot)))
                            CYnewlist[turn, i] = Cnew
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                    elif np.random.choice(nji) == 1:
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeNg) / K3))):
                            Y_produce[i] = copyY_produce[i] + newinvesthot
                            Y_ratio[i] = (1 - (((1 - copyY_ratio[i]) * copyY_produce[i] + newinvesthot) / (
                                        copyY_produce[i] + newinvesthot)))
                            CYnewlist[turn, i] = Cnew
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                    elif np.random.choice(nji) == 2:
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeYh) / K3))):
                            Y_produce[i] = copyY_produce[i] + newinvesthot
                            Y_ratio[i] = (1 - (((1 - copyY_ratio[i]) * copyY_produce[i] + newinvesthot) / (
                                        copyY_produce[i] + newinvesthot)))
                            CYnewlist[turn, i] = Cnew
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                    else:
                        if random.random() <= (1 / (1 + np.exp((itypeU - itypeYg) / K3))):
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
                        else:
                            Y_produce[i] = copyY_produce[i]
                            Y_ratio[i] = copyY_ratio[i]
            else:
                if len(nearinvestpoint)==0 and np.sum(Ytime_utility[investpoint[-1]:turn,i])>=Cnew:
                    itypeU = np.mean(Ytime_utility[(turn - Bii):turn, i])
                    iNneighbor = np.where(YNfield[i] == 1)[0]
                    iYneighbor = np.where(YYfield[i] == 1)[0]
                    itypeNh = np.mean(Ntime_utility[(turn - Bii):turn, iNneighbor[iNneighbor < Nhnum]])
                    itypeNg = np.mean(Ntime_utility[(turn - Bii):turn, iNneighbor[iNneighbor >= Nhnum]])
                    itypeYh = np.mean(Ytime_utility[(turn - Bii):turn, iYneighbor[iYneighbor < Yhnum]])
                    itypeYg = np.mean(Ytime_utility[(turn - Bii):turn, iYneighbor[iYneighbor >= Yhnum]])
                    if i<Yhnum:
                        if np.random.choice(nji)==0:##Yh-Nh
                            if random.random()<=(1/(1+np.exp((itypeU-itypeNh)/K3))):
                                Y_produce[i]=copyY_produce[i]+newinvesthot
                                Y_ratio[i]=(1-(((1-copyY_ratio[i])*copyY_produce[i]+newinvesthot)/(copyY_produce[i]+newinvesthot)))
                                CYnewlist[turn,i]=Cnew
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                        elif np.random.choice(nji)==1:##Yh-Ng
                            if random.random()<=(1/(1+np.exp((itypeU-itypeNg)/K3))):
                                Y_produce[i]=copyY_produce[i]+newinvestgreen
                                Y_ratio[i]=(copyY_ratio[i]*copyY_produce[i]+newinvestgreen)/(copyY_produce[i]+newinvestgreen)
                                CYnewlist[turn, i] = Cnew
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                        elif np.random.choice(nji)==2:##Yh-Yh
                            if random.random()<=(1/(1+np.exp((itypeU-itypeYh)/K3))):
                                Y_produce[i]=copyY_produce[i]
                                Y_ratio[i]=copyY_ratio[i]
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                        else:##Yh-Yg
                            if random.random()<=(1/(1+np.exp((itypeU-itypeYg)/K3))):
                                Y_produce[i]=copyY_produce[i]+newinvestgreen
                                Y_ratio[i]=(copyY_ratio[i]*copyY_produce[i]+newinvestgreen)/(copyY_produce[i]+newinvestgreen)
                                CYnewlist[turn, i] = Cnew
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                    else:
                        if np.random.choice(nji) == 0:##Yg-Nh
                            if random.random() <= (1 / (1 + np.exp((itypeU - itypeNh) / K3))):
                                Y_produce[i] = copyY_produce[i] + newinvesthot
                                Y_ratio[i] = (1-(((1-copyY_ratio[i])*copyY_produce[i]+newinvesthot)/(copyY_produce[i]+newinvesthot)))
                                CYnewlist[turn, i] = Cnew
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                        elif np.random.choice(nji) == 1:
                            if random.random() <= (1 / (1 + np.exp((itypeU - itypeNg) / K3))):
                                Y_produce[i] = copyY_produce[i] + newinvesthot
                                Y_ratio[i] =(1-(((1-copyY_ratio[i])*copyY_produce[i]+newinvesthot)/(copyY_produce[i]+newinvesthot)))
                                CYnewlist[turn, i] = Cnew
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                        elif np.random.choice(nji) == 2:
                            if random.random() <= (1 / (1 + np.exp((itypeU - itypeYh) / K3))):
                                Y_produce[i] = copyY_produce[i] + newinvesthot
                                Y_ratio[i] = (1-(((1-copyY_ratio[i])*copyY_produce[i]+newinvesthot)/(copyY_produce[i]+newinvesthot)))
                                CYnewlist[turn, i] = Cnew
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                        else:
                            if random.random() <= (1 / (1 + np.exp((itypeU - itypeYg) / K3))):
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
                            else:
                                Y_produce[i] = copyY_produce[i]
                                Y_ratio[i] = copyY_ratio[i]
        for j in range(Nnum):
            investpointj=np.where(CNnewlist[:turn,j])
            nearinvestpointj=np.where(CNnewlist[(turn - Bii):turn,j])
            if len(investpointj)==0:
                jtypeU = np.mean(Ntime_utility[(turn - Bii):turn, j])
                jYneighbor = np.where(YNfield[:, j] == 1)[0]
                jNneighbor = np.where(NNfield[j] == 1)[0]
                jtypeNh = np.mean(Ntime_utility[(turn - Bii):turn, jNneighbor[jNneighbor < Nhnum]])
                jtypeNg = np.mean(Ntime_utility[(turn - Bii):turn, jNneighbor[jNneighbor >= Nhnum]])
                jtypeYh = np.mean(Ytime_utility[(turn - Bii):turn, jYneighbor[jYneighbor < Yhnum]])
                jtypeYg = np.mean(Ytime_utility[(turn - Bii):turn, jYneighbor[jYneighbor >= Yhnum]])
                if j < Nhnum:
                    if np.random.choice(nji) == 0:  ##Nh-Nh
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeNh) / K3))):
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                    elif np.random.choice(nji) == 1:
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeNg) / K3))):
                            N_produce[j] = copyN_produce[j] + newinvestgreen
                            N_ratio[j] = (copyN_ratio[j] * copyN_produce[j] + newinvestgreen) / (
                                        copyN_produce[j] + newinvestgreen)
                            CNnewlist[turn, j] = Cnew
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                    elif np.random.choice(nji) == 2:
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeYh) / K3))):
                            N_produce[j] = copyN_produce[j] + newinvestgreen
                            N_ratio[j] = (copyN_ratio[j] * copyN_produce[j] + newinvestgreen) / (
                                        copyN_produce[j] + newinvestgreen)
                            CNnewlist[turn, j] = Cnew
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                    else:
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeYg) / K3))):
                            N_produce[j] = copyN_produce[j] + newinvestgreen
                            N_ratio[j] = (copyN_ratio[j] * copyN_produce[j] + newinvestgreen) / (
                                        copyN_produce[j] + newinvestgreen)
                            CNnewlist[turn, j] = Cnew
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                else:
                    if np.random.choice(nji) == 0:  ###Ng-Nh
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeNh) / K3))):
                            N_produce[j] = copyN_produce[j] + newinvesthot
                            N_ratio[j] = (1 - (((1 - copyN_ratio[j]) * copyN_produce[j] + newinvesthot) / (
                                        copyN_produce[j] + newinvesthot)))
                            CNnewlist[turn, j] = Cnew
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                    elif np.random.choice(nji) == 1:
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeNg) / K3))):
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                    elif np.random.choice(nji) == 2:  ###Ng-Yh
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeYh) / K3))):
                            N_produce[j] = copyN_produce[j] + newinvesthot
                            N_ratio[j] = (1 - (((1 - copyN_ratio[j]) * copyN_produce[j] + newinvesthot) / (
                                        copyN_produce[j] + newinvesthot)))
                            CNnewlist[turn, j] = Cnew
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
                    else:  ###Ng-Yg
                        if random.random() <= (1 / (1 + np.exp((jtypeU - jtypeYg) / K3))):
                            N_produce[j] = copyN_produce[j] + newinvestgreen
                            N_ratio[j] = (copyN_ratio[j] * copyN_produce[j] + newinvestgreen) / (
                                        copyN_produce[j] + newinvestgreen)
                            CNnewlist[turn, j] = Cnew
                        else:
                            N_produce[j] = copyN_produce[j]
                            N_ratio[j] = copyN_ratio[j]
            else:
                if len(nearinvestpointj)==0 and np.sum(Ytime_utility[investpointj[-1]:turn,j])>=Cnew:
                    jtypeU = np.mean(Ntime_utility[(turn - Bii):turn, j])
                    jYneighbor = np.where(YNfield[:,j] == 1)[0]
                    jNneighbor = np.where(NNfield[j] == 1)[0]
                    jtypeNh = np.mean(Ntime_utility[(turn - Bii):turn, jNneighbor[jNneighbor < Nhnum]])
                    jtypeNg = np.mean(Ntime_utility[(turn - Bii):turn, jNneighbor[jNneighbor >= Nhnum]])
                    jtypeYh = np.mean(Ytime_utility[(turn - Bii):turn, jYneighbor[jYneighbor < Yhnum]])
                    jtypeYg = np.mean(Ytime_utility[(turn - Bii):turn, jYneighbor[jYneighbor >= Yhnum]])
                    if j<Nhnum:
                        if np.random.choice(nji)==0:##Nh-Nh
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeNh)/K3))):
                                N_produce[j]=copyN_produce[j]
                                N_ratio[j]=copyN_ratio[j]
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                        elif np.random.choice(nji)==1:
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeNg)/K3))):
                                N_produce[j]=copyN_produce[j]+newinvestgreen
                                N_ratio[j]=(copyN_ratio[j]*copyN_produce[j]+newinvestgreen)/(copyN_produce[j]+newinvestgreen)
                                CNnewlist[turn, j] = Cnew
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                        elif np.random.choice(nji)==2:
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeYh)/K3))):
                                N_produce[j]=copyN_produce[j]+newinvestgreen
                                N_ratio[j]=(copyN_ratio[j]*copyN_produce[j]+newinvestgreen)/(copyN_produce[j]+newinvestgreen)
                                CNnewlist[turn, j] = Cnew
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                        else:
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeYg)/K3))):
                                N_produce[j]=copyN_produce[j]+newinvestgreen
                                N_ratio[j]=(copyN_ratio[j]*copyN_produce[j]+newinvestgreen)/(copyN_produce[j]+newinvestgreen)
                                CNnewlist[turn, j] = Cnew
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                    else:
                        if np.random.choice(nji)==0:###Ng-Nh
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeNh)/K3))):
                                N_produce[j]=copyN_produce[j]+newinvesthot
                                N_ratio[j]=(1-(((1-copyN_ratio[j])*copyN_produce[j]+newinvesthot)/(copyN_produce[j]+newinvesthot)))
                                CNnewlist[turn, j] = Cnew
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                        elif np.random.choice(nji)==1:
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeNg)/K3))):
                                N_produce[j]=copyN_produce[j]
                                N_ratio[j]=copyN_ratio[j]
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                        elif np.random.choice(nji)==2:###Ng-Yh
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeYh)/K3))):
                                N_produce[j]=copyN_produce[j]+newinvesthot
                                N_ratio[j]=(1-(((1-copyN_ratio[j])*copyN_produce[j]+newinvesthot)/(copyN_produce[j]+newinvesthot)))
                                CNnewlist[turn, j] = Cnew
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
                        else:###Ng-Yg
                            if random.random()<=(1/(1+np.exp((jtypeU-jtypeYg)/K3))):
                                N_produce[j]=copyN_produce[j]+newinvestgreen
                                N_ratio[j]=(copyN_ratio[j]*copyN_produce[j]+newinvestgreen)/(copyN_produce[j]+newinvestgreen)
                                CNnewlist[turn, j] = Cnew
                            else:
                                N_produce[j] = copyN_produce[j]
                                N_ratio[j] = copyN_ratio[j]
    ###策略更新完了，接下来是移动
    angle=np.random.uniform(-np.pi,np.pi,size=(Ynum,2))
    Yanglecos=np.multiply(np.cos(angle[:,0]),velocity)
    Yanglesin=np.multiply(np.sin(angle[:,0]),velocity)
    Nanglecos=np.multiply(np.cos(angle[:,1]),velocity)
    Nanglesin=np.multiply(np.sin(angle[:,1]),velocity)
    Yloc[:,0]=Yloc[:,0]+Yanglecos
    Yloc[:,1]=Yloc[:,1]+Yanglesin
    Nloc[:,0]=Nloc[:,0]+Nanglecos
    Nloc[:,1]=Nloc[:,1]+Nanglesin
    Yloc=boundary(Yloc)
    Nloc=boundary(Nloc)
    wao = np.array([-powerchange, powerchange])
    teste = ef(e, f, wao)[0]
    testf = ef(e, f, wao)[1]
    testsign = ef(e, f, wao)[2]
    testEY = teste * EEY
    testZN = testf * ZZN
    bhu = np.sum(RY) + np.sum(RN)  + np.sum(testZN)-np.sum(testEY)
    department_utility[turn] = bhu
    departmentsign[turn] = testsign
    Ee[turn] = e
    Ff[turn] = f
    Yg_strategy = Y_strategy[Ygnum:]
    Yh_strategy = Y_strategy[:Yhnum]
    Ng_strategy = N_strategy[Ngnum:]
    Nh_strategy = N_strategy[:Nhnum]
    if bb in XX:
        zheyi=department_utility[(bb-powerinterval):bb]
        zheyisign=departmentsign[(bb-powerinterval):bb]
        jiajia=np.where(zheyisign==1)[0]
        jiajian=np.where(zheyisign==2)[0]
        jianjia=np.where(zheyisign==3)[0]
        jianjian=np.where(zheyisign==4)[0]
        jiajiamean=np.mean(zheyi[jiajia])
        jiajianmean = np.mean(zheyi[jiajian])
        jianjiamean = np.mean(zheyi[jianjia])
        jianjianmean = np.mean(zheyi[jianjian])
        if jiajiamean==np.maximum(np.maximum(np.maximum(jiajiamean,jiajianmean),jianjiamean),jianjianmean):
            e=e+powerchange
            f=f+powerchange
        elif jiajianmean==np.maximum(np.maximum(np.maximum(jiajiamean,jiajianmean),jianjiamean),jianjianmean):
            e=e+powerchange
            f=f-powerchange
        elif jianjiamean==np.maximum(np.maximum(np.maximum(jiajiamean,jiajianmean),jianjiamean),jianjianmean):
            e=e-powerchange
            f=f+powerchange
        else:
            e=e-powerchange
            f=f-powerchange
    if bb2 in XX2:
        Ygloc=Yloc[Ygnum:,:]
        Yhloc = Yloc[:Yhnum, :]
        Ngloc = Nloc[Ngnum:, :]
        Nhloc = Nloc[:Nhnum, :]
        df0 = pd.DataFrame(Ygloc)
        df0.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业位置第'+str(bb2)+'轮.xlsx')
        df1 = pd.DataFrame(Yhloc)
        df1.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业位置第'+str(bb2)+'轮.xlsx')
        df2 = pd.DataFrame(Ngloc)
        df2.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业位置第'+str(bb2)+'轮.xlsx')
        df3 = pd.DataFrame(Nhloc)
        df3.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业位置第'+str(bb2)+'轮.xlsx')
        df4 = pd.DataFrame(Yg_strategy)
        df4.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业策略第'+str(bb2)+'轮.xlsx')
        df5 = pd.DataFrame(Yh_strategy)
        df5.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业策略第'+str(bb2)+'轮.xlsx')
        df6 = pd.DataFrame(Ng_strategy)
        df6.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业策略第'+str(bb2)+'轮.xlsx')
        df7 = pd.DataFrame(Nh_strategy)
        df7.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业策略第'+str(bb2)+'轮.xlsx')
    Ygdeal[turn] = np.sum(Yg_strategy)
    Yhdeal[turn] = np.sum(Yh_strategy)
    Ngdeal[turn] = np.sum(Ng_strategy)
    Nhdeal[turn] = np.sum(Nh_strategy)
Ygtime_utility =Ytime_utility[:,Ygnum:]
Yhtime_utility =Ytime_utility[:,:Yhnum]
Ngtime_utility = Ntime_utility[:,Ngnum:]
Nhtime_utility =Ntime_utility[:,:Nhnum]
CNgnewlist =CNnewlist[:,Ngnum:]
CNhnewlist = CNnewlist[:,:Nhnum]
CYgnewlist = CYnewlist[:,Ygnum:]
CYhnewlist = CYnewlist[:,:Yhnum]
df8 = pd.DataFrame(Ygdeal)
df8.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业交易人数.xlsx')
df9 = pd.DataFrame(Yhdeal)
df9.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业交易人数.xlsx')
df10 = pd.DataFrame(Ngdeal)
df10.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业交易人数.xlsx')
df11 = pd.DataFrame(Nhdeal)
df11.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业交易人数.xlsx')
df12 = pd.DataFrame(department_utility)
df12.to_excel('E:\\data\火电绿电\第三部分\监管部门效用.xlsx')
df13 = pd.DataFrame(Ee)
df13.to_excel('E:\\data\火电绿电\第三部分\监管部门奖励.xlsx')
df14 = pd.DataFrame(Ff)
df14.to_excel('E:\\data\火电绿电\第三部分\监管部门惩罚.xlsx')

df15 = pd.DataFrame(Ygtime_utility)
df15.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业收益.xlsx')
df16 = pd.DataFrame(Yhtime_utility)
df16.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业收益.xlsx')
df17 = pd.DataFrame(Ngtime_utility)
df17.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业收益.xlsx')
df18 = pd.DataFrame(Nhtime_utility)
df18.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业收益.xlsx')

df19 = pd.DataFrame(CYgnewlist)
df19.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业投资情况.xlsx')
df20 = pd.DataFrame(CYhnewlist)
df20.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业投资情况.xlsx')
df21 = pd.DataFrame(CNgnewlist)
df21.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业投资情况.xlsx')
df22 = pd.DataFrame(CNhnewlist)
df22.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业投资情况.xlsx')

df23 = pd.DataFrame(TimeYg_producegreen)
df23.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业生产绿电.xlsx')
df24 = pd.DataFrame(TimeYh_producegreen)
df24.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业生产绿电.xlsx')
df25 = pd.DataFrame(TimeNg_producegreen)
df25.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业生产绿电.xlsx')
df26 = pd.DataFrame(TimeNh_producegreen)
df26.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业生产绿电.xlsx')

df27 = pd.DataFrame(TimeYg_producehot)
df27.to_excel('E:\\data\火电绿电\第三部分\完成配额以可再生能源为主的电力企业生产火电.xlsx')
df28 = pd.DataFrame(TimeYh_producehot)
df28.to_excel('E:\\data\火电绿电\第三部分\完成配额以传统能源为主的电力企业生产火电.xlsx')
df29 = pd.DataFrame(TimeNg_producehot)
df29.to_excel('E:\\data\火电绿电\第三部分\未完成配额以可再生能源为主的电力企业生产火电.xlsx')
df30 = pd.DataFrame(TimeNh_producehot)
df30.to_excel('E:\\data\火电绿电\第三部分\未完成配额以传统能源为主的电力企业生产火电.xlsx')


#
