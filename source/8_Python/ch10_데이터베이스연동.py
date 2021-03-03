#!/usr/bin/env python
# coding: utf-8

# **21-03-03 python 09_파일 입출력 프로그래밍 (c)cherryuki (ji)**

# # <font color="red">ch10. 데이터베이스 연동</font>

# # 1절. SQLite 데이터 베이스 연결
# ## 1.1 SQLite와 Python
# - SQLite 데이터 베이스는 별도의 서버 프로세스 없이 SQL을 사용하여 DB 액세스 할 수 있도록 만든 간단한 디스크 기반 데이터 베이스를 제공하는 C라이브러리
# - SQLite는 프로토 타입을 만들 때까지 사용. 정식 제품은 오라클이나 다른 DBMS를 연결
# - [[SQLite DB Browser](https://sqlitebrowser.org/dl/)]

# In[1]:


import sqlite3
sqlite3.sqlite_version


# ## 1.2 데이터 베이스 연결

# In[2]:


#DB연결 객체 생성시 파일이 없으면 파일 생성. 파일 있으면 해당 파일 연결
conn = sqlite3.connect('data/ch10_example.db')
conn


# In[3]:


#커서 객체 반환. 커서는 SQL문을 실행시키고 결과 데이터를 조회하는데 사용
cursor = conn.cursor()


# In[4]:


cursor.execute("""
    CREATE TABLE MEMBER(
        NAME TEXT,
        AGE INT,
        EMAIL TEXT
    )
""")


# In[5]:


cursor.execute("DROP TABLE MEMBER")


# In[6]:


cursor.execute("""
    CREATE TABLE MEMBER(
        NAME TEXT,
        AGE INT,
        EMAIL TEXT
    )
""")


# In[7]:


cursor.execute("INSERT INTO MEMBER VALUES ('공지철', 43, 'kong@green.com')")
cursor.execute("INSERT INTO MEMBER VALUES ('한지민',39,'han@green.com')")
cursor.execute("INSERT INTO MEMBER VALUES ('윤여정',72,'yoon@green.com')")


# In[8]:


conn.commit()  #<-> conn.rollback()


# In[9]:


cursor.execute('SELECT NAME FROM MEMBER') #실행 결과는 cursor가 가리킴


# <select문의 결과를 받는 함수>
# - fetchall(); 결과를 모두 받을 때
# - fetchone(); 결과를 한 행씩 받을 때
# - fetchmany(n); 결과를 n행씩 받을 때

# In[10]:


#select문 결과를 받는 함수: fetchall(), fetchone(), fetchmany(n)
print(cursor.fetchall())


# In[11]:


print(cursor.fetchall()) #한번 fetch한 건 다시 데이터 가져올 수 없음(계속 사용하려면 변수에 담아서 사용)


# In[12]:


cursor.execute('SELECT * FROM MEMBER')
members = cursor.fetchall()
for member in members:
    print(member)


# In[13]:


members[0]


# In[14]:


cursor.execute('SELECT * FROM MEMBER')
while True:
    member = cursor.fetchone()
    if member is None:
        break;
    print(member)


# In[15]:


cursor.execute('SELECT * FROM MEMBER')
for member in cursor.fetchmany(2):
    print(member[0], member[1], member[2]) #튜플로 나오지 않게 하려면


# In[16]:


cursor.fetchmany(2)


# In[17]:


cursor.close() #생략 가능
conn.close()


# ## 1.3 SQL구문에 파라미터 사용하기
# - qmark 스타일; 매개변수를 포함해야 할 값에 ?로 표시한 후 튜플을 통해 물음표에 전달할 값을 지정
# - named 스타일(추천); 매개 변수를 포함해야 할 값 : 값을 받을 이름 표시한 후 딕셔너리 이용해 이름에 값 전달

# In[20]:


#qmark 파라미터 사용
conn = sqlite3.connect('data/ch10_example.db')
cursor = conn.cursor()
cursor.execute('SELECT * FROM MEMBER WHERE NAME IN (?, ?)', ('공지철', '공유'))
print(cursor.fetchall())


# In[21]:


name1 = input("검색할 이름1: ")
name2 = input("검색할 이름2: ")
names = (name1, name2)
cursor.execute('SELECT * FROM MEMBER WHERE NAME IN (?, ?)', names)
print(cursor.fetchall())


# In[24]:


#named 파라미터 사용
name = input("검색할 이름: ")
cursor.execute('SELECT * FROM MEMBER WHERE NAME=:name', {'name':name})
members=cursor.fetchall()
if len(members)==0:
    print("해당 이름의 데이터가 없습니다")
else:
    print(members)


# In[25]:


name = input("추가할 이름: ")
try:
    age = int(input("나이: "))
except ValueError:
    print("유효하지 않은 나이를 입력해서 20살로 처리")
    age=20
email=input("이메일: ")
cursor.execute("INSERT INTO MEMBER VALUES(:name, :age, :email)", {'name':name, 'age':age, 'email':email})


# In[26]:


cursor.execute('SELECT * FROM MEMBER')
print(cursor.fetchall())


# # 2절. 오라클 데이터 베이스 연결

# In[27]:


#Anaconda prompt 에서 cx_Oracle 설치
#pip install cx_Oracle
#pip show cx_Oracle


# In[29]:


#데이터 베이스 설정(DBMS가 있는 서버 주소)
import cx_Oracle
oracle_dsn = cx_Oracle.makedsn(host="localhost", port=1521, sid="xe")
oracle_dsn


# In[30]:


conn = cx_Oracle.connect("scott", "tiger", dsn=oracle_dsn)
conn
#에러가 날 경우 VC_redist.x64.exe 인스톨


# In[31]:


#conn 가져오기(1)
oracle_dsn = cx_Oracle.makedsn(host="localhost", port=1521, sid="xe")
conn = cx_Oracle.connect("scott", "tiger", dsn=oracle_dsn)


# In[32]:


conn.close()


# In[34]:


#conn 가져오기(2)
conn = cx_Oracle.connect("scott", "tiger", "localhost:1521/xe")
conn


# In[35]:


#cursor 가져오기
cursor = conn.cursor()


# In[36]:


sql = "SELECT * FROM EMP"
cursor.execute(sql)
emp=cursor.fetchall()


# In[37]:


for e in emp:
    print(e)


# In[38]:


#변수에 저장 안하고 한 번만 출력할 경우
sql= "SELECT * FROM EMP"
cursor.execute(sql)
for c in cursor:
    print(c)


# In[39]:


sql = 'SELECT * FROM EMP WHERE DEPTNO=:deptno'
deptno=input("검색하고자 하는 부서 번호는?")
cursor.execute(sql, {'deptno':deptno})
for emp in cursor:
    print(emp)


# In[40]:


sql = "SELECT * FROM EMP WHERE DEPTNO=:deptno"
deptno=input("검색하고자 하는 부서 번호는? ")
cursor.execute(sql, {'deptno':deptno})
emp = cursor.fetchall()
if len(emp)==0:
    print("입력한 부서번호의 데이터가 없습니다")
else:
    for e in emp:
        print(e)


# In[41]:


import pandas as pd
cursor.execute("SELECT * FROM EMP")
data = cursor.fetchall() #튜플 리스트
data_df = pd.DataFrame(data) #데이터 프레임
data_df


# In[45]:


#각 필드 특징 정보(필드명, type, display_size, 내부 크기, 정확도, scale, nullable)
cursor.description


# In[46]:


[row[0] for row in cursor.description]


# In[47]:


data_df.columns


# In[48]:


data_df.columns = [row[0] for row in cursor.description]


# In[49]:


data_df.columns


# In[50]:


data_df.head()


# In[51]:


data_df.tail()


# In[52]:


cursor.close()
conn.close()


# # 3절. MariaDB 연결

# In[53]:


#Anaconda prompt(관리자 권한 실행) 에서 pip install pymysql설치
import pymysql


# In[54]:


conn = pymysql.connect(host="localhost", port=3306, db="kimdb", user="root", passwd="mysql",
                      charset="utf8", autocommit=True)
conn


# In[55]:


cursor=conn.cursor()
sql = "select * from personal"
cursor.execute(sql)
result = cursor.fetchall()
for r in result:
    print(r)


# In[56]:


personal = pd.DataFrame(result)
personal.columns = [row[0] for row in cursor.description]
personal


# In[57]:


personal = pd.DataFrame(result, columns=[row[0] for row in cursor.description])
personal


# In[58]:


cursor.close()
conn.close()


# # 4절. 회원 입력/조회(검색)/출력/삭제 애플리케이션
# - SQLite 이용: ch10_db 폴더 ch10_SQLite 파일 참조
# - Oracle 이용: ch10_db 폴더 ch10_Oracle 파일 참조

# In[ ]:




