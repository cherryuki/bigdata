#!/usr/bin/env python
# coding: utf-8

# **21-03-09 python 12_데이터 프레임과 시리즈(Pandas) (c)cherryuki (ji)**

# # <font color="blue">ch12. 데이터 프레임과 시리즈(Pandas)</font>

# # 8절. 데이터 그룹화 및 집계

# In[2]:


import pandas as pd
import numpy as np
from statsmodels.api import datasets
iris_df = datasets.get_rdataset("iris", package="datasets").data
iris_df.head()


# ## 8.1 Group by

# In[3]:


iris_df.groupby(iris_df.Species).mean()


# In[4]:


iris_df.groupby(iris_df.Species)['Sepal.Length', 'Sepal.Width'].mean()


# In[5]:


iris_df.pivot_table(index="Species", values=["Sepal.Length", "Sepal.Width"]) #기본값: aggfunc='mean'


# In[6]:


iris_df.pivot_table(index="Species", values=["Sepal.Length"], aggfunc="sum")


# In[7]:


iris_df.groupby(iris_df.Species)['Sepal.Length'].sum()


# In[8]:


iris_grouped = iris_df.groupby(iris_df.Species)
iris_grouped


# In[9]:


iris_grouped.count()


# In[10]:


iris_df.loc[1, 'Sepal.Length']


# In[12]:


import random
rownum=random.sample(range(len(iris_df)),4)
rownum


# In[16]:


for row in rownum:
    iris_df.loc[row, 'Sepal.Length'] = np.nan #결측치 넣기


# In[17]:


iris_df.loc[rownum, 'Sepal.Length']


# In[18]:


iris_grouped = iris_df.groupby(iris_df.Species)
iris_grouped.count()


# ### 다중열로 그룹화

# In[19]:


iris_df.groupby([iris_df['Species'], iris_df['Sepal.Length']]).describe().head()


# In[20]:


g = iris_df.groupby(iris_df.Species).mean()
g


# In[21]:


iris_df.groupby(iris_df.Species).mean().plot(kind="bar")


# In[22]:


import matplotlib.pyplot as plt
plt.plot() #shift_Tab 눌러서 도움말 확인


# - 그래프 양식 참고: https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot

# In[23]:


import matplotlib.pyplot as plt
g.plot(kind="bar", rot=0, figsize=(10,3))
plt.legend(bbox_to_anchor=(1.02, 0.7), loc=2, borderaxespad=0.) #범례 위치 조정(그래프 밖으로)


# In[26]:


iris_df.groupby(iris_df.Species).describe().transpose()
iris_df.groupby(iris_df.Species).describe().T #전치행렬 .T로도 가능(transpose()와 같은 효과)


# In[27]:


g = iris_df.groupby([iris_df['Species'], iris_df['Petal.Width']]).mean()
g


# In[28]:


g.unstack() #끝에 있는 인덱스 Petal.Width가 컬럼값으로 이동


# In[29]:


g.unstack().T


# In[30]:


g.plot.box(figsize=(10,5))


# In[31]:


g = iris_df.groupby([iris_df['Species'], iris_df['Petal.Width']])['Sepal.Length'].mean()
g


# In[32]:


type(g) #Series


# In[33]:


g.unstack()


# In[34]:


import pandas as pd
pd.options.display.max_columns


# In[35]:


pd.options.display.max_columns = 22


# In[36]:


g.unstack()


# In[37]:


g.unstack().T


# ## 8.2 그룹간 데이터(반복문 처리)

# In[38]:


iris_group = iris_df.groupby(iris_df.Species)
iris_group


# In[39]:


for idx, (species_name, group) in enumerate(iris_group):
    print(idx,"번째 그룹은",species_name)
    print(type(group))
    print("----------------------------------------")


# In[40]:


for idx, (species_name, group) in enumerate(iris_group):
    print(idx,'번째 그룹은 ', species_name)
    print(group.sample(5).sort_index())
    print("----------------------------------------")


# In[41]:


for group, item in iris_group:
    print(group, "그룹")
    print(item.head())
    print("----------------------------------------")


# ## 8.3 데이터 프레임 그룹 인덱싱

# In[42]:


for group, item in iris_group:
    print(group, '그룹')
    print(item.iloc[[1,11,21]]) #각 종별 1,11,21번째
    print("----------------------------------------")


# In[44]:


#각 종별 1,11,21번째
t = iris_df.groupby(iris_df.Species).take([1,11,21])
t


# In[45]:


t.loc['setosa']


# ## 8.4 레이블(원핫 인코딩)

# In[46]:


iris_df.head()


# In[47]:


iris_df.Species.describe()


# In[48]:


#레이블을 지원하는 패키지 이용
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
iris_df['species'] = le.fit_transform(iris_df['Species'])
iris_df


# # 9절. 데이터 구조 변경
# ## 9.1 와이드 포맷과 롱 포맷
# - 판다스 공식 문서에 나오는 melt: https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-by-melt
# - Tidy Data란? : https://vita.had.co.nz/papers/tidy-data.pdf (7페이지)

# In[49]:


import statsmodels.api as sm
airquality_data = sm.datasets.get_rdataset('airquality', package='datasets') #package 생략시 datasets(기본값)
airquality = airquality_data.data
airquality


# ## 9.2 melt()를 이용한 언피벗팅

# In[50]:


#열이름(Ozone, Solar.R, Wind, Temp)를 melt로 데이터로 넣을 예정
airquality.melt(id_vars=('Month','Day'))  #airquality 데이터가 변하는 것X


# In[51]:


airquality.sample()


# In[52]:


airquality_melted = airquality.melt(id_vars=['Month','Day'])
airquality_melted


# In[53]:


airquality.melt(id_vars=['Month','Day'], var_name='변수', value_name='값')


# In[54]:


airquality_melted_sort = airquality_melted.sort_values(by=["Month","Day"]) #롱 포맷(long format)
airquality_melted_sort.head()


# In[55]:


airquality.head() #와이드 포맷(wide format)


# In[56]:


import pandas as pd
airquality.melt(id_vars=['Month','Day'])
#pd.melt(airquality, id_vars=['Month','Day'])


# ## 9.3 pivot_table()을 이용한 피벗팅(롱형 -> 와이드형)

# In[57]:


#멜트된 데이터 프레임: airquality_melted, airquality_melted_sort
airquality2 = airquality_melted.pivot_table(index=['Month','Day'],
                                           columns=['variable'],
                                           values=['value']) #aggfunc='mean'
airquality2


# In[58]:


airquality2.loc[5].head()


# In[59]:


airquality2 = airquality2.reset_index(level=['Month','Day'],
                                     col_level=1)
airquality2


# In[60]:


airquality2.columns #(level0, levle1)


# In[63]:


airquality2.columns = airquality2.columns.droplevel(level=0) #level=0 없애기
airquality2


# In[64]:


#airquality_melted_sort 데이터 프레임을 와이드형으로 피벗팅
airquality3 = airquality_melted_sort.pivot_table(index=['Month','Day'],
                                                columns=['variable'],
                                                values=['value'])
airquality3


# In[65]:


airquality3 = airquality3.reset_index(level=['Month','Day'],
                                     col_level=1)
airquality3


# In[67]:


airquality3.columns = airquality3.columns.droplevel(level=0)
airquality3


# In[68]:


#결측치(NaN) 있어서 airquality2==airquality3 으로 비교 불가 (NaN이 False로 나옴)
import numpy as np
a = np.nan
a


# In[70]:


if a==np.nan:
    print("a==nan")
elif a is np.nan:
    print("a is nan")
else:
    print("a is not nan")


# In[ ]:


#주택도시보증공사_전국 평균 분양가격(2019년 12월).csv을 df_last 변수
#전국 평균 평당 분양가격(2013년 9월부터 2015년 8월까지).csv 을 df_first 변수
###df_last랑 df_first를 concat하기(df_first를 df_last를 참조하여 변환해야 함)###
#단, 시간별 평당분양 가격의 추이, 지역별 평단분양 가격의 추이를 분석할 예정
#concat한 데이터 프레임 columns:지역명, 연도월, 평당분양가격


# In[71]:


df_last = pd.read_csv('data/주택도시보증공사_전국 평균 분양가격(2019년 12월).csv', encoding='CP949')
df_last.head()


# In[72]:


df_first=pd.read_csv('data/전국 평균 평당 분양가격(2013년 9월부터 2015년 8월까지).csv', encoding='CP949')
df_first.head()


# In[73]:


#결측치 확인
df_first.isnull().sum()


# In[76]:


df_last.isna().sum()


# In[77]:


df_last.info()


# In[79]:


#pd.to_numeric(member_df['나이'], errors='coerce') #숫자 필드가 문자로 되어 있을 경우
df_last['분양가격(㎡)'] = pd.to_numeric(df_last['분양가격(㎡)'], errors='coerce')
df_last.info() #object -> float64


# In[80]:


df_last['평당분양가격'] = df_last['분양가격(㎡)']*3.3
df_last.head()


# In[90]:


new_df_last = df_last.loc[df_last['규모구분']=='전체',
                         ['지역명','연도','월','평당분양가격']]
new_df_last.head()


# In[98]:


new_df_last['연도월'] = new_df_last['연도'].astype(np.str)+'년'+ new_df_last['월'].astype(np.str)+'월'
new_df_last = new_df_last[['지역명','평당분양가격','연도월']]
new_df_last.head()


# In[86]:


#df_first 의 열이름을 행으로 melt하기
df_first_melted = df_first.melt(id_vars=['지역'],
                                var_name='연도월',
                                value_name='평당분양가격')
df_first_melted.head()


# In[100]:


df_first_melted.columns = ['지역명','연도월','평당분양가격']
new_df_first = df_first_melted
new_df_first.head()


# In[106]:


result = pd.concat([new_df_first, new_df_last])
result.sample(5).sort_index()


# In[ ]:


# 데이터프레임의 구조를 바꾸는 함수들 : melt, pivot_table(연산O), pivot(연산 X)


# In[107]:


year = [2020,2020,2020,2021,2021,2021]
month = [1,2,3]*2
latte=[410,401,402,400,404,405]
americano=[500,483,484,470,486,488]
mocha=[350,299,300,301,302,300]
sales = pd.DataFrame(np.c_[year, month, latte, americano, mocha],
                    columns=['year','month','latte','americano','mocha'])
sales


# In[108]:


sales_melted = sales.melt(id_vars=['year','month'],
                         var_name='coffee')
sales_melted.head()


# In[109]:


sales2 = sales_melted.pivot_table(index=['year','month'],
                                        columns=['coffee'],
                                        values=['value'])
sales2


# In[110]:


latte_sales = sales.loc[:,'year':'latte']
latte_sales


# In[111]:


latte_sales.pivot('year','month') #index=year, columns=month


# # 10절. 데이터프레임에 함수적용시키기
# ## 10.1 apply
# - 데이터 프레임이나 시리즈의 각 열 또는 각 행에 함수 적용 가능

# In[112]:


import statsmodels.api as sm
iris_df = sm.datasets.get_rdataset('iris').data  #package="datasets" 생략 가능
iris_df.sample()


# In[113]:


#독립변수
iris_df.iloc[:,:-1].head()


# In[114]:


x = iris_df.loc[:, 'Sepal.Length':'Petal.Width']
x.head()


# In[115]:


x.apply(np.round).head() #모든 요소에 np.round(반올림) 적용


# In[116]:


x.apply(np.sum, axis=0) #열별sum
#X.apply(np.sum, axis=1) #행별 sum


# In[117]:


#각 데이터와 평균과의 거리를 출력
iris_avg=x.apply(np.average)
iris_avg


# In[118]:


x.apply(lambda x:x-iris_avg, axis=1)
x.apply(lambda x:list(x-iris_avg), axis=1) #리스트 형태로 출력(가독성 떨어짐)
#result_type='broadcast'; 출력 타입을 원본데이터(X) 그대로
x.apply(lambda x:list(x-iris_avg), axis=1, result_type='broadcast')


# In[120]:


new_df_first.head()


# In[121]:


date="2021년3월"
date.split("년")


# In[122]:


def parse_year(x):
    return int(x.split("년")[0])
parse_year(date)


# In[123]:


def parse_month(x):
    return int(x.split("년")[-1].replace("월",""))
parse_month(date)


# In[124]:


new_df_first["연도"] = new_df_first["연도월"].apply(lambda x:int(x.split("년")[0]))
new_df_first["월"] = new_df_first["연도월"].apply(lambda x:int(x.split("년")[-1].replace("월","")))
new_df_first.head()


# ## 10.2 applymap
# - apply: 행 또는 열 단위로 함수 적용(데이터프레임이나 시리즈에 적용 가능)
# - applymap: 각 요소 하나하나 별로 적용(데이터프레임에서만 가능)

# In[126]:


x.apply(np.sum) #열단위로 sum(axis=0)


# In[127]:


#x.applymap(np.sum) #데이터 하나하나에 적용되므로 sum, max, mean 등 의미X
x.applymap(lambda x:x**2)


# ## 10.3 map
# - 시리즈타입의 벡터만 가능

# In[128]:


new_df_first["연도"] = new_df_first["연도월"].map(lambda x:int(x.split("년")[0]))


# In[129]:


x = pd.Series(["공지철",43,"서울특별시"], index=["Name","Age","Address"])
x


# In[130]:


def my_func(data):
    return data, len(str(data))
x.map(my_func)


# In[131]:


x.map(lambda data:(data, len(str(data))))


# In[132]:


#딕셔너리를 map에 적용하면 딕셔너리의 키별로 시리즈 값이 적용
dic = {"공지철":"공유", 43:45, "마포":"서대문"}
x.map(dic)


# In[133]:


s = pd.Series([1,2,3,4,None])


# In[134]:


s.map(lambda x:(x,x**2))


# In[135]:


#연산 적용이 안되는 부분은 건너뛰기(함수 적용X)
s.map(lambda x:(x, x**2), na_action='ignore')


# # 11절. 일괄 변경하기(결측치나 특정값)
# ## 11.1 fillna(특정값); 결측치를 특정값으로 변경

# In[136]:


df = pd.DataFrame([[np.nan, 2, np.nan, 0],
                  [3,4,np.nan,1],
                  [np.nan, 3, np.nan, 5],
                  [np.nan,3,np.nan,4]],
                columns=list('ABCD'))
df


# In[137]:


#모든 결측치를 0으로 채움
df.fillna(0)


# - 결측치가 아닌 이전값 또는 바로 다음값으로 채움
#  - pad/ffill; 결측치가 아닌 이전값으로 채움
#  - backfill/bfill; 결측치가 아닌 다음값으로 채움

# In[139]:


df.fillna(method="ffill")


# In[140]:


df.fillna(method="bfill")


# In[141]:


values = {"A":99, "B":98, "C":97, "D":95} #열별 결측치 대체값
df.fillna(value=values)


# In[142]:


df.fillna(value=df.mean())  #모두 결측치인 C컬럼은 결측치 대체가 안 됨


# In[143]:


mean = df.mean()
mean


# In[144]:


from math import isnan
for idx, value in mean.items():
    if isnan(value):
        mean[idx]=0
mean


# In[146]:


df.fillna(value=mean)


# In[147]:


df.fillna(value=values, limit=3) #3번째 결측치까지만 대체


# ## 11.2 replace(to_value, new_value, inplace=False)
# - to_value를 new_value로 변경
# - inplace=False; 변경된 내용을 반환. 데이터 프레임에 적용되지 않음(기본값)
# - inplace=True; 변경된 내용이 데이터 프레임에 적용. 반환값 없음

# In[148]:


s = pd.Series([0,1,2,3,4,None])
s.replace(0,5,inplace=True)
s


# In[149]:


s.replace(np.nan,3)


# In[150]:


df = pd.DataFrame({"A":[0,1,2,3,4],
                  "B":[5,6,7,8,9],
                  "C":['a','b','c','d','e']})
df


# In[151]:


df.replace([0,1,2,3,],99)


# In[152]:


df.replace([0,1,2,3],[99,98,97,96])


# In[153]:


df.replace(range(4),range(4,0,-1))  #[0,1,2,3]을 [4,3,2,1]로 대체


# In[154]:


df.replace({"A":0, "B":5},99) #A열의 0과 B열의 5를 99로 대체


# In[155]:


df = pd.DataFrame({'A':['bat','foo','bait'],
                   'B':['abc','bar','xyz']})
df


# In[156]:


#to_value에 정규표현식이 사용된 경우
#ba로 시작하고 마지막 임의의 문자가 있는 문자열로 변경
df.replace(r'^ba.$', 'newBar', regex=True)


# In[158]:


df.replace({'A':r'^ba.$'}, {'A':'newBar'}, regex=True)


# ## 11.3 where, mask
# - where; 조건이 만족하는 요소는 그대로 출력 <-> mask

# In[159]:


s = pd.Series([0,1,2,3,4])
s


# In[160]:


s.where(s>0) #수정


# In[161]:


s.mask(s>0, -s)


# ## 11.4 dropna
# - 결측치 있는 데이터를 누락시킴

# In[162]:


df = pd.DataFrame({"name":['김','이','박', np.nan],
                  "age":[np.nan, 20, 60, np.nan],
                  "born":[np.nan, '서울', np.nan, np.nan]})
df


# In[163]:


#결측치가 있는 행 제거
df.dropna()


# In[164]:


#모든 데이터가 다 결측치인 행만 제거
df.dropna(how='all', inplace=True)
df


# In[165]:


#결측치가 있는 열들 제거
df.dropna(axis='columns')


# In[166]:


#결측치가 2개 이상인 행만 제거
df.dropna(thresh=2)


# ## 11.5 astype()
# - 판다스의 dtype속성을 변경

# In[169]:


new_df_first.head()


# In[170]:


new_df_first.info()


# In[171]:


new_df_first["월"] = new_df_first["월"].astype(str)
new_df_first["평당분양가격"] = new_df_first["평당분양가격"].astype('float64', copy=True)
new_df_first.info()


# # 12절. 시리즈

# In[172]:


s = pd.Series([1000, 2000, 2500, 3000, 4000],
             index=['apple', 'banana', 'mango', 'cherry', 'orange'])
s


# In[173]:


s['mango']


# In[174]:


s['mango':'orange']


# In[175]:


s[['banana','cherry']]


# In[176]:


s.drop('mango') #inplace=True해야 적용


# In[177]:


s


# In[178]:


s.drop('banana', inplace=True)


# In[179]:


s.sort_values(ascending=False) #내림차순 정렬


# In[180]:


s.to_frame()


# In[181]:


s.to_frame().T


# In[ ]:




