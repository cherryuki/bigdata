#!/usr/bin/env python
# coding: utf-8

# **21-03-10 python 12_데이터프레임과 시리즈(Pandas) (c)cherryuki (ji)**

# # 판다스 연습문제

# In[6]:


import pandas as pd
import numpy as np
import random
from statsmodels.api import datasets
iris_df = datasets.get_rdataset("iris", package="datasets").data
iris_df.head()


# In[2]:


#1단계: iris 데이터에서 결측치를 인위적으로 random하게 열마다 20씩 결측치를 할당한다
print(random.sample(range(len(iris_df)),20), end=' ')


# In[3]:


rownum = {0:random.sample(range(len(iris_df)), 20), 1:random.sample(range(len(iris_df)), 20), 
          2:random.sample(range(len(iris_df)), 20), 3:random.sample(range(len(iris_df)), 20)}
print(rownum)


# In[5]:


#방법1
for (idx, row) in rownum.items():
    iris_df.iloc[row, idx] = np.nan
iris_df.isnull().sum()


# In[7]:


#방법2
for col in range(iris_df.shape[1]-1):
    iris_df.iloc[random.sample(range(len(iris_df)),20),col] = np.nan
iris_df.isna().sum()


# In[9]:


#2단계: 결측치가 있는 iris데이터를 출력
iris_df_grouped = iris_df.groupby(iris_df.Species)
iris_df_grouped.count()


# In[10]:


iris_df[iris_df['Sepal.Length'].isnull()] #20개


# In[11]:


iris_df[iris_df['Sepal.Width'].isnull()].head()


# In[12]:


iris_df[iris_df['Petal.Length'].isnull()].head()


# In[13]:


iris_df[iris_df['Petal.Width'].isnull()].head() 


# In[14]:


#3단계: 결측치를 열평균으로 대체된 iris데이터를 출력
iris_df.mean()


# In[15]:


iris_df = iris_df.fillna(value=iris_df.mean())
iris_df.head()


# In[16]:


iris_df.groupby(iris_df.Species).count()


# ## 연습문제 실습형

# In[18]:


import seaborn as sns
iris = sns.load_dataset('iris')
type(iris)


# In[20]:


#1. iris 데이터에서 처음 다섯개 행만 출력하세요
iris.head()
iris[:5]


# In[22]:


#2. iris 데이터를 독립변수 X와 종속변수 y로 나누세요. 종속변수는 species 열입니다.
X = iris.iloc[:, :-1]
y = iris.iloc[:, -1]


# In[23]:


type(X), type(y)


# In[24]:


y.to_frame() #데이터프레임으로 바꿔도 되고 안바꿔도 문제 없음


# In[25]:


#3. iris 데이터에서 처음 50개행을 빼내서 temp변수에 저장하세요
temp = iris[:50]


# In[26]:


#4.  3번에서 선택한 데이터프레임의 요약정보를 출력하세요. 모든 열에 대해 요약정보가출력되어야 합니다.
temp.describe(include='all')


# In[29]:


#5. versicolor종의 데이터만 iris_versicolor변수에 저장하세요
iris_versicolor = iris[iris.species=='versicolor']
iris_versicolor.head()


# In[30]:


#6. 2번의 X와 y변수를 합해서 iris_df데이터 프레임으로 만드세요
iris_df = pd.concat([X,y], axis=1)
iris_df.head()


# In[31]:


#7. iris데이터의 각 열 평균값을 출력
iris.mean()


# In[32]:


#8. iris 데이터의 각 열들 사이의 상관계수를 출력
iris.corr()


# In[34]:


import seaborn as sns
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
sns.heatmap(iris.corr(), annot=True, cmap="Blues", fmt=".1f")
plt.show()


# In[36]:


#9. iris 데이터에서 각 요소들과 변수별 평균과의 차이를 출력(처음 다섯개 행 출력)
iris.iloc[:,:4].apply(lambda x:x-iris.mean(), axis=1).head()


# In[39]:


#10. iris 데이터의 종별 평균
species_mean = iris.groupby(iris.species).mean()
species_mean


# In[40]:


#11. iris 데이터에서 각 요소들과 종별 변수의 평균과의 차이를 출력(각 종별로 3개씩 출력)
species_mean.loc['setosa', :]


# In[41]:


iris.apply(lambda x:x-species_mean.loc[x.species,:], axis=1)


# In[42]:


iris.apply(lambda x:x-species_mean.loc[x.species,:], axis=1).groupby(iris.species).head(3)


# In[43]:


iris.apply(lambda x:x-species_mean.loc[x.species,:], axis=1).groupby(iris.species).take(range(3))


# In[44]:


#참고: Why 열 순서가 변경되는지(열 개수가 다름;4개에서 5개를 뺌)
iris_mean_by_species = iris.groupby(iris.species).mean()
print(iris_mean_by_species.index)
print(iris_mean_by_species.columns)
print(iris_mean_by_species.loc['setosa',:])


# In[45]:


a = iris_mean_by_species.loc['setosa',:]
b = iris.loc[0]
print(a)
print()
print(b[:-1])
print()
print(a-b[:-1])
print()
print(a-b) #4개에서 5개를 빼면 순서가 뒤바뀜


# In[ ]:




