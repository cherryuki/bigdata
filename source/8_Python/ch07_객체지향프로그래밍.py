#!/usr/bin/env python
# coding: utf-8

# **21-02-26 python 07_객체지향 프로그래밍 (c)cherryuki (ji)**

# # <font color="red"> ch07. 객체지향 프로그래밍 </font>

# # 1절. 객체와 클래스
# <p>
# 　class 클래스명(상속 받을 클래스명): <br>
# 　　　　함수나 변수 선언
# </p>

# In[3]:


class Person:
    "Person 클래스"
    pass
p1 = Person()


# In[4]:


type(p1)


# In[5]:


print(p1)


# In[6]:


isinstance(p1, Person)


# In[7]:


print(p1.__doc__) #docstirng 확인


# # 2절. 변수와 메소드
# - 일반 변수, static 변수 / 일반 메소드, static 메소드, 클래스 메소드

# In[8]:


#변수 추가
class Person:
    name="Kong"
    gender="male"
p1=Person()
print(p1.name, p1.gender)


# In[9]:


p2 = Person()
p2.name = "Han"
print(p2.name, p2.gender)


# In[10]:


Person.name="Jenny"
Person.gender = "female"


# In[11]:


print(p1.name, p1.gender) #데이터를 셋팅하지 않으면 Person을 계속 참조(Person 데이터로 바뀜)
print(p2.name, p2.gender) #name은 셋팅한 그대로. gender는 셋팅한 적 없으므로 Person 데이터 참조


# In[12]:


p1.name="Park"
p1.gender="male"
print(Person.name, Person.gender)
print(p1.name, p1.gender)
print(p2.name, p2.gender)


# In[13]:


#메소드 추가
class Person:
    name="Richard"
    gender="male"
    def print_info():
        print("Person method")
print(Person.name, Person.gender)
Person.print_info()


# In[14]:


p1 = Person()
p1.name="Han"
print(p1.name, p1.gender)
print(Person.name, Person.gender)


# In[15]:


p1.print_info() #매개변수가 없을 때는 객체에서 실행 불가능(객체만 실행 가능하려면 첫 인수: self)


# In[16]:


Person.print_info()


# In[17]:


#인스턴트 메소드
class Person:
    name="Richard"
    gender="male"
    age=36
    def print_info(self): #객체만 실행 가능한 메소드 = 인스턴트 메소드
        print("{}는 {}세이고 {}입니다".format(self.name, self.age, self.gender))
print(Person.name, Person.gender, Person.age)
p1 = Person()
p1.name="Jenny"
p1.gender="female"
p1.print_info() #객체만 실행 가능! Person.print_info()는 에러 발생


# In[19]:


p1.name, p1.gender, p1.age


# - 파이썬은 클래스와 인스턴스(객체)의 이름 공간 분리되어 있음
# - 클래스와 인스턴스의 변수명이 다를 수 있음
# - 동적으로 인스턴스(객체)에 멤버 추가 가능

# In[20]:


p1.address="Seoul"
p1.nickname="Pooh"


# In[21]:


p1.print_info()


# **인스턴스 메소드 vs. 클래스 메소드 vs. static 메소드**
# 
# 1. 인스턴스 메소드: 첫 인자에 self 삽입. 객체를 통해서 호출할 메소드
# 2. 클래스 메소드: @classmethod를 통해서 선언한 메소드. 인자에 cls(clazz)를 삽입
# 3. static 메소드: @staticmethod를 통해서 선언한 메소드.

# In[22]:


#인스턴스 메소드 vs. 클래스 메소드 vs. static 메소드
class Person:
    name="리차드"
    gender="남성"
    age=36
    def print_info(self): #인스턴스 메소드(인자에 self)
        print("일반(인스턴스=객체) 메소드 - {}는 {}세 {}입니다".format(self.name, self.age, self.gender))
    @classmethod
    def do_(cls): #클래스 메소드(인자에 cls, class)
        cls.name="제니"
        cls.gender="여성"
        cls.age=33
        print("클래스 메소드 - {}는 {}세 {}입니다".format(cls.name, cls.age, cls.gender))
    @staticmethod
    def that_(): #static 메소드(인자 없음)
        print("static 메소드 = {}는 {}세 {}입니다".format(Person.name, Person.age, Person.gender))


# In[23]:


p1 = Person()
p2 = Person()
p1.print_info()
p2.print_info()


# In[24]:


p1.name = "수련"
p1.age += 1
p1.print_info()
p2.print_info()
p2.that_() #static 메소드는 객체를 통해서도 클래스를 통해서도 호출 가능
Person.that_() #static 메소드


# In[25]:


Person.do_() #클래스 메소드


# In[26]:


p1.print_info()
p2.print_info()


# In[27]:


Person.name="공유"
Person.gender="남성"
Person.age=477
p1.print_info()
p2.print_info() #변경(지정)하지 않은 데이터는 클래스 데이터 계속해서 참조(클래스 데이터가 바뀌면 바뀜)


# # 3절. 생성자(\_\_init__())와 소멸자(\_\_del__())
# - 생성자 함수: \_\_init__(self[, 매개변수1, ...]); 객체가 생성될 때 자동 실행 <br>
# 　　　　　생성시 필요한 코드(객체 멤버의 초기화)를 포함
# - 소멸자 함수: \_\_del__(self); 객체가 소멸될 때 자동 실행 <br>
# 　　　　　소멸시 필요한 코드를 포함 <br>
# 　　　　　인스턴스 객체의 레퍼런스 카운트가 0이 될 때 실행

# In[28]:


#생성자와 소멸자를 갖는 클래스
class Person:
    def __init__(self):
        print("Person 객체를 생성")
        self.name="공유" #일반 변수
        self.gender="남성"
    def __del__(self):
        print("Person 객체를 소멸")
    def print_info(self):
        print("일반 메소드 - {}님은 {}입니다".format(self.name, self.gender))


# In[29]:


p1 = Person()
p1.print_info()


# In[30]:


p1.name="공지철"
p1.print_info()


# In[31]:


type(p1), isinstance(p1, Person)


# In[32]:


del p1 #인스턴스 객체의 레퍼런스 카운트가 0이 되면 소멸


# In[33]:


p1 = Person()


# In[34]:


p1 = Person() #이전 주소 소멸, 새로운 주소 생성


# In[35]:


p2 = p1


# In[36]:


del p1


# In[37]:


del p2 #인스턴스 객체의 레퍼런스 카운트가 0이 되면 소멸


# In[38]:


class Person:
    def __init__(self, name, gender):
        print("Person 객체를 생성")
        self.name= name
        self.gender= gender
    def __del__(self):
        print("Person 객체를 소멸")
    def print_info(self):
        print("일반 메소드 - {}님은 {}입니다".format(self.name, self.gender))


# In[39]:


p1 = Person("이지아", "여성")
p1.print_info()


# In[40]:


del p1


# <font color="red">
# * 생성자 함수를 통한 멤버변수의 초기화 <br>
# * 파이썬은 함수를 중복정의(오버로딩) 불가 <br>
# * 생성자 함수도 중복정의 불가** </font>

# In[1]:


class Person:
    def __init__(self, name="리차드", gender="남성"):
        print("Person 객체를 생성")
        self.name= name
        self.gender= gender
    def __del__(self):
        print("Person 객체를 소멸")
    def print_info(self):
        print("일반 메소드 - {}님은 {}입니다".format(self.name, self.gender))
    def __str__(self): #자바의 toString
        return "{}님은 {}입니다".format(self.name, self.gender)


# In[2]:


p1 = Person("제니", "여성")
p2 = Person("박보검")
p3 = Person()
p1.print_info()
p2.print_info()
p3.print_info()


# In[3]:


print(p1)
print(p2)
print(p3)


# # 4절. 상속과 재정의

# In[1]:


class Person:
    "name과 gender를 갖는 Person 타입"
    def __init__(self, name, gender): #매개변수 2개로 호출될 생성자
        print("Person 객체를 생성")
        self.name= name
        self.gender= gender
    def __del__(self):
        print("Person 객체를 소멸")
    def print_info(self):
        print("일반 메소드 - {}님은 {}입니다".format(self.name, self.gender))
    def __str__(self): 
        return "{}님은 {}입니다".format(self.name, self.gender)


# In[5]:


p1 = Person("리차드", "남성")


# In[6]:


class Student(Person): #class 클래스명(상속받을 클래스):
    pass


# In[7]:


issubclass(Student, Person)


# In[8]:


s1 = Student("제니", "여성") #super 클래스의 __init__상속


# In[9]:


print(s1)


# In[10]:


s1.print_info()


# In[11]:


class Student(Person):
    "name, gender, major를 매개변수로 갖는 Student 타입"
    def __init__(self, name, gender, major):
        self.name=name
        self.gender=gender
        self.major=major
    def __del__(self):
        pass
    def print_info(self):
        print("{}({})님 전공은 {}입니다".format(self.name, self.gender, self.major))
    def __str__(self):  
        return "{}({})님 전공은 {}입니다".format(self.name, self.gender, self.major)


# In[12]:


s1 = Student("공지철", "남성", "빅테이터 분석")
print(s1)
print(s1.__str__())


# In[14]:


isinstance(s1, Student), isinstance(s1, Person)


# In[17]:


#super() 사용
class Student(Person):
    "name, gender, major를 매개변수로 갖는 Student 타입"
    def __init__(self, name, gender, major):
        #부모 클래스의 생성자를 호출하여 자식 클래스의 생성자 쉽게
        Person.__init__(self, name, gender)
        self.major=major
    def __del__(self):
        pass
    def print_info(self):
        print("{}({})님 전공은 {}입니다".format(self.name, self.gender, self.major))
    def __str__(self):  
        return super().__str__() + " 전공은 {}입니다".format(self.major)
        #return Person.__str__(self) + " 전공은 {}입니다".format(self.major)


# In[18]:


s1 = Student("한지민", "여성", "통계학")
print(s1)


# **static 변수: 여러 객체들 사이에 데이터를 공유하고 싶을 때 사용**
# - 클래스 변수 이름 앞에 under bar 2개(\_\_) 붙이면 내부적으로 클래스명._클래스명\_\_변수 이름으로 참조

# In[2]:


class Student(Person):
    "name, gender, major를 매개변수로 갖는 Student 타입(객체 개수 포함)"
    __count = 0; #static 변수
    def __init__(self, name, gender, major):
        Student._Student__count +=1 #객체가 생설될 때 마다 __count 증가
        Person.__init__(self, name, gender)
        self.major=major
    def __del__(self):
        Student._Student__count -=1 #객체가 소멸될 때마다 __count 감소
    def print_info(self):
        print("{}({})님 전공은 {}입니다".format(self.name, self.gender, self.major))
    def __str__(self):  
        return super().__str__() + " 전공은 {}입니다".format(self.major)
        #return Person.__str__(self) + " 전공은 {}입니다".format(self.major)
    @classmethod
    def get_count(cls):
        #return Student._Student__count
        return cls.__count


# In[3]:


s1 = Student("이지아", "여성", "빅데이터")
print(s1)
print("객체 개수:", s1.get_count())


# In[4]:


s2 = Student("한지민", "여성", "빅데이터 분석")
print(s2)
print("객체 개수:", s2.get_count())


# In[5]:


s3 = Student("공유", "남성", "통계학")
s3.print_info()
print("객체 개수:", s2.get_count())
print("객체 개수:", s3.get_count())
print("객체 개수:", Student.get_count())


# In[6]:


del s3
print("객체 개수:", Student.get_count())


# # 5절. 연습문제

# In[1]:


#실습형
class Shape:
    "x, y 좌표를 갖는 도형 클래스"
    def __init__(self, x=0, y=0):
        print("Shape 클래스 생성")
        self.x=x
        self.y=y
    def __del__(self):
        print("Shape 클래스 소멸")
    def __str__(self):
        return "x:{}, y:{}".format(self.x, self.y)
    def move(self, x, y):
        self.x += x
        self.y += y
    def cal_area(self):
        raise Exception("상속 받는 도형에 맞게 수정")
    @staticmethod
    def print_info():
        print("static method - x:{}, y:{}".format(self.x, self.y))


# In[2]:


class Triangle(Shape):
    "width, height를 변수로 갖는 삼각형 클래스"
    __count=0
    def __init__(self, width, height, x=0, y=0):
        Triangle._Triangle__count += 1
        Shape.__init__(self, x, y)
        self.width=width
        self.height=height
    def __del__(self):
        Triangle._Triangle__count -= 1
    def __str__(self):
        #return Shape.__str__(self) + ", width:{}, height:{}".format(self.width, self.height)
        return super().__str__() + ", width:{}, height{}".format(self.width, self.height)
    def cal_area(self):
        return "삼각형의 넓이: {}".format(self.width*self.height/2)
    @classmethod
    def get_count(cls):
        return cls.__count
        #return Triangle._Triangle__count


# In[3]:


t1 = Triangle(3,4)


# In[4]:


type(t1), isinstance(t1, Triangle), isinstance(t1, Shape), issubclass(Triangle, Shape)


# In[5]:


print(t1)


# In[6]:


t2 = Triangle(4,3)


# In[7]:


print(t1.cal_area())
print(t2.cal_area())
print(Triangle.get_count())


# In[8]:


s1 = Shape()
s2 = Shape(3,4)


# In[9]:


print(s1)
print(s2.__str__())


# In[10]:


t1.move(10,10)


# In[11]:


s1.move(2,4)


# In[12]:


print(s1)
print(t1)


# In[13]:


s1.cal_area()


# In[14]:


print(t1.get_count())


# In[15]:


del t1


# In[17]:


Triangle.get_count()


# - 서술형1 올바른 클래스 정의: class Person():
# - 서술형2 Person 클래스 객체 생성: p1=Person()
# - 서술형3 인스턴스 메소드 선언: def print_info(self):
# - 서술형4 생성자와 소멸자에 대해 잘못 설명: 1번 -> 파이썬은 함수 오버로딩 지원X
# - 서술형5 Student is Person 클래스 상속: clss Student(Person):
# - 서술형6 상속과 재정의에 대해 잘못 설명: 3번 -> 매개변수 수가 같아야 함
# - 서술형7 클래스 메소드 호출방법 중 잘못 된 것: 3번(인스턴스 메소드(self)는 객체로 호출)
# - 서술형8 빈 칸에 넣을 수 없는 것: 3번
# - 서술형9 속성과 메소드에 대한 설명 중 잘못: 2번 -> \_\_str__()메소드는 self 매개변수 필요

# In[18]:


class SomeClass:
    def method_a(self): #객체로만 호출
        print("method_a")
    @classmethod
    def method_b(cls): 
        print("method_b")
obj=SomeClass()


# In[19]:


obj.method_a()
obj.method_b()
SomeClass.method_b()


# In[21]:


SomeClass.method_a() #객체로 호출해야 함


# In[22]:


#서술형9
class Person:
    "서술형 9번 문제 풀이"
    def __init__(self, name="서술형", no=9):
        self.name=name
        self.no=no
    def __del__(self):
        pass
    def __str__(self): #self 매개변수 필요
        return "이름은 "+self.name
    def print_info(self):
        print(self.name)


# In[23]:


p = Person()
print(p)


# In[24]:


p.__dict__ #클래스 멤버 확인


# In[ ]:




