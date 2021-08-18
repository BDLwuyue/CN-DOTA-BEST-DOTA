import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import random
import time
# A=["1次","2次","3次","4次","5次"]
# B=[", ${C_p}$=2",", ${C_d}$=2",", ${C_p}$=0",", ${C_d}$=0",", e=0",", e=2",", ${p_g}$=0",", ${p_g}$=2",", ${p_e}$=0",", ${p_g}$=2"]
# print(len(A))
A=["大0次","大1次","大2次","大3次","大4次","大5次","大6次","大7次","大8次","大9次"]
for ti in range(len(A)):
    name=A[ti]
    np.random.seed(0)
    pehigh =0.5
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
    f = 1
    L = 5
    r = 1
    K = 2
    K2 = 2
    C = 5
    velocity = 1
    powerchange = 0.01
    Total_rounds = 350
    powerinterval = 10
    photointerval = 50
    Ygnum = 125
    Ngnum = 125
    Yhnum = 125
    Nhnum = 125
    Ynum = Ygnum + Yhnum
    Nnum = Ngnum + Nhnum
    Ynum_list = np.arange(Ynum)
    Nnum_list = np.arange(Nnum)

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
    quota = np.array([hot_quota] * Yhnum + [green_quota] * Ygnum)
    Yh_ratio = np.random.uniform(hot_quota, hot_quota_upper, size=(1, Yhnum))[0]
    Yg_ratio = np.random.uniform(green_quota, green_quota_upper, size=(1, Ygnum))[0]
    Y_ratio = np.append(Yh_ratio, Yg_ratio)
    Nh_ratio = np.random.uniform(hot_quota_lower, hot_quota, size=(1, Nhnum))[0]
    Ng_ratio = np.random.uniform(green_quota_lower, green_quota, size=(1, Ngnum))[0]
    N_ratio = np.append(Nh_ratio, Ng_ratio)
    Yh_produce = np.random.uniform(100, 120, size=(1, Yhnum))[0]
    Yg_produce = np.random.uniform(100, 120, size=(1, Ygnum))[0]
    Y_produce = np.append(Yh_produce, Yg_produce)
    Nh_produce = np.random.uniform(100, 120, size=(1, Nhnum))[0]
    Ng_produce = np.random.uniform(100, 120, size=(1, Ngnum))[0]
    N_produce = np.append(Nh_produce, Ng_produce)

    Nbuy = (quota - N_ratio) * N_produce
    Nsellgreen = N_ratio * N_produce
    Nsellhot = (1 - N_ratio) * N_produce
    Ysell = (Y_ratio - quota) * Y_produce
    Ysellgreen = quota * Y_produce
    Ysellhot = (1 - Y_ratio) * Y_produce


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
        f =pehigh+x*0
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


    Y_strategy = np.random.randint(0, 3, size=(1, Ynum))[0]
    N_strategy = np.random.randint(0, 3, size=(1, Nnum))[0]
    Yloc = np.random.uniform(0, L, size=(Ynum, 2))
    Nloc = np.random.uniform(0, L, size=(Nnum, 2))

    RY = a * Y_ratio * Y_produce
    RN = a * N_ratio * N_produce

    EEY = (Y_ratio - hot_quota) * Y_produce
    ZZN = (green_quota - N_ratio) * N_produce


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


    def pairlist(x):
        linshi = copy.copy(x)
        pair = np.zeros((Ynum, 2))
        unfold = np.arange(Ynum * Nnum)
        fold = unfold.reshape(Ynum, Nnum)
        for i in range(Ynum):
            try:
                reshap_p = linshi.reshape(1, Ynum * Nnum)[0]
                Want_delete = np.random.choice(unfold, p=reshap_p)
                rowdelete = np.where(fold == Want_delete)[0][0]  # Y的编号
                columndelete = np.where(fold == Want_delete)[1][0]  # N的编号
                pair0 = np.array([rowdelete, columndelete])
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


    def greenbook(x):
        inpool = np.zeros((1, Ynum))[0]
        outpool = np.zeros((1, Nnum))[0]
        dog0 = copy.copy(Ynum_list)
        god0 = copy.copy(Nnum_list)
        for i in range(Ynum):
            jiu = x[i]
            jiu0 = int(jiu[0])
            jiu1 = int(jiu[1])
            if jiu0 != 99999:
                dog0 = np.delete(dog0, np.where(dog0 == jiu0)[0])
                god0 = np.delete(god0, np.where(god0 == jiu1)[0])
                xiu = Y_strategy[jiu0] * 10 + N_strategy[jiu1]
                if xiu == 0:
                    inpool[jiu0] = np.maximum((Ysell[jiu0] - Nbuy[jiu1]), 0)
                    outpool[jiu1] = np.maximum((Nbuy[jiu1] - Ysell[jiu0]), 0)
                elif xiu in [1, 10, 11, 20, 21]:
                    inpool[jiu0] = Ysell[jiu0]
                    outpool[jiu1] = Nbuy[jiu1]
                else:
                    inpool[jiu0] = 0
                    outpool[jiu1] = 0
            else:
                for j in dog0:
                    if Y_strategy[j] == 2:
                        inpool[j] = 0
                    else:
                        inpool[j] = Ysell[j]
                for j0 in god0:
                    if N_strategy[j0] == 2:
                        outpool[j0] = 0
                    else:
                        outpool[j0] = Nbuy[j0]
        poolsd = np.sum(inpool) - np.sum(outpool)
        return np.sum(inpool), np.sum(outpool), poolsd


    def costame(x):
        cost0 = copy.copy(x)
        cost1 = copy.copy(x)
        cost2 = copy.copy(x)
        cost3 = copy.copy(x)
        cost0[x[x < Yhnum]] = cost_hpg(Ysellgreen[x[x < Yhnum]])
        cost0[x[x > Yhnum]] = cost_gpg(Ysellgreen[x[x > Yhnum]])
        cost1[x[x < Yhnum]] = cost_hph(Ysellhot[x[x < Yhnum]])
        cost1[x[x > Yhnum]] = cost_gph(Ysellhot[x[x > Yhnum]])
        cost2[x[x < Nhnum]] = cost_hpg(Nsellgreen[x[x < Nhnum]])
        cost2[x[x > Nhnum]] = cost_gpg(Nsellgreen[x[x > Nhnum]])
        cost3[x[x < Nhnum]] = cost_hph(Nsellhot[x[x < Nhnum]])
        cost3[x[x > Nhnum]] = cost_gph(Nsellhot[x[x > Nhnum]])
        return cost0, cost1, cost2, cost3


    Ygdeal = np.zeros((len(X), 1))
    Yhdeal = np.zeros((len(X), 1))
    Ngdeal = np.zeros((len(X), 1))
    Nhdeal = np.zeros((len(X), 1))
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
    greeninpool = np.zeros((len(X), 1))
    greenprice = np.zeros((len(X), 1))
    greenoutpool = np.zeros((len(X), 1))
    beforced = np.zeros((len(X), 1))
    Ybeforced = np.zeros((len(X), 1))
    Nbeforced = np.zeros((len(X), 1))
    for turn in X:
        print(turn)
        bb = turn
        bb2 = turn
        EY = e * EEY
        ZN = f * ZZN
        # print(ZZN[:10])
        copyZZN = copy.copy(ZZN)
        copyEEY = copy.copy(EEY)
        # print(copyZZN[:10])
        YNdistancematrix = np.zeros((Ynum, Nnum))
        NNdistancematrix = np.zeros((Nnum, Nnum))
        YYdistancematrix = np.zeros((Ynum, Ynum))
        for i in range(Ynum):
            YNdistancematrix[i] = distance(plane(Yloc), i, Nloc)
        for i in range(Nnum):
            NNdistancematrix[i] = distance(plane(Nloc), i, Nloc)
        for i in range(Ynum):
            YYdistancematrix[i] = distance(plane(Yloc), i, Yloc)

        NNdistancematrix_inverse = (1. / NNdistancematrix)
        NNdistancematrix_inverse[np.isinf(NNdistancematrix_inverse)] = 0
        NNlinshimatrix = NNdistancematrix_inverse * field(NNdistancematrix)
        YYdistancematrix_inverse = (1. / YYdistancematrix)
        YYdistancematrix_inverse[np.isinf(YYdistancematrix_inverse)] = 0
        YYlinshimatrix = YYdistancematrix_inverse * field(YYdistancematrix)
        YNprobmatrix = ((1. / YNdistancematrix) * field(YNdistancematrix)) / (
            np.sum((1. / YNdistancematrix) * field(YNdistancematrix)))

        YNpairlist = pairlist(YNprobmatrix)
        green = greenbook(YNpairlist)
        # print("绿证供给、需求、差值",green)
        greeninpool[turn] = green[0]
        greenoutpool[turn] = green[1]
        price = pe(green[2])
        # print("价格",price)
        greenprice[turn] = price

        Y_utility = np.zeros((1, Ynum))[0]
        N_utility = np.zeros((1, Nnum))[0]
        fgnb0 = copy.copy(Ynum_list)
        fgnb1 = copy.copy(Nnum_list)
        beforcedY = np.zeros((1, Ynum))[0]
        beforcedN = np.zeros((1, Nnum))[0]
        for i in range(Ynum):
            bjiu = YNpairlist[i]
            bjiu0 = int(bjiu[0])
            bjiu1 = int(bjiu[1])
            if bjiu0 != 99999:
                fgnb0 = np.delete(fgnb0, np.where(fgnb0 == bjiu0)[0])
                fgnb1 = np.delete(fgnb1, np.where(fgnb1 == bjiu1)[0])
                if bjiu0 < Yhnum:
                    cost0 = cost_hpg(Ysellgreen[bjiu0])
                    cost00 = cost_hpg(Ysell[bjiu0])
                    cost1 = cost_hph(Ysellhot[bjiu0])
                else:
                    cost0 = cost_gpg(Ysellgreen[bjiu0])
                    cost00 = cost_gpg(Ysell[bjiu0])
                    cost1 = cost_gph(Ysellhot[bjiu0])
                if bjiu1 < Nhnum:
                    cost2 = cost_hpg(Nsellgreen[bjiu1])
                    cost3 = cost_hph(Nsellhot[bjiu1])
                else:
                    cost2 = cost_gpg(Nsellgreen[bjiu1])
                    cost3 = cost_gph(Nsellhot[bjiu1])
                Sven = Y_strategy[bjiu0] * 10 + N_strategy[bjiu1]
                if Sven == 0:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + (price + pg) * Ysell[bjiu0] - cost0 + ph * Ysellhot[
                        bjiu0] - cost1 - Cd(YNdistancematrix[bjiu0, bjiu1]) / 2 - Cp((Ysell[bjiu0] - Nbuy[bjiu1]))
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - price * Nbuy[bjiu1] - cost2 + ph * Nsellhot[
                        bjiu1] - cost3 - Cd(YNdistancematrix[bjiu0, bjiu1]) / 2 - Cp((Nbuy[bjiu1] - Ysell[bjiu0]))
                    copyZZN[bjiu1] = 0
                    copyEEY[bjiu0] = 0
                elif Sven == 1:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + (price + pg) * Ysell[bjiu0] - cost0 + ph * Ysellhot[
                        bjiu0] - cost1 - Cp(Ysell[bjiu0])
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - price * Nbuy[bjiu1] - cost2 + ph * Nsellhot[
                        bjiu1] - cost3 - Cd(YNdistancematrix[bjiu0, bjiu1]) - Cp(Nbuy[bjiu1])
                    copyZZN[bjiu1] = 0
                    copyEEY[bjiu0] = 0
                elif Sven == 10:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + (price + pg) * Ysell[bjiu0] - cost0 + ph * Ysellhot[
                        bjiu0] - cost1 - Cd(YNdistancematrix[bjiu0, bjiu1]) - Cp(Ysell[bjiu0])
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - price * Nbuy[bjiu1] - cost2 + ph * Nsellhot[
                        bjiu1] - cost3 - Cp(Nbuy[bjiu1])
                    copyZZN[bjiu1] = 0
                    copyEEY[bjiu0] = 0
                elif Sven == 11:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + (price + pg) * Ysell[bjiu0] - cost0 + ph * Ysellhot[
                        bjiu0] - cost1 - Cp(Ysell[bjiu0])
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - price * Nbuy[bjiu1] - cost2 + ph * Nsellhot[
                        bjiu1] - cost3 - Cp(Nbuy[bjiu1])
                    copyZZN[bjiu1] = 0
                    copyEEY[bjiu0] = 0
                elif Sven == 20:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + (price + pg) * Ysell[bjiu0] - cost0 + ph * Ysellhot[
                        bjiu0] - cost1 - Cp(Ysell[bjiu0])
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - cost2 + ph * Nsellhot[bjiu1] - cost3 - ZN[bjiu1]
                    copyZZN[bjiu1] = 0
                    beforcedY[bjiu0] = 1
                elif Sven == 21:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + (price + pg) * Ysell[bjiu0] - cost0 + ph * Ysellhot[
                        bjiu0] - cost1 - Cp(Ysell[bjiu0])
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - cost2 + ph * Nsellhot[bjiu1] - cost3 - ZN[bjiu1]
                    copyZZN[bjiu1] = 0
                elif Sven == 2:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + pg * Ysell[bjiu0] - cost0 - cost00 + ph * Ysellhot[
                        bjiu0] - cost1 + EY[bjiu0]
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - price * Nbuy[bjiu1] - cost2 + ph * Nsellhot[
                        bjiu1] - cost3 - Cp(Nbuy[bjiu1])
                    copyZZN[bjiu1] = 0
                    beforcedN[bjiu1] = 1
                elif Sven == 12:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + pg * Ysell[bjiu0] - cost0 - cost00 + ph * Ysellhot[
                        bjiu0] - cost1 + EY[bjiu0]
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - price * Nbuy[bjiu1] - cost2 + ph * Nsellhot[
                        bjiu1] - cost3 - Cp(Nbuy[bjiu1])
                    copyZZN[bjiu1] = 0
                else:
                    Y_utility[bjiu0] = pg * Ysellgreen[bjiu0] + pg * Ysell[bjiu0] - cost0 - cost00 + ph * Ysellhot[
                        bjiu0] - cost1 + EY[bjiu0]
                    N_utility[bjiu1] = pg * Nsellgreen[bjiu1] - cost2 + ph * Nsellhot[bjiu1] - cost3 - ZN[bjiu1]
            else:
                for COCO in fgnb0:
                    if COCO < Yhnum:
                        COCOcost0 = cost_hpg(Ysellgreen[COCO])
                        COCOcost00 = cost_hpg(Ysell[COCO])
                        COCOcost1 = cost_hph(Ysellhot[COCO])
                    else:
                        COCOcost0 = cost_gpg(Ysellgreen[COCO])
                        COCOcost00 = cost_gpg(Ysell[COCO])
                        COCOcost1 = cost_gph(Ysellhot[COCO])
                    if Y_strategy[COCO] == 2:
                        Y_utility[COCO] = pg * Ysellgreen[COCO] + pg * Ysell[COCO] - COCOcost0 - COCOcost00 + ph * \
                                          Ysellhot[COCO] - COCOcost1 + EY[COCO]
                    elif Y_strategy[COCO] == 1:
                        Y_utility[COCO] = pg * Ysellgreen[COCO] + (price + pg) * Ysell[COCO] - COCOcost0 + ph * \
                                          Ysellhot[COCO] - COCOcost1 - Cp(Ysell[COCO])
                        copyEEY[COCO] = 0
                    else:
                        Y_utility[COCO] = pg * Ysellgreen[COCO] + (price + pg) * Ysell[COCO] - COCOcost0 + ph * \
                                          Ysellhot[COCO] - COCOcost1 - Cp(Ysell[COCO])
                        copyEEY[COCO] = 0
                        beforcedY[COCO] = 1
                for Panda in fgnb1:
                    if bjiu1 < Nhnum:
                        Pandacost2 = cost_hpg(Nsellgreen[Panda])
                        Pandacost3 = cost_hph(Nsellhot[Panda])
                    else:
                        Pandacost2 = cost_gpg(Nsellgreen[Panda])
                        Pandacost3 = cost_gph(Nsellhot[Panda])
                    if N_strategy[Panda] == 2:
                        N_utility[Panda] = pg * Nsellgreen[Panda] - Pandacost2 + ph * Nsellhot[Panda] - Pandacost3 - \
                                           ZN[Panda]
                    elif N_strategy[Panda] == 1:
                        N_utility[Panda] = pg * Nsellgreen[Panda] - price * Nbuy[Panda] - Pandacost2 + ph * \
                                           Nsellhot[Panda] - Pandacost3 - Cp(Nbuy[Panda])
                        copyZZN[Panda] = 0
                    else:
                        N_utility[Panda] = pg * Nsellgreen[Panda] - price * Nbuy[Panda] - Pandacost2 + ph * \
                                           Nsellhot[Panda] - Pandacost3 - Cp(Nbuy[Panda])
                        copyZZN[Panda] = 0
                        beforcedN[Panda] = 1
        # print(Y_utility)
        beforced[turn] = np.sum(beforcedY) + np.sum(beforcedN)
        Ybeforced[turn] = np.sum(beforcedY)
        Nbeforced[turn] = np.sum(beforcedN)
        copyY_strategy = copy.copy(Y_strategy)
        copyN_strategy = copy.copy(N_strategy)
        # print(copyZZN[:10])
        for i in range(Ynum):
            cjiu = NNlinshimatrix[i]
            if np.all(cjiu == 0) == False:
                cjiu_p = cjiu / np.sum(cjiu)
                ineighbor = np.random.choice(Nnum_list, p=cjiu_p)
                # print((N_utility[i]-N_utility[ineighbor]))
                if random.random() <= (1 / (1 + np.exp((N_utility[i] - N_utility[ineighbor]) / K))):
                    N_strategy[i] = copyN_strategy[ineighbor]
                else:
                    N_strategy[i] = copyN_strategy[i]
            else:
                N_strategy[i] = copyN_strategy[i]
            djiu = YYlinshimatrix[i]
            if np.all(djiu == 0) == False:
                djiu_p = djiu / np.sum(djiu)
                ineighbor0 = np.random.choice(Ynum_list, p=djiu_p)
                # print((Y_utility[i]-Y_utility[ineighbor0]))
                if random.random() <= (1 / (1 + np.exp((Y_utility[i] - Y_utility[ineighbor0]) / K))):
                    Y_strategy[i] = copyY_strategy[ineighbor0]
                else:
                    Y_strategy[i] = copyY_strategy[i]
            else:
                Y_strategy[i] = copyY_strategy[i]
        ###策略更新完了，接下来是移动
        angle = np.random.uniform(-np.pi, np.pi, size=(Ynum, 2))
        Yanglecos = np.multiply(np.cos(angle[:, 0]), velocity)
        Yanglesin = np.multiply(np.sin(angle[:, 0]), velocity)
        Nanglecos = np.multiply(np.cos(angle[:, 1]), velocity)
        Nanglesin = np.multiply(np.sin(angle[:, 1]), velocity)
        Yloc[:, 0] = Yloc[:, 0] + Yanglecos
        Yloc[:, 1] = Yloc[:, 1] + Yanglesin
        Nloc[:, 0] = Nloc[:, 0] + Nanglecos
        Nloc[:, 1] = Nloc[:, 1] + Nanglesin
        Yloc = boundary(Yloc)
        Nloc = boundary(Nloc)

        bhujiajia = np.sum(RY) + np.sum(RN) + np.sum(copyZZN * (f + powerchange)) - np.sum(
            copyEEY * (e + powerchange))
        bhujiajian = np.sum(RY) + np.sum(RN) + np.sum(copyZZN * (f + powerchange)) - np.sum(
            copyEEY * (e - powerchange))
        bhujianjia = np.sum(RY) + np.sum(RN) + np.sum(copyZZN * (f - powerchange)) - np.sum(
            copyEEY * (e + powerchange))
        bhujianjian = np.sum(RY) + np.sum(RN) + np.sum(copyZZN * (f - powerchange)) - np.sum(
            copyEEY * (e - powerchange))
        bhu = (bhujiajia + bhujiajian + bhujianjia + bhujianjian) / 4
        # print(bhujiajia,bhujiajian,bhujianjia,bhujianjian)
        department_utility[turn] = bhu
        department_utilityjiajia[turn] = bhujiajia
        department_utilityjiajian[turn] = bhujiajian
        department_utilityjianjia[turn] = bhujianjia
        department_utilityjianjian[turn] = bhujianjian
        Ee[turn] = e
        Ff[turn] = f
        Yg_strategy = Y_strategy[Ygnum:]
        Yh_strategy = Y_strategy[:Yhnum]
        Ng_strategy = N_strategy[Ngnum:]
        Nh_strategy = N_strategy[:Nhnum]

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
        Ygdealtoneighbor[turn] = len(np.where(Yg_strategy == 0)[0])
        Ygdealtopool[turn] = len(np.where(Yg_strategy == 1)[0])
        Ygnotdeal[turn] = len(np.where(Yg_strategy == 2)[0])
        Yhdealtoneighbor[turn] = len(np.where(Yh_strategy == 0)[0])
        Yhdealtopool[turn] = len(np.where(Yh_strategy == 1)[0])
        Yhnotdeal[turn] = len(np.where(Yh_strategy == 2)[0])
        Ngdealtoneighbor[turn] = len(np.where(Ng_strategy == 0)[0])
        Ngdealtopool[turn] = len(np.where(Ng_strategy == 1)[0])
        Ngnotdeal[turn] = len(np.where(Ng_strategy == 2)[0])
        Nhdealtoneighbor[turn] = len(np.where(Nh_strategy == 0)[0])
        Nhdealtopool[turn] = len(np.where(Nh_strategy == 1)[0])
        Nhnotdeal[turn] = len(np.where(Nh_strategy == 2)[0])


    df8 = pd.DataFrame(Ygdealtoneighbor)
    df8.to_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与邻居交易人数' + name + '.xlsx')
    df9 = pd.DataFrame(Ygdealtopool)
    df9.to_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业与pool交易人数' + name + '.xlsx')
    df10 = pd.DataFrame(Ygnotdeal)
    df10.to_excel('E:\\data\火电绿电2\第一部分\完成配额以可再生能源为主的电力企业不交易人数' + name + '.xlsx')
    df11 = pd.DataFrame(Yhdealtoneighbor)
    df11.to_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与邻居交易人数' + name + '.xlsx')
    df12 = pd.DataFrame(Yhdealtopool)
    df12.to_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业与pool交易人数' + name + '.xlsx')
    df13 = pd.DataFrame(Yhnotdeal)
    df13.to_excel('E:\\data\火电绿电2\第一部分\完成配额以传统能源为主的电力企业不交易人数' + name + '.xlsx')
    df14 = pd.DataFrame(Ngdealtoneighbor)
    df14.to_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与邻居交易人数' + name + '.xlsx')
    df15 = pd.DataFrame(Ngdealtopool)
    df15.to_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业与pool交易人数' + name + '.xlsx')
    df16 = pd.DataFrame(Ngnotdeal)
    df16.to_excel('E:\\data\火电绿电2\第一部分\未完成配额以可再生能源为主的电力企业不交易人数' + name + '.xlsx')
    df17 = pd.DataFrame(Nhdealtoneighbor)
    df17.to_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与邻居交易人数' + name + '.xlsx')
    df18 = pd.DataFrame(Nhdealtopool)
    df18.to_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业与pool交易人数' + name + '.xlsx')
    df19 = pd.DataFrame(Nhnotdeal)
    df19.to_excel('E:\\data\火电绿电2\第一部分\未完成配额以传统能源为主的电力企业不交易人数' + name + '.xlsx')
    df20 = pd.DataFrame(department_utility)
    df20.to_excel('E:\\data\火电绿电2\第一部分\监管部门效用' + name + '.xlsx')
    df21 = pd.DataFrame(Ee)
    df21.to_excel('E:\\data\火电绿电2\第一部分\监管部门奖励' + name + '.xlsx')
    df22 = pd.DataFrame(Ff)
    df22.to_excel('E:\\data\火电绿电2\第一部分\监管部门惩罚' + name + '.xlsx')
    df23 = pd.DataFrame(greeninpool)
    df23.to_excel('E:\\data\火电绿电2\第一部分\绿证数量供给' + name + '.xlsx')
    df24 = pd.DataFrame(greenprice)
    df24.to_excel('E:\\data\火电绿电2\第一部分\绿证价格' + name + '.xlsx')
    df25 = pd.DataFrame(greenoutpool)
    df25.to_excel('E:\\data\火电绿电2\第一部分\绿证数量需求' + name + '.xlsx')
    df26 = pd.DataFrame(beforced)
    df26.to_excel('E:\\data\火电绿电2\第一部分\被迫进入pool' + name + '.xlsx')
    df27 = pd.DataFrame(Ybeforced)
    df27.to_excel('E:\\data\火电绿电2\第一部分\完成配额被迫进入pool' + name + '.xlsx')
    df28 = pd.DataFrame(Nbeforced)
    df28.to_excel('E:\\data\火电绿电2\第一部分\未完成配额被迫进入pool' + name + '.xlsx')



#
#

