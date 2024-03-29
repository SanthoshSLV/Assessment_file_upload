# -*- coding: utf-8 -*-
"""LVADSUSR112_Santhosh_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18dtijsw2wBYmxygmo-uJ-vuhnpLazL2H
"""

import pandas as pd
import numpy as np
expenses_df=pd.read_csv("/content/booking.csv")
expenses_df

expenses_df.isnull().sum()

expenses_df.describe()

import matplotlib.pyplot as plt
expenses_df['lead time'].plot(kind='hist')
expenses_df['average price'].plot(kind='hist')

q3=expenses_df.describe().loc['75%']
q1=expenses_df.describe().loc['25%']
uw=q3+(q3-q1)*1.5
lw=q1-(q3-q1)*1.5

for index in q3.index:
  for data in expenses_df[((expenses_df[index]>uw[index]) | (expenses_df[index]<lw[index]))].index:
    expenses_df.loc[data,index]=expenses_df.describe().loc['50%',index]

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
expenses_df['type of meal']=le.fit_transform(expenses_df['type of meal'])
expenses_df['room type']=le.fit_transform(expenses_df['room type'])
expenses_df['booking status']=le.fit_transform(expenses_df['booking status'])
expenses_df['market segment type']=le.fit_transform(expenses_df['market segment type'])
expenses_df

expenses_df.corr()

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
LR=LogisticRegression()
x_train,x_test,y_train,y_test=train_test_split(expenses_df.iloc[:,:-1],expenses_df.iloc[:,-1],test_size=0.2)
LR=LR.fit(x_train,y_train)
result=LR.predict(x_test)
print(metrics.accuracy_score(y_test,result))