#!/usr/bin/env python
# coding: utf-8

# #### 21-02-22 python  02_자료형과 연산자               (c)cherryuki (ji)

# <b><font size="5" color="red">ch02. 자료형과 연산자</font><b>

# # 6절. 문자열 다루기

# - 문자열 슬라이싱
# - len()
# - upper(); 대문자로
# - lower(); 소문자로
# - title(); 각 단어의 앞글자만 대문자로
# - capitalize(); 첫문자만 대문자로
# - count('찾을 문자열'); '찾을 문자열'이 몇 개 들어있는지 개수 반환
# - find('찾을 문자열'); '찾을 문자열'이 왼쪽부터 시작하여 몇번째에 있는지 index 반환
# - rfind('찾을 문자열'); '찾을 문자열'이 오른쪽부터 시작하여 몇번째 있는지 index 반환
# - startswith('특정 문자열'); '특정 문자열'로 시작하는지 여부 반환
# - endswith('특정 문자열'); '특정 문자열'로 끝나는지 여부 반환
# 
# - srtip(); 좌우 공백 제거
# - rstrip(); 오른쪽 공백 제거
# - lstrip(); 왼쪽 공백 제거
# - split(); 문자열을 공백이나 다른 문자 기준으로 나누어 리스트로 반환
# 
# - isdigit(); 문자열이 숫자 문자열인지 여부 반환
# 
# - islower(); 문자열이 소문자인지 여부 반환
# - isupper(); 문자열이 대문자인지 여부 반환

# In[2]:


temp = 'Python is easy. Python is smart. python'
#       012345678901234567890123456789012345678 (39)
temp


# In[3]:


print('첫번째 글자는 {}, 마지막 글자는 {}'.format(temp[0], temp[-1]))
print('글자수:', len(temp))


# In[6]:


temp = 'python is easy. Python is smart. python'
#       012345678901234567890123456789012345678 (39)
print('대문자로:', temp.upper())
print('소문자로:', temp.lower())
print('title():', temp.title())
print('capitalize():', temp.capitalize())
print('python 등장 횟수:', temp.count('python'))
print('대소문자 구분없이 python 등장 횟수:', temp.title().count('Python'))
print('python의 첫위치:', temp.find('python'))
print('python의 마지막 위치:', temp.rfind('python'))
print('python으로 시작하는 문자열 인지:', temp.startswith('python'))
print('python으로 끝나는 문자열 인지:', temp.endswith('python'))


# In[7]:


temp = '     Python is easy.     '
print('strip(): [{}]'.format(temp.strip()))
print('rstrip(): [{}]'.format(temp.rstrip()))
print('lstrip(): [{}]'.format(temp.lstrip()))
print('spcae 단위로 텍스트 분리:', temp.split())
date='2021-02-22'
print('-단위로 텍스트 분리:', date.split('-'))


# In[8]:


# Python - Java - R - c => Python / Java / R / c
temp = 'Python - Java - R - c'
temp1=temp.split(' - ')
temp1


# In[10]:


temp2= ' / '.join(temp1)
print('원 텍스트: ', temp)
print('분리된 텍스트: ', temp1)
print('join된 텍스트: ', temp2)


# In[11]:


num = '100'
num.isdigit()


# In[12]:


temp = 'PYTHON'
temp.isupper()


# In[13]:


temp.islower()


# In[15]:


print('ABCD'.find('C'))
print('ABCD'.index('C'))


# In[16]:


str = ['A', 'B', 'C']
for s in str:
    print(s)


# In[17]:


str='ABC'
for s in str:
    print(s)


# In[18]:


dir(str) #문자열을 다룰 수 있는 변수, 함수들의 목록; __변수__, 함수


# # 7절. 날짜 및 시간 다루기

# ## 7.1 날짜

# In[19]:


from datetime import date #datetime패키지에서 date만 가져와서 사용
someday = date(2021, 2, 22)
someday


# In[21]:


print('{:%Y년 %m월 %d일 %H}'.format(someday))


# In[24]:


print(someday.year, someday.month, someday.day)


# In[25]:


today = date.today() #오늘
today


# In[26]:


print(today)


# ## 7.2 시간

# In[27]:


from datetime import time #datetime패키지에서 time가져옴
t = time(7) #7tl 저장
t


# In[28]:


print(t)


# In[31]:


t2= time(18, 20)
print(t2)


# ## 7.3 날짜 및 시간

# In[32]:


from datetime import datetime
now = datetime.now()
now #현재 날짜 및 시간


# In[33]:


print(now)


# In[34]:


thattime=datetime(2021,4,30,18,20,0)
print(thattime)


# In[36]:


year = now.strftime('%Y')
month = now.strftime('%m')
day = now.strftime('%d')
hour = now.strftime('%H')
minute = now.strftime('%M')
second = now.strftime('%S')
print('{}년 {}월 {}일 {}시 {}분 {}초'.format(year, month, day, hour, minute, second))
print('%s년 %s월 %s일 %s시 %s분 %s초'%(year, month, day, hour, minute, second))
type(year)


# ## 7.4 시간대

# In[37]:


from datetime import datetime #datetime패키지의 datetime()함수 사용
import pytz  #pytz패키지 사용
tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print('뉴욕 시간:', datetime_NY)
datetime_KR = datetime.now()
print('한국 시간:', datetime_KR)


# In[38]:


tz_KR=pytz.timezone('Asia/Seoul')
datetime_KR=datetime.now(tz_KR)
print('한국 시간:', datetime_KR)


# In[39]:


#셋팅 가능한 timezone list
pytz.all_timezones


# In[40]:


len(pytz.all_timezones)


# # 8절. 연습문제

# In[41]:


#3. 문자열의 분리하기와 합치기 기능을 이용하여 ‘Hello World’를 ‘World Hello’로 출력하세요
temp = 'Hello World'
temp_split=temp.split()
temp_split


# In[42]:


temp_split[::-1]


# In[43]:


' '.join(temp_split[::-1])


# In[44]:


text = "Seoul A001 - programming with python"
print(text[:4]+text[-1]+text.split()[0]) #Seou + n + Seoul

