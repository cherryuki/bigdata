#!/usr/bin/env python
# coding: utf-8

# **21-03-08 python 12_데이터 프레임과 시리즈(Pandas) (c)cherryuki (ji)**

# # <font color="blue">ch12. 데이터 프레임과 시리즈(Pandas)</font>

# # 1절. 판다스(Pandas) 패키지
# - 1차원 구조를 갖는 시리즈, 2차원 구조를 갖는 데이터 프레임 제공
# - 결측치 처리, 크기 변경(열 삽입, 열 삭제, 원하는 부분만 슬라이싱 등), 데이터 분할하거나 병합 구조 변경, 데이터 정렬, 파일 입출력 등이 용이
# - 판다스 패키지 index: https://pypi.org/project/pandas/
# - 판다스 API Docs: https://pandas.pydata.org/pandas-docs/stable/reference/index.html

# In[2]:


import pandas as pd
data = pd.read_json('data/ch09_member2.json', encoding='utf8')
data


# In[3]:


type(data)


# # 2절. 데이터 프레임 만들기
# ## 2.1 딕셔너리를 이용해서 데이터 프레임 만들기

# In[4]:


import pandas as pd
d = {'col1':[1,2], 'col2':[3,4]}
df = pd.DataFrame(data=d)
df


# In[5]:


d = [{'col1':1, 'col2':3}, {'col1':2, 'col2':4}]
df = pd.DataFrame(data=d)
df


# In[6]:


d = [{'col1':1, 'col2':3}, {'col1':2, 'col2':4}, {'col':5}]
df = pd.DataFrame(data=d)
df


# ## 2.2 리스트를 이용해서 데이터 프레임 만들기

# In[7]:


kor = [100, 95, 94, 90, 90]
math = [90, 95, 82, 73, 60]
df = pd.DataFrame({'kor':kor, 'mat':math})
df


# In[8]:


import numpy as np
df = pd.DataFrame(np.c_[kor,math], columns=['kor','math'])
df


# In[9]:


np.c_[[kor], [math]]


# In[10]:


pd.DataFrame(np.c_[[kor],[math]],
            columns=['score1', 'score2', 'score3','score4', 'score5', 
                    'score6','score7', 'score8', 'score9', 'score10'])


# ## 2.3 read_csv()

# In[11]:


df = pd.read_csv('C:\\Bigdata_자료\\Note_1\\08_Python\\상가업소정보_201912_01.csv', sep='|', encoding='UTF8')
df.head(3)


# In[12]:


pd.options.display.max_columns #최대로 출력할 수 있는 컬럼(열) 수


# In[13]:


pd.options.display.max_columns = 39 #최대 39열까지 출력하게끔 변경
df.head(3)


# In[14]:


#(1) csv파일로 읽어오기, (2)주석행(#) 지정
member_df = pd.read_csv('data/ch12_member_data.csv', sep=',', encoding='utf-8', comment='#')
member_df


# In[15]:


type(member_df) #2차원: DataFrame


# In[16]:


type(member_df['Name']) #1차원: Series


# In[17]:


#(3) 행 제외해서 읽어오기 #0행을 없애면 header가 없어지므로 주의
member_df = pd.read_csv('data/ch12_member_data.csv', skiprows=[1,3], comment='#')
member_df


# ## 2.4 sklearn.datasets 모듈 데이터를 데이터 프레임으로 변환하기
# - sklearn 패키지에는 학습을 위한 많은 데이터셋 제공. 딕셔너리 형태로 제공

# In[18]:


from sklearn import datasets
import pandas as pd
import numpy as np


# In[20]:


iris=datasets.load_iris()
iris['feature_names'] #독립변수의 colums
iris.feature_names


# In[23]:


iris['data'] #독립변수
iris.data


# In[24]:


iris['target'] #레이블 인코딩(문자로 표현된 레이블을 숫자로 바꿈) 된 종속변수 cf.One-Hot encoding; 0,1
iris.target


# In[25]:


iris['target_names']
iris.target_names


# In[27]:


#레이블 인코딩 되지 않은 종속 변수
iris.target_names[iris.target]
iris['target_names'][iris['target']]


# In[28]:


x = pd.DataFrame(iris.data, columns=iris.feature_names)
x


# In[30]:


x.columns


# In[31]:


#x.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
x.columns = [col[:12].strip().replace(' ','_') for col in x.columns]
x


# In[32]:


y = pd.DataFrame(iris.target_names[iris.target], columns=['species'])
y


# In[33]:


iris = pd.concat([x,y], axis=1) #열병합
iris.head(2)


# In[34]:


iris.head(-148) #총 150열 head(-148) = head(2)와 동일 (음수: 뒤에서 부터)


# In[35]:


iris.tail(-145) 


# In[36]:


iris.tail(5)


# In[37]:


iris.shape


# # 3절. 이름 지정하기(열, 행)
# ## 3.1 열이름 지정하기

# In[38]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df


# In[39]:


member_df.columns = ['이름', '나이', '이메일', '주소']
member_df


# ## 3.2 행이름 지정하기

# In[40]:


member_df.index


# In[41]:


member_df.index = ['동', '서', '남', '북']
member_df


# In[42]:


member_df.loc[['동','남'], '이름']


# ## 3.3 레벨 이름 지정하기

# In[43]:


member_df.columns = [['기본정보','기본정보','추가정보','추가정보'],
                    ['이름','나이','이메일','주소']]
member_df.columns.names=['대분류','소분류']
member_df


# In[47]:


member_df.index = [['좌우','좌우','상하','상하'],
                  ['동','서','남','북']]
member_df


# In[50]:


member_df.loc['상하', '기본정보']['이름']['남']


# # 4절. 부분 데이터 조회
# - 단일 열만 조회, loc, iloc

# In[51]:


#member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df.columns = ['이름', '나이', '이메일', '주소']
member_df.index =range(member_df.shape[0]) #행수
member_df


# In[52]:


member_df.shape


# ## 4.1 단일열 조회

# In[53]:


member_df["이름"]


# In[54]:


#데이터 프레임 읽은 후
member_df.shape


# In[55]:


member_df.head()


# In[56]:


member_df.info()


# In[59]:


#pd.to_numeric(member_df['나이'], errors='coerce') #숫자 필드가 문자로 되어 있을 경우


# In[60]:


member_df.isnull() #결측치 확인


# In[61]:


False == 0


# In[62]:


True == 1


# In[63]:


member_df.isnull().sum() #열별 결측치 수 확인(결측치 없으면 0으로 나옴)


# In[65]:


member_df.isna() #결측치면 True, 결측치가 아니면 False


# In[66]:


member_df.isna().sum() #열별 결측치 수


# In[67]:


member_df["이름"] #dtype: 요소의 타입


# In[68]:


type(member_df["이름"]) #1차원(단일열): 시리즈


# ## 4.2 loc을 이용한 조회(columns, index로 조회)

# In[69]:


member_df.index=['동','서','남','북']
member_df


# In[70]:


member_df.loc[:, '이름':'이메일'] #모든 행의 이름, 나이, 이메일


# In[71]:


member_df.loc[:, ['이름', '이메일']] #모든 행의 이름, 이메일


# In[72]:


member_df.loc[['동', '서'], ['이름', '주소']]


# In[73]:


member_df.loc['동':'남', ['이름','주소']] #동~남행까지(남행 포함)


# In[74]:


member_df.loc["동":"남", "이름":"이메일"]


# In[75]:


#loc안에는 columns 이름, index이름, 조건
member_df.loc[member_df.나이>40]


# In[76]:


member_df.loc[member_df.나이<40, "이름":"이메일"]


# ## 4.3 iloc을 이용한 조회(정수로 조회)
# - iloc[from, to, by]; from부터 by씩 증가해서 to전(to미포함)까지(정수를 이용해서 데이터 셋 조회)
# - from, to, by에는 음수 가능. 음수 인덱스 번호는 뒤에서부터
# - 맨 처음: 0, 맨 마지막: -1

# In[79]:


member_df.iloc[1:3, 1:3]


# In[78]:


member_df.iloc[1,1:3]


# In[80]:


member_df.iloc[2] #열인덱스 번호가 생략되면 전체 열 의미


# In[81]:


member_df.iloc[-2, 0:2]


# In[82]:


member_df.iloc[::-1, ::-1] #열과 행을 거꾸로 출력


# In[83]:


member_df.iloc[[0,3],[0,1,3]]


# ## 4.4 조건으로 조회하기

# In[84]:


#iris 데이터 가져오는 방법1
from sklearn import datasets
iris = datasets.load_iris() #딕셔너리
x = pd.DataFrame(iris["data"], columns=iris.feature_names)
y = pd.DataFrame(iris.target_names[iris.target], columns=['species'])
iris_df=pd.concat([x,y], axis=1)
iris_df


# In[85]:


#iris 데이터 가져오는 방법2
import seaborn as sbn
iris_df = sbn.load_dataset("iris")
iris_df


# In[86]:


#iris 데이터 가져오는 방법3
#statsmodels 패키지를 통해 R데이터 셋 가져오기
#get_rdataset()함수로 R패키지 데이터셋을 가져옴
import statsmodels.api as sm
iris = sm.datasets.get_rdataset("iris", package="datasets")
iris_df = iris.data #.data: 데이터를 데이터 프레임 형태로 가져옴
iris_df


# In[87]:


iris_df.iloc[0:5, :-1] #독립변수 top5행만


# In[88]:


iris_df.iloc[:, -1] #종속변수만


# In[89]:


print(member_df.이름)
print(member_df['이름'])


# In[90]:


iris_df.loc[iris_df.Species=='virginica'].head()


# In[91]:


#종이 virginica 행의 특정 열
iris_df.loc[iris_df["Species"]=="virginica", ["Sepal.Length", "Sepal.Width", "Species"]].head()


# In[92]:


#종이 virginica, Sepal.Length가 7.0이상인 데이터만 모든 열 조회
iris_df.loc[(iris_df['Species']=='virginica') & (iris_df['Sepal.Length']>=7.0)]
#괄호 반드시 필요! 괄호 없으면 & 비트연산 먼저 진행 됨


# # 5절. 데이터 추가 및 삭제
# ## 5.1 데이터 프레임 요소 삭제

# In[93]:


import pandas as pd
member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df


# ### 1) 단일행 삭제하기

# In[94]:


member_df.drop(3, axis=0) #axis=0은 생략가능. 행에서 찾아 삭제된 데이터 반환(실제 삭제X)
#member_df에서 삭제된 것은 X


# In[96]:


member_df


# In[97]:


member_df = member_df.drop(2, axis=0)
member_df


# In[98]:


member_df.drop(3, inplace=True) #inplace_Ture이면 member_df 데이터셋에서 데이터 삭제


# In[99]:


member_df


# In[100]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df.index = ['동', '서', '남', '북']
member_df


# In[102]:


member_df.drop('북', axis=0) #axis=0, '북'은 index. 해당 index행을 삭제한 데이터를 반환


# In[103]:


#drop()으로 해당 index행을 삭제 후, 데이터를 member_df에 적용시키려면 inplace=True 를 기재하거나 member_df에 할당해야 함
member_df.drop('북', inplace=True)


# In[104]:


member_df


# ### 2) 단일열 삭제하기

# In[105]:


member_df.drop('Email', axis=1) #axis=1 해당 열을 삭제한 데이터셋을 반환(실제 삭제X)


# In[106]:


#위의 drop함수의 결과가 member_df에도 반영되게 하려면 inplace=True 추가
member_df.drop('Email', axis=1, inplace=True)
member_df


# In[107]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df.index=['동','서','남','북']


# ### 3) 여러행이나 열을 삭제

# In[108]:


member_df = member_df.drop(labels=['동','북'])
member_df


# In[109]:


member_df.drop(labels=['Age','Email','Address'],axis=1)


# ## 5.2 데이터 프레임의 요소 추가
# ### 1) 열 추가

# In[110]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df


# In[111]:


#특정 열을 이용해서 새로운 열 추가
member_df['BirthYear'] = year = 2021-member_df['Age']+1
member_df


# In[112]:


member_df['Register'] = 2000
member_df


# In[113]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df


# In[115]:


#member_df['Register'] = [2000]*len(member_df)
member_df['Register'] = 2000
member_df


# In[117]:


#member_df['Register'] = [2000]*len(member_df)
member_df['Register'] = [2001,2003,1990,2007] #추가한 열의 행마다 다른값 할당
member_df


# In[118]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df['Register']=[2001,2003, None, 2007] #하나가 실수면 전부 실수(NaN은 float타입)
member_df


# In[119]:


import numpy as np
np.nan


# In[120]:


import pandas as pd
pd.np.nan


# In[121]:


type(np.nan)


# ### 2) 행추가

# In[122]:


member_df = pd.read_csv('data/ch12_member_data.csv', comment='#')
member_df


# In[123]:


#행추가 방법1. 시리즈(리스트)를 이용한 행 추가
new_member = pd.Series(['박보검', 29, 'park@green.com', '서울특별시 양천구'], index=member_df.columns)
new_member


# In[124]:


member_df.append(new_member, ignore_index=True)#추가된 데이터 반환(실제 데이터에 추가X)


# In[125]:


member_df = member_df.append(new_member, ignore_index=True) 
member_df


# In[126]:


#시리즈 데이터를 이용한 열 추가
pd.Series([2001,1990,2007], index=[0,2,3])


# In[127]:


member_df['Register'] = pd.Series([2001, 1990, 2007], index=[0,2,3])
member_df


# In[128]:


#행추가 방법 2. 딕녀서리를 이용한 행 추가
member_df


# In[130]:


new_member={'Name':'조인성', 'Age':41, 'Email':'insung@green.com',
           'Address':'서울특별시 서대문구', 'Register':1997}
member_df.append(new_member, ignore_index=True) #member_df에 반영X


# In[131]:


#행추가 방법3. 데이터 프레임을 이용한 행 추가(여러 행을 한 번에 추가 가능)
new_member = pd.DataFrame({'Name':['박보영', '아이유'],
                          'Age': [32, 29],
                          'Email':['boyoung@green.com', 'jieun@green.com'],
                          'Address':['서울특별시 마포구', '서울특별시 구로구'],
                          'Register':[2006, 2008]})
new_member


# In[132]:


new_df = member_df.append(new_member)
new_df.index=range(len(new_df)) #데이터 프레임을 통해서 추가할 경우, index 다시 조정해야 함(중복된 것 없애기)
new_df


# # 6절. 정렬
# ## 6.1 행이름(index)으로 정렬

# In[133]:


member_df.index = ['동','서','남','북','양']
member_df


# In[134]:


member_df.sort_index() #행이름 순으로 정렬. member_df가 바뀌는 것X


# In[135]:


member_df


# In[136]:


member_df.sort_index(inplace=True) #결과 반영하려면 inplace=True
member_df


# ## 6.2 열이름(columns)으로 정렬

# In[137]:


member_df.sort_index(axis=1) #열이름 순으로 정렬


# In[138]:


member_df


# ## 6.3 값으로 정렬

# In[139]:


member_df.sort_values(by="Name", inplace=True) #by=['Name']으로 적어도 동일한 결과
member_df


# In[140]:


new_series = pd.Series(['이지아', 30, 'jiah@green.com', '경기도 광명시', 2013], index=member_df.columns)
new_series


# In[141]:


member_df = member_df.append(new_series, ignore_index=True)
member_df


# In[142]:


member_df.sort_values(by=['Name','Age','Email'], inplace=True)
member_df


# In[143]:


member_df.sort_values(by=['Age'], inplace=True, ascending=False) #내림차순 정렬
member_df


# # 7절. 기초 통계 분석
# - count: 결측치(NaN)를 제외한 개수
# - min: 최소값
# - max: 최대값
# - sum: 합
# - cumprod: 누적합
# - mean: 평균
# - median: 중앙값
# - quantile: 분위수
# - corr: 상관관계
# - std: 표준편차
# - var: 분산(=표준편차*표준편차)
# - describe: 요약 통계량

# In[145]:


import statsmodels.api as sm
iris_df = sm.datasets.get_rdataset("iris", package="datasets").data
iris_df.head()


# In[146]:


type(iris_df)


# In[147]:


iris_df.shape


# ## 7.1 최소값, 최대값, 평균, 중위수, 표준편차, 분위수, ...

# In[148]:


iris_df.min() #axis=0 열별 최소값


# In[149]:


iris_df.min(axis=1) #행별 최소값


# In[150]:


iris_df.max() #열별 최대값


# In[151]:


iris_df.mean(axis=0) #열별 평균


# In[152]:


iris_df.median() #열별 중앙값


# In[153]:


iris_df.var() #열별 분산


# In[154]:


iris_df.std() #열별 표준편차


# In[156]:


#평균, 최소값, 최대값, ... 결과: 시리즈
#사분위수는 결과가 데이터 프레임 형태
iris_df.quantile(q=[0,0.25,0.5,0.75,1], interpolation='nearest') #열별 사분위수 출력


# ## 7.2 요약 통계량

# In[157]:


iris_df.describe()


# In[158]:


iris_df.describe(include='all')


# In[159]:


#iris_df.describe() #기본적으로 숫자데이터만 요약통계 출력함
iris_df.iloc[:,:-1].describe()


# In[160]:


#문자 또는 타임 스탬프 자료의 요약 통계: unique(자료의 가지수), top(가장 많이 나온 자료), freq(top의 빈도수)
iris_df.iloc[:,-1].describe()


# In[161]:


#include와 exclude의 사용 예
df = pd.DataFrame({'a':[1,2]*3,
                 'b':[True, False]*3,
                 'c':[2.0, 4]*3})


# In[162]:


df.describe()


# In[163]:


df.info()


# In[164]:


#include 및 exclude 매개변수를 사용하여 분석되는 열을 추가하거나 제외
df.describe(include=['int64', 'bool'])


# In[165]:


df.describe(include='bool')


# In[166]:


df.describe(exclude=['bool','float64']) #exclude 분석열에서 제외할 타입


# In[167]:


df.describe(include=['int64'], exclude=['float64']) #include와 exclude에 같은 유형 사용시 오류 발생


# In[168]:


iris_df.mean()


# In[169]:


var = iris_df.var()
var


# In[170]:


import numpy as np
np.sqrt(var)


# In[171]:


iris_df.std()


# ## 7.3 공분산, 상관계수

# In[172]:


#https://destrudo.tistory.com/15 그래프 부분 참조
#공분산 Cov(x, y) = E((x-x의 평균)(y-y의 평균))
#분산 Var(x) = E((x-x의 평균)의 제곱)
iris_df.cov()


# In[173]:


#상관계수 -1 <= r <= 1
iris_df.corr()


# In[174]:


iris_df.plot(x="Petal.Width", y="Petal.Length", kind="scatter") #상관계수:0.962665


# In[175]:


iris_df.plot(x="Sepal.Length", y="Sepal.Width", kind="scatter") #상관계수: -0.117570 (상관계수=0 상관X)


# In[ ]:




