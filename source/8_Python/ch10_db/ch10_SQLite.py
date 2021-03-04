#!/usr/bin/env python
# coding: utf-8

# **21-03-03 python 10_데이터 베이스 연동 (c)cherryuki (ji)**

# # 회원 입력/조회(검색)/출력/삭제 애플리케이션
# - SQLite 이용

# In[1]:


def insert_member():
    global conn
    cursor = conn.cursor()
    sql = "INSERT INTO MEMBER VALUES (:name, :phone, :email, :age, :grade, :etc)"
    name = input("이름: ")
    phone = input("전화번호: ")
    email = input("이메일: ")
    try:
        age = int(input("나이: "))
    except:
        print("유효하지 않은 값을 입력하여 20으로 초기화")
        age=20
    try:
        grade = int(input("고객 등급(1~5): "))
    except:
        print("유효하지 않은 값을 입력하여 1로 초기화")
        grade=1
    etc = input("기타 정보: ")
    cursor.execute(sql, {'name':name, 'phone':phone, 'email':email, 'age':age, 'grade':grade, 'etc':etc})


# In[2]:


def select_all():
    global conn
    cursor=conn.cursor()
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    members = cursor.fetchall()
    import pandas as pd
    members_df = pd.DataFrame(members, columns=[row[0] for row in cursor.description])
    if len(members)==0:
        print("데이터가 존재하지 않습니다")
    else:
        print(members_df)


# In[3]:


def select_name():
    global conn
    cursor = conn.cursor()
    sql = "SELECT * FROM MEMBER WHERE NAME=:name"
    name = input("조회할 이름: ")
    cursor.execute(sql, {'name':name})
    members = cursor.fetchall()
    import pandas as pd
    members_df=pd.DataFrame(members, columns=[row[0] for row in cursor.description])
    if len(members)==0:
        print("데이터가 존재하지 않습니다")
    else:
        print(members_df)


# In[4]:


def delete_mail():
    global conn
    cursor = conn.cursor()
    sql = "SELECT * FROM MEMBER WHERE EMAIL=:email"
    email = input("삭제할 이메일 주소: ")
    cursor.execute(sql, {'email':email})
    members=cursor.fetchall()
    if len(members)==0:
        print("입력한 이메일의 데이터가 존재하지 않습니다")
    else:
        cursor.execute('DELETE FROM MEMBER WHERE EMAIL=:email', {'email':email})
        print("삭제되었습니다")


# In[5]:


def save_csv():
    global conn
    cursor=conn.cursor()
    sql = "SELECT * FROM MEMBER"
    cursor.execute(sql)
    members = cursor.fetchall()
    import pandas as pd
    members_df = pd.DataFrame(members, columns = [row[0] for row in cursor.description])
    import csv
    filename = input("파일명: ")
    members_df.to_csv(filename+'.csv')
    print(filename+'.csv로 저장되었습니다')


# In[6]:


def close_sql():
    global conn
    conn.commit()
    conn.close()
    print("종료합니다")


# In[7]:


def main():
    while True:
        print("1.입력", "2.전체 조회", "3.이름 찾기", "4.메일 삭제", "5.CSV 내보내기", "0.종료",
             sep=" | ")
        try:
            menu = int(input("메뉴 선택: "))
        except:
            print("유효하지 않은 값을 입력하였습니다. 다시 선택해주세요.")
        if menu==1:
            insert_member()
        elif menu==2:
            select_all()
        elif menu==3:
            select_name()
        elif menu==4:
            delete_mail()
        elif menu==5:
            save_csv()
        elif menu==0:
            close_sql()
            break


# In[8]:


if __name__=='__main__':
    import sqlite3
    global conn
    conn = sqlite3.connect('data.db')
    main()

