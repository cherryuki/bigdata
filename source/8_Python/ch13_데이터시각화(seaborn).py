#!/usr/bin/env python
# coding: utf-8

# **21-03-11 python 13_데이터 시각화(seaborn) (c)cherryuki (ji)**

# # ch13. 데이터 시각화

# # 3절. Seaborn
# - matplotlib을 기반으로 만든 고수준 그래픽 라이브러리
# - 공식사이트: https://seaborn.pydata.org/
# - API: https://seaborn.pydata.org/api.html
# - Seaborn으로 그래프를 그리기 위해서 다음단계를 따름 <br>
# 1) 데이터 준비<br>
# 2) 미적속성 설정<br>
# 3) 함수를 이용하여 그래프 그리기<br>
# 4) 그래프 출력, 저장

# In[2]:


#새 파일 시작전 설정
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format='retina'")
#한글 설정
plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False) # y축
# 경고 메세지 안 보이게 
import warnings
warnings.filterwarnings(action='ignore')
# warnings.filterwarnings(action='default')


# ## 3.1 데이터 준비하기

# In[3]:


import seaborn as sns
iris = sns.load_dataset('iris')
iris.shape


# In[4]:


iris.tail()


# In[5]:


iris.info() #결측치를 제외한 개수, dtype 등


# In[6]:


iris.isnull().sum()


# In[7]:


iris.describe()


# In[8]:


iris.describe(exclude='float64')


# In[9]:


#R패키지 데이터셋 가져오기(Titanic)
import statsmodels.api as sm
r_titanic = sm.datasets.get_rdataset('Titanic', package='datasets').data
r_titanic.head()


# In[10]:


titanic = sns.load_dataset('titanic')
titanic.head()
#survived; 생존여부, pclass; 티켓 클래스(1,2,3등석), sibsp; 함께 탑승한 형제와 배우자 수
#parch; 함께 탑승한 부모와 아이 수, fare; 탑승료 


# In[11]:


titanic.info()


# ## 3.2 미적 속성 설정하기
# 1) style: white(기본), darkgrid, whitegrid, dark, ticks

# In[12]:


sns.set(style='darkgrid')
ax = sns.scatterplot(x='petal_length', y='petal_width', data=iris)


# 2) 컬러 팔레트
# - https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette
# - https://matplotlib.org/stable/tutorials/colors/colormaps.html
# - https://seaborn.pydata.org/tutorial/color_palettes.html
# - http://hleecaster.com/wp-content/uploads/2019/12/article2_image9.png

# In[14]:


sns.set(palette='Accent', style='white')
# bright/deep/muted/pastel/dark/color blind, ... 등등
sns.scatterplot(x='petal_length', y='petal_width', data=iris, hue='species')


# 3) 컨텍스트(비율) 지정<br>
# - notebook(기본값: 1배율), paper(0.8), talk(1.3), poster(1.6)

# In[15]:


plt.figure(figsize=(10,5))
sns.set_context('notebook', font_scale=1.5, rc={'lines.linewidth':3})
sns.lineplot(x='petal_length', y='petal_width', data=iris)
sns.scatterplot(x='petal_length', y='petal_width', data=iris)
plt.show()


# ## 3.3 Seaborn 함수로 그래프 그리기
# 1) Relational plots: 관계형 그래프

# In[17]:


sns.set(palette='Paired', style='white', font_scale=1, rc={'lines.linewidth':1})
sns.scatterplot(x='petal_length', y='petal_width', data=iris)
plt.show()


# In[18]:


#hue속성에 그룹변수를 넣어 그릅화하여 그룹별 다른 색상, 다른 style
sns.scatterplot(x='petal_length', y='petal_width', data=iris,
                hue='species', palette='husl', style='species')
plt.show()


# In[19]:


sns.lineplot(x='petal_length', y='petal_width', data=iris)
plt.show()


# In[20]:


sns.lineplot(x='petal_length', y='petal_width', data=iris,
             hue='species', palette='husl', style='species')
plt.show()


# In[21]:


sns.scatterplot(x='petal_length', y='petal_width', data=iris, hue='species')
sns.lineplot(x='petal_length', y='petal_width', data=iris)
plt.show()


# In[22]:


fig, axes = plt.subplots(ncols=2, figsize=(8,5))
plt.subplots_adjust(wspace=0.3)
sns.scatterplot(x='petal_length', y='petal_width', data=iris, hue='species', ax=axes[0])
sns.lineplot(x='petal_length', y='petal_width', data=iris, ax=axes[1])
plt.show()


# In[24]:


#lineplot을 서브플롯으로 표현: relplot
sns.relplot(x='petal_length', y='petal_width', data=iris, hue='species',
           kind='line',    #기본값은 scatter
           col='species',  #col단위로 서브플롯 표현
           col_wrap=3)     #한 줄에 표현될 서브플롯 수
plt.show()


# 2) categorical plots; 범주형 그래프

# In[25]:


#x축이 범주형 데이터일 경우 scatterplot은 적합하지 않음
sns.scatterplot(x='species', y='petal_length', data=iris)


# In[26]:


#x축이 범주형일 때 쓰는 산점도1
ax = sns.stripplot(x='species', y='petal_length', data=iris)


# In[27]:


##x축이 범주형일 때 쓰는 산점도2: 산점도들이 중첩되지 않게
ax = sns.swarmplot(x='species', y='petal_length', data=iris)


# In[28]:


titanic.head()


# In[29]:


#성별 survived의 평균을 막대 그래프로
sns.barplot(x='sex', y='survived', data=titanic)  #기본값: estimator=mean, ci=95(95%신뢰구간)


# In[30]:


#class별로 따로 성별 생존률 평균 (hue:그룹화 조건) 
sns.barplot(x='sex', y='survived', data=titanic, ci=None, hue='class')


# In[31]:


# barplot을 서브플롯으로: catplot
ax = sns.catplot(x='sex', y='survived', data=titanic, hue='class', kind='bar', col='class', ci=None)


# In[33]:


#deck별 관측수를 막대그래프로
sns.countplot(x='deck', data=titanic, palette='Greens_d')


# In[34]:


#class별 survived 값을 sex별로 pointplot
plt.figure(figsize=(8,4))
sns.pointplot(x='class', y='survived', hue='sex', data=titanic,
             palette={'male':'b', 'female':'r'}, markers=['^','o'], linestyles=['-','--'])


# 범례 위치 조정: https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot

# In[35]:


#boxplot, voilinplot, boxenplot
sns.set(palette='Set3', style='white', font_scale=1, rc={'lines.linewidth':1})
sns.boxplot(y='sex', x='age', data=titanic, hue='survived')
plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
plt.show()


# In[36]:


sns.violinplot(y='sex', x='age', data=titanic, hue='survived')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()


# - 산점도 관련 참고: https://www.autodesk.com/research/publications/same-stats-different-graphs (공룡 모양)

# In[37]:


sns.boxplot(x='alive', y='age', hue='adult_male', data=titanic)
plt.show()


# In[38]:


sns.boxenplot(x='alive', y='age', hue='adult_male', data=titanic)
plt.show()


# 3) pairplot; 쌍관계 그래프

# In[39]:


sns.pairplot(data=iris, hue='species', palette='husl', markers=['o', 's', 'D'])


# In[44]:


import numpy as np
x = np.random.randn(100)
len(x)


# In[45]:


sns.displot(x, kde=False)


# 4) lmplot, regplot; 회귀 그래프

# In[47]:


sns.lmplot(x='petal_length', y='petal_width', data=iris, hue='species', palette='Accent')


# In[48]:


#회귀 모형을 만드는 함수: lmplot, regplot
sns.lmplot(x='petal_width', y='petal_length', data=iris)


# In[49]:


#회귀 모형을 만드는 함수: lmplot, regplot
#regplot의 단점: hue를 사용할 수 없음
sns.regplot(x='petal_width', y='petal_length', data=iris)


# In[50]:


sns.lmplot(x='petal_width', y='petal_length', data=iris, hue='species',
          col='species', col_wrap=3, palette='deep')


# 5) Matrix plots; 행렬 그래프

# In[53]:


plt.figure(figsize=(10,5))
sns.heatmap(iris.corr(), vmin=-1, vmax=1, annot=True, cmap='YlGnBu', fmt='.1f')
#annot=True; 값 표현


# ## 3.4 다중 그래프를 위한 FacetGrid
# - https://seaborn.pydata.org/tutorial/axis_grids.html#conditional-small-multiples

# In[55]:


g = sns.FacetGrid(iris, col='species', hue='species', palette='Set2')
g.map(plt.hist, 'sepal_length')
g.set_axis_labels(y_var='count')
plt.show()


# In[57]:


g = sns.FacetGrid(iris, col='species', hue='species', palette='Set2')
g.map(sns.scatterplot, 'petal_length', 'petal_width', size=iris.sepal_length)
plt.savefig('data/ch13_graph2.png')
#sns.scatterplot(x='petal_length', y='petal_width', data=iris)


# In[ ]:




