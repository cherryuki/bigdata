#!/usr/bin/env python
# coding: utf-8

# **21-03-15 python 13_데이터 시각화_예제2 (c)cherryuki (ji)**

# ### 1.필요한 라이브러리를 로드하고 시각화에서 디스플레이를 선명하게 표시되도록 하고, 한글 폰트가 나오도록 설정하고 확인한다.

# In[1]:


#새 파일 시작전 설정
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
#%config InlineBackend.figure_format='retina'
#레티나 설정하는 다른 방법
from IPython.display import set_matplotlib_formats
set_matplotlib_formats("retina")
#한글 설정
plt.rc("font", family="Malgun Gothic")
plt.rc("axes", unicode_minus=False) # y축
import pandas as pd
import numpy as np
import seaborn as sns


# ### 2.https://www.data.go.kr에서 “상가(상권)정보”를 다운 받아, 서울과 부산데이터만 df 변수에 읽어들인다.

# In[2]:


df_seoul = pd.read_csv('C:/Bigdata_자료/src/08_Python/data/소상공인시장진흥공단_상가(상권)정보_서울_202012.csv', 
                       encoding='utf8', sep='|', engine='python')
df_pusan = pd.read_csv('C:/Bigdata_자료/src/08_Python/data/소상공인시장진흥공단_상가(상권)정보_부산_202012.csv', 
                       encoding='utf8', sep='|', engine='python')
#경고 메시지 날 경우: engine='python' 기입


# In[3]:


df_seoul.head(1)


# In[4]:


all(df_pusan.columns==df_seoul.columns)


# In[5]:


df_data = pd.concat([df_seoul, df_pusan], ignore_index=True)
df_data.sample(1)


# ### 3.df 데이터 셋의 결측치 확인 및 시각화

# ① df 변수의 컬럼들을 확인하고 상위 3줄, 하위3줄을 출력한다.

# In[6]:


df_data.columns


# In[7]:


df_data.head(3)


# In[8]:


df_data.tail(3)


# ② df 변수의 결측치를 제외한 데이터 개수 및 dtype들을 출력하고 변수가 사용되는 메모리 사용량 확인한다.

# In[9]:


df_data.info()


# In[10]:


#dtype만 확인할 때
df_data.dtypes


# In[11]:


df_data.shape


# In[12]:


missing_cnt = df_data.isnull().sum().sort_values()
missing_cnt


# In[13]:


missing_cnt = missing_cnt[missing_cnt!=0]
missing_cnt


# In[14]:


missing_cnt.plot.bar(figsize=(12,5), rot=45)
#그래프 위에 값을 표시하고 싶을 때
for i, data in enumerate(missing_cnt):
    plt.text(i-0.25, data+5000, data)  #위치조정은 해당 그래프 값의 범위에 따라 조정
plt.show()


# In[15]:


missing_cnt.plot(kind='barh', figsize=(8,5), xlim=[0,500000])
for i, data in enumerate(missing_cnt):
    plt.text(data+5000, i-0.15, data)
plt.show()


# ## ※ missingno로 결측치 시각화 라이브러리
# - https://github.com/ResidentMario/missingno
# - 아나콘다 prompt: pip install missingno

# In[16]:


import missingno as msno


# In[17]:


msno.matrix(df_data) #결측치가 없는 부분은 검정색으로  (결측치 있는 부분은 흰색으로 표현)


# In[18]:


msno.heatmap(df_data)
plt.show()


# In[19]:


#군집화; 비슷한 성격의 컬럼들을 묶어줌(결측치가 있는 것들 위주로)
msno.dendrogram(df_data)


# ### 4.	df 데이터 셋에서 사용하지 않을 컬럼은 제거

# In[20]:


missing_cnt.tail(9)


# In[21]:


#동정보 컬럼의 결측치 비율(약 91%)
missing_cnt['동정보'] / df_data.shape[0] * 100


# In[22]:


#표준산업분류코드 컬럼의 결측치 비율(약 6%)
missing_cnt['표준산업분류코드'] / df_data.shape[0] * 100


# In[23]:


df_data['표준산업분류코드'].unique()


# ①	결측치가 너무 많은 컬럼은 제거한다. 결측치가 너무 많은 상위 9개 컬럼은 제거함.

# In[24]:


df_data = df_data.drop(missing_cnt.tail(9).index, axis=1)
#df_data = df_data.drop(['동정보', '건물부번지', '지점명','호정보','건물명',
#                       '층정보','지번부번지','표준산업분류명','표준산업분류코드'],axis=1)


# In[25]:


missing_cnt.tail(9).index


# ②	컬럼명에 “코드”나 “번호”가 있는 컬럼은 분석에 사용되지 않을 예정입니다. 제거함( df.columns.str.contains(“코드|번호”) 이용).

# In[27]:


df_data = df_data.drop(df_data.columns[df_data.columns.str.contains("코드|번호")], axis=1)


# ③ 컬럼을 제거 후 제거 전과 memory usage를 확인하고 줄어든 columns수도 확인한다.

# In[28]:


df_data.columns


# In[29]:


df_data.info() #제거전 메모리: memory usage: 145.4+ MB (제거후: memory usage: 59.6+ MB)


# In[30]:


df_data.shape #컬럼수: 39->16


# In[31]:


get_ipython().run_line_magic('load_ext', 'memory_profiler')
get_ipython().run_line_magic('memit', '')


# ### 5.	df 데이터 셋의 값을 가져온다(loc함수, iloc함수등을 사용하기도 하고 사용하지 않기도 하며 서브셋을 가져온다)

# ①	상호명 필드만 가져온다

# In[32]:


df_data['상호명']
df_data.loc[:, ['상호명']]
df_data.iloc[:, [0]]


# ②	상호명의 종류별 데이터수를 가져온다(df.상호명.value_counts()이용)

# In[33]:


df_data['상호명'].value_counts()


# ③	“상호명”과 "도로명주소” 컬럼 가져오기

# In[34]:


df_data[['상호명','도로명주소']]


# ④	0~2행을 출력하라 (head()함수를 이용하지 않고, loc과 iloc을 이용)

# In[35]:


df_data.iloc[0:3]


# In[36]:


df_data.index


# In[37]:


df_data.loc[0:3]


# ### 6.	기술 통계값 보기 
# - https://pandas.pydata.org/docs/user_guide/computation.html#method-summary

# ①	df 데이터셋의 요약기술 통계량

# In[38]:


"""
DataFrame.count: Count number of non-NA/null observations.
DataFrame.max: Maximum of the values in the object.
DataFrame.min: Minimum of the values in the object.
DataFrame.mean: Mean of the values.
DataFrame.std: Standard deviation of the observations.
DataFrame.select_dtypes: Subset of a DataFrame including/excluding
     columns based on their dtype
"""
df_data.describe()


# ②	df 데이터셋의 “지번본번지", "건물본번지” 컬럼의 데이터 개수와  dtype 메모리 사용량을 확인한다.

# In[39]:


df_data[['지번본번지','건물본번지']].info()


# In[40]:


df_data[['지번본번지','건물본번지']].count()


# In[41]:


#int64만 서브셋으로 가져올 때 select_dtypes 이용
df_data.select_dtypes(include='int64')


# ③	“위도", "경도” 컬럼만의 요약 기술통계량

# In[42]:


df_data[['위도','경도']].describe()


# In[43]:


"""
argmax(axis=0); 열별 최대값 인덱스 리턴(axis=1은 행별)
max(axis=1); 행별 최대값 리턴(axis=0은 열별) - min으로 하면 최소값
cumsum(axis=0); 열별 누적합
cumprod(axis=1); 행별 누적곱
var(); 분산
std(); 표준편차 (분산의 양의 제곱근)
quantile(q=0.25); 1사분위 수(25%)
"""


# ### 7.	단별량 수치형 변수 시각화

# ①	위도의 빈도표를 시각화

# In[44]:


df_data['위도'].hist()


# In[45]:


plt.hist(df_data['위도'], bins=50)
plt.show()


# In[46]:


sns.histplot(x='위도', data=df_data, palette="viridis").set_title("위도의 빈도표")
plt.show()


# In[47]:


sns.displot(df_data['위도'])


# ②	경도의 빈도표를 시각화

# In[48]:


df_data['경도'].hist()
plt.show()


# In[49]:


plt.hist(df_data['경도'], bins=50)
plt.show()


# In[50]:


sns.histplot(x='경도', data=df_data).set_title("경도의 빈도표")
plt.show()


# ### 8.	상관계수
# - http://seaborn.pydata.org/examples/many_pairwise_correlations.html (heatmap 시각화) <br>
# ①	전체 숫자 컬럼끼리의 상관계수

# In[51]:


df_data.corr()


# ②	상관계수를 이용하여 heatmap 시각화

# In[52]:


plt.figure(figsize=(10,6))
sns.heatmap(df_data.corr(), vmin=-1, vmax=1, annot=True, cmap='viridis', fmt='.2f').set_title("상관계수 heatmap")
plt.savefig('data/ch13_example2-1.png')


# In[53]:


#윗부분 삼각형 숨기기 mask = np.triu(np.ones_like(corr, dtype=bool))
plt.figure(figsize=(10,6))
mask = np.triu(np.ones_like(df_data.corr(), dtype=bool))
sns.heatmap(df_data.corr(), annot=True, cmap='viridis', fmt='.2f', mask=mask)
plt.show()


# In[54]:


#아랫부분 삼각형 숨기기 mask=~mask
plt.figure(figsize=(10,6))
mask = np.triu(np.ones_like(df_data.corr(), dtype=bool))
sns.heatmap(df_data.corr(), annot=True, cmap='viridis', fmt='.2f', mask=~mask)
plt.show()


# ### 9.	경도와 위도 컬럼을 이용하여 산점도
# ①	X축에는 경도, y축에는 위도 컬럼을 산점도로 시각화

# In[55]:


df_data1 = df_data[['위도','경도','시도명']]
df_data1


# In[56]:


sns.scatterplot(x='경도', y='위도', data=df_data1, hue='시도명')
plt.show()


# ②	경도와 위도의 산점도를 “시도명” 컬럼별로 서브플롯으로 시각화

# In[57]:


df_data2 = df_data1.sample(10000)


# In[58]:


sns.relplot(x='경도', y='위도', data=df_data2, col='시도명', hue='시도명')
plt.show()


# ③	위의 1번에서 시각화된 산점도를 바탕으로 회귀선을 그린다.

# In[59]:


sns.scatterplot(x='경도', y='위도', data=df_data2, hue='시도명')
sns.lineplot(x='경도',y='위도', data=df_data2, hue='시도명')


# In[60]:


sns.regplot(data=df_data2, x='경도', y='위도')


# In[61]:


sns.lmplot(data=df_data2, x='경도', y='위도', col='시도명', hue='시도명', sharex=False, sharey=False)
plt.show()


# ### 10.	상권업종대분류명별 상호명의 개수를 도출하고 시각화하기

# In[62]:


df_data2 = df_data.groupby('상권업종대분류명')['상호명'].count()
df_data2 = df_data2.to_frame().sort_values(by='상호명')
df_data2


# In[63]:


df_data['상권업종대분류명'].describe()


# In[64]:


plt.figure(figsize=(8,6))
ax = sns.barplot(x=df_data2.index, y='상호명', data=df_data2, palette='Set3').set_ylabel('상호 개수')


# In[65]:


df_data.groupby('상권업종대분류명')['상호명'].count()


# ### 11.	상권업종대분류명이 음식인 서브셋을 이용한 분석
# ①	“상권업종대분류명”이 음식인 서브셋을 변수 df_food에 할당하고 확인

# In[66]:


df_food = df_data[df_data['상권업종대분류명']=='음식'].copy() #깊은복사
df_food.sample()


# ②	“상권업종대분류명”이 음식이면서, "시군구명”이 강남구 데이터만 가져와 “상권업종중분류명”별로 빈도수를 구함(loc함수를 이용 vs loc함수 이용안함)

# In[67]:


df_food[df_food['시군구명']=='강남구']['상권업종중분류명'].value_counts()


# In[68]:


df_food[df_food['시군구명']=='강남구'].loc[:,['상권업종중분류명']].value_counts()


# In[69]:


df_food.loc[df_food['시군구명']=='강남구', '상권업종중분류명'].value_counts()


# ### 12.	df 데이터셋에서 “상권업종대분류명”이 음식인 데이터 중 서울특별시 데이터 서브셋
# ①	“상권업종대분류명”이 음식인 서브셋 중 서울특별시 데이터만 변수 df_seoul_food에 할당하고 확인

# In[70]:


df_seoul_food = df_food[df_food['시도명']=='서울특별시'].copy()
df_seoul_food.head(3)


# ②	df_seoul_df. 데이터 셋을 시군구명, 상권업종중분류명으로 그룹화하여 상점수를 count한 내용을 food_gu 변수에 할당

# In[71]:


food_gu = df_seoul_food.groupby(['시군구명', '상권업종중분류명'])['상호명'].count().to_frame()


# ③	food_gu 변수를 다음과 같은 스타일의 표로 출력(groupby 이용).

# In[72]:


food_gu_temp = food_gu.unstack()
food_gu_temp.columns = food_gu_temp.columns.droplevel(level=0)
food_gu_temp


# ④	위 3번 스타일의 표를 pivot_table함수를 이용하여 출력

# In[73]:


df_seoul_food.pivot_table(index='시군구명', values='상호명', columns='상권업종중분류명', aggfunc='count')


# ⑤	3번의 결과 중 강남구 데이터만 뽑아 barplot으로 시각화(판다스 plot이용)

# In[74]:


food_gu_temp.loc['강남구'].sort_values(ascending=False).plot(kind='bar').set_title("강남구 상권업종중분류명별 음식점 수")
plt.show()


# ⑥	3번의 결과를 seaborn을 이용하여 구별 음식점 상호 개수를 시각화

# In[75]:


plt.figure(figsize=(15,4))
sns.barplot(data=food_gu_temp.T).set_title("구별 음식점 상호 개수")
plt.ylabel("상호 수")
plt.savefig('data/ch13_example2-2.png')


# ⑦	상권업종중분류명별 음식점 상호갯수

# In[76]:


plt.figure(figsize=(15,3))
sns.barplot(data=food_gu_temp).set_title("상권업종중분류명별 음식점 상호 개수")
plt.ylabel("상호 수")
plt.savefig('data/ch13_example2-3.png')


# ⑧	Seaborn의 catplot을 이용하여 상권업종중분류별 음식점을 구별로 시각화(서브플롯으로 시각화)

# In[77]:


food_gu2 = food_gu_temp.reset_index()


# In[78]:


plt.figure(figsize=(30,30))
sns.catplot(data=food_gu2, col='시군구명', col_wrap=5, kind='bar').set_xticklabels(rotation=45)
plt.savefig('data/ch13_example2-4.png')


# ⑨	Seaborn의 catplot을 이용하여 구별 음식점을 상권업종중분류명별로 서브 플롯으로 시각화

# In[79]:


food_gu3 = food_gu_temp.T


# In[80]:


food_gu3 = food_gu3.reset_index()


# In[81]:


plt.figure(figsize=(25,15))
sns.catplot(data=food_gu3, kind='bar', ci=None, col='상권업종중분류명', col_wrap=3).set_xticklabels(rotation=60)
plt.savefig('data/ch13_example2-5.png')


# ### 13.	구별로 학원수 비교 : 서울 대치동이나 목동에 사교육이 발달되었다는 가설을 뒷받침할 수 있는 분석
# ①	서울시 학원(상권업종대분류명 이용) 데이터를 df_academy 변수에 할당하고 확인

# In[82]:


df_academy = df_data[(df_data['상권업종대분류명']=='학문/교육')&(df_data['시도명']=='서울특별시')].copy()
df_academy


# In[83]:


#df_academy = df_academy[df_academy['상권업종중분류명'].str.contains("학원")].copy()
#df_academy


# ②	df_academy 데이터 셋을 상호명별로 빈도수 출력(value_counts()함수 이용하거나 groupby이용)

# In[84]:


df_academy['상호명'].value_counts()


# In[85]:


df_academy.groupby('상호명')['상호명'].count().sort_values(ascending=False)


# ③	df_academy 데이터 셋을 상호명별로 빈도수 상위 10개 출력

# In[86]:


df_academy['상호명'].value_counts().head(10)


# ④	df_academy 데이터 셋을 시군구명 별로 빈도수 출력(학원이 가장 많은 구부터 출력)

# In[87]:


df_academy['시군구명'].value_counts()


# In[88]:


df_academy.groupby('시군구명')['상호명'].count().sort_values(ascending=False)


# ⑤	df_academy 데이터 셋에서 어떤 종류의 학원들이 많은지 상위 30개만 academy_count변수에 할당하고 출력(상권업종소분류명 컬럼 이용)

# In[89]:


academy_count = df_academy['상권업종소분류명'].value_counts().head(30)
academy_count


# ⑥	df_academy 데이터셋에서 상권업종소분류명별로 빈도수를 구했을 때 빈도가 1000이상인 데이터만 따로 academy_count_1000변수에 할당

# In[90]:


academy_count_1000 = academy_count[academy_count>=1000]
academy_count_1000


# ⑦	df_academy 데이터셋을 “시군구명”, "상권업종소분류명” 별 상호명 빈도수를 academy_group 변수에 할당 출력

# In[91]:


academy_group = df_academy.groupby(['시군구명','상권업종소분류명'])['상호명'].count().to_frame()
academy_group


# ⑧	academy_group 데이터셋에서 강남구 데이터만 출력 및 시각화(barplot)

# In[92]:


academy_group_gangnam = academy_group.loc['강남구']
academy_group_gangnam


# In[93]:


academy_group_gangnam.plot(kind='bar', figsize=(15,3), legend=None)
plt.show()


# In[94]:


academy_group_gangnam = academy_group_gangnam.reset_index()
academy_group_gangnam.sample()


# In[95]:


plt.figure(figsize=(30,5))
sns.barplot(data=academy_group_gangnam, x='상권업종소분류명', y='상호명')
plt.ylabel("상호명 수")
plt.show()


# In[96]:


plt.figure(figsize=(20,5))
sns.barplot(data=academy_group_gangnam[academy_group_gangnam['상호명']>10].sort_values(by='상호명'), 
            x='상권업종소분류명', y='상호명').set_title("강남구 학원 종류별 개수(10개 이상만)")
plt.ylabel("상호명 수")
plt.savefig('data/ch13_example2-6.png')


# ⑨	df_academy데이터 중 “법정동명”컬럼이 “대치동”과 “목동”인 데이터만 가져와 상권업종소분류명별 빈도수 출력

# In[97]:


df_academy[(df_academy['법정동명']=='대치동')|(df_academy['법정동명']=='목동')]['상권업종소분류명'].value_counts()


# ⑩	“상권업종소분류명”별 "시군구명” 별 상호명 빈도수를 g변수에 할당하고 출력

# In[98]:


g = df_academy.groupby(['상권업종소분류명','시군구명'])['상호명'].count()
g.to_frame()


# ⑪	g변수의 내용중 "상권업종소분류명” 컬럼이 “학원-입시”데이터만 시각화(pandas의 plot.bar, pandas의 barh,seaborn의 barplot –seaborn으로 barplot을 그릴 경우 g 변수의 내용을 reset_index()하여야 합니다)

# In[99]:


g.loc['학원-입시'].plot.bar(figsize=(15,5))
plt.show()


# In[100]:


g.loc['학원-입시'].plot(kind='barh', figsize=(8,8), cmap='Accent')
plt.show()


# In[101]:


g = g.to_frame()
g = g.reset_index()


# In[102]:


plt.figure(figsize=(20,5))
sns.barplot(data=g, x='시군구명', y='상호명', ci=None).set_title("시군구별 학원-입시(수)")
plt.ylabel("상호명 수")
plt.savefig('data/ch13_example2-7.png')


# In[103]:


plt.figure(figsize=(8,8))
sns.barplot(data=g, y='시군구명', x='상호명', ci=None).set_title("시군구별 학원-입시(수)")
plt.xlabel("상호명 수")
plt.savefig('data/ch13_example2-8.png')


# ### 14.	서울시 데이터만 경도와 위도를 산점도로 시각화
# ①	df_academy 데이터셋의 경도와 위도를 “시군구명”별로 색상을 다르게 scatterplot으로 시각화

# In[104]:


plt.figure(figsize=(12,10))
sns.scatterplot(x='경도', y='위도', hue='시군구명', data=df_academy)
plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
plt.savefig('data/ch13_example2-9.png')


# ②	df_academy 데이터셋의 경도와 위도를 “상권업종소분류명”별로 색상을 다르게 scatterplot으로 시각화

# In[105]:


plt.figure(figsize=(15,10))
sns.scatterplot(x='경도', y='위도', hue='상권업종소분류명', data=df_academy)
plt.legend(ncol=3, bbox_to_anchor=(1.01,1), loc=2, borderaxespad=0.)
plt.savefig('data/ch13_example2-10.png')


# ③	df_academy 데이터셋 중 “학원-입시” 데이터만, 경도와 위도를 “시군구명”별로 색상을 다르게 scatterplot으로 시각화

# In[106]:


temp = df_academy[df_academy['상권업종소분류명']=='학원-입시']


# In[107]:


plt.figure(figsize=(15,10))
ax = sns.scatterplot(x='경도', y='위도', hue='시군구명', data=temp)
ax.legend(loc='center right', bbox_to_anchor=(1.11,0.5), ncol=1)
plt.show()


# ④	df_academy 데이터셋 중 “어린이집” 데이터만, 경도와 위도를 “시군구명”별로 색상을 다르게 scatterplot으로 시각화

# In[108]:


df_academy['상권업종소분류명'].unique()


# In[109]:


temp2 = df_academy[df_academy['상권업종소분류명']=='어린이집']
temp2


# In[110]:


plt.figure(figsize=(15,10))
ax = sns.scatterplot(x='경도', y='위도', hue='시군구명', data=temp2)
ax.legend(loc='center right', bbox_to_anchor=(1.11, 0.5), ncol=1)
plt.show()


# ⑤ df_academy 데이터셋 중 “학원-입시”데이터와 "어린이집" 데이터만, 경도와 위도를 “상권업종소분류명”별로 색상을 다르게 scatterplot으로 시각화

# In[111]:


temp3 = pd.concat([temp2, temp])


# In[112]:


plt.figure(figsize=(12,10))
sns.scatterplot(x='경도', y='위도', hue='상권업종소분류명', data=temp3)
plt.show()


# **21-03-16 python 13_데이터 시각화_지도시각화(folium) (c)cherryuki (ji)**

# ## 15. 지도시각화: Folium
# - 아나콘다 prompt에서 pip install folium 혹은 conda install -c conda-forge folium 로 다운로드
# - https://nbviewer.jupyter.org/github/python-visualization/folium/tree/master/examples/
# - https://nbviewer.jupyter.org/github/python-visualization/folium/blob/master/examples/Quickstart.ipynb

# In[113]:


import folium


# In[114]:


m = folium.Map(location=[45.5236, -122.6750])
m


# In[115]:


lat_mean = df_academy['위도'].mean()
long_mean = df_academy['경도'].mean()


# In[118]:


m = folium.Map(location=[lat_mean, long_mean])
m


# In[119]:


folium.Map(location=[lat_mean, long_mean], zoom_start=12)
#zomm_start=10이 기본값, 10보다 크면 확대된 모습


# ### Markers

# In[126]:


#df_academy[(df_academy['상권업종소분류명']=='어린이집') | (df_academy['상권업종소분류명']=='학원-입시')]
df_selected = df_academy[df_academy['상권업종소분류명'].isin(['어린이집','학원-입시'])]
df_sel = df_selected.sample(1000)
df_sel.iloc[0]


# In[128]:


m = folium.Map(location=[lat_mean, long_mean], zoom_start=12)

folium.Marker([37.5464, 126.932], tooltip='새말논술국어학원').add_to(m)

m


# In[129]:


df_sel.index[:10]


# In[130]:


for i in df_sel.index[:10]:
    print(df_sel.loc[i, '상호명'], end=' - ')
    print(df_sel.loc[i, '도로명주소'], end=' - ')
    print(df_sel.loc[i, '위도'], ',', df_sel.loc[i, '경도'])


# In[131]:


m = folium.Map(location=[lat_mean, long_mean], zoom_start=12)
for i in df_sel.index[:100]:
    lat = df_sel.loc[i, '위도']
    long = df_sel.loc[i, '경도']
    tooltip = df_sel.loc[i, '상호명'] + ' : ' +df_sel.loc[i, '도로명주소']
    folium.Marker([lat, long], tooltip=tooltip).add_to(m)
m


# In[136]:


#CircleMarker
m = folium.Map(location=[lat_mean, long_mean], zoom_start=11)
for i in df_sel.index:
    lat = df_sel.loc[i, '위도']
    long = df_sel.loc[i, '경도']
    #tooltip = df_sel.loc[i, '상호명'] + ' : ' +df_sel.loc[i, '도로명주소']
    folium.CircleMarker([lat, long], radius=2).add_to(m)
#radius 기본값 10
m


# In[137]:


temp.shape #temp; 상권업종소분류명: 학원-입시


# In[138]:


temp2.shape #temp2; 상권업종소분류명: 어린이집


# In[141]:


#temp; 상권업종소분류명: 학원-입시
#temp2; 상권업종소분류명: 어린이집
m = folium.Map(location=[lat_mean, long_mean], zoom_start=11)

for i in temp2.index:
    lat = temp2.loc[i, '위도']
    long = temp2.loc[i, '경도']
    folium.CircleMarker([lat, long], radius=1).add_to(m)

for i in temp.index:
    lat = temp.loc[i, '위도']
    long = temp.loc[i, '경도']
    folium.CircleMarker([lat, long], radius=1, color='orange').add_to(m)

m


# In[142]:


#지도 저장시
m.save('data/seoul.html')


# In[ ]:




