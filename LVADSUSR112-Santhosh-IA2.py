# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VlcI7bJesTlrLc-70jH5-HjOL2NUfFKc
"""

#1
import numpy as np
rbg_image=np.array([[[255,0,0],[0,255,0],[0,0,255]],
                    [[255,255,0],[255,0,255],[0,255,255]],
                    [[127,127,127],[200,200,200],[50,50,50]]])
grey_scale=np.empty((3,3))
for row in range(len(rbg_image)):
  for column in range(len(rbg_image[0])):
    grey_scale[row][column]=0.2989*rbg_image[row][column][0]+0.5870*rbg_image[row][column][1]+0.1140*rbg_image[row][column][2]
print(grey_scale)

#3
sensors=np.array([[[255,0,0],[0,255,0],[0,0,255]],
                    [[255,255,0],[255,0,255],[0,255,255]],
                    [[127,127,127],[200,200,200],[50,50,50]]])

altered_data=sensors.flatten()
altered_data=altered_data.reshape(len(sensors),int(sensors.size/len(sensors)))
print(altered_data)

#4
athletes=np.array([[80,96,98,76,78,89,92,99],[80,96,68,76,74,39,82,93],[89,86,98,96,88,79,97,89]])
improvement=[]
for athlete in athletes:
  improvement.append(athlete[-1]-athlete[0])

for i in range(len(improvement)):
  print(f"Athlete {i+1}:{improvement[i]}")

#5
students=np.array([[90,99,98,89,88],[90,89,98,89,-1],[80,99,78,80,98],
                    [90,89,78,99,98],[90,-1,98,89,-1],[70,80,68,-1,88]])
avg_last3=[]
for student in students:
  avg_last3.append(np.mean(student[-3:][np.where(student[-3:]!=-1)]))
print(avg_last3)

#6
cities=np.array([[90,99,98,89,88],[90,89,98,89,90],[80,99,78,80,98],
                    [90,89,78,99,98],[90,98,98,89,99],[70,80,68,89,88]])
calibration=np.array([0.98,0.99,0.95,0.89,0.88])
cities=cities*calibration
print(cities)

#7
import pandas as pd
data={'Name':['Alice','Bob','Charlie','Eve','Frank','Grace'],
      'Age':[25,30,35,40,45,50,55],
      'City':['New York','Los Angeles','Chicago','Houston','Phoenix','Miami','Boston'],
      'Department':['HR','IT','Finance','Marketing','Sales','IT','HR']}
for column,value in data.items():
  data[column]=pd.Series(value)
emp_df=pd.DataFrame(data)
emp_df[(emp_df['Age']<45)&(emp_df['Department']!='HR')][['Name','City']]

#8
data_dict={'Product':['Apples','Bananas','Cherries','Dates','Elderberries','Flour','Grapes'],
      'Category':['Fruit','Fruit','Fruit','Fruit','Fruit','Bakery','Fruit'],
      'Price':[1.2,0.5,3.0,2.5,4.0,1.5,2.0],
      'Promotion':[True,False,True,True,False,True,False]}
data=pd.DataFrame(data_dict)
data[(data['Category']=='Fruit')&(data['Promotion']==False)&(data['Price']>data[data['Category']=='Fruit']['Price'].mean())]

#9
emp_data={'Employee':['Alice','Bob','Charlie','David'],
      'Department':['HR','IT','Finance','IT'],
      'Manager':['John','Rachel','Emily','Rachel']}
emp_df=pd.DataFrame(emp_data)
project_data={'Employee':['Alice','Charlie','Eve'],
              'Project':['P1','P3','P2']}
project_df=pd.DataFrame(project_data)
org_data=pd.merge(emp_df,project_df,on='Employee',how='outer')
print(org_data)

#10
data={'Department':['Electronics','Electronics','Clothing','Clothing','Home','Goods'],
      'Salesperson':['Alice','Bob','Charlie','David','Eve'],
      'Sales':[70000,50000,30000,40000,60000]}
for key,value in data.items():
  data[key]=pd.Series(value)
sale_df=pd.DataFrame(data)
pd.pivot_table(sale_df,values='Sales',index=['Department','Salesperson'],aggfunc='mean')