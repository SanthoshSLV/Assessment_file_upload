# -*- coding: utf-8 -*-
"""LVADSUSR112_Santhosh_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r1P9Jhu_9-a6wUvyJODUIuI-5Y5Qix36
"""

#LAB 2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv('/content/auto-mpg.csv')

#Removing null and dupliactes
data['displacement'].replace(np.NaN,data['displacement'].mean(),inplace=True)
data['horsepower'].replace(np.NaN,0,inplace=True)
data['horsepower'].replace('?',0,inplace=True)
data['horsepower']=data['horsepower'].astype(dtype='int64')
data['acceleration'].replace(np.NaN,data['acceleration'].mean(),inplace=True)
print(data.isnull().sum())
print(data.duplicated().sum())


#Outlier detection
data.info()
print(data.describe())

data.plot(kind='box')
plt.xticks(rotation=90)
plt.show()

for column in data.describe():
  data[column].plot(kind='hist')
  plt.xlabel(column)
  plt.show()

values=data.describe()
Q1=values.loc['25%']
Q3=values.loc['75%']
upper_bound=Q3+(Q3-Q1)*1.5
lower_bound=Q1-(Q3-Q1)*1.5
outlier=[]
for index in Q1.index:
  number=len(data[(data[index]>upper_bound[index])|(data[index]<lower_bound[index])])
  if number>0:
    outlier.append([index,number])
print(outlier)

#Model Building

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA
from sklearn.metrics import mean_squared_error,mean_absolute_percentage_error,mean_absolute_error,r2_score
from sklearn.model_selection import train_test_split


data.corr()['mpg']

pca=PCA(n_components=1)
decomp1=pca.fit_transform(data[['cylinders','displacement','horsepower','weight','acceleration']])
comparison=pd.DataFrame()
comparison['mpg']=data['mpg']
comparison['design']=decomp1

RFC=LinearRegression()

xtrain,xtest,ytrain,ytest=train_test_split(comparison['design'],comparison['mpg'],test_size=0.2)
RFC=RFC.fit(xtrain,ytrain)
result=RFC.predict(xtest)

print(f'Mean Square Error:{mean_squared_error(ytest,result)}\nMean Absolute Error:{mean_absolute_error(ytest,result)}\nR2 Score:{r2_score(ytest,result)}\n')