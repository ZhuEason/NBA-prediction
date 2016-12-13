# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 16:13:50 2016

@author: Eason
"""

import pandas as pd
from sklearn import linear_model
import numpy as np
import math
from sklearn import preprocessing

playerPerformanceLastSeasonAvg = []
teamPerformanceThisSeason = []

min_max_scaler = preprocessing.MinMaxScaler()

for year in range(5, 15):
    df0 = pd.read_table(str(year) + "-" + str(year+1) + 'RD.Each.txt')
    df1 = pd.read_table(str(year+1) + "-" + str(year+2) + 'RD.Each.txt')
    
    df2 = pd.read_table(str(year+1) + '-' + str(year+2) + 'RD.Team.txt')
    df3 = pd.read_table(str(year+1) + '-' + str(year+2) + 'RD.Team.Opp.txt')
    
    df4 = pd.concat([df2, df3[df3.columns[4:]]], axis = 1)
    
    for i in range(len(df4.index)):
        df4.ix[i, 'team'] =  df4["team"][i][0:3].lower()
    
    playerPerformanceInLastSeason = {} # a map, key is the player's name, value is sta for this player.
    teamMemberInThisSeason = {} # a map, key is the team name, value is the current member name    
    
    for i in range(len(df0.index)):
        playerPerformanceInLastSeason[df0.iloc[i][0]] = df0.loc[i][df0.columns[3:]]
    
    #teamMemberInThisSeason is the new season sta.
    for i in range(len(df1.index)):
        teamMemberInThisSeason.setdefault(df1.iloc[i][1], []).append(df1.iloc[i][0])
        
    # The last season's player's performance in the new team.
    relationBetweenTeamAndPlayer = {} #a map, key is the team name, the value is a list of avg new player performance
    test_playerPerformanceLastSeasonAvg = {}
    for teamName in teamMemberInThisSeason:
        totalMin = 0.0
        playerAvgPerformance = []
        playerToTeamPerformance = []
        for player in teamMemberInThisSeason[teamName]:
            if (playerPerformanceInLastSeason.has_key(player)):
                totalMin += playerPerformanceInLastSeason[player]['Min']
                playerToTeamPerformance.append(playerPerformanceInLastSeason[player])
        for j in range(len(playerToTeamPerformance[0])):
            sum = 0.0
            for i in range(len(playerToTeamPerformance)):
                sum += playerToTeamPerformance[i][j] * playerToTeamPerformance[i]['Min']
            playerAvgPerformance.append(sum / totalMin)
        relationBetweenTeamAndPlayer[teamName] = playerAvgPerformance
        if len(df4[df4[u'team'] == teamName]) != 0:
            playerPerformanceLastSeasonAvg.append(playerAvgPerformance)
            if len(playerPerformanceLastSeasonAvg) >= 270:
                test_playerPerformanceLastSeasonAvg[teamName] = len(playerPerformanceLastSeasonAvg)
        else:
            print teamName, year
        
    
    df5 = df4[df4[u'team'] == 'san'];
    Col = df4.columns[3:]
    teamPerformanceThisSeason.append(df4[df4[u'team'] == 'san'][Col].values.tolist()[0])
    for teamName in relationBetweenTeamAndPlayer:
        if teamName != 'san':
            if len(df4[df4[u'team'] == teamName]) != 0:
                df5 = df5.append(df4[df4[u'team'] == teamName])
                teamPerformanceThisSeason.append(df4[df4[u'team'] == teamName][Col].values.tolist()[0])
            else:
                print teamName, year

LR = linear_model.LinearRegression()
minmax_playerPerformanceLastSeasonAvg = min_max_scaler.fit_transform(playerPerformanceLastSeasonAvg)
LR.fit(minmax_playerPerformanceLastSeasonAvg[:270], teamPerformanceThisSeason[:270])

res = LR.predict(minmax_playerPerformanceLastSeasonAvg[test_playerPerformanceLastSeasonAvg['san']])
