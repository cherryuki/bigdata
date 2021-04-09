#!/usr/bin/env python
# coding: utf-8

# **python 데이터 분석 및 시각화 (c)cherryuki (ji)**

# # Project (2021-04-01~2021-04-07)
# ## 05. 데이터 시각화를 위한 자료 분석
# ### 1) 1인당 1일 식품 공급량(g)

# In[1]:


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
import seaborn as sns


# In[2]:


import pandas as pd 
data1 = pd.read_excel('data/1인당1일식품공급량(g).xlsx')
data1 = data1.apply(lambda x:x.replace('\xa0', ''))


# In[3]:


data1['국가'] = data1['국가'].str.replace('\xa0', '')
data1['연도'] = data1['연도'].str.replace('\xa0', '')
data1['연도'] = data1['연도'].apply(lambda x:int(x.split('-')[0]))
data1['육류'] = data1['육류'].str.replace('\xa0', '')
data1['육류'] = data1['육류'].apply(lambda x:int(x))
data1['계란류'] = data1['계란류'].str.replace('\xa0', '')
data1['계란류'] = data1['계란류'].apply(lambda x:int(x))
data1['우유류'] = data1['우유류'].str.replace('\xa0', '')
data1['우유류'] = data1['우유류'].apply(lambda x:int(x))


# In[4]:


data1[data1['연도']==36951] #434, 623


# In[5]:


data1 = data1.drop([434, 623])
data1


# In[6]:


data1.groupby('연도')[['육류']].sum()


# In[7]:


data1.groupby('국가')[['육류']].mean()


# In[8]:


plt.figure(figsize=(10,5))
#sns.barplot(x='연도', y='육류', data=data1, ci=None)
sns.lineplot(x='연도', y='육류', data=data1)
plt.title('연도별(1974~2013) 1인당 1일 육류 공급량(g)_전체국가')
plt.savefig('data/연도별_1인당1일_육류공급량_전체국가.png')


# In[9]:


plt.figure(figsize=(10,5))
sns.barplot(x='연도', y='육류', data=data1, ci=None)
plt.title('연도별(1974~2013) 1인당 1일 육류 공급량(g)_전체국가')
plt.savefig('data/연도별_1인당1일_육류공급량_전체국가_bar.png')


# In[10]:


data1 = data1[data1['국가'].str.startswith(('한국', '일본', '중국', '미국'))]


# In[11]:


data1.describe()


# In[12]:


data1.groupby('연도').sum()


# In[13]:


data1.groupby('국가')[['육류']].mean()


# In[14]:


data1[:18]


# In[15]:


data1[data1['연도']==2013][['국가', '육류']]


# In[16]:


plt.figure(figsize=(7,5))
ax = sns.lineplot(x='연도', y='육류', hue='국가', data=data1, linewidth=2.0)
ax.plot(marker='^')
#plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.title('연도별(1974~2013) 1인당 1일 육류 공급량(g)')
plt.savefig('data/연도별_1인당1일_육류공급량.png')


# In[17]:


plt.figure(figsize=(7,5))
sns.boxplot(x='국가', y='육류', data=data1)
plt.show()


# In[18]:


data1 = data1[data1['국가'].str.startswith(('한국', '일본', '중국'))]


# In[19]:


plt.figure(figsize=(7,5))
sns.boxplot(x='연도', y='육류', data=data1)
plt.show()


# In[20]:


plt.figure(figsize=(7,5))
sns.boxplot(x='국가', y='육류', data=data1)
plt.show()


# In[21]:


sns.lineplot(x='연도', y='육류', data=data1[data1['국가'].str.startswith('한국')])
sns.lineplot(x='연도', y='계란류', data=data1[data1['국가'].str.startswith('한국')])
sns.lineplot(x='연도', y='우유류', data=data1[data1['국가'].str.startswith('한국')])


# In[22]:


type(data1.iloc[0,4])


# In[23]:


plt.figure(figsize=(7,5))
sns.barplot(x='연도', y='육류', data=data1, ci=None)
plt.title('연도별(1974~2013) 1인당 1일 육류 공급량(g)_한중일')
plt.savefig('data/연도별_1인당1일_육류공급량_한중일.png')


# In[24]:


plt.figure(figsize=(7,5))
sns.barplot(x='연도', y='육류', data=data1[data1['국가'].str.startswith('한국')])
plt.title('연도별(1974~2013) 1인당 1일 육류 공급량(g)_한국')
plt.savefig('data/연도별_1인당1일_육류공급량_한국.png')


# In[25]:


#data1.to_csv('data/1_1인당1일식품공급량(g)_수정.csv')
data=data1[data1['국가'].str.startswith('한국')]


# In[26]:


plt.figure(figsize=(10,5))
sns.barplot(x='연도', y='육류', data=data1, hue='국가', ci=None, palette='Set3')
#sns.lineplot(x='연도', y='육류', data=data1, hue='국가')


# In[27]:


plt.figure(figsize=(20,5))
sns.catplot(x='연도', y='육류', data=data1, hue='국가', kind='bar', col='국가', palette='Set3', ci=None)
plt.show()


# In[28]:


#data1.to_csv('data/1_1인당1일식품공급량(g)_수정.csv')


# In[29]:


data1 = data1[data1['국가'].str.startswith(('한국', '일본', '중국', '미국'))]


# In[30]:


sns.relplot(x='연도', y='육류', hue='국가', data=data1,
           kind='line',
           col='국가',
           col_wrap=4)
plt.show()


# In[31]:


sns.barplot(x='연도', y='육류', data=data1, ci=None)


# In[32]:


sns.barplot(x='연도', y='육류', data=data1, hue='국가', ci=None, palette='Set3')


# In[33]:


sns.catplot(x='연도', y='육류', data=data1, hue='국가', kind='bar', col='국가', ci=None)


# ### 2) 자료확인 
# - 국내 1인 1일당 식품공급량(g)
# - 국내 연도별식품 식품공급량
# - 축산물 수급실적

# In[34]:


data4 = pd.read_excel('data/국내1인1일당식품공급량(g).xlsx')
data4 = data4[84:96] #육류, 계란, 우유
data4


# In[35]:


data6 = pd.read_excel('data/국내연도별식품공급량(천톤).xlsx')
data6 = data6[84:96] #육류, 계란류, 우유류
data6


# In[36]:


data8 = pd.read_excel('data/축산물수급실적_수정.xlsx')
data8


# ### 3) 축산물 수급실적 자료 전처리 및 시각화

# In[37]:


data8.iloc[21,20]


# In[38]:


data8.info()


# In[39]:


data8.shape


# In[40]:


for i in range(data8.shape[0]):
    for j in range(data8.shape[1]):
        data8.iloc[i,j] = data8.iloc[i,j].replace('\xa0','').replace(',','').replace(' ','').replace('-','')
        #data8.iloc[i,j] = pd.to_numeric(data8.iloc[i,j])


# In[41]:


for i in range(data8.shape[1]):
    data8.iloc[:, i] = pd.to_numeric(data8.iloc[:,i])


# In[42]:


data8.info()


# In[43]:


data8.to_csv('data/1_축산물수급실적_수정.csv')


# In[44]:


data8.columns


# In[45]:


data8_1 = data8.loc[:,['연도', '육류 공급 계', '1인당 소비량 계', '육류 자급률(%)']]


# In[46]:


data8_1


# In[47]:


plt.figure(figsize=(10,5))
sns.barplot(x='연도', y='1인당 소비량 계', data=data8, ci=None)


# In[48]:


plt.figure(figsize=(10,5))
sns.barplot(x='연도', y='육류 자급률(%)', data=data8, ci=None)
#sns.lineplot(x='연도', y='육류 자급률(%)', data=data8, ci=None)


# In[49]:


data8.iloc[:, 8:12]


# In[50]:


ax = sns.lineplot(x='연도', y='1인당 소비량 계', data=data8)


# In[51]:


sns.lineplot(x='연도', y='1인당 소비량 계', data=data8)
sns.lineplot(x='연도', y='육류 자급률(%)', data=data8)


# In[53]:


import numpy as np
fig, ax1 = plt.subplots(figsize=(10,5))
ax2 = ax1.twinx()
sns.barplot(x='연도', y='1인당 소비량 계', data=data8, ax=ax1, alpha=.7)
sns.lineplot(x=np.arange(0,len(data8)), y='육류 자급률(%)', data=data8, ax=ax2)
plt.title('한국 1인당 육류 소비량(kg) vs 육류 자급률(%)')
plt.savefig('data/한국_1인당육류소비량vs육류자급률.png')


# In[54]:


sns.lineplot(x='연도', y='1인당 소비 쇠고기(kg)', data=data8, label='소고기')
sns.lineplot(x='연도', y='1인당 소비 돼지고기(kg)', data=data8, label='돼지고기')
sns.lineplot(x='연도', y='1인당 소비 닭고기(kg)', data=data8, label='닭고기')
plt.ylabel('1인당 소비 고기(kg)')
plt.title('한국 고기별 1인당 육류 소비량(kg)')
plt.savefig('data/한국_1인당육류소비량(kg).png')


# ## 06. 지도 시각화

# ### 1) 데이터 전처리

# In[135]:


import pandas as pd
import json
import folium
data = pd.read_csv('data/가축+질병+발생+정보_20210405.csv', encoding='utf-8')
data


# In[136]:


data.info()


# In[137]:


data['축종'] = data['축종(품종)'].apply(lambda x:x.split('-')[0])
data['법정동'] = data['농장소재지 법정동 코드']
data = data.drop('농장소재지 법정동 코드', axis=1)
data = data.drop('축종(품종)', axis=1)
data


# In[30]:


#data.to_csv('data2/가축_질병_전처리.csv', sep=',')


# In[138]:


data = data[['법정동', '축종', '발생두수(마리)']]
data


# In[139]:


map_data = pd.read_excel('data/행정_법정동 중심좌표.xlsx')


# In[140]:


map_data = map_data[['코드', '위도', '경도']]
map_data


# In[141]:


for i in range(len(data)):
    data.loc[i, '법정동'] = str(data.loc[i, '법정동'])


# In[143]:


data.columns = ['코드', '축종', '수']
data


# In[144]:


len(set(data['코드']))


# In[150]:


data2 = data.groupby(['코드']).sum()
data2.reset_index(inplace=True)
data2['코드'] = data2['코드'].apply(pd.to_numeric)
data2


# In[151]:


data_result = pd.merge(map_data, data2, on='코드')
data_result


# In[152]:


data_result.to_csv('data/법정동코드별_축산감염수_위도경도추가.csv')


# In[153]:


df = data_result[data_result['수']>=100]


# In[154]:


df.reset_index(inplace=True)


# ### 2) 지도시각화

# In[156]:


import pandas as pd
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster


# In[158]:


lat_mean = df['위도'].mean()
long_mean = df['경도'].mean()
m = folium.Map(location=[lat_mean, long_mean], tiles='openstreetmap', zoom_start=7)
marker_cluster = MarkerCluster().add_to(m)
for i in range(len(df)):
    lat = df.loc[i, '위도']
    long = df.loc[i, '경도']
    folium.Marker([lat, long], radius=2).add_to(marker_cluster)
m.save('data/map1.html')
m


# In[68]:


df['index'] = [str(x)[:2] for x in df['코드']]
df


# In[162]:


df['code'] = df['코드']
df_temp = df[['code','수']]


# In[163]:


geo_path = 'data/skorea_submunicipalities_geo_simple.json'
geo_str = json.load(open(geo_path, encoding='utf-8'))


# In[165]:


lat_mean = df['위도'].mean()
long_mean = df['경도'].mean()
m = folium.Map(location=[lat_mean, long_mean], tiles='openstreetmap', zoom_start=7)
for i in range(len(df)):
    lat = df.loc[i, '위도']
    long = df.loc[i, '경도']
    folium.CircleMarker([lat, long], 
                        radius=df.loc[i, '수']/15000,
                       popup=df.loc[i, '수'],
                        color='blue',
                       fill=True).add_to(m)
m.save('data/map2.html')
m


# In[166]:


data2 = pd.read_excel('data2/법정가축전염병_전체.xls')
data2 = data2[:29]


# In[167]:


fig, ax1 = plt.subplots(figsize=(15,5))
ax2 = ax1.twinx()
sns.barplot(x='연도(월)', y='소계', data=data2, alpha=.7)
sns.lineplot(x=np.arange(0,len(data2)), y='소계', data=data2)
plt.title('연도별 법정 가축 전염병 전체 통계')
plt.savefig('data2/연도별법정가축전염병_전체통계.png')


# In[34]:


temp4 = enumerate(data2['소계'])
temp4


# In[168]:


fig, ax1 = plt.subplots(figsize=(15,5))
g = sns.barplot(x='연도(월)', y='소계', data=data2, ax=ax1, alpha=.7)
for i in range(data2.shape[0]):
    g.text(x=i, y=data2['소계'][i], s=data2['소계'][i],
          horizontalalignment='center')


# In[ ]:




