#!/usr/bin/env python
# coding: utf-8

# #### 21-02-19 python  02_자료형과 연산자               (c)cherryuki (ji)

# <b><font color="red">ch02. 자료형과 연산자</font><b>

# # 01절. 변수

# ## 1.1 변수 선언

# - 값을 저장할 수 있는 변수를 만드는 것
# - 파이썬은 변수 선언을 위한 타입이나 별도의 변수 선언 과정이 없음(모두 객체 변수)

# ## 1.2 변수 할당

# - 어떤 값에 이름을 부여하는 과정(다른 변수나 자료와 구분 용이)
# - 할당 연산자(=)를 이용

# In[3]:


r = 5
area = 3.14*5*5
print(area)


# In[4]:


import numpy as np
r=5
area = np.pi*r*r
print('반지름이 5인 원의 넓이: ', area)


# ## 1.3 id(); 객체 주소값 출력, type(); 객체 타입

# In[ ]:





# In[11]:


a=10


# In[12]:


print(id(a)) #a변수의 주소
print(type(a)) #a의 타입


# In[13]:


a = 5


# In[14]:


print(id(a)) #a변수의 주소
print(type(a))


# In[15]:


a = 'Python'


# In[16]:


print(id(a)) #a변수의 주소
print(type(a))


# ## 1.4 변수 이름 규칙

# - 문자(대소문자 구분), 숫자, 밑줄(_)을 포함(변수명은 숫자로 시작할 수 없음)
# - 공백, 문장부호, 특수문자, 예약어(class, def 등) 등은 사용 불가 (특수문자는 _만 가능)

# In[17]:


불용어 = "북한"


# In[18]:


불용어


# In[39]:


print('Hello', ', World'+str(2))


# ## 1.5 변수 삭제

# - 변수삭제: del 변수명, 변수명
# - whos; 현재 커널에 정의되어 있는 변수 목록 확인

# In[40]:


del 불용어


# In[42]:


del a, r  #여러개 동시 삭제


# In[44]:


whos #현재 정의되어 있는 변수 목록 확인


# In[ ]:





# In[ ]:





# In[ ]:





# In[20]:


i = 5j+4 #복소수


# In[21]:


type(i) #변수의 타입 반환


# In[22]:


#자동완성(Tab키)
isinstance(i, complex) #변수의 타입이 complex인지 확인


# In[23]:


i= "i"
type(i)


# ## 1.6 다중 변수선언

# - 한 라인에 여러개 변수 선언해 사용

# In[24]:


a, b = 10, 20 


# In[25]:


print('a=',a,'\t b=',b)


# In[26]:


a, b = b, a+b


# In[27]:


print('a=',a,'\t b=',b)


# In[45]:


a, b = 10, 20
a = b
b = a+b


# In[46]:


print('a=',a,'\t b=',b)


# In[28]:


print


# ## 1.7 도움말

# - help(함수명)
# - 함수명 + shift_Tab

# In[29]:


help() #도움말 제공, 종료하려면 q 입력


# In[30]:


#도움말 기능: shift+Tab (+누르면 더 많은 내용)
print()


# # 02절. 화면 입출력

# In[31]:


first = input('첫번째 숫자')
second = input('두번째 숫자')


# In[32]:


print('두 수의 합은', (first+second))


# In[33]:


print('두 수의 합은', (int(first)+int(second)))


# In[34]:


first = int(input('첫번째 수'))
second = int(input('두번째 수'))


# In[35]:


type(first)


# In[36]:


print('두 수의 합은', (first+second))


# In[38]:


print('Hello', 'World', sep='/', end='\n\n')
print('Hello', 'Python', sep='★')


# # 03절. 기본 자료형 - 숫자형(정수, 실수, 복소수), 문자, 논리형

# ## 3.1 숫자형

# - 정수(int), 실수(float), 복소수(complex) 형
# - 소수점이 없는 정수는 int형, 소수점이 있는 숫자는 float형
# - 허수부를 포함하는 복소수는 complex형(j로 표현)

# In[48]:


import sys
print(sys.maxsize) #정수 최대값


# In[49]:


i = 9223372036854775
type(i)


# In[50]:


f = 3.5
type(f)


# In[51]:


f = 3/2
print(f)
print(type(f))


# In[53]:


f = 2/2
print(f) #1.0
print(type(f)) #나눗셈 연산 결과는 실수(float)


# In[55]:


a = 3+2j #복소수
b = 1j    #복소수


# In[56]:


print(a)
print(type(a))


# In[57]:


a+b


# In[62]:


_ #_변수: 마지막으로 인쇄 된 표현식(a+b)이 변수 _에 저장됨


# In[64]:


c= 5
print(c+_) #c+_=c+a+b


# In[59]:


print(b**2) #b의 제곱


# In[60]:


f = 1.13e-8 #지수형 사용 가능
print(f) # 1.13e-08
g = 1.13e8
print(g) #113000000.0b


# ## 3.2 문자형

# - 단일 문자와 문자열 구분하지 않음
# - "", '' 사용
# - 여러줄 문자열은 '''문자열 입력''', """문자열 입력""" 사용 (줄바꿈 포함)

# In[65]:


name= '공지철'
address = "서울시 '종로'구"
print(name, address)


# In[66]:


text = '''이렇게 작성하면
줄바꿈도 그래도 적용해서 여러줄의 문자를
입력할 수 있습니다'''
print(text)
text ="""이렇게 작성해도
같은 결과"""
print(text)


# In[67]:


greeting = """Hello
World"""
print(greeting)


# In[70]:


greeting = "Hello\nWorld"
print(greeting)


# In[71]:


print('Hello\nWorld')


# In[72]:


print(r'Hello\nWorld') #r: raw (역슬래시 문자 해석하지 않고 남겨둠)


# In[73]:


print('Hello'+", World")


# In[75]:


print("Hello"*3) #문자열*숫자; 숫자만큼 문자열 반복


# In[76]:


str = "0123456789"


# In[ ]:


#문자열 슬라이싱
#문자열[start:stop] start위치 문자 포함, stop위치 문자 포함X (숫자 생략 가능)
#문자열[start:stop:step] start위치 문자 포함, stop위치 문자 포함X, 매 step번째 아이템 추출


# In[77]:


str[0:3] #0번째부터 3번째 앞까지


# In[78]:


str[-3] #음수 인덱스는 뒤에서 부터: 뒤에서부터 3번째


# In[79]:


str[5:] #5번째부터 끝까지


# In[80]:


str[:5] #처음부터 5번째 앞까지


# In[81]:


str[:] #처음부터 끝까지


# In[82]:


str[5:100] #5번째부터 끝까지


# In[83]:


print(str[0:9:2]) #0번째부터 2씩 증가해서 9번째 앞까지 (0,2,4,6,8)
print(str[::2]) #동일한 결과


# In[84]:


#끝부터 처음까지(거꾸로) 출력
print(str[9:0:-1]) #9번째부터 0번째 전까지 -1씩 감소 (0출력X)
print(str[9::-1]) #9번째부터 처음까지 -1씩 감소
print(str[::-1]) #끝부터 처음까지 -1씩 감소


# In[85]:


import re #정규표현식 관련 패키지
data="이름:공지철, 주소:서울, 전화:02-000-0000, 별명:공룡"
print(data)


# In[87]:


phone_pattern = r'[0-9]{2,3}-[\d]{3,4}-[\d]{4}'
phone = re.findall(phone_pattern, data)
print('data에서 추출된 전화번호:', phone)


# ## 3.3 논리형(True, False)

# - 논리형(Bool)은 True, False (첫번째 문자만 대문자)
# - False로 판단되는 값: None, False, 0, "", '', (), {}, []
# - 널문자(\0)와 공백문자(' ')는 True

# In[88]:


a = True
print(a)
print(type(a))
print(isinstance(a, bool))


# In[89]:


if "":
    print(True)
else:
    print(False)


# In[90]:


a = 10
b= 10
if a-b :
    print(True)
else :
    print(False)


# In[91]:


if 0+0j :
    print(True)
else:
    print(False)


# In[93]:


if ' ':
    print(True)
else :
    print(False)


# In[94]:


if '\0':
    print(True)
else:
    print(False)

