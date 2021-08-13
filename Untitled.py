#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


playstore_data=pd.read_csv('googleplaystore.csv')
playstore_data.head()


# In[3]:


playstore_data.shape


# In[4]:


playstore_data.info()


# In[5]:


playstore_data.describe()


# In[6]:


playstore_data.isnull().sum()


# In[7]:


playstore_data.boxplot('Rating')


# In[8]:


playstore_data['Rating'].fillna(value=playstore_data['Rating'].mean(),inplace=True)


# In[9]:


playstore_data.isnull().sum()


# In[10]:


playstore_data.boxplot('Rating')


# In[22]:


playstore_data['Current Ver'].fillna(str(playstore_data['Current Ver'].mode().values[0]),inplace=True)
playstore_data['Type'].fillna(str(playstore_data['Type'].mode().values[0]),inplace=True)
playstore_data['Android Ver'].fillna(str(playstore_data['Android Ver'].mode().values[0]),inplace=True)


# In[23]:


playstore_data.isnull().sum()


# In[14]:


playstore_data.boxplot('Reviews')


# In[15]:


playstore_data.hist()


# In[27]:


playstore_data["Price"]=playstore_data["Price"].apply(lambda x: str(x).replace('$','')if '$' in str(x) else str(x))
playstore_data["Price"]=playstore_data["Price"].apply(lambda x: float(x))


# In[28]:


playstore_data["Installs"]=playstore_data["Installs"].apply(lambda x: str(x).replace('+','')if '+' in str(x) else str(x))
playstore_data["Installs"]=playstore_data["Installs"].apply(lambda x: str(x).replace(',','')if ',' in str(x) else str(x))
playstore_data["Installs"]=playstore_data["Installs"].apply(lambda x: float(x))


# In[29]:


playstore_data.head()


# In[30]:


playstore_data.info()


# In[32]:


playstore_data.describe()


# In[44]:


grp=playstore_data.groupby('Category')
a=grp['Installs'].agg(np.sum)
x=grp['Rating'].agg(np.mean)
y=grp['Price'].agg(np.sum)
z=grp['Reviews'].agg(np.mean)
print(x)
print(y)
print(z)


# In[40]:


plt.figure(figsize=(16,5))
plt.plot(x,'ro')
plt.xticks(rotation=90)
plt.show()


# In[41]:


plt.figure(figsize=(16,5))
plt.plot(y,'--')
plt.xticks(rotation=90)
plt.show()


# In[43]:


plt.figure(figsize=(16,5))
plt.plot(z,'v')
plt.xticks(rotation=90)
plt.show()


# In[45]:


plt.figure(figsize=(16,5))
plt.plot(a,'ro')
plt.xticks(rotation=90)
plt.show()


# In[46]:


sns.jointplot(x=x,y=y)
plt.show()


# In[ ]:




