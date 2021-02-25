#!/usr/bin/env python
# coding: utf-8

# **21-02-24 python 05_함수   (c)cherryuki (ji)**

#  **<font size=5 color="red">ch05. 함수</font>**

# # 1절. 함수의 정의 및 사용
# - 반복해서 사용할 코드를 묶어 놓고 그것에 이름을 붙인 것
# - 반복해서 사용할 코드는 함수를 이용하면 보다 구조적이고 간결한 코드 작성 가능
# - 함수의 정의 <br>
#   def 함수명([param1, param2, ...]): <br>
#      expressions

# # 1.1 함수 정의하기

# In[2]:


def my_hello():
    print('Hello, World')
    print('Hello, Python')


# In[3]:


my_hello


# In[4]:


my_hello()


# In[5]:


print(__name__) #예약어, 시스템 변수 등과 구분하기 위해 under bar(_)는 함수명 중간에 들어가는 걸 추천


# In[6]:


if __name__=='__main__':
    my_hello()


# In[7]:


def my_add(num1, num2, num3=0): #기본값을 갖는 매개변수는 맨 뒤에 기재
    return num1+num2+num3
print(my_add(20,30,40))
print(my_add(20,30))
print(my_add(20))


# ## 1.2 Docstring

# In[8]:


def my_function():
    """
    함수의 첫 라인에 독스트링(docstring)을 포함시킬 수 있음
    독스트링은 함수의 설명서(도움말)를 달아주는 역할. 주석보다 더 많은 기능
    함수명(Shift+Tab) 키 입력시 해당 함수의 독스트링 확인 가능
    """
    pass


# In[9]:


print(my_function.__doc__) #my_function( Shift+Tab 키 입력시 독스트링 확인 가능)


# ## 1.3 함수 정의하고 호출하기

# In[11]:


def fibonacci(n):
    "매개 변수로 들어온 n값 미만까지 피보나치 수열을 출력"
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

if __name__=='__main__':
    fibonacci(10)


# In[12]:


fibonacci(10)


# ## 1.4 지역변수와 전역변수

# In[13]:


global_var = 100 #전역변수(함수 밖에서 선언한 변수) - 어디서든 사용 가능
def fun1():
    print(global_var) #전역변수는 함수 안에서도 사용 가능
fun1()


# In[14]:


global_var #함수 밖에서도 사용 가능


# In[15]:


def fun2():
    local_var = 200 #지역변수(함수 안에서 선언한 변수) - 함수 안에서만 사용 가능
    print(local_var)
fun2()


# In[16]:


local_var #지역변수는 해당 함수 밖에서 사용시 에러 발생


# ## 1.5 Lexical 특성

# In[17]:


g_var = 100
def fun3():
    print("before:", g_var) #지역변수 선언 전에 사용해서 에러 발생
    g_var=200 #지역변수를 선언하면서 할당
    print('after:', g_var)
fun3()


# In[18]:


g_var = 100
def fun3():
    global g_var #global 예약어를 사용하면 전역변수를 참조함
    print('before:', g_var)  
    g_var=200 
    print('after:', g_var)
print('fun3() 실행 전:', g_var)
fun3()
print('fun3() 실행 후:', g_var)


# In[19]:


global_var = 100 #전역변수
def fun1():
    global_var = 200 #지역변수 선언(전역변수에 영향X)
    print(global_var)
print('fun1() 실행 전 global_var:', global_var)
fun1()
print('fun1() 실행 후 global_var:', global_var)


# In[20]:


global_var = 100 # 전역변수
def fun1():
    global global_var #전역변수 참조
    global_var = 200 #함수 호출 시 전역변수 값도 변경됨
    print(global_var)
print('fun1() 실행 전 global_var:', global_var)
fun1()
print('fun1() 실행 후 global_var:', global_var)


# ## 1.6 값에 의한 호출
# - 함수에 인수로 전달되는 변수가 스칼라 변수(숫자, 문자, 논리)일 경우: 값이 전달 됨

# In[21]:


foo = 'a' #전역변수
id(foo)


# In[22]:


def fun1(foo): #매개변수는 지역변수
    print('Before:', foo, '의 주소:', id(foo))
    foo=foo*3
    print('After:', foo, '의 주소:', id(foo))
fun1(foo)


# In[23]:


print(foo, id(foo)) #전역 변수


# ## 1.7 참조에 의한 호출
# - 함수에 인수로 전달되는 변수가 리스트, 딕셔너리, 셋, ... 일 경우

# In[24]:


L=[1,2,3,4,5]
id(L)


# In[25]:


def fun2(foo): #foo는 지역변수
    print('Before:', foo, '의 주소:', id(foo))
    foo.append(6)
    print('After:', foo, '의 주소:', id(foo))
fun2(L)
print('함수 호출 후 L:', L, '의 주소:', id(L))


# ## 1.8 함수 이름 변경
# - Python; 함수형 언어, 객체 지향 언어

# In[26]:


def fibonacci(n):
    """
    매개변수로 들어온 n값 미만까지 피보나치 수열을 출력합니다
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


# In[27]:


fibonacci


# In[28]:


type(fibonacci)


# In[29]:


fibo = fibonacci #fibonacci 함수를 fibo로도 사용 가능


# In[30]:


fibo(100)


# # 2절. 함수의 실행결과를 반환하는 return

# In[35]:


def fibonacci_print(n):
    """
    매개변수로 들어온 n값 미만까지 피보나치 수열을 출력합니다
    """
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fibonacci(n):
    "n값 미만의 피보나치 수열을 return"
    result = []
    a,b = 0,1
    while a<n:
        result.append(a)
        a, b = b, a+b
    return result


# In[36]:


x=fibonacci_print(100)


# In[37]:


print(x, type(x)) #return값 없으므로 저장된 값 없음


# In[38]:


L=fibonacci(100)


# In[39]:


print(L, type(L))


# ## 2.1 여러개 값 반환; 하나의 튜플로 반환
# - 여러개 값을 반환하면 값들이 튜플에 저장되어 반환
# - 반환 값을 하나의 튜플 변수에 저장하거나 함수가 반환하는 값의 개수 만큼 변수를 선언하여 반환 값 저장할 수 있음

# In[40]:


def swap(a, b):
    return b, a


# In[41]:


x, y = 5, 10
print('함수 실행 전:', x, y)
x, y = swap(x, y)
print('함수 실행 후:', x, y)


# In[42]:


a = swap(x, y)
print(type(a))
print(a)


# # <font color="red">3절. 함수의 매개 변수</font>

# ## 3.1 기본 값을 갖는 매개변수

# In[45]:


def make_url(ip, port=80):
    return 'http://{}:{}'.format(ip, port)
make_url("localhost") #기본 값을 갖는 매개변수는 선택적으로 사용 가능


# In[46]:


make_url("localhost", 70)


# ## 3.2 기본 변수를 갖는 매개 변수
# - 기본 변수가 스칼라 변수일 경우: 기본 값은 함수가 정의 되는 시점에 평가됨(기본 값 변경X)
# - 기본 변수가 리스트, 셋, 딕셔너리 또는 변경 가능한 객체일 때: 호출시마다 다시 전달(기본 값 변경O)

# In[48]:


i = 5
def fun2(arg=i): #스칼라 변수일 경우 arg의 기본값은 함수가 정의되는 시점에 한 번만 평가됨
    print('arg=', arg)
i=7
fun2()


# In[49]:


fun2(i)


# In[50]:


fun2()


# In[51]:


# 기본 변수가 리스트, 셋, 딕셔너리 또는 객체 일때 함수를 호출 후 다시 전달(계속해서 공유)
list_ = []
def fun3(a, L=list_):
    L.append(a)
    return L
print(fun3(2))
print(list_)


# In[52]:


print(fun3(3))
print(list_)


# In[53]:


def fun3(a, L=[]):
    L.append(a)
    return L
print(fun3(1))


# In[54]:


print(fun3(2))


# ## 3.3 순서 인수와 키워드 인수
# - 순서 인수와 키워드 인수(기본 값을 갖는 인수)가 같이 올 때는 키워드 인수를 반드시 뒤에 기재
# <pre>  def function명(변수명1, 변수명2, ... 변수명n=기본값):
#                          순서인수          키워드 인수
# </pre>

# In[56]:


def fun4(a, L=None): #a는 순서 인수. 변수명 적지 않으면 a부터 들어감
    if L is None:
        L=[]
    L.append(a)
    return L
fun4(10)


# In[57]:


fun4(30)


# In[58]:


list_=[] #매개 변수 공유하고 싶을 경우
fun4(10, list_)


# In[59]:


fun4(20, list_)


# In[61]:


fun4(L=list_, a=10)


# In[62]:


fun4([], a=30) #a에 []를  먼저 전달 (a가 두개있어서 에러)


# In[63]:


fun4([])


# In[64]:


fun4(L=list_, 30)
#변수명 적을 경우 전부 다 기재해야 함; L=list_, a=30  
#변수명 하나라도 적지 않을 경우 순서인수, 키워드 인수 순으로 들어감


# ## 3.4 튜플 매개변수를 이용한 가변인수 설정
# - 매개변수 앞에 를 붙여 정의; 매개변수
# - *매개변수: 인수들이 튜플에 저장되어 전달
# - 매개변수 순서: 순서 인수, 튜플 인수, 키워드 인수 순으로 작성

# In[65]:


def add(a,b):
    return a+b
print(add(1,2))


# In[66]:


def add(a,b,c):
    return a+b+c
print(add(1,2,3))


# In[67]:


print(add(10,20))
#파이썬은 함수의 중복(overloading) 지원X


# In[68]:


# *매개변수: 매개변수가 튜플로 전달
def add(*args): #args = ()
    sum = 0
    for num in args:
        sum += num
    return sum
print(add(1))
print(add(1,2,3,4,5))
print(add(1,2,3))


# - 인수 순서: 순서 인수 > 튜플 인수 > 키워드 인수 순

# In[69]:


def concat(*args, sep):
    return sep.join(args)


# In[70]:


concat('Hello', 'World', '/')


# In[71]:


#해결책1: 파라미터 이름(sep) 지정 (파라미터 이름 지정안할 경우 args 매개변수 안으로 들어감)
concat('Hello', 'World', sep='/')


# In[73]:


#해결책2: 순서 인수, 튜플인수, (키워드 인수) 순으로 작성
def concat(sep, *args):
    return sep.join(args)
concat('/', 'Hello', 'World')


# In[76]:


#해결책3: (순서 인수), 튜플인수, 키워드 인수(기본값 설정) 순으로 작성
def concat(*args, sep='/'):
    return sep.join(args)
concat('Python', 'R', 'Hadoop')


# In[75]:


concat('earth', 'mars', 'venus', sep='-')


# ## 3.5 딕셔너리 매개변수
# - **매개변수: 인수들을 딕셔너리에 저장해서 전달
# - 순서인수, 튜플인수, 키워드인수, 딕셔너리 인수 순으로 같이 사용될 수 있음

# In[77]:


def fun5(**args): #**args: 딕셔너리로 전달되는 매개변수
    for key, value in args.items():
        print("{}:{}".format(key, value))
fun5(name='Kong', age=43, address='Seoul')


# In[78]:


# 순서인수 > 튜플인수 > 키워드 인수 > 딕셔너리 인수 순
def fun6(a, *b, **c):
    print('a=',a)
    print('b=',b)
    print('c=',c)
fun6(10, 1, 2, 3, 4, 5, name='kim', age=30)


# In[79]:


fun6(10, 1,2,3)


# ## 3.6 함수 정의시 매개변수의 순서
# - 순서 인수 > 튜플 인수 > 키워드 인수 > 딕셔너리 인수

# In[80]:


def func(a,b,c,*d,e=10,**f):
    print('a=',a)
    print('b=',b)
    print('c=',c)
    print('d=',d)
    print('e=',e)
    print('f=',f)


# In[81]:


func(10, 20, 30, 1,2,3,4,2,4, e=20, name='Kim', age=30, address='Seoul')


# ## 3.7 인수의 언패킹
# - 함수(*튜플 변수); 튜플 인수 언패킹
# - 함수(**딕셔너리 변수); 딕셔너리 인수 언패킹

# In[82]:


def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
add(1,2,3,4)


# In[83]:


numbers=(1,2,3,4)
#add(numbers); 에러 발생
add(*numbers) #튜플 인수 언패킹


# In[84]:


# 예제: 튜플인수를 매개변수로 갖는 range2 함수 생성
def range2(*args):
    L = []
    if len(args)==0:
        raise Exception('매개변수를 입력하세요')
    elif len(args)==1:
        for i in range(args[0]):
            L.append(i)
    elif len(args)==2:
        for i in range(args[0], args[1]):
            L.append(i)
    elif len(args)==3:
        for i in range(args[0], args[1], args[2]):
            L.append(i)
    else:
        print('매개변수는 최대 3개까지 입력 가능합니다')
        return
    return L
        
print(range2(10))
print(range2(5, 10))
print(range2(5, 10, 2))
print(range2(5,10,2,2))


# In[85]:


t = (5, 10, 2)
range2(*t) #튜플 인수 언패킹


# In[91]:


def fun5(**data):
    for item in data.items():
        print(item)
fun5(name='Kong', age=30, address='Seoul')


# In[89]:


customerInfo = {'name':'Kong', 'age':30, 'address':'Seoul'}
fun5(**customerInfo) #딕셔너리 인수 언패킹


# # 4. 람다(lambda)식
# - 람다식; 작은 익명 함수
# - 실행할 문장이 한 문장일 경우만 작성 가능
# - return 구문이 없어도 statement 결과를 반환함
# - 람다식은 lambda 키워드를 이용해 생성 가능
# <br>
# - list comprehension 같이 참조해서 사용多
# - filter(), map()함수와 같이 참조해서 사용多

# ## 4.1 람다식; 한 줄 짜리 작은 익명 함수

# In[93]:


def add(a,b):
    return a+b
add(5,7)


# In[94]:


add2 = lambda a,b:a+b


# In[95]:


add2(10, 20)


# In[96]:


(lambda a,b:a+b) (30, 40)


# ## 4.2 함수의 인수에 람다식 사용
# - 람다식은 함수 실행할 문장이 한 문장일 경우만 사용
# - 람다식을 가장 많이 사용하는 경우: 함수의 인수로 전달하거나 return할 때

# In[97]:


def map_template(fun, L=[]):
    result=[]
    for item in L:
        result.append(fun(item))
    return result


# In[99]:


list_data=[1,2,3,4,5]
def x_2(x):
    return x*2
map_template(x_2, list_data)


# In[100]:


#람다식 이용
print(list_data)
map_template(lambda x:x*2, list_data)


# In[101]:


#map()함수 이용
list(map(lambda x:x*2, list_data))


# In[102]:


#list comprehension
[ x*2 for x in list_data ]


# In[106]:


list_data=[1,2,3,4,5]
def filter_template(fun, L=[]):
    result=[]
    for item in L:
        if(fun(item)):
            result.append(item)
    return result


# In[107]:


def evenornot(x):
    if x%2==0:
        return True
filter_template(evenornot, list_data)


# In[108]:


filter_template(lambda x:x%2==0, list_data)


# In[109]:


#list comprehension
[x for x in list_data if x%2==0]


# In[124]:


pairs = [(1, 'one'), (3, 'three'), (2, 'two'), (4, 'four')]
pairs.sort() #첫번째 요소 오름차순 정렬
pairs


# In[125]:


pairs.sort(key=lambda pair:pair[1])
pairs


# In[126]:


(lambda pair:pair[1])([10,20,30])


# In[127]:


def apply(data, fun=None):
    if fun==None:
        return data
    else:
        return fun(data)
apply(10, lambda x:x**3)


# ## 4.3 리턴문에 람다식 이용

# In[128]:


#함수를 return하는 함수
'''
make_box((5,)) => 1차원 5열 list를 만드는 함수 fun => fun(10) => [10, 10, 10, 10, 10]
make_box((2,3)) => 2차원 2행 3열 list를 만드는 함수 fun => fun(10) => [[10, 10, 10], [10, 10, 10]]
'''
def make_box(shape):
    def box(init_value):
        if len(shape)==1:
            return [init_value]*shape[0]
        elif len(shape)==2:
            return [[init_value]*shape[1]]*shape[0]
    return box


# In[129]:


box1=make_box([5,])
type(box1)


# In[130]:


box1(10)


# In[131]:


box2=make_box([2,3])
box2(10)


# In[132]:


def make_box1(shape):
    if len(shape)==1:
        return lambda x:[x]*shape[0]
    elif len(shape)==2:
        return lambda x: [[x]*shape[1]]*shape[0]


# In[134]:


box1=make_box1((3,2))
box1(5)


# In[135]:


box2 = make_box1((3,))
box2(5)


# # 5절. 파이썬 내장 함수
# - import하지 않고 바로 사용 가능한 함수
# - 키워드로 간주되므로 식별자로 사용하는 것 피하기

# In[136]:


int("1")


# In[137]:


int(float("1.2"))


# In[1]:


var = 10
globals() #전역변수들 딕셔너리


# In[2]:


def abc(n): #매개변수로 들어온 수 5 [0,1,2,3,4]
    L=[]
    for i in range(n):
        L.append(i)
    print(locals()) #지역변수들 출력
    return L
abc(5)


# In[3]:


isinstance(3.5, float)


# In[4]:


class Test:
    def __init__(self, a,b):
        self.a=a
        self.b=b
    def print_info(self):
        print(self.a, self.b)


# In[5]:


t = Test(10, 8) #t.a=10, t.b=8
t.print_info()


# In[6]:


isinstance(t, Test)


# In[7]:


list(enumerate([10, 20, 30]))


# In[8]:


all([0,1,2,3]) #all(); 전부 True인지 확인하는 함수


# In[9]:


any([0,1,2,3]) #any();하나라도 True가 있는지 확인하는 함수


# In[10]:


round(3.69), round(3.69,1) #numpy패키지 안에도 round 有


# In[12]:


import numpy as np
np.floor(3.67), np.ceil(3.67), np.round(3.67)


# # 6절. 연습문제

# ## 6.1 실습형 연습문제

# In[14]:


#1. 함수의 인자로 리스트를 받은 후 리스트 내에 있는 모든 정수 값에 대한 최대값과 최소값을 리턴하는 함수를 작성
def get_max_min(data_list):
    if len(data_list)>0:
        return "최대값:{}, 최소값:{}".format(max(data_list), min(data_list))


# In[15]:


L=[1,2,3,4,5]
get_max_min(L)


# In[18]:


get_max_min_ = lambda data_list: (max(data_list), min(data_list))
get_max_min_([0,5,2])


# In[21]:


#2. 체질량지수(Body Mass Index, BMI)는 체중과 키를 이용해 인간의 비만도를 나타내는 지수이다.
## 함수의 인자로 체중과 신장을 입력받은 후 BMI값에 따라 '마른체형', '표준', '비만', '고도비만' 중 하나의 상태를 출력하는 함수 작성
def BMI(weight=0, height=1):
    weight = float(input('체중을 입력하세요>'))
    height = float(input('키를 입력하세요>'))
    bmi = weight / ((height/100)**2)
    if bmi < 18.5 :
        result='마른 체형'
    elif 18.5 <= bmi < 25:
        result='표준'
    elif 25 < bmi < 30:
        result='비만'
    elif bmi >= 30 :
        result='고도 비만'
    return result


# In[22]:


BMI()


# In[23]:


#3. 직각삼각형의 밑변과 높이를 입력 받은 후 삼각형의 면적과 둘레를 계산하는 함수 작성
## 리턴 값은 면적과 둘레를 동시에 리턴
# 직각삼각형의 빗변 길이 계산시 사용할 함수(제곱근 구하는 함수)
import math
#math.sqrt(); 제곱근을 구하는 함수
def get_triangle(width, height):
    area = width*height/2
    perimeter = width+height+math.sqrt(width**2 + height**2)
    print('밑변:{}, 높이:{}인 삼각형의 넓이:{}, 둘레:{}'.format(width, height, area, perimeter))
    return area, perimeter
get_triangle(3,4)


# In[24]:


#4. 함수의 인자로 시작과 끝 숫자가 주어질 때 시작부터 끝까지의 모든 정수 값의 합을 리턴하는 함수 작성
def mysum(from_, end_):
    sum=0
    for i in range(from_, end_+1):
        sum+=i
    return sum
mysum(3,5)


# In[25]:


#5. 함수의 인자로 문자열을 포함하는 리스트가 입력될 때 각 문자열의 첫 세글자로만 구성된 리스트를 리턴하는 함수 작성
def get_abbrs(list_):
    return [x[:3] for x in list_ if len(x)>=3]

L = ['Seoul', 'Daegu', 'Kwangju', 'Jeju', 'in']
get_abbrs(L)


# In[26]:


#6. 다음코드를 람다 함수 형태로 수정할 때 알맞은 코드를 작성
def f(x,y):
    return x**y
f(2,3)


# In[27]:


f = lambda x,y:x**y
f(2,3)


# In[28]:


(lambda x,y:x**y)(2,3)


# In[30]:


#7. ex = [1,2,3,4,5]를 [1,4,9,16,25]의 결과를 얻을 수 있도록 람다함수와 map()함수를 사용하여 구현과 리스트 컴프리헨션으로 구현하시오
ex=[1,2,3,4,5]
list(map(lambda x:x**2, ex))


# In[31]:


ex=[1,2,3,4,5]
[x**2 for x in ex]


# In[32]:


#8. 다음 코드를 각각 실행하면 서로 다른 결과가 나온다. 이런 결과가 나오는 이유를 서술하시오
a = [1,2,3]
print(*a) #*매개변수; 인수가 언패킹되어 요소가 하나씩 들어감 #print(*a) -> print(a[0], a[1], a[2])으로 나타남
print(a) #리스트 a가 통째로 출력


# In[33]:


#9. 다음 코드의 실행 결과는?
date_info = {'year':"2019", 'month':"9", 'day':"6"}
result="{year}-{month}-{day}".format(**date_info)
result


# In[34]:


#10. n개의 벡터(리스트나 튜플, 셋등)의 크기가 동일한지 확인하는 함수
##vector_size_check(*vector _var)를 한 줄의 코드(리스트 컴프리헨션)로 작성하시오.
def vector_size_check(*vector_var):
    return len(set([len(x) for x in vector_var]))==1

vector_size_check((1,2),[1,2],[22,345],{'a':1,'b':2})


# In[35]:


vector_size_check((1,2,3),[1,2],[22,345],{'a':1,'b':2})


# In[36]:


#11. 다음과 같은 결과를 얻기 위해 하나의 스칼라값을 리스트나 튜플, 셋등 벡터에 곱하는 코드를 작성하시오.
##(단 입력되는 벡터의 크기는 일정하지 않음)
def scalar_vector_product(n, L):
    return [x*n for x in L]
scalar_vector_product(5, [1,2,3,4])


# ## 6.2 서술형 연습문제

# In[37]:


def mapping(addr):
    table = [1,2,5,9,6,4,0,3,8,7]
    return table [addr//SIZE]
SIZE=20
group = [9,8,7,6,5,4,3,2,1,0]
loc = [127, 64, 188]
for a, b in enumerate(loc):
    print(group[mapping(loc[a])], end=' ')


# In[38]:


a = 10 #전역 변수
def sub():
    global a #전역변수 a 참조
    a+=1 
    print(a, end=' ')

def func():
    for i in range(2): 
        a=5   #지역변수 a
        a+=1
        print(a, end=' ') #들여쓰기 조정
        sub() #들여쓰기 조정
a+=1
func()

# 오류가 발생하는 라인:  4번째 줄: a+=1 (지역변수 선언 전 지역변수 사용해서 에러 발생)
# 문제 해결을 위한 코드: global a
# 코드 수정 후 실행 결과: 6 12 6 13 


# In[39]:


#서3
var = 100 #전역변수
def func(var):
    var=200 #지역변수(전역 변수에 영향X)
func(var) 
print(var) #100


# In[40]:


#서4
def my_func(func, *args):
    return func(*args)
import numpy as np
my_func(np.add, 2,3) #5


# In[41]:


#서5
def my_func(func, *args):
    return func(*args)
my_func(lambda a,b:a**b, 3,2) #9


# In[ ]:


#서6
"""
파이썬 함수에 대한 설명 중 잘못된 것은?
① 파이썬의 함수는 중복 정의해 사용할 수 있다.
② 파이썬의 함수 매개변수는 기본값을 가질 수 있다.
③ **args 형식의 매개변수가 있으면 키워드 인수는 딕셔너리 형식으로 받는다.
④ 함수를 호출할 때 매개변수 이름이 없는 인수는 매개변수 이름이 있는 인수
보다 앞에 와야 한다.
"""
# 1번: 파이썬 함수는 오버로딩 지원X
# 매개변수 순서: 순서 인수 > 튜플 인수 > 키워드 인수 > 딕셔너리 인수


# In[43]:


#서7: 오류가 발생하는 함수 호출은? #func([], a=40)
list_=[]
def func(a, L=None):
    if L is None:
        L=[]
    L.append(a)
    return L
func(10, list_)
func(20, L=list_)
func(a=30)
#func([], a=40) -> func(L=[], a=40)이면 오류X


# In[ ]:


#서8 lambda


# In[44]:


#서9 다음 코드의 실행 결과는?
pairs=[(1, 'd'), (2,'c'), (3,'b'), (4,'a')]
pairs.sort(key=lambda pair:pair[1])
pairs #[(4, 'a'), (3, 'b'), (2, 'c'), (1, 'd')]

