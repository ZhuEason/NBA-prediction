#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:23:06 2016

@author: Eason
"""

import pandas as pd
import numpy as np
import math
import operator
from sklearn import preprocessing

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(1, length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getNeighbors(trainingSet, testInstance, k):
    distances = []
    length = len(testInstance)
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key = operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors


def calResult(neighbors):
    result = {}
    count = 0
    
    s = 0
    for neighbor in neighbors:
        s += neighbor[0]
        count += 1
        
    return s / count

    
train_performance = []
train_result = []

for year in range(5, 15): 
    df = pd.read_table(str(year) + '-' + str(year+1) + 'RD.Team.txt')
    train_performance.extend(df[df.columns[2:]].values.tolist())
    season_per = df[df.columns[1]].values.tolist()
    for i in season_per:
        train_result.append([i])

min_max_scaler = preprocessing.MinMaxScaler()
train_minmax = min_max_scaler.fit_transform(train_performance)

for i in range(len(train_result)):
    train_result[i].extend(train_minmax[i])
    

#test data
predict_y = []
for testIns in train_result[-30:]:
    neighbors = getNeighbors(train_result[0:-30], testIns, 5)
    #print neighbors
    predict_y.append(calResult(neighbors))



'''

df = pd.read_table(str(15) + '-' + str(16) + 'RD.Team.txt')

test_minmax = min_max_scaler.fit_transform(df[df.columns[1:]].values.tolist())

test_df = pd.read_table(str(15) + '-' + str(16) + 'RD.Team.txt')
testData = test_df[test_df.columns[2:]].values.tolist()

for testIns in test_minmax:
    neighbors = getNeighbors(train_minmax, testIns, 5)
    print neighbors

'''

'''
votes_train = pd.read_table("votes-train.tsv")
votes_test = pd.read_table("votes-test.tsv")

min_max_scaler = preprocessing.MinMaxScaler()
train_minmax = min_max_scaler.fit_transform(votes_train[votes_train.columns[:]])
test_minmax = min_max_scaler.fit_transform(votes_test[votes_test.columns[:]])

train_y = votes_train[u'Democrat']

test_y = votes_test[u'Democrat']


predict_y = []
for testIns in test_minmax:
    neighbors = getNeighbors(train_minmax, testIns, 5)
    predict_y.append(calResult(neighbors))

index = 0
correct = 0
for index in range(len(predict_y)):
    real_y = test_y[index]
    if real_y == predict_y[index]:
        correct += 1
    index += 1

print (float)(correct)/len(predict_y)
'''

