#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,ConfusionMatrixDisplay


# In[2]:


df=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\movies.csv")


# In[3]:


df.shape


# In[4]:


df=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\ratings.csv")


# In[5]:


df.shape


# In[8]:


uq_you_ids=df['userId'].nunique()

print("unique userId:", uq_you_ids)


# In[9]:


movi_rate_cnt=df.groupby('movieId')['rating'].count()

max_rat_movi_id=movi_rate_cnt.idxmax()

df=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\movies.csv")

max_rat_movi=df[df['movieId']==max_rat_movi_id]['title'].values[0]

print("max no of rating:", max_rat_movi)


# In[11]:


df1=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\movies.csv")

df=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\tags.csv")

mx_movi_id=df1[(df1['title']=='Matrix,The(1999)')]['movieId'].values[0]

mx_tgs=df[df['movieId']==mx_movi_id]['tag']

print("tgs sbmtd by urs to 'Matrix,The(1999)':")
print(mx_tgs.unique())


# In[18]:


df=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\ratings.csv")

df1=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\movies.csv")

trm_movi_id=df1[(df1['title']=='Terminator 2: Judgment Day (1991)')]['movieId'].values[0]

trm_rtgs=df[df['movieId']==trm_movi_id]

avg_rtg=trm_rtgs['rating'].mean()

print("avg usr rtg for 'Terminator 2: Judgment Day (1991)':", avg_rtg)


# In[24]:


df=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\ratings.csv")

df1=pd.read_csv(r"C:\Users\viraj\Desktop\movie_data\links.csv")

avg_rtgs=df.groupby('movieId')['rating'].agg(['count', 'mean']).reset_index()

plr_movis= avg_rtgs[avg_rtgs['count']>50]

df3=pd.merge(plr_movis,df1,on='movieId',how='inner')

high_imdb_movi=df3.nlargest(1,'imdbId')

print("high imdb rtgs:",high_imdb_movi['movieId'].values[0])


# In[ ]:





# In[ ]:





# In[ ]:




