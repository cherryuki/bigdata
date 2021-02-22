#!/usr/bin/env python
# coding: utf-8

# #### 21-02-22 python  02_자료형과 연산자               (c)cherryuki (ji)

# <b><font size="5" color="red">ch02. 자료형과 연산자</font><b>

# # 04절. 포맷팅
# - 포맷팅: 문자, 숫자, 날짜 데이터에 출력 형식을 지정하는 것
# - 변수와 텍스트를 결합해서 보기 좋은 형식의 새로운 텍스트를 만들 때 사용

# # 4.1 문자열에 형식 지정

# In[4]:


name = '공지철'
age = 43
print(name, '님의 나이는 ', age,'세 입니다', sep='')
#변수와 텍스트를 벌갈아 사용해서 형식을 지정하는 것은 가독성이 떨어지고 코드 작성하기 불편


# - 이전 스타일
# - %s: 문자열, %c: 문자, %d: 정수, %f: 실수, %x: 16진수, %o:8진수, %%:문자 %

# In[5]:


print('%s님의 나이는 %d세 입니다'%(name, age))
'%s님의 나이는 %d세 입니다'%(name, age)


# - 새로운 스타일
# - "{}".format()

# In[6]:


"{}님의 나이는 {}세 입니다".format(name, age)


# In[7]:


"{1}님의 나이는 {0}세 입니다".format(age, name)


# ## 4.2 format()함수 문법
# <font color="red">'{[인덱스]:[공백 대체 문자][정렬 방법][자릿수][타입]}'.format(변수명)</font>
# 
# - 인덱스: 출력할 인수의 인덱스(순서)
# - 정렬 방법: < 왼쪽 정렬, > 오른쪽 정렬, ^ 가운데 정렬
# - 자릿수: 출력할 자릿수 지정. 변수보다 적은 자릿수가 지정될 경우 무시되고 변수 출력
# - 타입: d 10진수, f 실수, s 문자, b 2진수, o 8진수, x 16진수

# In[9]:


name = input('이름은? ')
age=int(input('나이는? '))
print('{}님의 나이는 {}세입니다'.format(name, age))
print('{1}님의 나이는 {0}세입니다'.format(age, name)) #인덱스는 순서 지정


# In[10]:


print("{0}세 {1}님은 {0}살이 참 좋은 것을 안다".format(age, name))


# In[11]:


#{}만 쓸 경우 변수의 수보다 {}개수가 적으면 오류
a, b = 10, 20
print('출력: {}, {}'.format(a,b))


# <자릿수 지정>
# - 숫자의 경우 출력할 변수보다 큰 자릿수를 지정하면 오른쪽 정렬(기본값)
# - 문자의 경우 출력할 변수보다 큰 자릿수를 지정하면 왼쪽 정렬(기본값)
# - 변수보다 작은 자릿수를 지정하면 자릿수 지정이 무시되고 변수 출력

# In[12]:


a = 12345
b = 'Hello'
print("출력: [{}], [{:10}], [{:3}]".format(a,a,a))
print("출력: [{}], [{:10}], [{:3}]".format(b,b,b))


# In[13]:


a = 12345 #숫자의 경우 다양한 진수로 표현
print("""출력
10진수(정수): {:d}, 실수: {:f},
2진수: {:b}, 8진수: {:o}, 16진수: {:x}
""".format(a, a, a, a, a))


# - 정렬방법: <, >, ^
# - '{[인덱스]:[공백대체문자][정렬방법][자릿수][타입]}'.format(변수명)

# In[16]:


a, b, c = 10, 20, 3
print("출력: [{:<6d}], [{:>6}], [{:^6}]".format(a,b,c))


# In[17]:


#인덱스: 공백대체문자 정렬방법 자릿수 타입
a = 10
s = "Hello"
print("출력: [{0:$>10}], [{1:*<20}], [{1:_<10.3}]".format(a,s))
                                      #10.3: 전체 10자리 확보, 변수는 3자리만 출력


# In[21]:


#주의점: 공백 대체 문자를 지정할 때는 반드시 정렬 방법, 자릿수를 기재해야 한다
print("{0:$10} / {1:*20}".format(a,s))


# In[22]:


a, b = 123, -123
print('출력: [{:5}] [{:5}] [{:5}]'.format(b,a,a))


# - +를 붙이면 양수의 경우 숫자 앞에 부호 붙여줌
# - =를 붙이면 전체 자릿수만큼 출력하는 문자의 맨 앞에 부호 표시(양수는 부호 나타나지 않음)
# - =+를 사용하면 양수, 음수 모두 붙여줌(자릿수 맨 앞자리)
# - 자릿수 앞에 0을 넣으면 빈자리에 0을 채움
# - 공백대체문자는 = 앞에 기재
# - 공백 대체 문자와 자릿수 앞에 0 기재를 같이 하면 자릿수 앞에 0이 무시됨(공백 대체 문자가 우선순위 높음)

# In[24]:


a, b = 123, -123
print("출력: [{:+10}] [{:+10}] [{:+010}]".format(b, a, a))
print("출력: [{:=10}] [{:=10}] [{:=010}]".format(b, a, a))
print("출력: [{:=+10}] [{:=+10}] [{:=+010}]".format(b, a, a))
print("출력: [{:=+10}] [{:=+10}] [{:=+010}]".format(b, a, a))

print("출력: [{:*=+10}] [{:$=+10}] [{:_=+010}]".format(b, a, a))


# In[27]:


#전체 자릿수. 표현될 자릿수
a = 2.785
s = 'Hello'
print("  [0123456789]")
print("a=[{:>10.2}]".format(a))
print("s=[{:>10.2}]".format(s))


# In[28]:


#전체 자릿수. 소수점 자리수f (전체 자릿수에는 소수점 포함)
print("a=[{:4.1f}]".format(a)) #_ _ . _


# In[30]:


#format 함수의 매개 변수에 출력 포맷
a = 2.785
print("출력: [0123456789]")
print("출력: [{:>+10.3}]".format(a))
print("출력: [{:{}{}{}.{}}]".format(a,'>','+', 10, 3))


# In[31]:


#가독성읖 높이고자 포맷인자에 이름 부여
a=2.785
print("출력: [0123456789]")
print("출력: [{:>+10.3}]".format(a))
print("출력: [{:{div}{sign}{width}.{precision}}]".format(a, 
                div='>', sign='+', width=10, precision=3))


# In[32]:


a=15
print("10진수: [{:8d}]".format(a))
print(" 2진수: [{:08b}]".format(a))
print(" 8진수: [{:08o}]".format(a))
print("16진수: [{:02x}]".format(a))


# # 4.3 날짜 출력
# - %Y: 연도4자리(2021), %y: 연도2자리(21), %m: 월(02), %d: 일(22)
# - %H: 24시간, %I: 12시간, %p: AM, PM, %M: 분, %S: 초

# In[33]:


from time import localtime #time패키지에서 localtiom 함수 사용
now=localtime()
now #현재 날짜와 시간


# In[35]:


#날짜를 문자열로 출력하기 위해 strftime()함수 이용
from time import strftime
print(strftime('%Y-%m-%d %H:%M:%S', now))
print(strftime('%Y년 %m월 %d일 %p %I:%M:%S', now))


# In[36]:


#format함수 이용
from datetime import datetime
thatday=datetime(2021,4,30,18,20,0)
thatday


# In[37]:


print('{:%Y년 %m월 %d일 %H시 %M분 %S초}'.format(thatday))
print("{:%Y년 %m월 %d일 %p %I시 %M분 %S초}".format(thatday))


# In[39]:


name="한지민"
age=39
print(f"Hello, {name}. You are {age}years old.")
print("Hello, %s. You are %dyaers old."%(name, age))
print("Hello, {}. You are {}years old.".format(name, age))


# # 05절. 연산자

# ## 5.1 산술 연산자

# In[40]:


a = 10
print(a**3) #a의 3제곱
print(a//3) #a 나누기 3의 몫
print(a/3) #3.3333
print(9/3) #3.0 (파이썬에서 나눗셈 연산의 결과는 항상 실수)


# In[41]:


print(10.0%3.0) #실수끼리 나머지 연산


# In[42]:


print(3.8%1.2) #실수끼리 나머지 연산시 결과 다소 오차가 존재할 수 있음


# ## 5.2 대입 연산자
# - =, +-, -=, *=, **=, /=, //=, %= 등

# In[44]:


a = 10
a //= 2 #a=a//2
a


# ## 5.3 논리 연산자
# - &, |, not, and, or

# In[46]:


print((10>3)&(10>5)) #논리 연산자: True&True=Ture
print((12&1))        #비트 연산: 1100&0001 (2진수로 변환하여 연산)
print(5<8<10<100)    #논리연산자 3항 이상에서도 사용 가능


# In[47]:


print(10>3 & 10>5) #비트 연산자가 논리, 비교 연산보다 우선 순위 높음
#       0011 & 1010 = 0010 (2)
#print(10>2>5)이므로 False


# In[48]:


#''(빈 스트링):False, 그 외:True
if'':
    print('빈 스트링은 True')
else:
    print('빈 스트링은 False')


# In[49]:


#논리 연산자에 문자열이 오면 에러
True | ''


# In[50]:


True | bool('')


# In[53]:


#주피터 노트북에서는 !명령행을 실행시킬 수 있음
get_ipython().system('dir')


# In[52]:


#논리의 반전은 !이 아닌 not(cf. 다르다: !=)
not True


# In[54]:


not 0 #0은 False, 그 외 숫자는 True


# In[55]:


not -999


# In[57]:


a = False
if not a:
    print(a)


# In[58]:


a, b = 15, 16
if a!=b:
    print("두 수는 다르다")
else :
    print("두 수는 같다")


# - and 연산자: 거짓으로 판별되는 첫번째 항의 결과가 반환
# -           모든 항이 참이면 마지막 항의 결과 반환

# In[59]:


print(True and 3 and 0)
print(True and 0 and 3)
print(True and 0 and 3 and False)
print(True and 3 and True)
print(3 and 2)


# In[60]:


print(3 and 5.4 and True and 'Hello' and 'Python')
print(3 and 5.4 and True and 0 and 'Python')
print(3 and 5.4 and True and -0 and 'Python')


# - or 연산자: 참으로 판별되는 첫번째 항의 결과가 반환
# - 모든 항이 거짓이면 마지막 항의 결과 반환

# In[61]:


print('' or False or None or 0)
print('' or 100 or None or False)


# # 5.4 비교 연산자
# <span> >, >=, <, <=, ==, != </span>
# - 문자는 ASCII코드 순으로 비교: 특수문자 < '숫자' < 대문자 < 소문자 <한글

# In[62]:


'아'>'하'


# In[64]:


'1' < 'a'


# In[65]:


True > False #Ture:1, False:0으로 매핑(간주)


# In[66]:


int(True), int(False)


# In[67]:


bool(0), bool(-9)


# In[68]:


score = int(input('점수를 입력하세요 ')) #입력한 수는 문자로 반환
if score > 60:
    print('합격') #문자로 비교할 경우 두 수의 자릿수가 다를경우 제대로 비교X
else:
    print('불합격')


# ## 5.5 비트 연산자
# - &: 비트가 모두 1이면 1
# - |: 하나 이상 1이면 1
# - ^(XOR): 같으면 0, 다르면 1

# In[70]:


a = '''
x  y  x&y  x|y  x^y(XOR)
0  0   0    0    0
0  1   0    1    1
1  0   0    1    1
1  1   1    1    0
'''


# In[71]:


a = 15 # 0 0 0 0 1 1 1 1
b = 2  # 0 0 0 0 0 0 1 0
print("{:08b}".format(a))
print("{:08b}".format(b))
print('a&b:', a&b) # 0 0 0 0 0 0 1 0 (2)
print('a|b:', a|b) # 0 0 0 0 1 1 1 1 (15)
print('a^b:', a^b) # 0 0 0 0 1 1 0 1 (13)


# In[72]:


#shift
# A >> B ; A를 Bbit 오른쪽으로 이동(A를 2의B승으로 나눈 몫과 동일)
# A << B ; A를 Bbit 왼쪽으로 이동(A를 2의B승 곱한 것과 동일)
a = 15 # 1 1 1 1 
print(a >> 2) #a를 오른쪽으로 2bit 이동 # 1 1 (3)
print(a << 2) #a를 왼쪽으로 2bit 이동 # 1 1 1 1 0 0 (60)


# In[73]:


#not: 논리 연산자의 반전 ~비트 연산의 반전
print(~a) # 0 1 1 1 1 => - 1 0 0 0 0 (음수는 2의 보수 취함)


# ## 5.6 isinstance
# - isinstance(data, type); 스칼라 데이터나 객체의 유형 확인

# In[74]:


isinstance(3.5, float)


# In[ ]:





# # 8절. 연습문제

# 1. 이름과 나이 변수를 다음 형식으로 출력하도록 format() 함수를 이용해 형식화하세요 [출력형식 : 홍길동님의 나이는 23살입니다]

# In[76]:


name = '홍길동'
age = 23
print("[출력형식: {}님의 나이는 {}살입니다]".format(name, age))


# 2. 두 정수를 입력받아 두 수의 덧셈, 뺄셈, 곱셈, 나눗셈, 몫, 나머지를 출력하세요

# In[77]:


num1 = int(input('첫번째 수: '))
num2 = int(input('두번째 수: '))
print(num1+num2)
print(num1-num2)
print(num1*num2)
try:
    print(num1/num2)
    print(num1//num2)
    print(num1%num2)
except Exception:
    print('두번째 수에 0을 입력하여 나누기 연산이 불가합니다')


# 3. 문자열의 분리하기와 합치기 기능을 이용하여 ‘Hello World’를 ‘World Hello’로 출력하세요

# In[79]:


str='Hello World'
print(str[6:], str[:5])
print(str[-5:], str[:5])


# 4. x = 'abcdef＇를 이용하여 ‘bcdefa’로 출력하세요(문자 슬라이싱이용).

# In[81]:


x = 'abcdef'
print(x[1:], x[:1], sep='')


# 5. x = ‘abcdef’를 이용하여 ‘fedcba’로 출력하세요

# In[83]:


x='abcdef'
print(x[::-1])


# 6. 오늘의 온도를 섭씨온도로 입력받아 화씨 온도로 변환하는 프로그램을 작성하세요. 화씨 온도는 소수점 두번째 자리까지 출력되어야 합니다(다음은 섭씨와 화씨의 변환 공식입니다. C는 섭씨, F는 화씨)
# - C = (F-32) / 1.8
# - F = (C*1.8) + 32

# In[86]:


C = float(input('오늘의 섭씨 온도는? '))
print('[오늘의 화씨온도: {}]'.format((C*1.8)+32))
F = (C*1.8)+32
if C == round(C):
    print("오늘의 섭씨 온도: {:.0f}, 오늘의 화씨 온도: {:.2f}".format(C,F))
else :
    print("오늘의 섭씨 온도: {}, 오늘의 화씨 온도:{:.2.f}".format(C,F))

