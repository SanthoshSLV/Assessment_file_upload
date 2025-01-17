# -*- coding: utf-8 -*-
"""LVADSUSR112-Santhsoh-FA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wqNdL7zExHsmmxiNNaGPOMJ8jw-u1lMm
"""

#1
import pandas as pd
data=pd.read_excel('/content/Walmart_Dataset Python_Final_Assessment.xlsx')
data.info()
print(f'Number of rows:{data.shape[0]}\nNumber of columns:{data.shape[1]}')

#2
print(f"Number of null values:\n{data.isnull().sum()}")
print(f"Number of duplicate values{data.duplicated().sum()}")

#3
print('Sales Data')
print(f"Mean of Sales Data:{data.describe()['Sales'].loc['mean']}")
print(f"Standard Deviation of Sales Data:{data.describe()['Sales'].loc['std']}")
print(f"Median of Sales data:{data['Sales'].median()}")
print(f"Mode of Sales data:{data['Sales'].mode().iloc[0]}")
print(f"Maximum of Sales Data:{data.describe()['Sales'].loc['max']}")
print(f"Minimum of Sales Data:{data.describe()['Sales'].loc['min']}")
print(f"Variance of Sales data:{data['Sales'].var()}")

#4
pd.to_numeric(data['Profit'])
sales_by_category=data.groupby(['Category','Order Date']).aggregate({'Sales':'sum','Quantity':'sum','Profit':'sum'})
sns.barplot(sales_by_category,x='Category',y='Sales',hue='Category')

#5
data.corr()
print(data.describe())

#6
q1=data.describe().loc['25%']
q3=data.describe().loc['75%']
uw=q3+(q3-q1)*1.5
lw=q1-(q3-q1)*1.5
data[(data['Sales']>uw[0])|(data['Sales']<lw[0])|
 ((data['Quantity']>uw[1])|(data['Quantity']<lw[1]))|
  ((data['Profit']>uw[2])|(data['Profit']<lw[2]))]

#7.1
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt
order_year=[]
for date in data['Order Date']:
  order_year.append(date.year)
data['Order Year']=order_year
sales_by_category=data.groupby(['Category','Order Year']).aggregate({'Sales':'sum','Quantity':'sum','Profit':'sum'})
sns.lineplot(sales_by_category,x='Order Year',y='Sales',hue='Category')
plt.legend(loc=(1,0))
plt.show()
sns.lineplot(sales_by_category,x='Order Year',y='Profit',hue='Category')
plt.legend(loc=(1,0))
plt.show()

#7.2
sales_by_customer=data.groupby('EmailID').aggregate({'Sales':'sum','Order ID':'count'}).reset_index()
names=[]
for email in sales_by_customer.iloc[:,0]:
  names.append(email[:email.index('@')])
sales_by_customer['Names']=names
top5_by_sales=sales_by_customer.sort_values(by='Sales',ascending=False).iloc[:5]
sns.barplot(top5_by_sales,x='Names',y='Sales')
plt.title('Top 5 Customers by Total sales')
plt.ylabel('Total Sales')
plt.show()
top5_by_order=sales_by_customer.sort_values(by='Order ID',ascending=False).iloc[:5]
sns.barplot(top5_by_order,x='Names',y='Order ID')
plt.title('Top 5 Customers by Total Orders')
plt.ylabel('Total Orders')
plt.show()
sales_by_customer=data.groupby('EmailID').aggregate({'Order Date':['max','min'],'Order ID':'count'}).reset_index()
sales_by_customer['Average_bt_orders']=(sales_by_customer['Order Date']['max']-sales_by_customer['Order Date']['min'])/sales_by_customer['Order ID']['count']
print(sales_by_customer)

#7.3
sales_by_loc=data.groupby('Geography').aggregate({'Sales':'sum','Order ID':'count'}).reset_index()
sales_by_loc['Sales'].plot(kind='pie')
plt.show()
top5_by_loc=sales_by_loc.sort_values(by='Sales',ascending=False).iloc[:5]
print(top5_by_loc)
sns.barplot(top5_by_loc,x='Geography',y='Sales')
'''The sales data has been analyzed for based on the geography and the total sales amount
and the total orders placed are observed from the given table for tehanalysis of the sales volume and
order intensity in the given data'''

data['Days']=data['Ship Date']-data['Order Date']
order_to_shipment_loc=data.groupby('Geography').aggregate({'Days':['max','min','mean'],'EmailID':'count'}).reset_index()
'''From the above data we can obtain the average time, maximum time and minimum time from order date to shipment date
to better understand the time taken foe delivery focused on the geography and the number of orders to
prioritize the specific regions for shipment. '''