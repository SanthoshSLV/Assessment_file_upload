# -*- coding: utf-8 -*-
"""LADSUSR112_Santhosh_lab4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cPwjHMb6361QEzEUPTYuugKAKLeRvBa8
"""

#LAB 4
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('/content/social_network.csv')

#Removing null and dupliactes
data.isnull().sum()
data.duplicated().sum()

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

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

LE=LabelEncoder()
#Approved 0 Rejected 1
data['account_creation_date']=LE.fit_transform(data['account_creation_date'])
data['account_status']=LE.fit_transform(data['account_status'])


RFC=IsolationForest(contamination=0.5)
result=RFC.fit_predict(data.iloc[:,2:-1])
data['predicted']=result