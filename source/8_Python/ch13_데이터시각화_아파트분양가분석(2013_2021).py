#!/usr/bin/env python
# coding: utf-8

# **21-03-12 python 13_데이터 시각화(seaborn) (c)cherryuki (ji)**

# # ch13_데이터 시각화_빅데이터 처리 시스템 포트폴리오
# ## 예제1) 전국 신규 민간 아파트 분양가격 동향

# ### 1. 시작 전 설정

# In[1]:


#새 파일 시작전 설정
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineVackend.figure_format = 'retina'")
#한글 설정
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False) #y축
#경고 메시지 안보이게
import warnings
warnings.filterwarnings(action='ignore')
# warnings.filterwarnings(action='default') #경고 메시지 보이게


# In[54]:


import pandas as pd
import numpy as np
import seaborn as sns


# ### 2. https://www.data.go.kr “주택도시보증공사_전국 신규 민간아파트 분양가격 동향”
# - ① 2013년9월부터 2015년8월까지 데이터는 df_first 변수에 담아 탐색
# - ② 이후 데이터는 df_last 변수에 담아 탐색

# In[16]:


df_first = pd.read_csv('data/전국 평균 평당 분양가격(2013년 9월부터 2015년 8월까지).csv', encoding='cp949')
df_last = pd.read_csv('data/주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20210215.csv', encoding='CP949')


# In[4]:


df_first.head()


# ### 3. df_last의 데이터 결측치를 확인하고 대체할지 고민

# In[5]:


df_last.isnull().sum() #분양가격에만 결측치 


# In[6]:


df_last.info() #5440 데이터


# ### 4. df_last 데이터셋에 평당분양가격 칼럼 추가

# In[7]:


df_last['분양가격(㎡)'] = pd.to_numeric(df_last['분양가격(㎡)'], errors='coerce')
df_last.info()


# In[8]:


df_last['평당분양가격'] = df_last['분양가격(㎡)']*3.3
df_last.head()


# ### 4-2. 분양가격 , 있는 것도 바꿔서 처리

# In[22]:


df_last = pd.read_csv('data/주택도시보증공사_전국 신규 민간아파트 분양가격 동향_20210215.csv', encoding='CP949')


# In[23]:


type(df_last.loc[0, "분양가격(㎡)"])


# In[24]:


#공백인 부분 결측치 처리하기
df_last[df_last["분양가격(㎡)"]=="  "]


# In[25]:


df_last[df_last["분양가격(㎡)"]=="  "]["분양가격(㎡)"].index
row = [28, 29, 34, 81, 113, 114, 119, 166, 198, 199, 204, 251, 283, 284, 289, 336]
for r in row:
    df_last.loc[r, '분양가격(㎡)'] = np.nan #결측치 넣기


# In[26]:


df_last[df_last["분양가격(㎡)"]=="  "]["분양가격(㎡)"]


# In[27]:


df_last.loc[df_last["분양가격(㎡)"].notnull() & (df_last["분양가격(㎡)"].str.find(",")!=-1)]


# In[28]:


#,를 제거하고 숫자로 바꾸기
df_last['분양가격(㎡)'] = df_last['분양가격(㎡)'].str.replace(',', '')


# In[29]:


df_last.iloc[2125:2129, :]


# In[30]:


type(df_last.loc[2125,'분양가격(㎡)'])


# In[31]:


df_last.isnull().sum() #공백 부분 결측치 처리하여 결측치 개수 늘어남


# In[32]:


df_last['분양가격(㎡)'].describe() #문자형기술통계 요약정보


# In[33]:


#df_last['분양가격(㎡)'] = pd.to_numeric(df_last['분양가격(㎡)'], errors='coerce')
df_last['분양가격(㎡)'] = df_last['분양가격(㎡)'].astype('float64')


# In[34]:


df_last['분양가격(㎡)'].describe() #숫자형 기술통계 요약정보


# In[35]:


df_last.info() #분양가격 개수 4918 -> 4994로 증가(76개)


# In[36]:


df_last['평당분양가격'] = df_last['분양가격(㎡)']*3.3
df_last.head()


# ### 5. df_last 데이터셋에서 전용면적 컬럼을 추가한다(아래와 같이 규모구분 컬럼을 이용)

# In[39]:


df_last['전용면적'] = df_last['규모구분'].apply(lambda x:x.replace('전용면적', '').strip().replace(' ',''))
df_last['전용면적'] = df_last['전용면적'].apply(lambda x:x.replace('초과','~').replace('이하',''))
df_last['전용면적'] = df_last['전용면적'].apply(lambda x:x.replace('모든면적','전체'))
df_last.head()


# In[40]:


#apply대신 str.replace 이용도 동일
df_last['전용면적'] = df_last['규모구분'].str.replace("전용면적", "")
df_last['전용면적'] = df_last['전용면적'].str.replace('초과','~').str.replace('이하','')
df_last['전용면적'] = df_last['전용면적'].str.replace('모든면적','전체').str.replace(' ','')
df_last.head()


# ### 6. 메모리 사용량을 줄이기 위해 사용하지 않을 컬럼은 제거한 후(df_last.drop([‘규모구분’,’분양가격((㎡)’], axis=1 이용), 메모리 사용량을 전후로 확인

# In[41]:


df_last.info() #memory usage: 297.6+ KB


# In[42]:


df_last = df_last.drop(['규모구분', '분양가격(㎡)'], axis=1)
df_last.info() #memory usage: 212.6+ KB


# ### 7. GroupBy(unstack()함수 이용) vs. pivot_table
# - 지역별 데이터 수
# - 지역별 평당분양가격(평균)
# - 전용면적별 평당분양가격(평균)
# - 지역별, 전용면적별 평당분양가격(평균)
# - 연도, 지역별 평당분양가격(평균) - 힌트:unstack()

# In[43]:


#지역별 데이터 수1 - groupby
df_last.groupby(df_last['지역명']).count()


# In[44]:


#지역별 데이터 수2 - pivot_table
df_last.pivot_table(index='지역명', aggfunc='count')


# In[45]:


#지역별 평당분양가격(평균)1 - groupby
df_last.groupby(['지역명'])['평당분양가격'].mean().to_frame()


# In[46]:


#지역별 평당분양가격(평균)2 - pivot_table
pd.pivot_table(df_last, index='지역명', values='평당분양가격')


# In[47]:


#전용면적별 평당분양가격(평균)1 - groupby
t = df_last.groupby(['전용면적'])['평당분양가격'].mean().to_frame()
t = t.loc[['60㎡','60㎡~85㎡','85㎡~102㎡','102㎡~','전체'],:]
t


# In[48]:


#전용면적별 평당분양가격(평균)2 - pivot_table
t = df_last.pivot_table(index='전용면적', values='평당분양가격')
t = t.loc[['60㎡','60㎡~85㎡','85㎡~102㎡','102㎡~','전체'],:]
t


# In[49]:


#지역별, 전용면적별 평당분양가격(평균)1 - groupby
t = df_last.groupby(['지역명','전용면적'])['평당분양가격'].mean().unstack()
t = t.loc[:,['전체','60㎡','60㎡~85㎡','85㎡~102㎡','102㎡~']]
t


# In[50]:


#지역별, 전용면적별 평당분양가격(평균)2 - pivot_table
t = df_last.pivot_table(index=['지역명','전용면적'],values='평당분양가격').unstack()
t.columns = t.columns.droplevel(level=0)
t = t.loc[:,['전체','60㎡','60㎡~85㎡','85㎡~102㎡','102㎡~']]
t


# In[51]:


#연도, 지역별 평당분양가격(평균) - 힌트:unstack()1- groupby
t = df_last.groupby(['지역명', '연도'])['평당분양가격'].mean().unstack()
t


# In[52]:


#5) 연도, 지역별 평당분양가격(평균) - 힌트: unstack()2 - pivot_table
t = df_last.pivot_table(index=['연도', '지역명'], values='평당분양가격').unstack().T
t.index = t.index.droplevel(level=0)
t


# In[55]:


plt.figure(figsize=(15,6))
sns.heatmap(t, annot=True, fmt='.0f', cmap='Blues', annot_kws={'size':12})
plt.show()


# ### 8. 위의 그룹화한 내용을 선그래프와 막대그래프로 시각화

# In[56]:


t2 = df_last.groupby(['지역명'])['평당분양가격'].mean()
t2.plot()
plt.show()


# In[57]:


t2 = pd.pivot_table(df_last, index='지역명', values='평당분양가격').sort_values(by='평당분양가격', ascending=False)
t2.plot(kind='bar', figsize=(10,4), legend=None, 
        title="지역별 평당분양가격(평균)", ylabel="평당분양가격",rot=0)
plt.show()


# In[58]:


t2.plot(legend=None)
plt.show()


# In[59]:


t = df_last.groupby(['지역명', '연도'])['평당분양가격'].mean().unstack()
t.plot(figsize=(10,5), title="연도별 지역별 평당분양가격(평균)", ylabel="평당분양가격")
plt.savefig('data/ch13_example1-1.png')


# In[60]:


a = df_last.groupby(['전용면적'])['평당분양가격'].mean().to_frame()
a = a.loc[['60㎡','60㎡~85㎡','85㎡~102㎡','102㎡~','전체'],:]
a.plot(kind='bar', legend=None, rot=0)
plt.show()


# In[61]:


price_per_year=df_last.groupby(df_last['연도'])['평당분양가격'].mean()
price_per_year.plot(legend=None, ylabel="평당분양가격(평균)")
plt.show()


# In[62]:


b = df_last.groupby(['지역명','전용면적'])['평당분양가격'].mean().unstack()
b = b.loc[:,['전체','60㎡','60㎡~85㎡','85㎡~102㎡','102㎡~']]
b.boxplot()


# In[63]:


c = df_last.groupby(['연도','전용면적'])['평당분양가격'].mean().unstack().T
c = c.loc[['60㎡', '60㎡~85㎡', '85㎡~102㎡', '102㎡~', '전체'],:]
c.boxplot(grid=False)
plt.show()


# In[64]:


d = df_last.pivot_table(index='월', columns='연도', values='평당분양가격')
d.boxplot(grid=False)
plt.show()


# In[65]:


d = df_last.pivot_table(index='월', columns='연도', values='평당분양가격')
d.plot.box()
plt.show()


# In[66]:


#연도별 월별 평당분양가격의 추이
d.plot()
plt.legend(bbox_to_anchor=(1.01, 1), loc=0, borderaxespad=0.)
plt.show()


# ### 9. seaborn으로 시각화(위에서 그린 시각화내용을 일부또는 그 이상을 seaborn으로 시각화
# 1) 지역별 평당분양가격(평균)

# In[67]:


import seaborn as sns
plt.figure(figsize=(10,3))
sns.barplot(x='지역명', y='평당분양가격', data=df_last, ci=None).set_title("지역별 평당분양가격(평균)")
plt.savefig('data/ch13_example1-2.png')


# In[68]:


m = df_last.groupby(["지역명"])["평당분양가격"].mean().sort_values().to_frame()
plt.figure(figsize=(10,3))
sns.barplot(data=m, x=m.index, y='평당분양가격', palette='Blues')


# In[69]:


sns.barplot(x='연도', y='평당분양가격', data=df_last).set_title("연도별 평당분양가격(평균)")
plt.show()


# In[70]:


plt.figure(figsize=(12,4))
sns.barplot(x='지역명', y='평당분양가격', data=df_last, ci=None, hue='연도').set_title("지역별 연도별 평당분양가격(평균)")
plt.legend(bbox_to_anchor=(1.01,1), loc=2, borderaxespad=0.)
plt.show()


# In[71]:


plt.figure(figsize=(10,5))
sns.lineplot(data=df_last, x='연도', y='평당분양가격', hue='지역명', palette='Accent')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


# In[72]:


plt.figure(figsize=(10,5))
sns.relplot(data=df_last, x='연도', y='평당분양가격', hue='지역명', 
            kind='line', col='지역명', col_wrap=4)


# In[73]:


plt.figure(figsize=(8,4))
sns.boxplot(data=df_last, x='연도', y='평당분양가격', palette='Set3')
plt.savefig('data/ch13_example1-3.png')


# In[74]:


sns.boxenplot(x='연도', y='평당분양가격', data=df_last, palette='Set3')
plt.show()


# In[75]:


plt.figure(figsize=(8,4))
sns.boxenplot(x='지역명', y='평당분양가격', data=df_last, palette='Set2')
plt.show()


# In[76]:


sns.boxenplot(x='전용면적', y='평당분양가격', data=df_last)
plt.show()


# In[77]:


plt.figure(figsize=(12,5))
sns.boxplot(data=df_last, x='연도', y='평당분양가격', hue='전용면적', palette='Set3')
plt.show()


# In[78]:


plt.figure(figsize=(10,4))
sns.violinplot(x='연도', y='평당분양가격', data=df_last, palette='Set3')


# In[79]:


plt.figure(figsize=(12,4))
sns.violinplot(x='지역명', y='평당분양가격', data=df_last, palette='Set3')


# In[80]:


plt.figure(figsize=(12,4))
sns.violinplot(x='전용면적', y='평당분양가격', data=df_last, palette='Set3')


# In[81]:


sns.stripplot(x='전용면적', y='평당분양가격', data=df_last, palette='Spectral')
plt.show()


# In[82]:


plt.figure(figsize=(10,4))
sns.swarmplot(x='전용면적', y='평당분양가격', data=df_last, palette='YlGnBu').set_title("전용면적별 평당분양가격(평균)")
plt.savefig('data/ch13_example1-4.png')


# In[83]:


plt.figure(figsize=(12,4))
sns.swarmplot(x='연도', y='평당분양가격', data=df_last, palette='Spectral')
plt.show()


# In[84]:


#상기 그래프를 통해 이상치로 추정되는 내용 표로 확인
max_price = df_last[df_last['평당분양가격']>40000]
max_price


# In[85]:


df_last['평당분양가격'].hist()
plt.show()


# In[86]:


sns.displot(df_last['평당분양가격'], kde=True)
plt.show()


# ### 10. 구조가 다른 df_first와 df_last의 전용면적 전체의 데이터를 하나의 같은 데이터 셋으로 합쳐서 분석

# In[87]:


df_last.sample()


# In[88]:


df_first.head()


# In[89]:


new_df_first = df_first.melt(id_vars='지역', var_name='연도월', value_name='평당분양가격')
new_df_first.head()


# In[90]:


new_df_first["연도"] = new_df_first["연도월"].apply(lambda x:int(x.split("년")[0]))
new_df_first["월"] = new_df_first["연도월"].apply(lambda x:int(x.split("년")[1].replace("월","")))
new_df_first.head()


# In[91]:


new_df_first.info()


# In[92]:


new_first = new_df_first.drop('연도월', axis=1)
new_first.head()


# In[93]:


new_first.columns=['지역명', '평당분양가격','연도','월']
new_first.head()


# In[94]:


new_last = df_last[df_last['전용면적']=='전체']
new_last.drop('전용면적', axis=1, inplace=True)
new_last.head()


# In[95]:


result=pd.concat([new_first, new_last])
result.head()


# In[96]:


result.info()


# In[97]:


result.pivot_table(index='연도', values='평당분양가격', columns='지역명').T


# In[98]:


temp = result.pivot_table(index='연도', values='평당분양가격', columns='지역명').T.plot()
temp.legend(loc='center right', bbox_to_anchor=(1.25, 0.5), ncol=1)
plt.show()


# In[99]:


result


# In[100]:


plt.figure(figsize=(10,4))
sns.lineplot(x='연도', y='평당분양가격', data=result)
plt.show()


# In[101]:


plt.figure(figsize=(10,4))
sns.barplot(x='연도', y='평당분양가격', data=result, palette='husl').set_title('연도별 평당분양가격(평균)')
plt.savefig('data/ch13_example1-5.png')


# In[102]:


plt.figure(figsize=(10,4))
sns.barplot(x='지역명', y='평당분양가격', data=result, ci=None).set_title('지역별 평당분양가격(평균)')
plt.savefig('data/ch13_example1-6.png')


# In[103]:


plt.figure(figsize=(8,3))
sns.boxplot(x='연도', y='평당분양가격', data=result, palette='husl')
plt.show()


# In[104]:


plt.figure(figsize=(8,3))
sns.countplot(x='연도', data=result, palette="viridis").set_title("연도별 평당가격 관측수")
plt.show()


# In[105]:


plt.figure(figsize=(8,3))
sns.countplot(x='지역명', data=result, palette='crest').set_title("지역별 평당가격 관측수")
plt.show()


# In[106]:


result.corr()


# In[107]:


plt.figure(figsize=(7,5))
sns.heatmap(result.corr(), vmin=-1, vmax=1, annot=True, cmap='mako', fmt='.2f')
plt.savefig('data/ch13_example1-7.png')


# In[108]:


g = sns.FacetGrid(result, col='연도', hue='연도', col_wrap=3, palette='husl')
g.map(plt.hist, '평당분양가격')
g.set_axis_labels(y_var='count')
plt.savefig('data/ch13_example1-8.png')


# In[ ]:




