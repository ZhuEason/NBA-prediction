# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:06:21 2016

@author: hbsong
"""

import pandas as pd
from sklearn import linear_model
import numpy as np
import math

df1 = pd.read_table(str(5) + '-' + str(6) + 'RD.Team.txt')
df2 = pd.read_table(str(5) + '-' + str(6) + 'RD.team.Opp.txt')
df = pd.concat([df1, df2[df2.columns[4:]]], axis = 1)
for i in range(6, 15):
    df1 = pd.read_table(str(i) + '-' + str(i + 1) + 'RD.Team.txt')
    df2 = pd.read_table(str(i) + '-' + str(i + 1) + 'RD.team.Opp.txt')
    df = df.append(pd.concat([df1, df2[df2.columns[4:]]], axis = 1))
LR_1 = linear_model.LinearRegression()
LR_1.fit(df[df.columns[3:]], df[u'won'])

df1 = pd.read_table(str(15) + '-' + str(16) + 'RD.Team.txt')
df2 = pd.read_table(str(15) + '-' + str(16) + 'RD.team.Opp.txt')
df_test = pd.concat([df1, df2[df2.columns[4:]]], axis = 1)

r = LR_1.predict(df_test[df_test.columns[3:]])
t = df_test[u'won']
l = []
for i in range(30):
    l.append(abs(r[i] - t[i]))
s = 0
for i in l:
    s += i
print s / 30.0
print np.std(l)
