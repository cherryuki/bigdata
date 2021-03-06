#!/usr/bin/env python
# coding: utf-8

# **21-03-04 python 11_N차원 배열 다루기(Numpy) (c)cherryuki (ji)**

# # <font color="blue"> ch11. N차원 배열 다루기 </font>
# - N차원 배열 객체
# - 행렬 개념으로 이해
# - C언어로 구현된 고성능 수치계산 패키지 Numpy 이용
# - C/C++, 포트란(Fortran) 코드 통합 도구

# # 1절. 넘파이(Numpy) 패키지

# In[2]:


import numpy as np
a = np.arange(15)
a


# In[3]:


a = np.arange(15).reshape(3,5) #3행5열로 변경
a


# In[4]:


type(a) #a변수 자체의 타입: N차원 배열(ndarray)


# In[5]:


a.dtype #a변수의 요소들의 type


# In[6]:


a.dtype.name #a변수의 요소들의 type


# In[7]:


a.itemsize #요소 하나하나 사이즈(byte단위)


# In[8]:


a.ndim #축 수(차원수)


# In[9]:


a.shape #배열 구조(행, 열)


# In[10]:


a.size #배열 요소의 총 수(행수*열수)


# In[11]:


#dtype속성을 바꾸면 형변환 되지 않음
a = np.arange(12).reshape(3,4)
print(a)
a.dtype


# In[12]:


a.size


# In[13]:


a.dtype = np.int64  #a배열의 요소 dtype을 int64로 변경??
a.dtype


# In[14]:


a #함부로 dtype변경X -> dtype변경할 경우 astype이용!


# In[15]:


a.size


# # 2절. 넘파이 배열
# - array()함수를 이용한 다른 파이썬 구조를 넘파이 배열로 변환
# - 넘파이 배열을 생성하는 기타 함수들: arange(), ones(), zeros()
# - 특수 라이브러리 함수(ex.random) 이용
# - [넘파이 Docs](https://numpy.org/doc/stable/index.html)

# ## 2.1 array()함수로 넘파이 배열 만들기

# In[16]:


import numpy as np
a = np.array([2,4,6])
a


# In[18]:


for i in a:
    print(i, end='\t')


# In[19]:


a[1]


# In[21]:


a = np.array([1,5,7.3]).reshape(3,1)
a


# In[22]:


a.shape


# In[23]:


a.dtype


# In[25]:


b = np.array([[1.5, 2.3], [5,7]]) #자동 type 셋팅(행마다 데이터 수가 같아야 함)
b


# In[26]:


np.__version__


# In[27]:


a = np.array([1,2,3,4.3]).reshape(2,2) #2행2열 2차원 배열
a


# In[28]:


a.dtype


# In[29]:


b = np.array([[1,2,3],[4,5,6]]) #dtype 자동 셋팅
b


# In[30]:


b.dtype


# In[31]:


b = np.array([[1,2,3],[4,5,6]], dtype=np.int64) #dtype을 인수로 셋팅
b


# In[32]:


b.dtype


# In[33]:


b = b.astype(np.int32) #dtype바꾸기
b.dtype


# In[34]:


list_=[[1,2,3],[4,5,6]]
list_


# In[35]:


for row in list_:
    for data in row:
        print(data, end='\t')
    print()


# In[36]:


for i, row in enumerate(list_):
    for j, data in enumerate(row):
        print("{}행{}열: {}".format(i, j, data), end='\t')
    print()


# In[37]:


#리스트에서 인덱싱
list_[0][1]


# In[38]:


#리스트에서 인덱싱 슬라이싱
list_[0][0:2] 


# In[39]:


b = np.array([[1,2,3],[4,5,6]], dtype=np.int16)
b


# In[40]:


for row in b:
    for data in row:
        print(data, end='\t')
    print()


# In[42]:


for i, row in enumerate(b):
    for j, data in enumerate(row):
        print("{}행{}열:{}".format(i,j,data), end='\t')
    print()


# In[43]:


#넘파이 배열에서의 인덱싱[num1, num2]
b[0,1]


# In[44]:


#넘파이 배열에서의 슬라이싱
b[1, 0:2]


# In[45]:


c = np.array([[1,2],[3,4]], dtype=complex) #dtype이 복소수
c


# In[48]:


d = np.array(c, copy=False)
print('d=',d, sep='\n')
print(id(c), id(d))
print('d의 요소 타입:', d.dtype)
d[0,0] = 100
print('c=',c,sep='\n')


# In[49]:


d = np.array(c, copy=True, dtype=int)
print('d=',d, sep='\n')
print(id(c), id(d))
print('d의 요소 타입:', d.dtype)
d[0,0] = 100
print('c=',c,sep='\n')


# ## 2.2 기본값이 있는 배열 만들기
# - zeros: 모든 요소가 0인 배열
# - ones: 모든 요소가 1인 배열
# - empty: 초기 내용은 임의 값인 배열(메모리 상태에 따라 달라짐)
# - 상기 함수들로 생성된 배열의 기본 dtype은 float64. dtype 속성 지정 가능

# In[50]:


np.zeros((3,4)) #3행4열 2차원 배열(요소값이 모두 0)


# In[51]:


x = np.zeros((2,3,4), dtype=np.int16) #2면3행4열 3차원 배열
print(x)
print(x.dtype)


# In[52]:


np.ones((2,5), dtype=np.int8)


# In[64]:


np.empty((3,3))


# ## 2.3 연속된 값을 갖는 배열 만들기
# - np.arange(from, to, by, type=None); from부터 by씩 증가한 값을 to 앞까지(to 미포함) 목록으로 N차원 배열 만듦. from 생략시 0, by 생략시 1
# - np.linspace(from, to, num): from부터 to까지(to포함) num개 숫자들을 N차원 배열로 만듦. num생략시 50

# In[54]:


np.arange(10, 30, 5, dtype=np.float64)


# In[55]:


np.arange(0,2,0.5)


# In[56]:


from numpy import linspace
linspace(0,2,9)


# In[57]:


#많은 수의 점들을 생성할 때 유용
from numpy import pi
x = linspace(0, 2*pi, 100)
print(x)
f = np.sin(x)
print(f)


# In[65]:


import matplotlib.pyplot as plt
plt.plot(x,f)
plt.show()


# In[66]:


x = np.random.normal(0,1,100) #평균0, 표준편차1인 표준정규 분포값 100개
x


# In[67]:


plt.hist(x)


# ## 2.4 배열의 차원 변경하기

# In[68]:


t = np.random.random((3,4)) #3행4열 2차원 배열(random수)
t


# In[69]:


t*10 #배열*10은 요소별로 10씩 곱한 결과


# In[70]:


a = np.floor(t*10) #floor(); 버림
a


# In[71]:


a.shape


# In[72]:


a.ravel() #차원이 풀린 배열을 반환(a가 바뀌는 것은 아님)


# In[73]:


a


# In[74]:


a.reshape(2,6) #shape가 수정된 배열을 반환(a는 그대로)


# In[75]:


a


# In[76]:


#a는 3행 4열 2차원 배열. 2차원 배열은 행렬(Matrix)로 이해
a.T #전치행렬(행과 열 거꾸로)


# In[77]:


a.transpose() #전치행렬을 반환(a는 그대로)


# In[78]:


a.reshape(3,-1) #-1로 셋팅하면 해당 차원의 크기가 자동으로 계산


# In[79]:


a.reshape(-1, 3) #reshape에는 -1 사용 가능


# In[80]:


a.resize(3,4) #resize에는 -1 넣을 수 없음
a


# In[81]:


#로또 번호6개(1~45)를 랜덤으로 뽑아서 sort()하여 1차원 배열에 넣기
45*np.random.random(6) #0부터 45미만의 실수


# In[82]:


while True:
    a = np.floor(45*np.random.random(6))+1
    a.sort()
    if len(set([int(data) for data in a]))==6:
        print(a)
        break


# In[83]:


np.array([[1,2],[2.0,'1']]) #문자를 하나 넣으면 문자 타입으로 


# ## 2.5 배열 인쇄
# - 배열이 너무 커서 인쇄할 수 없는 경우 자동으로 건너뛰고 모서리만 인쇄
# - 전체를 인쇄하고 싶을 경우: numpy.set_pintoptions(threshold=num)

# In[84]:


#배열이 너무 커서 인쇄할 수 없는 경우
print(np.arange(10000))


# In[87]:


#배열이 너무 커서 인쇄할 수 없는 경우 자동으로 건너뛰고 모서리만 인쇄
print(np.arange(1000).reshape(10,100))


# In[88]:


#전체를 인쇄하고 싶을 때 인쇄 옵션 중 threshold 값을 변경함
np.set_printoptions(threshold=1000)
#내 시스템에서 최대치: sys.maxsize
#무한대: np.inf


# In[89]:


print(np.arange(1000).reshape(10,100))


# ## 2.6 기본 연산 동작
# ### 1) 배열의 요소별 연산

# In[97]:


a = np.array([20,30,40,50])
b = np.array([1,2,3,4])


# In[98]:


print(a)
print(b)


# In[99]:


a + b #index 요소별로 연산


# In[100]:


a - b


# In[101]:


a * b


# In[102]:


a / b


# In[103]:


a


# In[104]:


a < 35 #요소별 연산


# In[105]:


a[a<35] #a배열에서 a<35 데이터만 추출


# ### 2) 행렬의 곱(@)

# In[106]:


A = np.array([[1,1], [0,1]])
B = np.array([[2,0], [3,4]])


# In[107]:


A, B


# In[108]:


print("요소별 곱 A*B=", A*B, sep='\n')
print("행렬 곱 A@B=", A@B, sep='\n')
print("행렬 곱 A.dot(B)=", A.dot(B), sep='\n')


# ### 3) 복합 대입 연산자 사용(+=, -=, *=, /= 등)

# In[113]:


a = np.ones((2,3), dtype=int) #int32


# In[110]:


b = np.random.random((2,3)) #2차원 2행2열 배열 float64
b


# In[114]:


a += 2
a


# In[115]:


b += a
b


# In[116]:


a += b #b가 float64이므로 a+b는 float64 -> 에러 발생(a는 int32)


# In[117]:


a = np.ones(3, dtype=np.int16)
b = np.linspace(0, np.pi, 3)
print(a)
print(b)


# In[118]:


c = a+b
print(c)
print(c.dtype)


# In[119]:


c = a+b*1j
c


# In[120]:


c.dtype


# ### 4) 배열 요소별 집계; 배열 요소 전체의 sum, min, max 등

# In[121]:


a = np.array([[0,1,2,3],[1,2,3,4]])
a


# In[122]:


print("a 배열 요소들 전체의 합:", a.sum())
print("a 배열 요소들 최소값:", a.min())
print("a 배열 요소들 최대값:", a.max())


# ### 5) 배열 축별 집계: 행별 sum, min, max 열별 sum, min, max 등
# - axis=1 행별
# - axis=0 열별

# In[123]:


a = np.array([[1,3,5,7],[2,4,6,8]])
a


# In[124]:


print('a배열의 행별 합:', a.sum(axis=1))
print('a배열의 열별 합:', a.sum(axis=0))


# In[125]:


print('a배열의 행별 최소값:', a.min(axis=1))
print('a배열의 열별 최소값:', a.min(axis=0))


# In[126]:


print('a배열의 행별 최대값:', a.max(axis=1))
print('a배열의 열별 최대값:', a.max(axis=0))


# In[127]:


#누적합
print(a)
print(a.cumsum(axis=1)) #행별로 누적합


# In[128]:


a.cumsum(axis=0) #열별로 누적합


# In[129]:


b = np.arange(24).reshape(2,3,4) #2면3행4열
b


# In[133]:


b[0,2,3] #0면 2행 3열


# In[134]:


b.sum(), b.min(), b.max()


# In[135]:


b.sum(axis=0) #면은 빼고 같은 행과 열끼리 sum


# In[136]:


b.sum(axis=1) #행은 빼고 같은 면, 열끼리 sum


# In[137]:


b.sum(axis=2) #열은 빼고 같은 면, 행끼리 sum


# In[138]:


np.sum(b) #요소들의 전체 합


# In[139]:


np.mean(b) #요소들의 전체 평균


# In[140]:


np.std(b) #요소들의 표준편차


# In[141]:


np.var(b) #분산


# In[142]:


np.std(b)**2


# In[143]:


np.sqrt(np.var(b)) #np.sqrt()의 매개변수에는 스칼라변수, 벡터변수 모두 가능


# In[144]:


import math
math.sqrt(np.var(b)) #math.sqrt()의 매개변수는 스칼라 변수


# ## 2.7 그 외 함수들

# In[145]:


a = np.arange(3)
np.sqrt(a)


# In[146]:


np.exp(a) #지수 e의 0승, 1승, 2승


# In[147]:


a


# In[148]:


b = np.array([10,11,12])
np.add(a,b)


# In[149]:


#메모리 사용량 측정(메모리 프로파일러)를 로드하고 임이의 데이터 생성 후 np.add
#아나콘다 프롬포트: pip install memory_profiler
get_ipython().run_line_magic('load_ext', 'memory_profiler')
A = np.random.randn(10000000)
B = np.random.randn(10000000)
C = np.random.randn(10000000)


# In[150]:


# %%는 주석과 같이 기재할 수 없음
# %%time: 셀을 실행할 때 소요시간 출력
# %memit: 메모리 사용량 출력


# In[151]:


get_ipython().run_cell_magic('time', '', '%memit G = A*B+C\nprint(G)')


# In[152]:


get_ipython().run_cell_magic('time', '', '%memit T=A*B; G=T+C; del T\nprint(G)')


# In[153]:


get_ipython().run_cell_magic('time', '', '%memit T=A*B; G=T+C\nprint(G)')


# In[154]:


# np.add()경우 배열 별 연산을 할 경우 메모리 절약


# In[155]:


get_ipython().run_cell_magic('time', '', '%memit T=A*B; np.add(T,C,T)\nprint(T)')


# ## 2.8 브로드 캐스팅

# In[156]:


#1차원 배열의 경우
from numpy import array
a = array([1,2,3])
np.add(a,10)


# In[157]:


#2차원 배열의 경우 두 배열의 열(후미 축)의 크키가 동일
a = array([[0.,0,0],
           [10,10.,10],
           [20,20,20],
           [30,30,30]])
b = array([5,5,5])
np.add(a,b)


# In[158]:


np.multiply(a,b)


# In[159]:


from numpy import array, newaxis
a = array([0,10,20,30])
b = array([1,2,3])


# In[160]:


a[:,newaxis] #newaxis 연산자는 배열에 새로운 축을 추가(-> 4행1열 2차원 배열)


# In[162]:


#4x1 배열 + 1x3 배열(브로드 캐스팅 규칙 따름)
x = np.add(a[:,newaxis], b) #a[:,newaxis]+b
x


# In[163]:


a[0]+b[1] == x[0,1]
a[1]+b[2] == x[1,2]


# # 3절. 배열 합치기/분할하기

# In[164]:


a = np.arange(10)*3
a


# ## 3.1 인덱싱과 슬라이싱

# In[165]:


#인덱싱
a[2], a[-1] #인덱스를 벗어나면 에러발생


# In[166]:


#슬라이싱
a[2:5] #2번째부터 5번째 앞까지


# In[167]:


a[0:12:2] #슬라이싱은 벗어난 인덱스 값 입력해도 에러X


# In[168]:


a[::-1] #a배열 거꾸로 출력


# In[169]:


a[:6:2] = 99
a


# 도움말 문서들
# - 인덱싱 : https://docs.scipy.org/doc/numpy/user/basics.indexing.html
# - 배열 인덱싱 : https://docs.scipy.org/doc/numpy/reference/arrays.indexing.html
# - newaxis : https://docs.scipy.org/doc/numpy/reference/constants.html#numpy.newaxis

# ## 3.2 다차원 인덱싱

# In[2]:


import numpy as np
np.ones((2,3))


# In[5]:


def f(x,y):
    return 10*x+y


# In[6]:


f(2,3)


# In[7]:


#5행4열 2차원 넘파이 배열 int16 dtype으로 생성(안에 데이터는 f함수에 의해 결정)
a = np.fromfunction(f, (5,4,), dtype=np.int16)
a


# In[8]:


a = np.fromfunction(lambda x,y:10*x+y, (5,4), dtype=np.int16)
a


# In[9]:


a[2,3]


# In[10]:


a[-2,-1] #인덱스는 음수 가능; 음수 인덱스는 끝에서 부터 n번째


# In[11]:


a[0:10, -1] #마지막 열들만 출력


# In[12]:


#1~3행 모든 열
a[1:4, :] 


# In[14]:


a[1:4,]


# In[13]:


a[1:4, ...] #...:누락된 인덱스의 전체를 의미


# In[15]:


a[1:4] #(마지막 축(열) 생략 가능 - 모든 열)


# In[16]:


a[:, -1:-3:-1] #모든 행에 마지막 열, 마지막 전 열


# In[17]:


a[..., -1:-3:-1]


# In[18]:


b = np.arange(24).reshape(2,3,4)
b


# In[19]:


b[1,0,0]


# In[20]:


#1면 데이터 모두 출력
b[1, :, :]


# In[21]:


b[1]


# In[22]:


b[1, ...] #,...은 생략 가능


# In[23]:


#1행 모두 출력
b[:,1,:]


# In[24]:


b[:,1,...] #,...은 생략 가능


# In[25]:


b[:,1]


# In[26]:


#1열 모두 출력
b[:,:,1]


# In[27]:


b[...,1] #...,은 생략 불가(마지막에 ,...이 올 경우만 생략 가능)


# In[28]:


b


# In[40]:


for i, data in enumerate(b):
     for j, row in enumerate(data):
            for k, item in enumerate(row):
                print("{}면{}행{}열: {}".format(i,j,k,item), end='\t')
            print()
     print()


# In[41]:


for i, data in enumerate(b):
    for j, row in enumerate(data):
        for k, item in enumerate(row):
            print(item, end=' ')


# In[42]:


#ravel(): n차원을 풀어서 1차원 배열로 반환(b의 차원은 그대로)
b.ravel()


# In[44]:


print(list(b.flat))


# In[45]:


for item in b.flat:
    print(item, end=' ')


# In[47]:


for item in b.ravel():
    print(item, end=' ')


# In[48]:


b.flat?? #example 확인 가능


# ## 3.3 두 배열을 쌓아 합치기
# - vstack(튜플): 아래에 추가하는 방식으로 쌓아 합침
# - hstack(튜플): 옆으로 추가하는 방식으로 쌓아 합침
# - dstack(튜플): 마지막 축(열)을 쌓아 합침

# In[50]:


c = np.arange(24).reshape(2,3,4)
c


# In[51]:


a, b = c[0], c[1]


# In[52]:


a


# In[53]:


b


# In[54]:


np.vstack((a,b)) #수직으로 합치기


# In[55]:


np.hstack((a,b)) #수평(옆)으로 합치기


# In[56]:


np.dstack((a,b)) #0열끼리 0면에, 1열끼리 1면, 2열끼리 2면


# **column_stack(튜플); 1차원 배열을 열단위로 배열하여 2차원 배열로 만듦**

# In[58]:


a=np.array([1,2,3,4])
b=np.array([5,6,7,8])
c=np.array([9,10,11,12])
get_ipython().run_line_magic('pinfo2', 'np.column_stack')


# In[59]:


np.column_stack((a,b,c))


# In[60]:


np.vstack((a,b))


# In[61]:


np.hstack((a,b,c))


# In[62]:


a


# In[63]:


a[:, np.newaxis]


# In[64]:


np.hstack((a[:, np.newaxis], b[:, np.newaxis], c[:, np.newaxis]))


# In[65]:


np.column_stack((a,b,c))


# **row_stack(튜플); vstack()과 동일. 행 단위로 쌓아줌**

# In[66]:


np.row_stack((a,b,c))


# In[67]:


np.vstack((a,b,c))


# **stack(튜플, axis=n); axis 속성에 따라 넘파이 배열을 합침** <br>
# 
# - axis=0(기본값); 첫번째 차원
# - axis=-1; 마지막 차원

# In[68]:


a = np.arange(12).reshape(3,4)
a


# In[69]:


b = np.arange(12,24).reshape(3,4)
b


# In[70]:


np.stack((a,b), axis=0) #a,b를 차원이 다르게 합침(다른 면으로)


# In[71]:


np.stack((a,b), axis=1) #같은 행끼리 합침


# In[72]:


np.stack((a,b), axis=2) #행들을 열로 바꿔서 합침


# In[73]:


np.stack((a,b), axis=-1) #마지막 차원(열)


# **r_[], c_[]**

# In[74]:


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([9,10,11,12])


# In[75]:


np.r_[a,b,c]


# In[76]:


np.r_[[a],[b],[c]]


# In[77]:


np.c_[a,b,c]


# ## 3.4 하나의 배열을 여러개 작은 배열로 분할하기
# - hsplit(array, indices_or_sections); 두번째 축(2차원의 경우 세로축)을 따라 분할
# - vsplit(array, indices_or_sections); 첫번째 축(2차원의 경우 가로축)을 따라 분할
# - dsplit(array, indices_or_sections); 3번째 차원으로 분할 <br>
# 　　　array: 분할할 배열 <br>
# 　　　indices_or_sections: 정수 -> 분할할 배열의 수<br>
# 　　　　　　　　　　　　　1차원 배열 형식->분할 될 인덱스를 의미

# In[78]:


a = np.arange(12).reshape(3,4)
a


# In[79]:


a_vsplit = np.vsplit(a,3) #가로 축을 따라서 3개의 배열로 분할
a_vsplit


# In[80]:


type(a_vsplit) #list


# In[81]:


a_vsplit[0]


# In[82]:


a_hsplit = np.hsplit(a,4) #세로축을 따라 4개의 배열로 분할
a_hsplit


# In[83]:


type(a_hsplit)


# In[84]:


a_hsplit[0].shape


# In[85]:


b = np.arange(24).reshape(2,3,4)
b


# In[86]:


b_split = np.hsplit(b,3) #두번째 축(행)을 이용해서 split -> 3차원 배열 b를 3개의 차원 배열로 split
b_split


# In[87]:


b_split[0].shape #3차원 배열(2면1행4열)


# In[88]:


b_vsplit = np.vsplit(b,2) #3차원 배열 b를 첫번째 축으 ㄹ기반으로 나눠 2개의 배열로 분할
b_vsplit


# In[90]:


b_vsplit[0].shape


# In[91]:


b_dsplit = np.dsplit(b,2) #3번째 차원을 기준으로 2개의 3차원 배열로 나눔
b_dsplit


# In[92]:


b_dsplit[0].shape


# **split(array, indices_or_sections, axis=n)**<br>
# 
# - axis=0 이면 vsplit()과 동일
# - axis=1 이면 hsplit()과 동일
# - axis=2 이면 dsplit()과 동일(3차원 이상에서만 사용 가능)<br>
# 
# **array_split(array, indices_or_sections, axis=n)**
# - split()함수와 동일하나, indices 부분에 축을 똑같이 나눌 수 없는 정수(나누어 떨어지지 않는 정수)도 사용 가능
# - 나누어 떨어지지 않을 경우 1//n+1 개의 배열 반환

# In[94]:


a = np.arange(20).reshape(2,10)
a


# In[95]:


np.split(a, [3,6], axis=1)


# In[96]:


np.split(a, (3,6), axis=1)


# In[97]:


np.hsplit(a, [1,6])


# In[98]:


np.vsplit(a,2)


# In[99]:


np.split(a,2,axis=0)


# In[100]:


#array_split
np.array_split(a,3,axis=1)


# In[101]:


np.array_split(a,2,axis=0)


# In[ ]:




