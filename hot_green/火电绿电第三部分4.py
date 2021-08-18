import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import random

# A=["1次","2次","3次","4次","5次"]#13
name="kaAka"
np.random.seed(0)
pehigh =1
pecanshu =250
Cgpg = 0.3
Cgph = 0.2
Chpg = 0.4
Chph = 0.1
Cdistance =0.5
Cpool =0.25
pg =1
ph =1
a = 0.5
W = 30
e =0.5
f =1
L = 5
r = 1
K = 2
K2 =2
C = 5
velocity = 1
powerchange = 0.01
Cnew = 1
newinvesthot =1
newinvestgreen =1
newinvest = 0

Total_rounds = 1050
powerinterval =10
photointerval = 25
Ygnum = 125
Ngnum = 125
Yhnum = 125
Nhnum = 125
Ynum = Ygnum + Yhnum
Nnum = Ngnum + Nhnum
number = Ynum + Nnum
Ynum_list = np.arange(Ynum)
Nnum_list = np.arange(Nnum)
number_list = np.arange(number)
Bii = 10  # 投资轮次

X = np.arange(0, Total_rounds)
XX = np.arange(powerinterval, Total_rounds, powerinterval)  # 监管力度变化
XX2 = np.arange(photointerval - 1, Total_rounds + photointerval - 1, photointerval)  # 瞬时快照
department_utility = np.zeros((1, len(X)))[0]
department_utilityjiajia = np.zeros((1, len(X)))[0]
department_utilityjiajian = np.zeros((1, len(X)))[0]
department_utilityjianjia = np.zeros((1, len(X)))[0]
department_utilityjianjian = np.zeros((1, len(X)))[0]
Ee = np.zeros((1, len(X)))[0]
Ff = np.zeros((1, len(X)))[0]
green_quota_upper = 0.5
green_quota = 0.35
green_quota_lower = 0.2
hot_quota_upper = 0.2
hot_quota = 0.1
hot_quota_lower = 0
quota = np.append(np.array([hot_quota] * Yhnum + [green_quota] * Ygnum),
                  np.array([hot_quota] * Nhnum + [green_quota] * Ngnum))
Yh_ratio = np.random.uniform(hot_quota, hot_quota_upper, size=(1, Yhnum))[0]
Yg_ratio = np.random.uniform(green_quota, green_quota_upper, size=(1, Ygnum))[0]
Nh_ratio = np.random.uniform(hot_quota_lower, hot_quota, size=(1, Nhnum))[0]
Ng_ratio = np.random.uniform(green_quota_lower, green_quota, size=(1, Ngnum))[0]
Yh_produce = np.random.uniform(100, 110, size=(1, Yhnum))[0]
Yg_produce = np.random.uniform(100, 110, size=(1, Ygnum))[0]
Nh_produce = np.random.uniform(100, 110, size=(1, Nhnum))[0]
Ng_produce = np.random.uniform(100, 110, size=(1, Ngnum))[0]
identity = np.array([0] * Yhnum + [1] * Ygnum + [2] * Nhnum + [3] * Ngnum)
produce = np.append(np.append(np.append(Yh_produce, Yg_produce), Nh_produce), Ng_produce)
ratio = np.append(np.append(np.append(Yh_ratio, Yg_ratio), Nh_ratio), Ng_ratio)
strategy = np.random.randint(0, 3, size=(1, number))[0]
loc = np.random.uniform(0, L, size=(number, 2))

def cost_gpg(x):
    c = Cgpg * x
    return c

def cost_gph(x):
    c = Cgph * x
    return c

def cost_hpg(x):
    c = Chpg * x
    return c

def cost_hph(x):
    c = Chph * x
    return c

def pe(x):
    f = (pehigh / (1 + np.exp((x) / pecanshu)))
    return f

def Cd(x):
    c = (x / r) * Cdistance
    return c

def Cp(x):
    if x <= 0:
        c = 0
    else:
        c = Cpool
    return c

def Cplist(x):
    x[x <= 0] = 0
    x[x > 0] = Cpool
    return x

def plane(x):
    up = copy.copy(x)
    up[:, 1] = np.add(x[:, 1], L)
    upright = np.add(x, L)
    upleft = copy.copy(x)
    upleft[:, 1] = np.add(x[:, 1], L)
    upleft[:, 0] = np.subtract(x[:, 0], L)
    down = copy.copy(x)
    down[:, 1] = np.subtract(x[:, 1], L)
    downleft = np.subtract(x, L)
    downright = copy.copy(x)
    downright[:, 1] = np.subtract(x[:, 1], L)
    downright[:, 0] = np.add(x[:, 0], L)
    right = copy.copy(x)
    right[:, 0] = np.add(x[:, 0], L)
    left = copy.copy(x)
    left[:, 0] = np.subtract(x[:, 0], L)
    xiao8 = [x, up, down, left, right, upright, upleft, downright, downleft]
    return xiao8

def boundary(x):
    x[x > 10] = x[x > 10] - 10
    x[x < 0] = x[x < 0] + 10
    return x

def distance(g, x, y):
    mindled = np.linalg.norm((g[0][x] - y), axis=1)
    up = np.linalg.norm((g[1][x] - y), axis=1)
    down = np.linalg.norm((g[2][x] - y), axis=1)
    left = np.linalg.norm((g[3][x] - y), axis=1)
    right = np.linalg.norm((g[4][x] - y), axis=1)
    upright = np.linalg.norm((g[5][x] - y), axis=1)
    upleft = np.linalg.norm((g[6][x] - y), axis=1)
    downright = np.linalg.norm((g[7][x] - y), axis=1)
    downleft = np.linalg.norm((g[8][x] - y), axis=1)
    f = np.minimum(np.minimum(np.minimum(
        np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(mindled, up), down), left), right), upright),
        upleft), downright), downleft)
    return f

def pairlist(x, sellnum, buynum):
    linshi = copy.copy(x)
    num0 = len(sellnum)
    num1 = len(buynum)
    pair = np.zeros((np.minimum(num0, num1), 2))
    unfold = np.arange(num0 * num1)
    fold = unfold.reshape(num0, num1)
    for i in range(np.minimum(num0, num1)):
        try:
            reshap_p = linshi.reshape(1, num0 * num1)[0]
            Want_delete = np.random.choice(unfold, p=reshap_p)
            rowdelete = np.where(fold == Want_delete)[0][0]  # Y的编号
            columndelete = np.where(fold == Want_delete)[1][0]  # N的编号
            rowdelete0 = sellnum[rowdelete]
            columndelete0 = buynum[columndelete]
            pair0 = np.array([rowdelete0, columndelete0])
            pair[i] = pair0
            linshi[rowdelete, :] = 0
            linshi[:, columndelete] = 0
            linshi = linshi / (np.sum(linshi))
        except:
            pair[i] = np.array([99999, 99999])
    return pair

def field(x):
    cc = copy.copy(x)
    cc[cc == 0] = r * 100000
    cc[cc <= r] = 1
    cc[cc > r] = 0
    return cc

def greenbook(x, sellnum, buynum):
    inpool = np.zeros((1, number))[0]
    outpool = np.zeros((1, number))[0]
    dog0 = copy.copy(sellnum)
    dog1 = copy.copy(buynum)
    bian0=np.arange(number)
    bian1=np.arange(number)
    for i in range(len(dog1)):
        bian0=np.delete(bian0,np.where(bian0==dog1[i])[0])
    for i in range(len(dog0)):
        bian1=np.delete(bian1,np.where(bian1==dog0[i])[0])
    # print(bian0,bian1)
    for i in range(len(x[:, 0])):
        jiu = x[i]
        jiu0 = int(jiu[0])
        jiu1 = int(jiu[1])
        if jiu0 != 99999:
            bian0=np.delete(bian0, np.where(bian0 == jiu0)[0])
            # print(dog0)
            bian1=np.delete(bian1, np.where(bian1 == jiu1)[0])
            xiu = strategy[jiu0] * 10 + strategy[jiu1]
            if xiu == 0:
                inpool[jiu0] = (np.maximum(
                    (produce[jiu0] * (ratio[jiu0] - quota[jiu0]) - produce[jiu1] * (quota[jiu1] - ratio[jiu1])),
                    0))
                outpool[jiu1] = (np.maximum(
                    (produce[jiu1] * (quota[jiu1] - ratio[jiu1]) - produce[jiu0] * (ratio[jiu0] - quota[jiu0])),
                    0))
            elif xiu in [1, 10, 11, 20, 21]:
                inpool[jiu0] = (produce[jiu0] * (ratio[jiu0] - quota[jiu0]))
                outpool[jiu1] = (produce[jiu1] * (quota[jiu1] - ratio[jiu1]))
            else:
                inpool[jiu0] = 0
                outpool[jiu1] = 0
    for j in bian0:
        if strategy[j] == 2:
            inpool[j] = 0
        else:
            inpool[j] = (produce[j] * (ratio[j] - quota[j]))
    for jj in bian1:
        if strategy[jj] == 2:
            outpool[jj] = 0
        else:
            outpool[jj] = (produce[jj] * (quota[jj] - ratio[jj]))
    poolsd = np.sum(inpool) - np.sum(outpool)
    return np.sum(inpool), np.sum(outpool), poolsd

def change(x):
    if x >= green_quota and x <= green_quota_upper:
        qw = green_quota
        qe = 1
    elif x < green_quota and x >= green_quota_lower:
        qw = green_quota
        qe = 3
    elif x >= hot_quota and x <= hot_quota_upper:
        qw = hot_quota
        qe = 0
    else:
        qw = hot_quota
        qe = 2
    return qw, qe

# Luna(i,choicennji,typematrix,copy_produce,copy_ratio,copy_quota,copy_identity)
def Luna(w0, w1, w2, w3, w4, w5, w6):
    if w2[w6[w0], w1] == 2:
        u0 = w3[w0] + newinvesthot
        u1 = (1 - (((1 - w4[w0]) * w3[w0] + newinvesthot) / (w3[w0] + newinvesthot)))
        u2 = 2
        u3 = change(ratio[w0])[0]
        u4 = change(ratio[w0])[1]
    elif w2[w6[w0], w1] == 1:
        u0 = w3[w0] + newinvestgreen
        u1 = (w4[w0] * w3[w0] + newinvestgreen) / (w3[w0] + newinvestgreen)
        u2 = 1
        u3 = change(ratio[w0])[0]
        u4 = change(ratio[w0])[1]
    else:
        u0 = w3[w0]
        u1 = w4[w0]
        u2 = 0
        u3 = w5[w0]
        u4 = w6[w0]
    return u0, u1, u2, u3, u4

typematrix = np.matrix([[0, 1, 2, 2], [2, 0, 2, 2], [1, 1, 0, 1], [1, 1, 2, 0]])
Ygdealtoneighbor = np.zeros((len(X), 1))
Ygdealtopool = np.zeros((len(X), 1))
Ygnotdeal = np.zeros((len(X), 1))
Yhdealtoneighbor = np.zeros((len(X), 1))
Yhdealtopool = np.zeros((len(X), 1))
Yhnotdeal = np.zeros((len(X), 1))
Ngdealtoneighbor = np.zeros((len(X), 1))
Ngdealtopool = np.zeros((len(X), 1))
Ngnotdeal = np.zeros((len(X), 1))
Nhdealtoneighbor = np.zeros((len(X), 1))
Nhdealtopool = np.zeros((len(X), 1))
Nhnotdeal = np.zeros((len(X), 1))
dealtoneighbor = np.zeros((len(X), 1))
dealtopool = np.zeros((len(X), 1))
notdeal = np.zeros((len(X), 1))
typeYh = np.zeros((len(X), 1))
typeYg = np.zeros((len(X), 1))
typeNh = np.zeros((len(X), 1))
typeNg = np.zeros((len(X), 1))
timeproduce = np.zeros((len(X), 1))
timegreenproduce = np.zeros((len(X), 1))
noinvesttime = np.zeros((len(X), 1))
greeninvesttime = np.zeros((len(X), 1))
hotinvesttime = np.zeros((len(X), 1))
time_utility = np.zeros((len(X), number))
Cnewlist = np.zeros((len(X), number))
greeninpool = np.zeros((len(X), 1))
greenprice = np.zeros((len(X), 1))
greenoutpool = np.zeros((len(X), 1))
Beforced = np.zeros((len(X), 1))
BeforcedY = np.zeros((len(X), 1))
BeforcedN = np.zeros((len(X), 1))
RY = a * ratio * produce
for turn in X:
    print(turn)
    bb = turn
    bb2 = turn
    EEZZ = (ratio - quota) * produce
    EEZZ[EEZZ < 0] = EEZZ[EEZZ < 0] * f
    EEZZ[EEZZ >= 0] = EEZZ[EEZZ >= 0] * e
    distancematrix = np.zeros((number, number))
    sellfirm = np.append(np.where(identity == 0)[0], np.where(identity == 1)[0])
    buyfirm = np.append(np.where(identity == 2)[0], np.where(identity == 3)[0])
    # print(len(sellfirm),len(buyfirm))
    for i in range(number):
        distancematrix[i] = distance(plane(loc), i, loc)
    totalfield = field(distancematrix)
    distancematrix_inverse = (1. / distancematrix)
    distancematrix_inverse[np.isinf(distancematrix_inverse)] = 0
    linshimatrix = distancematrix_inverse * totalfield
    linshimatrix0 = linshimatrix[sellfirm, :]
    linshimatrix1 = linshimatrix0[:, buyfirm]
    probmatrix = (linshimatrix1) / (np.sum((linshimatrix1)))
    totalpairlist = pairlist(probmatrix, sellfirm, buyfirm)
    # print(totalpairlist)
    green = greenbook(totalpairlist, sellfirm, buyfirm)
    # print(green)
    greeninpool[turn] = green[0]
    greenoutpool[turn] = green[1]
    price = pe(green[2])
    greenprice[turn] = price
    utility = np.zeros((1, number))[0]
    fgnb = copy.copy(number_list)
    beforced = np.zeros((1, number))[0]
    # print(green)
    # print(price)
    for i in range(len(totalpairlist[:, 0])):
        bjiu = totalpairlist[i]
        bjiu0 = int(bjiu[0])
        bjiu1 = int(bjiu[1])
        if bjiu0 != 99999:
            fgnb = np.delete(fgnb, np.where(fgnb == bjiu0)[0])
            fgnb = np.delete(fgnb, np.where(fgnb == bjiu1)[0])
            if identity[bjiu0] == 0:
                cost0 = cost_hpg(produce[bjiu0] * quota[bjiu0])
                cost00 = cost_hpg(produce[bjiu0] * ratio[bjiu0])
                cost1 = cost_hph(produce[bjiu0] * (1 - ratio[bjiu0]))
            else:
                cost0 = cost_gpg(produce[bjiu0] * quota[bjiu0])
                cost00 = cost_gpg(produce[bjiu0] * ratio[bjiu0])
                cost1 = cost_gph(produce[bjiu0] * (1 - ratio[bjiu0]))
            if identity[bjiu1] == 2:
                cost2 = cost_hpg(produce[bjiu1] * ratio[bjiu1])
                cost3 = cost_hph(produce[bjiu1] * (1 - ratio[bjiu1]))
            else:
                cost2 = cost_gpg(produce[bjiu1] * ratio[bjiu1])
                cost3 = cost_gph(produce[bjiu1] * (1 - ratio[bjiu1]))
            Sven = strategy[bjiu0] * 10 + strategy[bjiu1]
            # print("AA",pg*produce[bjiu0]*quota[bjiu0],price*produce[bjiu0]*(ratio[bjiu0]-quota[bjiu0]),-cost0,ph*produce[bjiu0]*(1-ratio[bjiu0]),-cost1,-Cd(distancematrix[bjiu0,bjiu1])/2,-Cp((produce[bjiu0]*(ratio[bjiu0]-quota[bjiu0])-produce[bjiu1]*(quota[bjiu1]-ratio[bjiu1]))),EEZZ[bjiu0])
            # print("BB",pg*produce[bjiu1]*ratio[bjiu1],-price*produce[bjiu1]*(quota[bjiu1]-ratio[bjiu1]),-cost2,ph*produce[bjiu1]*(1-ratio[bjiu1]),-cost3,-Cd(distancematrix[bjiu0,bjiu1])/2,-Cp((produce[bjiu1]*(quota[bjiu1]-ratio[bjiu1])-produce[bjiu0]*(ratio[bjiu0]-quota[bjiu0]))),EEZZ[bjiu1])
            if Sven == 0:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + (price + pg) * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 - Cd(
                    distancematrix[bjiu0, bjiu1]) / 2 - Cp((produce[bjiu0] * (ratio[bjiu0] - quota[bjiu0]) -
                                                            produce[bjiu1] * (quota[bjiu1] - ratio[bjiu1])))
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - price * produce[bjiu1] * (
                            quota[bjiu1] - ratio[bjiu1]) - cost2 + ph * produce[bjiu1] * (
                                             1 - ratio[bjiu1]) - cost3 - Cd(
                    distancematrix[bjiu0, bjiu1]) / 2 - Cp((produce[bjiu1] * (quota[bjiu1] - ratio[bjiu1]) -
                                                            produce[bjiu0] * (ratio[bjiu0] - quota[bjiu0])))
            elif Sven == 1:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + (price + pg) * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 - Cp(
                    (produce[bjiu0] * (ratio[bjiu0] - quota[bjiu0])))
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - price * produce[bjiu1] * (
                            quota[bjiu1] - ratio[bjiu1]) - cost2 + ph * produce[bjiu1] * (
                                             1 - ratio[bjiu1]) - cost3 - Cd(distancematrix[bjiu0, bjiu1]) - Cp(
                    (produce[bjiu1] * (quota[bjiu1] - ratio[bjiu1])))
            elif Sven == 10:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + (price + pg) * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 - Cd(distancematrix[bjiu0, bjiu1]) - Cp(
                    (produce[bjiu0] * (ratio[bjiu0] - quota[bjiu0])))
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - price * produce[bjiu1] * (
                            quota[bjiu1] - ratio[bjiu1]) - cost2 + ph * produce[bjiu1] * (
                                             1 - ratio[bjiu1]) - cost3 - Cp(
                    (produce[bjiu1] * (quota[bjiu1] - ratio[bjiu1])))
            elif Sven == 11:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + (price + pg) * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 - Cp(
                    (produce[bjiu0] * (ratio[bjiu0] - quota[bjiu0])))
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - price * produce[bjiu1] * (
                            quota[bjiu1] - ratio[bjiu1]) - cost2 + ph * produce[bjiu1] * (
                                             1 - ratio[bjiu1]) - cost3 - Cp(
                    (produce[bjiu1] * (quota[bjiu1] - ratio[bjiu1])))
            elif Sven == 20 or Sven == 21:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + (price + pg) * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 - Cp(
                    (produce[bjiu0] * (ratio[bjiu0] - quota[bjiu0])))
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - cost2 + ph * produce[bjiu1] * (
                            1 - ratio[bjiu1]) - cost3 + EEZZ[bjiu1]
                beforced[bjiu0] = 1
            elif Sven == 2 or Sven == 12:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + pg * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 - cost00 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 + EEZZ[bjiu0]
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - price * produce[bjiu1] * (
                            quota[bjiu1] - ratio[bjiu1]) - cost2 + ph * produce[bjiu1] * (
                                             1 - ratio[bjiu1]) - cost3 - Cp(
                    (produce[bjiu1] * (quota[bjiu1] - ratio[bjiu1])))
                beforced[bjiu1] = 1
            else:
                utility[bjiu0] = pg * produce[bjiu0] * quota[bjiu0] + pg * produce[bjiu0] * (
                            ratio[bjiu0] - quota[bjiu0]) - cost0 - cost00 + ph * produce[bjiu0] * (
                                             1 - ratio[bjiu0]) - cost1 + EEZZ[bjiu0]
                utility[bjiu1] = pg * produce[bjiu1] * ratio[bjiu1] - cost2 + ph * produce[bjiu1] * (
                            1 - ratio[bjiu1]) - cost3 - EEZZ[bjiu1]
    for COCO in fgnb:
        if identity[COCO] == 0:
            COCOcost0 = cost_hpg(produce[COCO] * quota[COCO])
            COCOcost00 = cost_hpg(produce[COCO] * ratio[COCO])
            COCOcost1 = cost_hph(produce[COCO] * (1 - ratio[COCO]))
            if strategy[COCO] == 2:
                utility[COCO] = pg * produce[COCO] * quota[COCO] + pg * produce[COCO] * (
                            ratio[COCO] - quota[COCO]) - COCOcost0 - COCOcost00 + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost1 + EEZZ[COCO]
            elif strategy[COCO] == 1:
                utility[COCO] = pg * produce[COCO] * quota[COCO] + (price + pg) * produce[COCO] * (
                            ratio[COCO] - quota[COCO]) + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost1 - Cp(
                    (produce[COCO] * (ratio[COCO] - quota[COCO])))
            else:
                utility[COCO] = pg * produce[COCO] * quota[COCO] + (price + pg) * produce[COCO] * (
                            ratio[COCO] - quota[COCO]) + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost1 - Cp(
                    (produce[COCO] * (ratio[COCO] - quota[COCO])))
                beforced[COCO] = 1
        elif identity[COCO] == 1:
            COCOcost0g = cost_gpg(produce[COCO] * quota[COCO])
            COCOcost00g = cost_gpg(produce[COCO] * ratio[COCO])
            COCOcost1g = cost_gph(produce[COCO] * (1 - ratio[COCO]))
            if strategy[COCO] == 2:
                utility[COCO] = pg * produce[COCO] * quota[COCO] + pg * produce[COCO] * (
                            ratio[COCO] - quota[COCO]) - COCOcost0g - COCOcost00g + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost1g + EEZZ[COCO]
            elif strategy[COCO] == 1:
                utility[COCO] = pg * produce[COCO] * quota[COCO] + (price + pg) * produce[COCO] * (
                            ratio[COCO] - quota[COCO]) + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost1g - Cp(
                    (produce[COCO] * (ratio[COCO] - quota[COCO])))
            else:
                utility[COCO] = pg * produce[COCO] * quota[COCO] + (price + pg) * produce[COCO] * (
                            ratio[COCO] - quota[COCO]) + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost1g - Cp(
                    (produce[COCO] * (ratio[COCO] - quota[COCO])))
                beforced[COCO] = 1
        elif identity[COCO] == 2:
            COCOcost2 = cost_hpg(produce[COCO] * ratio[COCO])
            COCOcost3 = cost_hph(produce[COCO] * (1 - ratio[COCO]))
            if strategy[COCO] == 2:
                utility[COCO] = pg * produce[COCO] * ratio[COCO] - COCOcost2 + ph * produce[COCO] * (
                            1 - ratio[COCO]) - COCOcost3 - EEZZ[COCO]
            elif strategy[COCO] == 1:
                utility[COCO] = pg * produce[COCO] * ratio[COCO] - price * produce[COCO] * (
                            quota[COCO] - ratio[COCO]) - COCOcost2 + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost3 - Cp(
                    (produce[COCO] * (quota[COCO] - ratio[COCO])))
            else:
                utility[COCO] = pg * produce[COCO] * ratio[COCO] - price * produce[COCO] * (
                            quota[COCO] - ratio[COCO]) - COCOcost2 + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost3 - Cp(
                    (produce[COCO] * (quota[COCO] - ratio[COCO])))
                beforced[COCO] = 1
        else:
            COCOcost2g = cost_gpg(produce[COCO] * ratio[COCO])
            COCOcost3g = cost_gph(produce[COCO] * (1 - ratio[COCO]))
            if strategy[COCO] == 2:
                utility[COCO] = pg * produce[COCO] * ratio[COCO] - COCOcost2g + ph * produce[COCO] * (
                            1 - ratio[COCO]) - COCOcost3g - EEZZ[COCO]
            elif strategy[COCO] == 1:
                utility[COCO] = pg * produce[COCO] * ratio[COCO] - price * produce[COCO] * (
                            quota[COCO] - ratio[COCO]) - COCOcost2g + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost3g - Cp(
                    (produce[COCO] * (quota[COCO] - ratio[COCO])))
            else:
                utility[COCO] = pg * produce[COCO] * ratio[COCO] - price * produce[COCO] * (
                            quota[COCO] - ratio[COCO]) - COCOcost2g + ph * produce[COCO] * (
                                            1 - ratio[COCO]) - COCOcost3g - Cp(
                    (produce[COCO] * (quota[COCO] - ratio[COCO])))
                beforced[COCO] = 1
    # print(utility)
    Beforced[turn] = np.sum(beforced)
    fade0 = np.sum(beforced[np.where(identity == 0)[0]])
    fade1 = np.sum(beforced[np.where(identity == 1)[0]])
    fade2 = np.sum(beforced[np.where(identity == 2)[0]])
    fade3 = np.sum(beforced[np.where(identity == 3)[0]])
    BeforcedY[turn] = fade0 + fade1
    BeforcedN[turn] = fade2 + fade3
    copy_strategy = copy.copy(strategy)
    conectmatrix = copy.copy(linshimatrix)
    for axe in sellfirm:
        conectmatrix[buyfirm, axe] = 0
    for axe2 in buyfirm:
        conectmatrix[sellfirm, axe2] = 0
    for i in range(number):
        cjiu = conectmatrix[i]
        if np.all(cjiu == 0) == False:
            cjiu_p = cjiu / np.sum(cjiu)
            ineighbor = np.random.choice(number_list, p=cjiu_p)
            # print(utility[i]-utility[ineighbor])
            if random.random() <= (1 / (1 + np.exp((utility[i] - utility[ineighbor]) / K))):
                strategy[i] = copy_strategy[ineighbor]
            else:
                strategy[i] = copy_strategy[i]
        else:
            strategy[i] = copy_strategy[i]

    time_utility[turn] = utility
    copy_produce = copy.copy(produce)
    copy_ratio = copy.copy(ratio)
    copy_quota = copy.copy(quota)
    copy_identity = copy.copy(identity)

    if turn >= Bii:
        nji = np.arange(4)
        for i in range(number):
            choicennji = np.random.choice(nji)
            investpoint = np.where(Cnewlist[:turn, i] != 0)[0]
            nearinvestpoint = np.where(Cnewlist[(turn - Bii):turn, i] != 0)[0]
            if len(investpoint) == 0 or (
                    len(nearinvestpoint) == 0 and np.sum(time_utility[investpoint[-1]:turn, i]) >= Cnew):
                itypeU = np.mean(time_utility[(turn - Bii):turn, i])
                inotneighbor = totalfield[i]
                ineighbor = inotneighbor * (identity + 1)

                itypeNh = np.mean(time_utility[(turn - Bii):turn, np.where(ineighbor == 3)[0]])
                itypeNg = np.mean(time_utility[(turn - Bii):turn, np.where(ineighbor == 4)[0]])
                itypeYh = np.mean(time_utility[(turn - Bii):turn, np.where(ineighbor == 1)[0]])
                itypeYg = np.mean(time_utility[(turn - Bii):turn, np.where(ineighbor == 2)[0]])
                itype = [itypeYh, itypeYg, itypeNh, itypeNg]
                # print(itype,"ddd",itypeU)
                SAG = Luna(i, choicennji, typematrix, copy_produce, copy_ratio, copy_quota,
                           copy_identity)
                ydui = itypeU - itype[choicennji]
                if str(ydui) == "nan":
                    ydui1 = 0
                else:
                    ydui1 = ydui
                if random.random() <= (1 / (1 + np.exp((ydui1) / K))):
                    produce[i] = SAG[0]
                    ratio[i] = SAG[1]
                    Cnewlist[turn, i] = SAG[2]
                    quota[i] =change(ratio[i])[0]
                    identity[i] =change(ratio[i])[1]
                else:
                    produce[i] = copy_produce[i]
                    ratio[i] = copy_ratio[i]
                    Cnewlist[turn, i] = 0
                    quota[i] = copy_quota[i]
                    identity[i] = copy_identity[i]
            else:
                produce[i] = copy_produce[i]
                ratio[i] = copy_ratio[i]
                Cnewlist[turn, i] = 0
                quota[i] = copy_quota[i]
                identity[i] = copy_identity[i]

        ###策略更新完了，接下来是移动
    angle = np.random.uniform(-np.pi, np.pi, size=(1, number))[0]
    anglecos = np.multiply(np.cos(angle), velocity)
    anglesin = np.multiply(np.sin(angle), velocity)
    loc[:, 0] = loc[:, 0] + anglecos
    loc[:, 1] = loc[:, 1] + anglesin
    loc = boundary(loc)

    POMjiajia = copy.copy(EEZZ)
    POMjiajia[POMjiajia < 0] = POMjiajia[POMjiajia < 0] * (f + powerchange)
    POMjiajia[POMjiajia > 0] = POMjiajia[POMjiajia > 0] * (e + powerchange)
    POMjiajian = copy.copy(EEZZ)
    POMjiajian[POMjiajian < 0] = POMjiajian[POMjiajian < 0] * (f + powerchange)
    POMjiajian[POMjiajian > 0] = POMjiajian[POMjiajian > 0] * (e - powerchange)
    POMjianjia = copy.copy(EEZZ)
    POMjianjia[POMjianjia < 0] = POMjianjia[POMjianjia < 0] * (f - powerchange)
    POMjianjia[POMjianjia > 0] = POMjianjia[POMjianjia > 0] * (e + powerchange)
    POMjianjian = copy.copy(EEZZ)
    POMjianjian[POMjianjian < 0] = POMjianjian[POMjianjian < 0] * (f - powerchange)
    POMjianjian[POMjianjian > 0] = POMjianjian[POMjianjian > 0] * (e - powerchange)
    bhujiajia = np.sum(RY) + np.sum(POMjiajia)
    bhujiajian = np.sum(RY) + np.sum(POMjiajian)
    bhujianjia = np.sum(RY) + np.sum(POMjianjia)
    bhujianjian = np.sum(RY) + np.sum(POMjianjian)
    bhu = (bhujiajia + bhujiajian + bhujianjia + bhujianjian) / 4
    department_utility[turn] = bhu
    department_utilityjiajia[turn] = bhujiajia
    department_utilityjiajian[turn] = bhujiajian
    department_utilityjianjia[turn] = bhujianjia
    department_utilityjianjian[turn] = bhujianjian
    Ee[turn] = e
    Ff[turn] = f

    if bb in XX:
        jiajiamean = np.mean(department_utilityjiajia[(bb - powerinterval):bb])
        jiajianmean = np.mean(department_utilityjiajian[(bb - powerinterval):bb])
        jianjiamean = np.mean(department_utilityjianjia[(bb - powerinterval):bb])
        jianjianmean = np.mean(department_utilityjianjian[(bb - powerinterval):bb])
        if jiajiamean == jiajianmean and jiajianmean == jianjiamean and jianjiamean == jianjianmean:
            e = e
            f = f
        else:
            if jiajiamean == np.maximum(np.maximum(np.maximum(jiajiamean, jiajianmean), jianjiamean), jianjianmean):
                e = np.maximum(0, e + powerchange)
                f = f + powerchange
            elif jiajianmean == np.maximum(np.maximum(np.maximum(jiajiamean, jiajianmean), jianjiamean),
                                           jianjianmean):
                e = np.maximum(0, e - powerchange)
                f = np.maximum(0, f + powerchange)
            elif jianjiamean == np.maximum(np.maximum(np.maximum(jiajiamean, jiajianmean), jianjiamean),
                                           jianjianmean):
                e = np.maximum(0, e + powerchange)
                f = f - powerchange
            else:
                e = np.maximum(0, e - powerchange)
                f = np.maximum(0, f - powerchange)
    if bb2 in XX2:
        df0 = pd.DataFrame(loc)
        df0.to_excel('E:\\data\火电绿电\第三部分\电力企业位置第' + str(bb2) + '轮.xlsx')
        df1 = pd.DataFrame(strategy)
        df1.to_excel('E:\\data\火电绿电\第三部分\电力企业策略第' + str(bb2) + '轮.xlsx')
        df2 = pd.DataFrame(identity)
        df2.to_excel('E:\\data\火电绿电\第三部分\电力企业类型第' + str(bb2) + '轮.xlsx')
    dealtoneighbor[turn] = len(np.where(strategy == 0)[0])
    dealtopool[turn] = len(np.where(strategy == 1)[0])
    notdeal[turn] = len(np.where(strategy == 2)[0])
    Yhstrategy = strategy[np.where(identity == 0)[0]]
    Ygstrategy = strategy[np.where(identity == 1)[0]]
    Nhstrategy = strategy[np.where(identity == 2)[0]]
    Ngstrategy = strategy[np.where(identity == 3)[0]]
    Yhdealtoneighbor[turn] = len(np.where(Yhstrategy == 0)[0])
    Yhdealtopool[turn] = len(np.where(Yhstrategy == 1)[0])
    Yhnotdeal[turn] = len(np.where(Yhstrategy == 2)[0])
    Ygdealtoneighbor[turn] = len(np.where(Ygstrategy == 0)[0])
    Ygdealtopool[turn] = len(np.where(Ygstrategy == 1)[0])
    Ygnotdeal[turn] = len(np.where(Ygstrategy == 2)[0])
    Nhdealtoneighbor[turn] = len(np.where(Nhstrategy == 0)[0])
    Nhdealtopool[turn] = len(np.where(Nhstrategy == 1)[0])
    Nhnotdeal[turn] = len(np.where(Nhstrategy == 2)[0])
    Ngdealtoneighbor[turn] = len(np.where(Ngstrategy == 0)[0])
    Ngdealtopool[turn] = len(np.where(Ngstrategy == 1)[0])
    Ngnotdeal[turn] = len(np.where(Ngstrategy == 2)[0])
    typeYh[turn] = len(np.where(identity == 0)[0])
    typeYg[turn] = len(np.where(identity == 1)[0])
    typeNh[turn] = len(np.where(identity == 2)[0])
    typeNg[turn] = len(np.where(identity == 3)[0])
    timeproduce[turn] = np.sum(produce)
    timegreenproduce[turn] = np.sum(produce * ratio)
    noinvesttime[turn] = len(np.where(Cnewlist[turn] == 0)[0])
    greeninvesttime[turn] = len(np.where(Cnewlist[turn] == 1)[0])
    hotinvesttime[turn] = len(np.where(Cnewlist[turn] == 2)[0])

df3 = pd.DataFrame(dealtoneighbor)
df3.to_excel('E:\\data\火电绿电2\第三部分\与邻居交易的人数'+name+'.xlsx')
df4 = pd.DataFrame(dealtopool)
df4.to_excel('E:\\data\火电绿电2\第三部分\与pool交易的人数'+name+'.xlsx')
df5 = pd.DataFrame(notdeal)
df5.to_excel('E:\\data\火电绿电2\第三部分\不交易人数'+name+'.xlsx')

df6 = pd.DataFrame(Ygdealtoneighbor)
df6.to_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx')
df7 = pd.DataFrame(Ygdealtopool)
df7.to_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx')
df8 = pd.DataFrame(Ygnotdeal)
df8.to_excel('E:\\data\火电绿电2\第三部分\完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx')
df9 = pd.DataFrame(Yhdealtoneighbor)
df9.to_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx')
df10 = pd.DataFrame(Yhdealtopool)
df10.to_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx')
df11 = pd.DataFrame(Yhnotdeal)
df11.to_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx')
df12 = pd.DataFrame(Ngdealtoneighbor)
df12.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与邻居交易人数'+name+'.xlsx')
df13 = pd.DataFrame(Ngdealtopool)
df13.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业与pool交易人数'+name+'.xlsx')
df14 = pd.DataFrame(Ngnotdeal)
df14.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以可再生能源为主的电力企业不交易人数'+name+'.xlsx')
df15 = pd.DataFrame(Nhdealtoneighbor)
df15.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与邻居交易人数'+name+'.xlsx')
df16 = pd.DataFrame(Nhdealtopool)
df16.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业与pool交易人数'+name+'.xlsx')
df17 = pd.DataFrame(Nhnotdeal)
df17.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的电力企业不交易人数'+name+'.xlsx')
df18 = pd.DataFrame(typeYh)
df18.to_excel('E:\\data\火电绿电2\第三部分\完成配额以传统能源为主的企业数量'+name+'.xlsx')
df19 = pd.DataFrame(typeYg)
df19.to_excel('E:\\data\火电绿电2\第三部分\完成配额以清洁能源为主的企业数量'+name+'.xlsx')
df20 = pd.DataFrame(typeNh)
df20.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以传统能源为主的企业数量'+name+'.xlsx')
df21 = pd.DataFrame(typeNg)
df21.to_excel('E:\\data\火电绿电2\第三部分\未完成配额以清洁能源为主的企业数量'+name+'.xlsx')

df22 = pd.DataFrame(timeproduce)
df22.to_excel('E:\\data\火电绿电2\第三部分\电力产量'+name+'.xlsx')
df23 = pd.DataFrame(timegreenproduce)
df23.to_excel('E:\\data\火电绿电2\第三部分\绿电量'+name+'.xlsx')
df24 = pd.DataFrame(noinvesttime)
df24.to_excel('E:\\data\火电绿电2\第三部分\不投资人数'+name+'.xlsx')
df25 = pd.DataFrame(greeninvesttime)
df25.to_excel('E:\\data\火电绿电2\第三部分\投资绿电人数'+name+'.xlsx')
df26 = pd.DataFrame(hotinvesttime)
df26.to_excel('E:\\data\火电绿电2\第三部分\投资火电人数'+name+'.xlsx')
df27 = pd.DataFrame(department_utility)
df27.to_excel('E:\\data\火电绿电2\第三部分\监管部门效用'+name+'.xlsx')
df28 = pd.DataFrame(Ee)
df28.to_excel('E:\\data\火电绿电2\第三部分\监管部门奖励'+name+'.xlsx')
df29 = pd.DataFrame(Ff)
df29.to_excel('E:\\data\火电绿电2\第三部分\监管部门惩罚'+name+'.xlsx')
df30 = pd.DataFrame(Beforced)
df30.to_excel('E:\\data\火电绿电2\第三部分\被迫进入pool'+name+'.xlsx')
df31 = pd.DataFrame(BeforcedY)
df31.to_excel('E:\\data\火电绿电2\第三部分\完成配额被迫进入pool'+name+'.xlsx')
df32 = pd.DataFrame(BeforcedN)
df32.to_excel('E:\\data\火电绿电2\第三部分\未完成配额被迫进入pool'+name+'.xlsx')
df33 = pd.DataFrame(greeninpool)
df33.to_excel('E:\\data\火电绿电2\第三部分\绿证数量供给'+name+'.xlsx')
df34 = pd.DataFrame(greenprice)
df34.to_excel('E:\\data\火电绿电2\第三部分\绿证价格'+name+'.xlsx')
df35 = pd.DataFrame(greenoutpool)
df35.to_excel('E:\\data\火电绿电2\第三部分\绿证数量需求'+name+'.xlsx')

