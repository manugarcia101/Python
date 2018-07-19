# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:40:46 2018

@author: Manu
"""

#!Python 3.6.3
#Author: Manuel García López

#Machine Learning
import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close',
         'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Open'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close' 
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])

x = preprocessing.scale(x)

#x = x[:-forecast_out+1] 
y = np.array(df['label'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size = 0.2)

clf = LinearRegression(n_jobs = -1) 
#linear regression algorithm (-1 is max n_jobs that your cores allow)
#clf=svm.SVR(kernel = 'poly') #support vector regression algorithm
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)



print(df.head())