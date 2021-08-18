import numpy as np
import pandas as pd
import copy
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

ES = np.linspace(0,2,35)
GA = np.linspace(0,2,35)
ESide = np.arange(0, len(ES))
GAide = np.arange(0, len(GA))
YgdealtoneighborVR=np.zeros((len(ES),len(GA)))
YgdealtopoolVR=np.zeros((len(ES),len(GA)))
YgnotdealVR=np.zeros((len(ES),len(GA)))
YhdealtoneighborVR=np.zeros((len(ES),len(GA)))
YhdealtopoolVR=np.zeros((len(ES),len(GA)))
YhnotdealVR=np.zeros((len(ES),len(GA)))
NgdealtoneighborVR=np.zeros((len(ES),len(GA)))
NgdealtopoolVR=np.zeros((len(ES),len(GA)))
NgnotdealVR=np.zeros((len(ES),len(GA)))
NhdealtoneighborVR=np.zeros((len(ES),len(GA)))
NhdealtopoolVR=np.zeros((len(ES),len(GA)))
NhnotdealVR=np.zeros((len(ES),len(GA)))
department_utilityVR=np.zeros((len(ES),len(GA)))
EeVR=np.zeros((len(ES),len(GA)))
FfVR=np.zeros((len(ES),len(GA)))
for faith in ESide:
    for lina in GAide:
        hang=ES[faith]
        lie=GA[lina]
        np.random.seed(0)
        Total_rounds = 5000
        powerinterval = 10
        photointerval = 2000
        Ygnum = 125
        Ngnum = 125
        Yhnum = 125
        Nhnum = 125
        Ygnum_list = np.arange(Ygnum)
        Ngnum_list = np.arange(Ngnum)
        Yhnum_list = np.arange(Yhnum)
        Nhnum_list = np.arange(Nhnum)

        obey = {"Ygnum_list": Ygnum_list, "Yhnum_list": Yhnum_list}
        disobey = {"Ngnum_list": Ngnum_list, "Nhnum_list": Nhnum_list}
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
        Yh_ratio = np.random.uniform(hot_quota, hot_quota_upper, size=(1, Yhnum))[0]
        Yg_ratio = np.random.uniform(green_quota, green_quota_upper, size=(1, Ygnum))[0]
        Nh_ratio = np.random.uniform(hot_quota_lower, hot_quota, size=(1, Nhnum))[0]
        Ng_ratio = np.random.uniform(green_quota_lower, green_quota, size=(1, Ngnum))[0]
        Yh_produce = np.random.uniform(100, 120, size=(1, Yhnum))[0]
        Yg_produce = np.random.uniform(100, 120, size=(1, Ygnum))[0]
        Nh_produce = np.random.uniform(100, 120, size=(1, Nhnum))[0]
        Ng_produce = np.random.uniform(100, 120, size=(1, Ngnum))[0]

        pg =hang
        ph =hang
        a = 0.1
        W = 30
        L=5
        K = 2
        K2 = 2
        C = 5
        velocity = 1
        powerchange = 0.001
        e = 0.5
        f = 1
        e0 = e
        f0 = f
        inv = 0.5
        inv2 = 0.5
        r=1
        def Pe(x):
            f =lie
            return f


        def Cd(x):
            c = (x / r) * 0.5
            return c


        def Cp(x):
            x[x <= 0] = 0
            x[x > 0] = 0.25
            return x


        def cost_gpg(x):
            c = 0.3 * x
            return c


        def cost_gph(x):
            c = 0.2 * x
            return c


        def cost_hpg(x):
            c = 0.4 * x
            return c


        def cost_hph(x):
            c = 0.1 * x
            return c


        Nhbuy = (hot_quota - Nh_ratio) * Nh_produce
        Ngbuy = (green_quota - Ng_ratio) * Ng_produce
        Yhsell = (Yh_ratio - hot_quota) * Yh_produce
        Ygsell = (Yg_ratio - green_quota) * Yg_produce
        Nhbuypoolcost = Cp(Nhbuy)
        Ngbuypoolcost = Cp(Ngbuy)
        Yhsellpoolcost = Cp(Yhsell)
        Ygsellpoolcost = Cp(Ygsell)

        Yg_strategy = np.random.randint(0, 3, size=(1, Ygnum))[0]
        Ng_strategy = np.random.randint(0, 3, size=(1, Ngnum))[0]
        Yh_strategy = np.random.randint(0, 3, size=(1, Yhnum))[0]
        Nh_strategy = np.random.randint(0, 3, size=(1, Nhnum))[0]
        Ygloc = np.random.uniform(0, L, size=(Ygnum, 2))
        Ngloc = np.random.uniform(0, L, size=(Ngnum, 2))
        Yhloc = np.random.uniform(0, L, size=(Yhnum, 2))
        Nhloc = np.random.uniform(0, L, size=(Nhnum, 2))

        BNh = Pe(1) * (hot_quota - Nh_ratio) * Nh_produce
        BNg = Pe(1) * (green_quota - Ng_ratio) * Ng_produce
        BYh = (Pe(1) + pg) * (Yh_ratio - hot_quota) * Yh_produce
        BYg = (Pe(1) + pg) * (Yg_ratio - green_quota) * Yg_produce
        ###成本单独拆出来
        P0Nh = pg * hot_quota * Nh_produce
        P0Ng = pg * green_quota * Ng_produce
        P0Yh = pg * hot_quota * Yh_produce
        P0Yg = pg * green_quota * Yg_produce
        P1Nh = pg * Nh_ratio * Nh_produce
        P1Ng = pg * Ng_ratio * Ng_produce
        P1Yh = pg * Yh_ratio * Yh_produce
        P1Yg = pg * Yg_ratio * Yg_produce
        FNh = ph * (1 - Nh_ratio) * Nh_produce
        FNg = ph * (1 - Ng_ratio) * Ng_produce
        FYh = ph * (1 - Yh_ratio) * Yh_produce
        FYg = ph * (1 - Yg_ratio) * Yg_produce

        costYg = cost_gpg(Yg_ratio * Yg_produce) + cost_gph((1 - Yg_ratio) * Yg_produce)
        costYh = cost_hpg(Yh_ratio * Yh_produce) + cost_hph((1 - Yh_ratio) * Yh_produce)
        costNg = cost_gpg(Ng_ratio * Yg_produce) + cost_gph((1 - Ng_ratio) * Yg_produce)
        costNh = cost_hpg(Nh_ratio * Nh_produce) + cost_hph((1 - Nh_ratio) * Nh_produce)

        RYh = a * Yh_ratio * Yh_produce
        RYg = a * Yg_ratio * Yg_produce
        RNh = a * Nh_ratio * Nh_produce
        RNg = a * Ng_ratio * Ng_produce


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
            if x > L:
                x = x - L
            elif x < 0:
                x = x + L
            else:
                x = x
            return x


        def distance(g, x, y, z):
            mindled = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[0][x], (y, 1)), z)), axis=1))
            up = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[1][x], (y, 1)), z)), axis=1))
            down = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[2][x], (y, 1)), z)), axis=1))
            left = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[3][x], (y, 1)), z)), axis=1))
            right = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[4][x], (y, 1)), z)), axis=1))
            upright = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[5][x], (y, 1)), z)), axis=1))
            upleft = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[6][x], (y, 1)), z)), axis=1))
            downright = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[7][x], (y, 1)), z)), axis=1))
            downleft = np.sqrt(np.sum(np.square(np.subtract(np.tile(g[8][x], (y, 1)), z)), axis=1))
            f = np.minimum(np.minimum(np.minimum(
                np.minimum(np.minimum(np.minimum(np.minimum(np.minimum(mindled, up), down), left), right), upright),
                upleft), downright), downleft)
            return f


        def field(x):
            cc = copy.copy(x)
            cc[cc == 0] = r * 100000
            cc[cc <= r] = 1
            cc[cc > r] = 0
            return cc


        def strategy_combination(v0, vg):
            VG = v0 * 10 + vg
            VG[VG == 12] = 2
            VG[VG == 21] = 20
            return VG


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
        EEYh = (Yh_ratio - hot_quota) * Yh_produce
        EEYg = (Yg_ratio - green_quota) * Yg_produce
        ZZNh = (hot_quota - Nh_ratio) * Nh_produce
        ZZNg = (green_quota - Ng_ratio) * Ng_produce

        for turn in X:
            print(faith,lina,turn)
            bb = turn
            bb2 = turn
            EYh = e * EEYh
            EYg = e * EEYg
            ZNh = f * ZZNh
            ZNg = f * ZZNg
            haha = np.random.choice(list(obey))
            ame = str(haha)
            choiceobey = np.random.choice(obey[ame])
            haha2 = np.random.choice(list(disobey))
            ame2 = str(haha2)
            choicedisobey = np.random.choice(disobey[ame2])
            ####选出来的服从RPS的电力公司与不服从RPS的电力公司的距离
            if ame == "Yhnum_list":
                YdisNg = distance(plane(Yhloc), choiceobey, Ngnum, Ngloc)
                YdisNh = distance(plane(Yhloc), choiceobey, Nhnum, Nhloc)
                YdisYg = distance(plane(Yhloc), choiceobey, Ygnum, Ygloc)
                YdisYh = distance(plane(Yhloc), choiceobey, Yhnum, Yhloc)
                choiceobey_strategy = Yh_strategy[choiceobey]
                choiceobey_sell = Yhsell[choiceobey]
                choiceobeypoolcost = Yhsellpoolcost[choiceobey]
                choiceobeycost = costYh[choiceobey]
                choiceobeyreward = EYh[choiceobey]
                choiceobeyB = BYh[choiceobey]
                choiceobeyP0 = P0Yh[choiceobey]
                choiceobeyP1 = P1Yh[choiceobey]
                choiceobeyF = FYh[choiceobey]
                choiceobeysign = 0
                # print("P0",choiceobeyP0,"B",choiceobeyB,"P1",choiceobeyP1,"F",choiceobeyF,"reward",choiceobeyreward)
            else:
                YdisNg = distance(plane(Ygloc), choiceobey, Ngnum, Ngloc)
                YdisNh = distance(plane(Ygloc), choiceobey, Nhnum, Nhloc)
                YdisYg = distance(plane(Ygloc), choiceobey, Ygnum, Ygloc)
                YdisYh = distance(plane(Ygloc), choiceobey, Yhnum, Yhloc)
                choiceobey_strategy = Yg_strategy[choiceobey]
                choiceobey_sell = Ygsell[choiceobey]
                choiceobeypoolcost = Ygsellpoolcost[choiceobey]
                choiceobeyreward = EYg[choiceobey]
                choiceobeyB = BYg[choiceobey]
                choiceobeycost = costYg[choiceobey]
                choiceobeyP0 = P0Yg[choiceobey]
                choiceobeyP1 = P1Yg[choiceobey]
                choiceobeyF = FYg[choiceobey]
                choiceobeysign = 1
                # print("P0", choiceobeyP0, "B", choiceobeyB, "P1", choiceobeyP1, "F", choiceobeyF, "reward", choiceobeyreward)
            ##Yh=0;Yg=1;Nh=2;Ng=3
            if ame2 == "Nhnum_list":
                NdisYg = distance(plane(Nhloc), choicedisobey, Ygnum, Ygloc)
                NdisYh = distance(plane(Nhloc), choicedisobey, Yhnum, Yhloc)
                NdisNg = distance(plane(Nhloc), choicedisobey, Ngnum, Ngloc)
                NdisNh = distance(plane(Nhloc), choicedisobey, Nhnum, Nhloc)
                choicedisobey_strategy = Nh_strategy[choicedisobey]
                choicedisobey_buy = Nhbuy[choicedisobey]
                choicedisobeypoolcost = Nhbuypoolcost[choicedisobey]
                choicedisobeyfine = ZNh[choicedisobey]
                choicedisobeyB = BNh[choicedisobey]
                choicedisobeycost = costNh[choicedisobey]
                choicedisobeyP0 = P0Nh[choicedisobey]
                choicedisobeyP1 = P1Nh[choicedisobey]
                choicedisobeyF = FNh[choicedisobey]
                choicedisobeysign = 2
            else:
                NdisYg = distance(plane(Ngloc), choicedisobey, Ygnum, Ygloc)
                NdisYh = distance(plane(Ngloc), choicedisobey, Yhnum, Yhloc)
                NdisNg = distance(plane(Ngloc), choicedisobey, Ngnum, Ngloc)
                NdisNh = distance(plane(Ngloc), choicedisobey, Nhnum, Nhloc)
                choicedisobey_strategy = Ng_strategy[choicedisobey]
                choicedisobey_buy = Ngbuy[choicedisobey]
                choicedisobeypoolcost = Ngbuypoolcost[choicedisobey]
                choicedisobeycost = costNg[choicedisobey]
                choicedisobeyfine = ZNg[choicedisobey]
                choicedisobeyB = BNg[choicedisobey]
                choicedisobeyP0 = P0Ng[choicedisobey]
                choicedisobeyP1 = P1Ng[choicedisobey]
                choicedisobeyF = FNg[choicedisobey]
                choicedisobeysign = 3
            # print(NdisYg)
            # 概率可能都是0，用try
            NtradeYg_p = ((1. / NdisYg) * field(NdisYg)) / (
                    np.sum(((1. / NdisYg) * field(NdisYg))) + np.sum(((1. / NdisYh) * field(NdisYh))))  # 选出来的N与Yg交易的概率
            NtradeYh_p2 = ((1. / NdisYh) * field(NdisYh)) / (
                    np.sum(((1. / NdisYg) * field(NdisYg))) + np.sum(((1. / NdisYh) * field(NdisYh))))
            YtradeNg_p = ((1. / YdisNg) * field(YdisNg)) / (
                    np.sum(((1. / YdisNg) * field(YdisNg))) + np.sum(((1. / YdisNh) * field(YdisNh))))  # 选出来的N与Yg交易的概率
            YtradeNh_p2 = ((1. / YdisNh) * field(YdisNh)) / (
                    np.sum(((1. / YdisNg) * field(YdisNg))) + np.sum(((1. / YdisNh) * field(YdisNh))))

            Nstrategy_combinationYg = strategy_combination(choicedisobey_strategy, Yg_strategy) * field(NdisYg)
            Nstrategy_combinationYh = strategy_combination(choicedisobey_strategy, Yh_strategy) * field(
                NdisYh)  ##0-[0,0];1-[0,1];2-[0,2][1,2];10-[1,0];11-[1,1];20=[2,0][2,1];22-[2,2]
            # [0,1,2]
            # [10,11,2]
            # [20,20,22]
            Ystrategy_combinationNg = strategy_combination(choiceobey_strategy, Ng_strategy) * field(YdisNg)
            Ystrategy_combinationNh = strategy_combination(choiceobey_strategy, Nh_strategy) * field(
                YdisNh)  ##0-[0,0];1-[0,1];2-[0,2][1,2];10-[1,0];11-[1,1];20=[2,0][2,1];22-[2,2]

            NcostYg = np.zeros((1, Ygnum))[0]
            NcostYh = np.zeros((1, Yhnum))[0]
            N0Yg0 = np.where(Nstrategy_combinationYg == 0)[0]
            N0Yg1 = np.where(Nstrategy_combinationYg == 1)[0]
            N0Yg2 = np.where(Nstrategy_combinationYg == 2)[0]
            N1Yg0 = np.where(Nstrategy_combinationYg == 10)[0]
            N1Yg1 = np.where(Nstrategy_combinationYg == 11)[0]
            N1Yg2 = np.where(Nstrategy_combinationYg == 2)[0]
            N2Yg0 = np.where(Nstrategy_combinationYg == 20)[0]
            N2Yg1 = np.where(Nstrategy_combinationYg == 20)[0]
            N2Yg2 = np.where(Nstrategy_combinationYg == 22)[0]
            N0Yh0 = np.where(Nstrategy_combinationYh == 0)[0]
            N0Yh1 = np.where(Nstrategy_combinationYh == 1)[0]
            N0Yh2 = np.where(Nstrategy_combinationYh == 2)[0]
            N1Yh0 = np.where(Nstrategy_combinationYh == 10)[0]
            N1Yh1 = np.where(Nstrategy_combinationYh == 11)[0]
            N1Yh2 = np.where(Nstrategy_combinationYh == 2)[0]
            N2Yh0 = np.where(Nstrategy_combinationYh == 20)[0]
            N2Yh1 = np.where(Nstrategy_combinationYh == 20)[0]
            N2Yh2 = np.where(Nstrategy_combinationYh == 22)[0]

            costN_diffproduceYg = Cp(choicedisobey_buy - Ygsell)
            costNdisYg = Cd(NdisYg)
            costN_diffproduceYh = Cp(choicedisobey_buy - Yhsell)
            costNdisYh = Cd(NdisYh)
            NcostYg[N0Yg0] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - costNdisYg[N0Yg0] / 2 - \
                             costN_diffproduceYg[N0Yg0] - choicedisobeycost
            NcostYg[N0Yg1] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - costNdisYg[
                N0Yg1] - choicedisobeypoolcost - choicedisobeycost
            NcostYg[N0Yg2] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeycost - costNdisYg[N0Yg2]
            NcostYg[
                N1Yg0] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeypoolcost - choicedisobeycost
            NcostYg[
                N1Yg1] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeypoolcost - choicedisobeycost
            NcostYg[N1Yg2] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeycost
            NcostYg[N2Yg0] = choicedisobeyP1 + choicedisobeyF - choicedisobeyfine - choicedisobeycost
            NcostYg[N2Yg1] = choicedisobeyP1 + choicedisobeyF - choicedisobeyfine - choicedisobeycost
            NcostYg[N2Yg2] = choicedisobeyP1 + choicedisobeyF - choicedisobeyfine - choicedisobeycost

            NcostYh[N0Yh0] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - costNdisYh[N0Yh0] / 2 - \
                             costN_diffproduceYh[N0Yh0] - choicedisobeycost
            NcostYh[N0Yh1] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - costNdisYh[
                N0Yh1] - choicedisobeypoolcost - choicedisobeycost
            NcostYh[N0Yh2] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeycost - costNdisYh[N0Yh2]
            NcostYh[
                N1Yh0] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeypoolcost - choicedisobeycost
            NcostYh[
                N1Yh1] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeypoolcost - choicedisobeycost
            NcostYh[N1Yh2] = choicedisobeyP1 - choicedisobeyB + choicedisobeyF - choicedisobeycost
            NcostYh[N2Yh0] = choicedisobeyP1 + choicedisobeyF - choicedisobeyfine - choicedisobeycost
            NcostYh[N2Yh1] = choicedisobeyP1 + choicedisobeyF - choicedisobeyfine - choicedisobeycost
            NcostYh[N2Yh2] = choicedisobeyP1 + choicedisobeyF - choicedisobeyfine - choicedisobeycost

            YcostNg = np.zeros((1, Ngnum))[0]
            YcostNh = np.zeros((1, Nhnum))[0]
            Y0Ng0 = np.where(Ystrategy_combinationNg == 0)[0]
            Y0Ng1 = np.where(Ystrategy_combinationNg == 1)[0]
            Y0Ng2 = np.where(Ystrategy_combinationNg == 2)[0]
            Y1Ng0 = np.where(Ystrategy_combinationNg == 10)[0]
            Y1Ng1 = np.where(Ystrategy_combinationNg == 11)[0]
            Y1Ng2 = np.where(Ystrategy_combinationNg == 2)[0]
            Y2Ng0 = np.where(Ystrategy_combinationNg == 20)[0]
            Y2Ng1 = np.where(Ystrategy_combinationNg == 20)[0]
            Y2Ng2 = np.where(Ystrategy_combinationNg == 22)[0]
            Y0Nh0 = np.where(Ystrategy_combinationNh == 0)[0]
            Y0Nh1 = np.where(Ystrategy_combinationNh == 1)[0]
            Y0Nh2 = np.where(Ystrategy_combinationNh == 2)[0]
            Y1Nh0 = np.where(Ystrategy_combinationNh == 10)[0]
            Y1Nh1 = np.where(Ystrategy_combinationNh == 11)[0]
            Y1Nh2 = np.where(Ystrategy_combinationNh == 2)[0]
            Y2Nh0 = np.where(Ystrategy_combinationNh == 20)[0]
            Y2Nh1 = np.where(Ystrategy_combinationNh == 20)[0]
            Y2Nh2 = np.where(Ystrategy_combinationNh == 22)[0]

            costY_diffproduceNg = Cp(choiceobey_sell - Ngbuy)
            costY_diffproduceNh = Cp(choiceobey_sell - Nhbuy)
            costYdisNg = Cd(YdisNg)
            costYdisNh = Cd(YdisNh)
            YcostNg[Y0Ng0] = choiceobeyP0 + choiceobeyB + choiceobeyF - costYdisNg[Y0Ng0] / 2 - costY_diffproduceNg[
                Y0Ng0] - choiceobeycost
            YcostNg[Y0Ng1] = choiceobeyP0 + choiceobeyB + choiceobeyF - costYdisNg[
                Y0Ng1] - choiceobeypoolcost - choiceobeycost
            YcostNg[Y0Ng2] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost - \
                             costYdisNg[
                                 Y0Ng2]
            YcostNg[Y1Ng0] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost
            YcostNg[Y1Ng1] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost
            YcostNg[Y1Ng2] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost
            YcostNg[Y2Ng0] = choiceobeyP1 + choiceobeyF + choiceobeyreward - choiceobeycost
            YcostNg[Y2Ng1] = choiceobeyP1 + choiceobeyF + choiceobeyreward - choiceobeycost
            YcostNg[Y2Ng2] = choiceobeyP1 + choiceobeyF + choiceobeyreward - choiceobeycost

            YcostNh[Y0Nh0] = choiceobeyP0 + choiceobeyB + choiceobeyF - costYdisNh[Y0Nh0] / 2 - costY_diffproduceNh[
                Y0Nh0] - choiceobeycost
            YcostNh[Y0Nh1] = choiceobeyP0 + choiceobeyB + choiceobeyF - costYdisNh[
                Y0Nh1] - choiceobeypoolcost - choiceobeycost
            YcostNh[Y0Nh2] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost - \
                             costYdisNh[
                                 Y0Nh2]
            YcostNh[Y1Nh0] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost
            YcostNh[Y1Nh1] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost
            YcostNh[Y1Nh2] = choiceobeyP0 + choiceobeyB + choiceobeyF - choiceobeypoolcost - choiceobeycost
            YcostNh[Y2Nh0] = choiceobeyP1 + choiceobeyF + choiceobeyreward - choiceobeycost
            YcostNh[Y2Nh1] = choiceobeyP1 + choiceobeyF + choiceobeyreward - choiceobeycost
            YcostNh[Y2Nh2] = choiceobeyP1 + choiceobeyF + choiceobeyreward - choiceobeycost

            #
            choiceobey_expected_utility = np.sum(YcostNg * YtradeNg_p + YcostNh * YtradeNh_p2)
            choicedisobey_expected_utility = np.sum(NcostYg * NtradeYg_p + NcostYh * NtradeYh_p2)

            obeyneighbor = {"obeyYgneighbor": Ygnum_list, "obeyYhneighbor": Yhnum_list}
            disobeyneighbor = {"disobeyNgneighbor": Ngnum_list, "disobeyNhneighbor": Nhnum_list}
            YdisYg_inverse = (1. / YdisYg)
            YdisYg_inverse[np.isinf(YdisYg_inverse)] = 0
            YdisYg_p = YdisYg_inverse * field(YdisYg) / np.sum(YdisYg_inverse * field(YdisYg))
            YdisYh_inverse = (1. / YdisYh)
            YdisYh_inverse[np.isinf(YdisYh_inverse)] = 0
            YdisYh_p = YdisYh_inverse * field(YdisYh) / np.sum(YdisYh_inverse * field(YdisYh))
            NdisNg_inverse = (1. / NdisNg)
            NdisNg_inverse[np.isinf(NdisNg_inverse)] = 0
            NdisNg_p = NdisNg_inverse * field(NdisNg) / np.sum(NdisNg_inverse * field(NdisNg))
            NdisNh_inverse = (1. / NdisNh)
            NdisNh_inverse[np.isinf(NdisNh_inverse)] = 0
            NdisNh_p = NdisNh_inverse * field(NdisNh) / np.sum(NdisNh_inverse * field(NdisNh))
            obeyneighbor_p = {"obeyYgneighbor": YdisYg_p, "obeyYhneighbor": YdisYh_p}
            disobeyneighbor_p = {"disobeyNgneighbor": NdisNg_p, "disobeyNhneighbor": NdisNh_p}
            # # 可能会没有邻居，用try
            biu = np.random.choice(list(obeyneighbor))
            xi = str(biu)
            choiceobeyneighbor = np.random.choice(np.array(obeyneighbor[xi]), p=obeyneighbor_p[xi])
            biu2 = np.random.choice(list(disobeyneighbor))
            xi2 = str(biu2)
            choicedisobeyneighbor = np.random.choice(disobeyneighbor[xi2], p=disobeyneighbor_p[xi2])
            #
            if xi == "obeyYhneighbor":
                YneighbordisNg = distance(plane(Yhloc), choiceobeyneighbor, Ngnum, Ngloc)
                YneighbordisNh = distance(plane(Yhloc), choiceobeyneighbor, Nhnum, Nhloc)
                YneighbordisYg = distance(plane(Yhloc), choiceobeyneighbor, Ygnum, Ygloc)
                YneighbordisYh = distance(plane(Yhloc), choiceobeyneighbor, Yhnum, Yhloc)
                choiceobeyneighbor_strategy = Yh_strategy[choiceobeyneighbor]
                choiceobeyneighbor_sell = Yhsell[choiceobeyneighbor]
                choiceobeyneighborpoolcost = Yhsellpoolcost[choiceobeyneighbor]
                choiceobeyneighborcost = costYh[choiceobeyneighbor]
                choiceobeyneighborreward = EYh[choiceobeyneighbor]
                choiceobeyneighborB = BYh[choiceobeyneighbor]
                choiceobeyneighborP0 = P0Yh[choiceobeyneighbor]
                choiceobeyneighborP1 = P1Yh[choiceobeyneighbor]
                choiceobeyneighborF = FYh[choiceobeyneighbor]
                choiceobeyneighborsign = 0
                # print("P0", choiceobeyneighborP0, "B", choiceobeyneighborB, "P1", choiceobeyneighborP1, "F", choiceobeyneighborF, "reward", choiceobeyneighborreward)
            else:
                YneighbordisNg = distance(plane(Ygloc), choiceobeyneighbor, Ngnum, Ngloc)
                YneighbordisNh = distance(plane(Ygloc), choiceobeyneighbor, Nhnum, Nhloc)
                YneighbordisYg = distance(plane(Ygloc), choiceobeyneighbor, Ygnum, Ygloc)
                YneighbordisYh = distance(plane(Ygloc), choiceobeyneighbor, Yhnum, Yhloc)
                choiceobeyneighbor_strategy = Yg_strategy[choiceobeyneighbor]
                choiceobeyneighbor_sell = Ygsell[choiceobeyneighbor]
                choiceobeyneighborpoolcost = Ygsellpoolcost[choiceobeyneighbor]
                choiceobeyneighborcost = costYg[choiceobeyneighbor]
                choiceobeyneighborreward = EYg[choiceobeyneighbor]
                choiceobeyneighborB = BYg[choiceobeyneighbor]
                choiceobeyneighborP0 = P0Yg[choiceobeyneighbor]
                choiceobeyneighborP1 = P1Yg[choiceobeyneighbor]
                choiceobeyneighborF = FYg[choiceobeyneighbor]
                choiceobeyneighborsign = 1
                # print("P0", choiceobeyneighborP0, "B", choiceobeyneighborB, "P1", choiceobeyneighborP1, "F", choiceobeyneighborF, "reward", choiceobeyneighborreward)

            if xi2 == "disobeyNhneighbor":
                NneighbordisYg = distance(plane(Nhloc), choicedisobeyneighbor, Ygnum, Ygloc)
                NneighbordisYh = distance(plane(Nhloc), choicedisobeyneighbor, Yhnum, Yhloc)
                NneighbordisNg = distance(plane(Nhloc), choicedisobeyneighbor, Ngnum, Ngloc)
                NneighbordisNh = distance(plane(Nhloc), choicedisobeyneighbor, Nhnum, Nhloc)
                choicedisobeyneighbor_strategy = Nh_strategy[choicedisobeyneighbor]
                choicedisobeyneighbor_buy = Nhbuy[choicedisobeyneighbor]
                choicedisobeyneighborpoolcost = Nhbuypoolcost[choicedisobeyneighbor]
                choicedisobeyneighborcost = costNh[choicedisobeyneighbor]
                choicedisobeyneighborfine = ZNh[choicedisobeyneighbor]
                choicedisobeyneighborB = BNh[choicedisobeyneighbor]
                choicedisobeyneighborP0 = P0Nh[choicedisobeyneighbor]
                choicedisobeyneighborP1 = P1Nh[choicedisobeyneighbor]
                choicedisobeyneighborF = FNh[choicedisobeyneighbor]
                choicedisobeyneighborsign = 2
            else:
                NneighbordisYg = distance(plane(Ngloc), choicedisobeyneighbor, Ygnum, Ygloc)
                NneighbordisYh = distance(plane(Ngloc), choicedisobeyneighbor, Yhnum, Yhloc)
                NneighbordisNg = distance(plane(Ngloc), choicedisobeyneighbor, Ngnum, Ngloc)
                NneighbordisNh = distance(plane(Ngloc), choicedisobeyneighbor, Nhnum, Nhloc)
                choicedisobeyneighbor_strategy = Ng_strategy[choicedisobeyneighbor]
                choicedisobeyneighbor_buy = Ngbuy[choicedisobeyneighbor]
                choicedisobeyneighborpoolcost = Ngbuypoolcost[choicedisobeyneighbor]
                choicedisobeyneighborcost = costNg[choicedisobeyneighbor]
                choicedisobeyneighborfine = ZNg[choicedisobeyneighbor]
                choicedisobeyneighborB = BNg[choicedisobeyneighbor]
                choicedisobeyneighborP0 = P0Ng[choicedisobeyneighbor]
                choicedisobeyneighborP1 = P1Ng[choicedisobeyneighbor]
                choicedisobeyneighborF = FNg[choicedisobeyneighbor]
                choicedisobeyneighborsign = 3
            # # # print(NdisYg)
            # # #概率可能都是0，用try
            NneighbortradeYg_p = ((1. / NneighbordisYg) * field(NneighbordisYg)) / (
                    np.sum(((1. / NneighbordisYg) * field(NneighbordisYg))) + np.sum(
                ((1. / NneighbordisYh) * field(NneighbordisYh))))  # 选出来的N与Yg交易的概率
            NneighbortradeYh_p2 = ((1. / NneighbordisYh) * field(NneighbordisYh)) / (
                    np.sum(((1. / NneighbordisYg) * field(NneighbordisYg))) + np.sum(
                ((1. / NneighbordisYh) * field(NneighbordisYh))))
            YneighbortradeNg_p = ((1. / YneighbordisNg) * field(YneighbordisNg)) / (
                    np.sum(((1. / YneighbordisNg) * field(YneighbordisNg))) + np.sum(
                ((1. / YneighbordisNh) * field(YneighbordisNh))))  # 选出来的N与Yg交易的概率
            YneighbortradeNh_p2 = ((1. / YneighbordisNh) * field(YneighbordisNh)) / (
                    np.sum(((1. / YneighbordisNg) * field(YneighbordisNg))) + np.sum(
                ((1. / YneighbordisNh) * field(YneighbordisNh))))
            # #
            # #
            Nneighborstrategy_combinationYg = strategy_combination(choicedisobeyneighbor_strategy, Yg_strategy) * field(
                NneighbordisYg)
            Nneighborstrategy_combinationYh = strategy_combination(choicedisobeyneighbor_strategy, Yh_strategy) * field(
                NneighbordisYh)  ##5是[1,1],4是[1,0]，3是[0,1]，2是[0,0]
            # # print(Nneighborstrategy_combinationYg)
            #
            Yneighborstrategy_combinationNg = strategy_combination(choiceobeyneighbor_strategy, Ng_strategy) * field(
                YneighbordisNg)
            Yneighborstrategy_combinationNh = strategy_combination(choiceobeyneighbor_strategy, Nh_strategy) * field(
                YneighbordisNh)  ##5是[1,1],4是[1,0]，3是[0,1]，2是[0,0]
            # #
            NneighborcostYg = np.zeros((1, Ygnum))[0]
            NneighborcostYh = np.zeros((1, Yhnum))[0]
            Nneighbor0Yg0 = np.where(Nneighborstrategy_combinationYg == 0)[0]
            Nneighbor0Yg1 = np.where(Nneighborstrategy_combinationYg == 1)[0]
            Nneighbor0Yg2 = np.where(Nneighborstrategy_combinationYg == 2)[0]
            Nneighbor1Yg0 = np.where(Nneighborstrategy_combinationYg == 10)[0]
            Nneighbor1Yg1 = np.where(Nneighborstrategy_combinationYg == 11)[0]
            Nneighbor1Yg2 = np.where(Nneighborstrategy_combinationYg == 2)[0]
            Nneighbor2Yg0 = np.where(Nneighborstrategy_combinationYg == 20)[0]
            Nneighbor2Yg1 = np.where(Nneighborstrategy_combinationYg == 20)[0]
            Nneighbor2Yg2 = np.where(Nneighborstrategy_combinationYg == 22)[0]
            Nneighbor0Yh0 = np.where(Nneighborstrategy_combinationYh == 0)[0]
            Nneighbor0Yh1 = np.where(Nneighborstrategy_combinationYh == 1)[0]
            Nneighbor0Yh2 = np.where(Nneighborstrategy_combinationYh == 2)[0]
            Nneighbor1Yh0 = np.where(Nneighborstrategy_combinationYh == 10)[0]
            Nneighbor1Yh1 = np.where(Nneighborstrategy_combinationYh == 11)[0]
            Nneighbor1Yh2 = np.where(Nneighborstrategy_combinationYh == 2)[0]
            Nneighbor2Yh0 = np.where(Nneighborstrategy_combinationYh == 20)[0]
            Nneighbor2Yh1 = np.where(Nneighborstrategy_combinationYh == 20)[0]
            Nneighbor2Yh2 = np.where(Nneighborstrategy_combinationYh == 22)[0]

            costNneighbor_diffproduceYg = Cp(choicedisobeyneighbor_buy - Ygsell)
            costNneighbordisYg = Cd(NneighbordisYg)
            costNneighbor_diffproduceYh = Cp(choicedisobeyneighbor_buy - Yhsell)
            costNneighbordisYh = Cd(NneighbordisYh)
            NneighborcostYg[Nneighbor0Yg0] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - \
                                             costNneighbordisYg[Nneighbor0Yg0] / 2 - costNneighbor_diffproduceYg[
                                                 Nneighbor0Yg0] - choicedisobeyneighborcost
            NneighborcostYg[Nneighbor0Yg1] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - \
                                             costNneighbordisYg[
                                                 Nneighbor0Yg1] - choicedisobeyneighborpoolcost - choicedisobeyneighborcost
            NneighborcostYg[
                Nneighbor0Yg2] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborcost - \
                                 costNneighbordisYg[Nneighbor0Yg2]
            NneighborcostYg[
                Nneighbor1Yg0] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborpoolcost - choicedisobeyneighborcost
            NneighborcostYg[
                Nneighbor1Yg1] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborpoolcost - choicedisobeyneighborcost
            NneighborcostYg[
                Nneighbor1Yg2] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborcost
            NneighborcostYg[
                Nneighbor2Yg0] = choicedisobeyneighborP1 + choicedisobeyneighborF - choicedisobeyneighborfine - choicedisobeyneighborcost
            NneighborcostYg[
                Nneighbor2Yg1] = choicedisobeyneighborP1 + choicedisobeyneighborF - choicedisobeyneighborfine - choicedisobeyneighborcost
            NneighborcostYg[
                Nneighbor2Yg2] = choicedisobeyneighborP1 + choicedisobeyneighborF - choicedisobeyneighborfine - choicedisobeyneighborcost

            NneighborcostYh[Nneighbor0Yh0] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - \
                                             costNneighbordisYh[Nneighbor0Yh0] / 2 - costNneighbor_diffproduceYh[
                                                 Nneighbor0Yh0] - choicedisobeyneighborcost
            NneighborcostYh[Nneighbor0Yh1] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - \
                                             costNneighbordisYh[
                                                 Nneighbor0Yh1] - choicedisobeyneighborpoolcost - choicedisobeyneighborcost
            NneighborcostYh[
                Nneighbor0Yh2] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborcost - \
                                 costNneighbordisYh[Nneighbor0Yh2]
            NneighborcostYh[
                Nneighbor1Yh0] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborpoolcost - choicedisobeyneighborcost
            NneighborcostYh[
                Nneighbor1Yh1] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborpoolcost - choicedisobeyneighborcost
            NneighborcostYh[
                Nneighbor1Yh2] = choicedisobeyneighborP1 - choicedisobeyneighborB + choicedisobeyneighborF - choicedisobeyneighborcost
            NneighborcostYh[
                Nneighbor2Yh0] = choicedisobeyneighborP1 + choicedisobeyneighborF - choicedisobeyneighborfine - choicedisobeyneighborcost
            NneighborcostYh[
                Nneighbor2Yh1] = choicedisobeyneighborP1 + choicedisobeyneighborF - choicedisobeyneighborfine - choicedisobeyneighborcost
            NneighborcostYh[
                Nneighbor2Yh2] = choicedisobeyneighborP1 + choicedisobeyneighborF - choicedisobeyneighborfine - choicedisobeyneighborcost

            YneighborcostNg = np.zeros((1, Ngnum))[0]
            YneighborcostNh = np.zeros((1, Nhnum))[0]
            Yneighbor0Ng0 = np.where(Yneighborstrategy_combinationNg == 0)[0]
            Yneighbor0Ng1 = np.where(Yneighborstrategy_combinationNg == 1)[0]
            Yneighbor0Ng2 = np.where(Yneighborstrategy_combinationNg == 2)[0]
            Yneighbor1Ng0 = np.where(Yneighborstrategy_combinationNg == 10)[0]
            Yneighbor1Ng1 = np.where(Yneighborstrategy_combinationNg == 11)[0]
            Yneighbor1Ng2 = np.where(Yneighborstrategy_combinationNg == 2)[0]
            Yneighbor2Ng0 = np.where(Yneighborstrategy_combinationNg == 20)[0]
            Yneighbor2Ng1 = np.where(Yneighborstrategy_combinationNg == 20)[0]
            Yneighbor2Ng2 = np.where(Yneighborstrategy_combinationNg == 22)[0]
            Yneighbor0Nh0 = np.where(Yneighborstrategy_combinationNh == 0)[0]
            Yneighbor0Nh1 = np.where(Yneighborstrategy_combinationNh == 1)[0]
            Yneighbor0Nh2 = np.where(Yneighborstrategy_combinationNh == 2)[0]
            Yneighbor1Nh0 = np.where(Yneighborstrategy_combinationNh == 10)[0]
            Yneighbor1Nh1 = np.where(Yneighborstrategy_combinationNh == 11)[0]
            Yneighbor1Nh2 = np.where(Yneighborstrategy_combinationNh == 2)[0]
            Yneighbor2Nh0 = np.where(Yneighborstrategy_combinationNh == 20)[0]
            Yneighbor2Nh1 = np.where(Yneighborstrategy_combinationNh == 20)[0]
            Yneighbor2Nh2 = np.where(Yneighborstrategy_combinationNh == 22)[0]

            costYneighbor_diffproduceNg = Cp(choiceobeyneighbor_sell - Ngbuy)
            costYneighbor_diffproduceNh = Cp(choiceobeyneighbor_sell - Nhbuy)
            costYneighbordisNg = Cd(YneighbordisNg)
            costYneighbordisNh = Cd(YneighbordisNh)
            YneighborcostNg[Yneighbor0Ng0] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - \
                                             costYneighbordisNg[Yneighbor0Ng0] / 2 - costYneighbor_diffproduceNg[
                                                 Yneighbor0Ng0] - choiceobeyneighborcost
            YneighborcostNg[Yneighbor0Ng1] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - \
                                             costYneighbordisNg[
                                                 Yneighbor0Ng1] - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNg[
                Yneighbor0Ng2] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost - \
                                 costYneighbordisNg[Yneighbor0Ng2]
            YneighborcostNg[
                Yneighbor1Ng0] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNg[
                Yneighbor1Ng1] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNg[
                Yneighbor1Ng2] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNg[
                Yneighbor2Ng0] = choiceobeyneighborP1 + choiceobeyneighborF + choiceobeyneighborreward - choiceobeyneighborcost
            YneighborcostNg[
                Yneighbor2Ng1] = choiceobeyneighborP1 + choiceobeyneighborF + choiceobeyneighborreward - choiceobeyneighborcost
            YneighborcostNg[
                Yneighbor2Ng2] = choiceobeyneighborP1 + choiceobeyneighborF + choiceobeyneighborreward - choiceobeyneighborcost

            YneighborcostNh[Yneighbor0Nh0] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - \
                                             costYneighbordisNh[Yneighbor0Nh0] / 2 - costYneighbor_diffproduceNh[
                                                 Yneighbor0Nh0] - choiceobeyneighborcost
            YneighborcostNh[Yneighbor0Nh1] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - \
                                             costYneighbordisNh[
                                                 Yneighbor0Nh1] - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNh[
                Yneighbor0Nh2] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost - \
                                 costYneighbordisNh[Yneighbor0Nh2]
            YneighborcostNh[
                Yneighbor1Nh0] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNh[
                Yneighbor1Nh1] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNh[
                Yneighbor1Nh2] = choiceobeyneighborP0 + choiceobeyneighborB + choiceobeyneighborF - choiceobeyneighborpoolcost - choiceobeyneighborcost
            YneighborcostNh[
                Yneighbor2Nh0] = choiceobeyneighborP1 + choiceobeyneighborF + choiceobeyneighborreward - choiceobeyneighborcost
            YneighborcostNh[
                Yneighbor2Nh1] = choiceobeyneighborP1 + choiceobeyneighborF + choiceobeyneighborreward - choiceobeyneighborcost
            YneighborcostNh[
                Yneighbor2Nh2] = choiceobeyneighborP1 + choiceobeyneighborF + choiceobeyneighborreward - choiceobeyneighborcost
            #
            choiceobeyneighbor_expected_utility = np.sum(
                YneighborcostNg * YneighbortradeNg_p + YneighborcostNh * YneighbortradeNh_p2)
            choicedisobeyneighbor_expected_utility = np.sum(
                NneighborcostYg * NneighbortradeYg_p + NneighborcostYh * NneighbortradeYh_p2)
            #
            angle = np.random.uniform(-np.pi, np.pi, size=(1, 2))[0]
            Yanglecos = np.multiply(np.cos(angle[0]), velocity)
            Yanglesin = np.multiply(np.sin(angle[0]), velocity)
            #
            if random.random() <= (
                    1 / (1 + np.exp((choiceobey_expected_utility - choiceobeyneighbor_expected_utility) / K))):
                good = choiceobeyneighbor_strategy
                if choiceobeysign == 0:
                    Yh_strategy[choiceobey] = good
                    jk0 = Yhloc[choiceobey, 0] + Yanglecos
                    jk1 = Yhloc[choiceobey, 1] + Yanglesin
                    Yhloc[choiceobey, 0] = boundary(jk0)
                    Yhloc[choiceobey, 1] = boundary(jk1)
                else:
                    Yg_strategy[choiceobey] = good
                    jk0 = Ygloc[choiceobey, 0] + Yanglecos
                    jk1 = Ygloc[choiceobey, 1] + Yanglesin
                    Ygloc[choiceobey, 0] = boundary(jk0)
                    Ygloc[choiceobey, 1] = boundary(jk1)
            else:
                good2 = choiceobey_strategy
                if choiceobeysign == 0:
                    Yh_strategy[choiceobey] = good2
                    jk0 = Yhloc[choiceobey, 0] + Yanglecos
                    jk1 = Yhloc[choiceobey, 1] + Yanglesin
                    Yhloc[choiceobey, 0] = boundary(jk0)
                    Yhloc[choiceobey, 1] = boundary(jk1)
                else:
                    Yg_strategy[choiceobey] = good2
                    jk0 = Ygloc[choiceobey, 0] + Yanglecos
                    jk1 = Ygloc[choiceobey, 1] + Yanglesin
                    Ygloc[choiceobey, 0] = boundary(jk0)
                    Ygloc[choiceobey, 1] = boundary(jk1)
            #
            Nanglecos = np.multiply(np.cos(angle[1]), velocity)
            Nanglesin = np.multiply(np.sin(angle[1]), velocity)

            if random.random() <= (
                    1 / (1 + np.exp((choicedisobey_expected_utility - choicedisobeyneighbor_expected_utility) / K))):
                good = choicedisobeyneighbor_strategy
                if choicedisobeysign == 2:
                    Nh_strategy[choicedisobey] = good
                    jd0 = Nhloc[choicedisobey, 0] + Nanglecos
                    jd1 = Nhloc[choicedisobey, 1] + Nanglesin
                    Nhloc[choicedisobey, 0] = boundary(jd0)
                    Nhloc[choicedisobey, 1] = boundary(jd1)
                else:
                    Ng_strategy[choicedisobey] = good
                    jd0 = Ngloc[choicedisobey, 0] + Nanglecos
                    jd1 = Ngloc[choicedisobey, 1] + Nanglesin
                    Ngloc[choicedisobey, 0] = boundary(jd0)
                    Ngloc[choicedisobey, 1] = boundary(jd1)
            else:
                good2 = choicedisobey_strategy
                if choicedisobeysign == 2:
                    Nh_strategy[choicedisobey] = good2
                    jd0 = Nhloc[choicedisobey, 0] + Nanglecos
                    jd1 = Nhloc[choicedisobey, 1] + Nanglesin
                    Nhloc[choicedisobey, 0] = boundary(jd0)
                    Nhloc[choicedisobey, 1] = boundary(jd1)
                else:
                    Ng_strategy[choicedisobey] = good2
                    jd0 = Ngloc[choicedisobey, 0] + Nanglecos
                    jd1 = Ngloc[choicedisobey, 1] + Nanglesin
                    Ngloc[choicedisobey, 0] = boundary(jd0)
                    Ngloc[choicedisobey, 1] = boundary(jd1)

            wao = np.array([-powerchange, powerchange])
            bhujiajia = -np.sum(EEYh * (e + powerchange)) - np.sum(EEYg * (e + powerchange)) + np.sum(
                ZZNh * (f + powerchange)) + np.sum(ZZNg * (f + powerchange))
            bhujiajian = -np.sum(EEYh * (e + powerchange)) - np.sum(EEYg * (e + powerchange)) + np.sum(
                ZZNh * (f - powerchange)) + np.sum(ZZNg * (f - powerchange))
            bhujianjia = -np.sum(EEYh * (e - powerchange)) - np.sum(EEYg * (e - powerchange)) + np.sum(
                ZZNh * (f + powerchange)) + np.sum(ZZNg * (f + powerchange))
            bhujianjian = -np.sum(EEYh * (e - powerchange)) - np.sum(EEYg * (e - powerchange)) + np.sum(
                ZZNh * (f - powerchange)) + np.sum(ZZNg * (f - powerchange))
            department_utilityjiajia[turn] = bhujiajia
            department_utilityjiajian[turn] = bhujiajian
            department_utilityjianjia[turn] = bhujianjia
            department_utilityjianjian[turn] = bhujianjian
            Ee[turn] = e
            Ff[turn] = f
            bhu = (bhujiajia + bhujiajian + bhujianjia + bhujianjian) / 4
            department_utility[turn] = bhu
            if bb in XX:
                jiajiamean = np.mean(department_utilityjiajia[(bb - powerinterval):bb])
                jiajianmean = np.mean(department_utilityjiajian[(bb - powerinterval):bb])
                jianjiamean = np.mean(department_utilityjianjia[(bb - powerinterval):bb])
                jianjianmean = np.mean(department_utilityjianjian[(bb - powerinterval):bb])
                if jiajiamean == np.maximum(np.maximum(np.maximum(jiajiamean, jiajianmean), jianjiamean), jianjianmean):
                    e = np.maximum(0, e + powerchange)
                    f = f + powerchange
                elif jiajianmean == np.maximum(np.maximum(np.maximum(jiajiamean, jiajianmean), jianjiamean),
                                               jianjianmean):
                    e = np.maximum(0, e + powerchange)
                    f = np.maximum(0, f - powerchange)
                elif jianjiamean == np.maximum(np.maximum(np.maximum(jiajiamean, jiajianmean), jianjiamean),
                                               jianjianmean):
                    e = np.maximum(0, e - powerchange)
                    f = f + powerchange
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
        YgdealtoneighborVR[faith, lina] = np.mean(Ygdealtoneighbor[-1000:])
        YgdealtopoolVR[faith, lina] = np.mean(Ygdealtopool[-1000:])
        YgnotdealVR[faith, lina] = np.mean(Ygnotdeal[-1000:])
        YhdealtoneighborVR[faith, lina] = np.mean(Yhdealtoneighbor[-1000:])
        YhdealtopoolVR[faith, lina] = np.mean(Yhdealtopool[-1000:])
        YhnotdealVR[faith, lina] = np.mean(Yhnotdeal[-1000:])
        NgdealtoneighborVR[faith, lina] = np.mean(Ngdealtoneighbor[-1000:])
        NgdealtopoolVR[faith, lina] = np.mean(Ngdealtopool[-1000:])
        NgnotdealVR[faith, lina] = np.mean(Ngnotdeal[-1000:])
        NhdealtoneighborVR[faith, lina] = np.mean(Nhdealtoneighbor[-1000:])
        NhdealtopoolVR[faith, lina] = np.mean(Nhdealtopool[-1000:])
        NhnotdealVR[faith, lina] = np.mean(Nhnotdeal[-1000:])
        department_utilityVR[faith, lina] = np.mean(department_utility[-1000:])
        EeVR[faith, lina] = np.mean(Ee[-1000:])
        FfVR[faith, lina] = np.mean(Ff[-1000:])

df8 = pd.DataFrame(YgdealtoneighborVR)
df8.to_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx')
df9 = pd.DataFrame(YgdealtopoolVR)
df9.to_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以可再生能源为主的电力企业与pool交易人数.xlsx')
df10 = pd.DataFrame(YgnotdealVR)
df10.to_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以可再生能源为主的电力企业不交易人数.xlsx')
df11 = pd.DataFrame(YhdealtoneighborVR)
df11.to_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以传统能源为主的电力企业与邻居交易人数.xlsx')
df12 = pd.DataFrame(YhdealtopoolVR)
df12.to_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以传统能源为主的电力企业与pool交易人数.xlsx')
df13 = pd.DataFrame(YhnotdealVR)
df13.to_excel('E:\\data\火电绿电\第一部分\pgpe\完成配额以传统能源为主的电力企业不交易人数.xlsx')
df14 = pd.DataFrame(NgdealtoneighborVR)
df14.to_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以可再生能源为主的电力企业与邻居交易人数.xlsx')
df15 = pd.DataFrame(NgdealtopoolVR)
df15.to_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以可再生能源为主的电力企业与pool交易人数.xlsx')
df16 = pd.DataFrame(NgnotdealVR)
df16.to_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以可再生能源为主的电力企业不交易人数.xlsx')
df17 = pd.DataFrame(NhdealtoneighborVR)
df17.to_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以传统能源为主的电力企业与邻居交易人数.xlsx')
df18 = pd.DataFrame(NhdealtopoolVR)
df18.to_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以传统能源为主的电力企业与pool交易人数.xlsx')
df19 = pd.DataFrame(NhnotdealVR)
df19.to_excel('E:\\data\火电绿电\第一部分\pgpe\未完成配额以传统能源为主的电力企业不交易人数.xlsx')
df20 = pd.DataFrame(department_utilityVR)
df20.to_excel('E:\\data\火电绿电\第一部分\pgpe\监管部门效用.xlsx')
df21 = pd.DataFrame(EeVR)
df21.to_excel('E:\\data\火电绿电\第一部分\pgpe\监管部门奖励.xlsx')
df22 = pd.DataFrame(FfVR)
df22.to_excel('E:\\data\火电绿电\第一部分\pgpe\监管部门惩罚.xlsx')
# Yh=0;Yg=1;Nh=2;Ng=3







