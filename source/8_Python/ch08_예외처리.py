#!/usr/bin/env python
# coding: utf-8

# **21-02-26 python 08_예외 처리(Exception Handling)   (c)cherryuki (ji)**

# **<font size=5 color="red">ch08. 예외처리</font>**

# # 1절. 예외처리
# - 예외(Exception): 실행 중에 발견된 오류
# - 예외 처리(Exception Handling): 오류 발생 가능성이 있는 부분에 대한 처리를 미리 프로그래밍 하는 것

# In[2]:


filename = input("파일명을 입력하세요: ")
f = open('data/'+filename+'.txt', 'r') #읽기모드(r)로 파일 열기
firstline = f.readline() #한 줄 읽어서 firstline에 저장
print(firstline)
f.close() #파일 닫기


# - 예외 발생 예시

# In[3]:


filename = input("파일명을 입력하세요: ") #없는 파일 입력시: FileNotFoundError
f = open('data/'+filename+'.txt', 'r') #읽기모드(r)로 파일 열기
firstline = f.readline() #한 줄 읽어서 firstline에 저장
print(firstline)
f.close() #파일 닫기


# In[4]:


num = int(input("정수를 입력하세요>")) #ValueError (실수나 문자 등 정수가 아닌 값 입력시)


# In[5]:


num = int(input("정수를 입력하세요>"))
print(10/num) #ZeroDivisionError (0으로 나눌경우)


# In[6]:


l = [1,2,3]
idx = int(input("조회할 인덱스는? "))
print("{}번째 값은 {}".format(idx, l[idx])) #IndexError (없는 인덱스 값 참조시)


# # 2절. 예외 처리하기(try ~ except)

# In[9]:


try:
    x = int(input("정수: "))
    print("입력한 정수: {}".format(x))
except ValueError as e: #ValueError 대신 상위 Exception 으로 기재해도 무방(최상위: BaseException)
    print(e)
    print("정수를 입력하시기 바랍니다")


# In[11]:


#입력한 값이 정수가 아닐 경우 예외 메시지를 출력, 다시 입력 받기
while True:
    try:
        x = int(input("정수를 입력하세요> "))
        print("입력한 정수: {}".format(x))
        break #반드시 입력해야함(제대로 입력시 while절 빠져나가기 위함)
    except Exception:
        print("유효한 정수가 아닙니다.")


# - 예외 별로 처리시 상속 관계에 있는 예외일 경우 <font color="red">상위 예외를 하단에 기재</font>해야 함

# In[12]:


#예외 별로 처리
#입력한 정수로 100을 나눈 값(100/입력한 정수) 출력 (두가지 예외 사항을 따로 처리)
while True:
    try:
        x = int(input("정수를 입력하세요> "))
        print("입력한 수: {}".format(x))
        print("100/{}={}".format(x, 100/x))
        break
    except ValueError:
        print("유효한 정수가 아닙니다")
    except ZeroDivisionError:
        print("0으로는 나눌 수 없습니다. 0을 제외한 정수를 입력하세요")
    except Exception: #상위 예외 클래스는 하단에 적어야 함 
        print("예외 별로 처리시 상위 예외 클래스는 하단에 기재해야 함")


# In[13]:


#다중 예외 처리
while True:
    try:
        x = int(input("정수를 입력하세요> "))
        print("입력한 수: {}".format(x))
        print("100/{}={}".format(x, 100/x))
        break
    except(ZeroDivisionError, ValueError) as e: #예외 인수
        print("문자나 실수, 0은 입력하실 수 없습니다. 다시 입력해주세요")
        print(e) #예외 인수로 에러 메시지 출력


# In[14]:


#다중 예외 처리
while True:
    try:
        x = int(input("정수를 입력하세요> "))
        print("입력한 수: {}".format(x))
        print("100/{}={}".format(x, 100/x))
        break
    except: #예외 이름 생략 가능
        print("다시 입력해주세요")


# **try ~ except ~ (else ~) finally**<br>
# - try블록에서 예외 발생시 except블록 실행. 예외 발생 안되면 else 블록 실행

# In[15]:


try:
    f = open("data/ch08_hello.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError: #try 블록에 예외 발생시 실행
    print("없는 파일입니다")
else: #try블록에 예외 발생 안할 경우 실행
    data = f.read()
    print(data)
finally: #try 블록 예외 발생여부와 상관없이 반드시 실행
    f.close()


# In[17]:


try:
    f = open("data/ch08_bye.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError :
    print("파일이 없습니다")
finally: #try 블록 예외 발생여부와 상관없이 반드시 실행
    f.close()


# In[19]:


while True:
    try:
        x = int(input("정수를 입력하세요> "))
        print("입력한 수: {}".format(x))
        result = 100/x
        print("100/{}={}".format(x, result))
        break
    except(ValueError, ZeroDivisionError) as e:
        print(e)
        print(e.args[0]) #e.args가 튜플 형식이므로 e.args[0]을 이용해서 예외 메시지 출력


# # 3절. raise로 예외 발생시키기

# In[20]:


raise NameError("예외 발생")


# In[21]:


def insert(data):
    if len(data)==0:
        raise Exception("빈 데이터라 입력할 수 없습니다")
    print(data, "를 입력하였습니다")


# In[23]:


try:
    insert([])
except Exception as e:
    print(e.args[0])


# # 4절. raise를 이용해서 추상 클래스 정의하기
# - python은 추상클래스나 추상메소드를 위한 키워드 없으나 raise를 이용해서 추상 클래스 흉내낼 수 있음

# # 5절. 사용자 정의 예외

# In[24]:


class AbstractError(Exception):
    "추상 클래스를 이용하여 객체 생성시 발생하는 오류"
    def __init__(self):
        Exception.__init__(self, "Shape는 추상클래스여서 객체 생성 불가")


# In[25]:


class Shape:
    def __init__(self):
        raise AbstractError()
    def cal_area(self):
        raise AbstractError()


# In[26]:


s = Shape()


# In[27]:


class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def cal_area(self):
        return self.r**2*3.14


# In[28]:


c = Circle(3)


# In[29]:


c.cal_area()


# # 6절. 파일 정리 작업

# In[31]:


filename = input("파일명> ")
try:
    f = open("data/"+filename, 'r')
    lines = f.readlines()
    print(lines)
except:
    print("없는 파일입니다. 파일명을 확인해주세요")
finally:
    f.close()


# In[2]:


#with절 이후에는 파일 자동적으로 close()
with open('data/ch08_hello.txt', 'r') as f:
    lines=f.readlines()
    print(lines)


# # 7절. 연습문제

# In[3]:


#실습형1
while True:
    try:
        num1 = float(input("첫번째 숫자: "))
        num2 = float(input("두번째 숫자: "))
        print("입력한 수는 {}와 {}입니다.".format(num1, num2))
        print("{}을 {}으로 나누면 {}입니다.".format(num1, num2, round(num1/num2, 2)))
        break
    except:
        print("유효한 숫자가 아닙니다. 다시 시도하세요.")


# In[4]:


#실습형2
while True:
    try:
        num1 = float(input("첫번째 숫자: "))
        num2 = float(input("두번째 숫자: "))
        print("입력한 수는 {}와 {}입니다.".format(num1, num2))
        print("{}을 {}으로 나누면 {}입니다.".format(num1, num2, round(num1/num2, 2)))
        break
    except ValueError:
        print("유효한 숫자가 아닙니다. 다시 시도하세요.")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다. 다시 시도하세요.")


# In[ ]:


#문제풀이형
"""
1) 예외처리에 대해 잘못 설명한 것: 3번 
 -> 상위 예외처리를 위한 except 블록은 하위 예외 처리 except 블록보다 하단에 선언되어야 함
2) 예외처리에 대한 설명 중 잘못된 것: 2번
 -> 파이썬에선 catch가 아닌 except를 이용함 (catch는 자바)
3) except절을 잘못 사용한 것은? 4번
 -> except Exception as e: (as e)는 생략 가능
4) 예외처리에 사용하지 않는 구문? with
 -> with절 이후에는 파일 자동으로 닫힘
"""

