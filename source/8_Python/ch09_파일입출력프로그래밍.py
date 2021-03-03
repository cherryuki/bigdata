#!/usr/bin/env python
# coding: utf-8

# **21-03-02 python 09_파일 입출력 프로그래밍 (c)cherryuki (ji)**

# # <font color="FF0000">ch09. 파일 입출력 프로그래밍</font>

# # 1절. 파일에 데이터 저장하고 불러오기

# In[8]:


f = open('data/ch09_sample.txt', 'w') #r;읽기(기본값)  w;쓰기(처음부터 다시 쓰기), a;기존 내용에 추가
print(f.writable())


# In[9]:


f.write("Hello\nWorld\nHello\nPython")
f.close() #파일 닫아야 적은 내용 확인 가능(닫지 않으면 변경 전)


# In[10]:


#with 구문 이용하면 파일 열어 사용한 후 매번 닫아주는 코드 작성하지 않아도 됨
with open('data/ch09_sample.txt', 'w') as f:
    print(f.writable())
    f.write('Python is easy.\nPython is smart.')


# In[11]:


with open('data/ch09_sample.txt', 'a') as f:
    print('\n프린트 함수로 파일 쓰기가 가능함', file=f)


# In[12]:


with open('data/ch09_sample.txt', 'a') as f:
    f.write('\n방법1. \nHello\nWorld')
    textlist=['Python is easy.', 'R is easy', 'Java is easy']
    f.write('\n방법2.\n')
    for line in textlist:
        f.write(line+'\n')
    f.write('방법3. \n')
    f.writelines(textlist)


# In[13]:


#파일 한꺼번에 읽기
with open('data/ch09_sample.txt', 'r') as f:
    lines=f.readlines() 
    for line in lines:
        #print(line, end='')
        print(line.strip())


# In[14]:


#파일을 한 줄씩 읽고 출력
with open('data/ch09_sample.txt', 'r') as f:
    line=f.readline()
    while line !='':
        print(line, end='')
        line=f.readline()


# # 2절. 피클을 이용한 객체 저장 및 불러오기
# ## 2.1 형식이 있는 텍스트 데이터

# In[16]:


with open('data/ch09_member.txt', 'r', encoding='UTF8') as f: #한글 파일 읽을 때 encoding='UTF8' 
    lines = f.readlines()
    for line in lines:
        data=line.strip().split(',')
        name=data[0]
        age=int(data[1].strip())
        email=data[2].strip()
        address=data[3].strip()
        print("이름:{}\t나이:{}\t메일:{}\t주소:{}".format(name, age, email, address))


# # 2.2 피클링

# In[17]:


class Member:
    def __init__(self, name, age, email, address):
        self.name=name
        self.age=age
        self.email=email
        self.address=address
    def __str__(self):
        return "이름:{}\t나이:{}\t메일:{}\t주소:{}".format(self.name, self.age, self.email, self.address)


# In[19]:


user1 = Member("공지철", 43, 'kong@green.com', "서울")
user2 = Member("한지민", 39, 'han@green.com', "경기도")
user3 = Member("윤여정", 72, 'yoon@green.com', '부산')
user_list = [user1, user2, user3]


# In[20]:


for user in user_list:
    print(user)


# In[22]:


with open('data/ch09_member.data', 'wb') as f:
    import pickle
    pickle.dump(user_list, f)


# In[23]:


with open('data/ch09_member.data', 'rb') as f:
    ul = pickle.load(f)


# In[24]:


for user in ul:
    print(user)


# # 3절. csv형식 파일 읽기/쓰기
# ## 3.1 reader

# In[2]:


#UTF8로 인코딩된 csv파일 read
import csv
with open('data/ch09_member1.csv', 'r', encoding='UTF8') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)


# In[8]:


#CP949(EUC-KR)로 인코딩 된 csv파일 read(ch09_member2.csv)
with open('data/ch09_member2.csv') as f:
    reader=csv.reader(f)
    for row in reader:
        print(' - '.join(row))


# In[13]:


#numeric엔 따옴표 붙이지 않기
with open('data/ch09_member1.csv', encoding='utf8') as f:
    reader=csv.reader(f, quotechar="'", quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)


# ## 3.2 writer

# In[15]:


user_list=[['공지철', 43, 'kong@green.com', '서울특별시 마포구'],
           ['한지민', 39, 'jimin@green.com', '서울특별시 서대문구']]


# In[17]:


#newline=''을 적지 않으면 개행 2번
with open('data/ch09_member3.csv', 'w', newline='', encoding='utf8') as f:
    writer=csv.writer(f)
    for user in user_list:
        writer.writerow(user)


# In[18]:


#숫자만 따옴표 없고 문자엔 따옴표 붙에 csv write
with open("data/ch09_member3-1.csv", "w", newline="", encoding="CP949") as f:
    writer=csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(user_list)


# ## 3.3 DictReader
# - csv파일의 자료를 딕셔너리 데이터로 읽기

# In[21]:


#header가 있는 csv파일을 딕셔너리로 읽기
#import csv
with open('data/ch09_member3-2.csv', 'r', encoding='UTF8') as f:
    dict_reader = csv.DictReader(f)
    #print(list(dict_reader))
    for row in dict_reader:
        print(row['이름'], row['나이'], row['이메일'], row['주소'])


# In[22]:


#header가 없는 csv파일을 딕셔너리로 읽기
with open('data/ch09_member2.csv', 'r') as f:
    dict_reader = csv.DictReader(f, fieldnames=['Name', 'Age', 'Email', 'Address'])
    for row in dict_reader:
        print(row['Name'], row['Age'], row['Email'], row['Address'])


# In[28]:


#한 행에만 팀장 표시 추가
with open('data/ch09_member2.csv', 'r', encoding='CP949') as f:
    dict_reader=csv.DictReader(f, fieldnames=['name', 'age', 'email', 'address', 'job'])
    for row in dict_reader:
        print(row['name'], row['age'], row['email'], row['address'], row['job'])


# In[30]:


#한 행에만 팀장 표시 추가(header가 없는 경우: ch09_member3.csv)
with open('data/ch09_member3.csv', 'r', encoding='UTF8') as f:
    dict_reader=csv.DictReader(f, fieldnames=['name', 'age', 'email', 'address', 'job'])
    for row in dict_reader:
        if row['job'] is None:
            print(row['name'], row['age'], row['email'], row['address'])
        else:
            print(row['name'], row['age'], row['email'], row['address'], row['job'])


# In[31]:


#한 행에 팀장 표시 추가(header가 있는 경우:ch09_member3-2.csv)
with open('data/ch09_member3-2.csv', 'r', encoding='utf8') as f:
    dict_reader=csv.DictReader(f, restval='')
    for row in dict_reader:
        print(row['이름'], row['나이'], row['이메일'], row['주소'], row['직책'])


# ## 3.4 DictWriter
# - 딕셔너리 변수의 내용을 csv파일로 쓰기

# In[32]:


user1 = {'name':'리차드', 'age':36, 'email':'richard@green.com', 'address':'시드니'}
user2 = {'name':'제니', 'age':33, 'email':'jenny@green.com', 'address':'서울'}
user3 = {'name':'지나', 'age':38, 'email':'jina@green.com', 'address':'싱가폴'}
user_list = [user1, user2, user3]
fieldnames=list(user1.keys()) #헤더로 사용: ['name', 'age', 'email', 'address']


# In[ ]:


"""
csv파일의 내용
name,age,email,address
리차드,36,richard@green.com,시드니
"""


# In[33]:


with open('data/ch09_member4.csv', 'w', encoding='utf8', newline='') as f:
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader() #header부분 write
    for user in user_list:
        dict_writer.writerow(user)


# In[36]:


user1 = {'name':'리차드', 'age':36, 'email':'richard@green.com', 'address':'시드니'}
user2 = {'name':'제니', 'age':33, 'email':'jenny@green.com', 'address':'서울', 'job':'팀장'}
user3 = {'name':'지나', 'age':38, 'email':'jina@green.com', 'address':'싱가폴'}
user_list=[user1, user2, user3]
fieldnames = list(user1.keys()) #헤더로 사용: ['name', 'age', 'email', 'address']
#fieldnames.append('job')


# In[37]:


with open('data/ch09_member4-1.csv', 'w', newline='', encoding='utf8') as f:
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames,
                                extrasaction='ignore') #fieldnames 없는 필드 무시
                                #extrasaction='raise') #fieldnames 없는 필드면 error
    dict_writer.writeheader()
    dict_writer.writerows(user_list)


# # 4절. JSON데이터 저장하고 불러오기(dump, load)
# ## 4.1 JSON dump
# <pre>
# [
#     {'location':'Seoul',
#     'time':12,
#     'temperature':2},
#     {'location':'Jeju',
#     'time':12,
#     'temperature':8}
# ]
# </pre>

# In[38]:


data = [
    {'name':'공유',
    'age':43,
     'email':'kong@green.com',
    'address':'Seoul'},
    {'name':'한지민',
    'age':39,
     'email':'han@green.com',
    'address':'Incheon'}
]


# In[39]:


data


# In[40]:


#딕셔너리 리스트를 json파일로 저장
#ensure_ascii=False; 한글이 깨질 경우 작성 필요
import json
with open('data/ch09_member1.json', 'w') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent='\t') #indent='\t'; tab 띄어쓰기


# In[41]:


#Member객체 리스트를 json파일로 저장
class Member:
    def __init__(self, name, age, email, address):
        self.name=name
        self.age=age
        self.email=email
        self.address=address
    def as_dict(self):
        return {"name":self.name, "age":self.age, "email":self.email, "address":self.address}
    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.name, self.age, self.email, self.address)


# In[42]:


member1 = Member('공지철', 43, 'kong@green.com', '서울')
member2 = Member('한지민', 39, 'han@green.com', '경기도')
member3 = Member('이지아', 43, 'jia@green.com', '제주도')
member_list = [member1, member2, member3]


# In[43]:


with open('data/ch09_member2.json', 'w', encoding='utf8') as jsonfile:
    json.dump(member_list, jsonfile, ensure_ascii=False, indent='\t', default=Member.as_dict)


# In[44]:


whos  #whos는 주석과 같이 쓸 수 없음


# In[45]:


del member1, member2, member3, member_list


# ## 4.2 JSON load

# In[46]:


with open('data/ch09_member2.json', 'r', encoding='UTF8') as jsonfile:
    member_list = json.load(jsonfile)
    for row in member_list:
        print(row)


# In[47]:


member_list


# In[48]:


type(member_list), type(member_list[0])


# In[50]:


#json파일을 객체 리스트 변수로 load()
class Member:
    def __init__(self, name, age, email, address):
        self.name=name
        self.age=age
        self.email=email
        self.address=address
    def __str__(self):
        return "{}\t{}\t{}\t{}".format(self.name, self.age, self.email, self.address)


# In[51]:


def as_member(dict):
    return Member(dict['name'], dict['age'], dict['email'], dict['address'])


# In[52]:


m1 = {'name':'리차드', 'age':36, 'email':'richard@green.com', 'address':'서울'}


# In[53]:


print(as_member(m1))


# In[55]:


with open('data/ch09_member2.json', 'r', encoding='UTF8') as jsonfile:
    member_list = json.load(jsonfile, object_hook=as_member)


# In[56]:


for member in member_list:
    print(member)


# In[57]:


type(member_list), type(member_list[0])


# # 5절. HDF5 파일 읽기/쓰기
# ## 5.1 h5py사용

# In[59]:


import seaborn as sns
iris_df = sns.load_dataset("iris")
iris_df


# In[60]:


type(iris_df)


# In[61]:


iris_dic = iris_df.to_dict() #데이터 프레임 변수를 딕셔너리 변수로
iris_dic


# In[62]:


iris_dic.keys()


# In[63]:


for group, value in iris_dic.items():
    print(group, value)


# In[64]:


for group, value in iris_dic.items():
    print('변수는', group)
    for key, data in value.items():
        print("{}:{}".format(key, data), end='\t')
    print('\n')


# In[65]:


#iris_dic을 hdf5 파일로 쓰기
import h5py
with h5py.File('data/ch09_iris.hdf5', 'w') as f:
    for group, value in iris_dic.items():
        grp = f.create_group(group)
        for key, data in value.items():
            grp.create_dataset(str(key), data=data)


# In[66]:


#iris_df를 hdf5 파일로 쓰기
iris_df.to_hdf('data/ch09_iris2.hdf5', key='iris')


# ## 5.2 pandas 라이브러리를 통해 hdf5 파일 읽어오기

# In[67]:


import pandas as pd
iris_df2 = pd.read_hdf('data/ch09_iris2.hdf5', key='iris')
iris_df2


# In[68]:


print(iris_df2)


# # 6절. 연습문제
# ## 6-1. 실습형: 고객관리 애플리케이션

# In[69]:


#필요한 클래스나 함수들 정의
class Customer:
    def __init__(self, name, phone, email, age, grade, etc):
        self.name=name
        self.phone=phone
        self.email=email
        self.age=age
        self.grade=grade
        self.etc=etc
    def as_dict(self): #csv파일 저장시 필요
        return {"grade":self.grade, "name":self.name, "phone":self.phone,
               "email":self.email, "age":self.age, "etc":self.etc}
    def to_list(self): #txt파일 저장시 필요
        temp = [self.name, self.phone, self.email, str(self.age), str(self.grade), self.etc, '\n']
        return ' '.join(temp)
    def __str__(self):
        return "{:>5}\t{:3}\t{:15}\t{:15}\t{:3}\t{}".format('*'*self.grade, self.name, 
                                                           self.phone, self.email, self.age, self.etc)


# In[70]:


#txt파일 내용: 홍길동 010-9999-9999 hong@hong.com, 30, 5, "열심히"
#txt파일의 내용을 Customer 객체로 반환
#row는 txt파일 한 줄 읽은 내용
def to_customer(row):
    data = row.strip().split(' ')
    name=data[0]
    phone=data[1]
    email=data[2]
    age=int(data[3])
    grade=int(data[4])
    etc=data[5]
    return Customer(name, phone, email, age, grade, etc)


# In[71]:


#0. 실행하면서 csutomers 파일의 내용 load
def load_customers():
    customer_list=[]
    try:
        with open('data/ch09_customers.txt', 'r', encoding='utf8') as f:
            lines=f.readlines()
            for row in lines:
                customer = to_customer(row)
                customer_list.append(customer)
            print("데이터가 로드되었습니다")
    except FileNotFoundError:
        print("데잍터 파일이 없어 초기화하였습니다")
        f = open('data/ch09_customers.txt', 'w', encoding='UTF8')
        f.write('')
        f.close()
    return customer_list


# In[72]:


#1.입력
def insert_customer_info():
    name=input('이름: ')
    phone=input('전화번호: ')
    email=input('이메일: ')
    try:
        age=int(input("나이: "))
    except ValueError as e:
        print("유효하지 않은 나이를 입력하여 나이를 0으로 초기화 함")
        age=0
    try:
        grade=int(input("고객등급(1~5): "))
        if grade<1:
            grade=1
        if grade>5:
            grade=5
    except ValueError as e:
        print("유효하지 않은 등급을 입력하여 등급은 1로 초기화 함")
        grade=1
    etc=input("기타 정보: ")
    customer = Customer(name, phone, email, age, grade, etc)
    return customer


# In[73]:


#2.전체 출력
def print_customers(customer_list):
    print("="*70)
    print("{:^70}".format("고객 정보"))
    print("-"*70)
    print("{}\t{}\t{}\t{}\t{}\t{}".format("GRADE", "이름", "전화", "메일", "나이", "기타"))
    print('='*70)
    for customer in customer_list:
        print(customer)
    print("="*70)


# In[74]:


#3. 이름으로 삭제
def delete_customer(customer_list):
    name=input("삭제할 고객 이름: ")
    delete_flag = False
    delete_idx = []
    for i, customer in enumerate(customer_list):
        #삭제할 이름과 같은 데이터의 인덱스를 delete_idx에 추가(동명이인 고려)
        if customer.name==name:
            delete_idx.append(i)
    #끝 idx부터 삭제해야함
    for i in range(len(delete_idx)-1, -1, -1):
        del customer_list[delete_idx[i]]
        delete_flag = True
    if delete_flag:
        print("\'{}\'님을 삭제하였습니다".format(name))
    else:
        print("\'{}\'님이 데이터에 존재하지 않습니다".format(name))


# In[75]:


#4. 이름으로 조회(동명이인도 모두 검색)
def search_customer(customer_list):
    name=input("조회할 고객 이름: ")
    search_result=[]
    for customer in customer_list:
        if customer.name==name:
            search_result.append(customer)
    if len(search_result)==0:
        print("데이터에 존재하지 않는 고객입니다")
    else:
        for customer in search_result:
            print(customer)


# In[76]:


#5. 내보내기(csv)
def save_customer_csv(customer_list):
    import csv
    fieldnames=['name', 'phone', 'email', 'age', 'grade', 'etc']
    customer_dict_list=[]
    for customer in customer_list:
        customer_dict_list.append(customer.as_dict())
    filename=input("저장할 파일 이름: ")
    try:
        with open('data/ch09_'+filename+'.csv', 'w', newline='', encoding='utf8') as f:
            dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
            dict_writer.writeheader()
            dict_writer.writerows(customer_dict_list)
    except Exception as e:
        print("데이터 내보내기 예외:", e)


# In[77]:


#9. 종료하기 전 txt파일로 저장
def save_customer_txt(customer_list):
    customer_text_list=[]
    for customer in customer_list:
        customer_text_list.append(customer.to_list())
    try:
        with open('data/ch09_customers.txt', 'w', encoding='utf8') as f:
            f.writelines(customer_text_list)
    except Exception as e:
        print("데이터 저장 예외:", e)


# In[ ]:


def main():
    customer_list=load_customers()
    while True:
        print("1:입력", "2:전체 출력", "3:삭제", "4:이름 조회", "5:내보내기(csv)", "9:종료", 
              sep="|", end=' ')
        try:
            menu=int(input("메뉴 선택: "))
        except ValueError as e:
            print("유효하지 않은 숫자를 입력하여 종료")
            menu=9
        if menu==1:
            customer = insert_customer_info()
            customer_list.append(customer)
        elif menu==2:
            print_customers(customer_list)
        elif menu==3:
            delete_customer(customer_list)
        elif menu==4:
            search_customer(customer_list)
        elif menu==5:
            save_customer_csv(customer_list)
        elif menu==9:
            save_customer_txt(customer_list)
            break
        


# In[85]:


if __name__=='__main__':
    main()


# In[1]:


#문제풀이형1: open()에 대해 잘못 설명한 것: 3번 -> wb로 같이 사용 가능
#문제풀이형2: pickling에 대해 잘못 설명한 것: 4번 -> 피클링을 하기 위한 모드는 wb여야 함
#문제풀이형3: 입출력 모듈에 대한 설명 중 잘못된 것: 1번 -> pandas패키지를 이용하면 데이터 프레임 데이터를 쉽게 읽고 쓸 


# In[2]:


#pandas 패키지를 이용한 csv파일 read
get_ipython().run_line_magic('ls', 'data')


# In[3]:


#ch09_member1.csv(UTF8)
#ch09_member2.csv(CP949)
import pandas as pd
members1 = pd.read_csv('data/ch09_member1.csv')
members1


# In[5]:


members1 = pd.read_csv("data/ch09_member1.csv", encoding='UTF8', #encoding='UTF8' 생략 가능
                      names=['name', 'age', 'email', 'address'], header=None)
members1


# In[6]:


members2 = pd.read_csv("data/ch09_member2.csv", encoding='CP949', #CP949생략 불가능
                      names=['Name', 'Age', 'Email', 'Address', 'Job'])
members2


# In[7]:


type(members1), type(members2) #DataFrame


# [[판다스](https://pandas.pydata.org/)] API reference, User Guide 참조

# In[ ]:




