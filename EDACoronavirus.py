#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Read CSV file
cor_virus=pd.read_csv(r'C:\Users\Geetha\Desktop\Applied ML class\2019_nCoV_data.csv')
#print top 5 rows
cor_virus.head()


# In[3]:


cor_virus.loc[cor_virus['Country']=='China','Country_label']='1'
cor_virus.head()


# In[122]:


#gives descriptive parameters
cor_virus.describe()


# In[123]:


#know the column names
cor_virus.columns


# In[124]:


#gives count of rows and columns
cor_virus.shape


# In[128]:


#To know max value of a column. Similarly we can find min value
M_value=max(cor_virus['Confirmed'])
M_value


# In[129]:


#info about dataset
cor_virus.info()


# In[130]:


#bool value will be TRUE if there is a null
cor_virus.isna()


# In[4]:


#count of null value
cor_virus.isna().sum()


# In[132]:


#extracting Date from last update
cor_virus['Last Update']=pd.to_datetime(cor_virus['Last Update'])
cor_virus['Last Update'].head(5)


# In[58]:


cor_virus['Date']=cor_virus['Last Update'].dt.day
cor_virus['Date'].head(5)


# In[59]:


#exracting month. Similarly can be done for year, week.
cor_virus['Month']=cor_virus['Last Update'].dt.month
cor_virus['Month'].head(5)


# In[133]:


#unique values of column country.
u_country=cor_virus['Country'].unique()
u_country


# In[134]:


u_values={}
j=1
for i in u_country:
    u_values[i]=j
    j=j+1
print(u_values)   


# In[135]:


#Country Vs Count
plt.figure(figsize = (60,30))
sns.countplot(x='Country',data=cor_virus)


# In[78]:


#sum the count of confirmed cases w.r.t country
CC=cor_virus.groupby('Country')['Confirmed'].sum().reset_index(drop=False).sort_values(by='Confirmed', ascending=True)
CC


# In[79]:


#confirmed Vs Count
plt.figure(figsize = (60,30))
sns.countplot(x='Confirmed',data=cor_virus)


# In[83]:


#sum the count of Death cases w.r.t country
CD=cor_virus.groupby('Country')['Deaths'].sum().reset_index(drop=False).sort_values(by='Deaths', ascending=True)
CD


# In[84]:


#Deaths Vs Count
plt.figure(figsize = (60,30))
sns.countplot(x='Deaths',data=cor_virus)


# In[85]:


#sum the count of Recovered cases w.r.t country
CR=cor_virus.groupby('Country')['Recovered'].sum().reset_index(drop=False).sort_values(by='Recovered', ascending=True)
CR


# In[86]:


#Recovered Vs Count
plt.figure(figsize = (60,30))
sns.countplot(x='Recovered',data=cor_virus)


# In[94]:


plt.figure(figsize=(35,17))
sns.heatmap(cor_virus.drop('Sno', axis=1).corr(),annot=True)


# In[4]:


x=cor_virus[['Confirmed', 'Deaths', 'Recovered']]
y=cor_virus['Country_label']


# In[7]:


from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0)


# In[8]:


import matplotlib.pyplot as plt
from matplotlib import cm
from pandas.plotting import scatter_matrix
cmap = cm.get_cmap('gnuplot')
scatter = scatter_matrix(x_train, c= y_train, marker = '*', diagonal='kde',s=100, alpha=0.6, figsize=(15,15),cmap=cmap)


# In[210]:


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d   # must keep
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x_train['Confirmed'], x_train['Deaths'], x_train['Recovered'], c = y_train, marker = 'o', s=100)
ax.set_xlabel('Confirmed')
ax.set_ylabel('Deaths')
ax.set_zlabel('Recovered')
plt.show()

