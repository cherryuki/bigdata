#!/usr/bin/env python
# coding: utf-8

# **21-02-23 python 04_제어문 (c)cherryuki (ji)**

# **<font size=5 color="red">ch04. 제어문</font>**
# - if, for-in, while, 중첨 가능, 중첩 루프 탈출

# # 1절. 조건문

# In[1]:


score = int(input('Enter your score>'))
if score>90:
    print('참 잘했어요')
else:
    print('분발하세요')
print('점수를 입력받아 점수에 따라 메시지를 출력함')


# In[2]:


score = int(input('Enter your score > '))
if 90<= score <= 100:
    grade = 'A'
elif 80<= score < 90:
    grade = 'B'
elif 70<= score <80:
    grade = 'C'
elif 60<= score <70:
    grade = 'D'
elif 0<= score <60:
    grade = 'F'
else :
    grade= '유효하지 않은 점수'
print('입력한 점수는 {}점이고 {}등급'.format(score, grade))


# # 2절. 반복문

# ## 2.1 for-in
# - for 변수 in 나열 가능한 자료: <br>
#     반복할 문장1 <br>
#     반복할 문장2 <br>
#     ... <br>
#     else: <br>
#     변수에 값이 할당되지 않을 경우 한 번 실행할 문장 
# - else 구문은 선택사항

# In[4]:


for i in range(1,10,2):
    print(i, end='\t')
else:
    print('Done')


# ## 2.2 while
# - while 조건: <br>
#     반복할 문장1 <br>
#     반복할 문장2 <br>
#     ... <br>
#   else: <br>
#     조건이 거짓일 경우 한 번 실행할 문장
# - else구문은 선택사항
# - 무한 반복문에 빠지지 않도록 조건식 결과가 바뀔 수 있는 변수값을 수정하는 코드 필

# In[5]:


i = 0
while i<10:
    print(i, end='\t')
    i += 1 #조건식 결과가 바뀔 수 있는 변수값 수정하는 코드
else:
    print()
    print('i값이 {}이므로 종료'.format(i))


# In[6]:


#1~100까지 짝수의 합
sum = 0
i = 1
while i<=100:
    if i%2==0:
        sum += i
    i+=1
else:
    print("1~100까지 짝수의 합:", sum)


# ## 2.3 break&continue
# - break를 만나면 break를 포함하는 반복문을 완전히 탈출
# - continue는 반복문 내에서 continue 이후의 문장을 건너 뜀

# In[7]:


num = 0
while num<=10:
    num += 1
    if num==5:
        break #현재 반복문 빠져나감
    print(num, end=' ')


# In[8]:


num = 0
while num<=10:
    num += 1
    if num==5:
        continue #반복문의 조건으로 감
    print(num, end=' ')


# In[9]:


#숫자 찾기 게임
'''
1~100사이의 숫자를 맞추는 프로그램을 작성
(프로그램 안에서 임의의 숫자가 생성되고, 
입력한 숫자와 비교하여 숫자를 맞출 때까지 up, down 출력)
'''
import random
#random.seed(1) #난수 발생 고정
random.randint(1, 100) #1~100사이 임의 숫자 생성


# In[12]:


min = 1
max = 100
random_num = random.randint(min, max)
num=0
while num!=random_num:
    num = int(input('숫자: '))
    if num>random_num:
        print('down')
    elif num<random_num:
        print('up')
    else:
        print('맞추셨습니다')


# In[13]:


min = 1
max = 100
random_num = random.randint(min, max)
while True:
    print(min, '~', max, '사이의 컴퓨터가 선택한 수를 맞춰보세요: ')
    num=int(input())
    if random_num < num:
        max=num-1
        print('당신이 입력한 수보다 작은 수입니다')
    elif random_num > num:
        min=num+1
        print('당신이 입력한 수보다 큰 수입니다')
    else:
        print("축하합니다")
        break;


# # 3절. 중첩루프; 반복문 안에 반복문
# - 2차원 이상의 데이터 구조의 모든 항목들을 처리하기 위해 사용

# In[14]:


list_2d = [[1,2,3,4,5],
          [10,20,30,40],
          [11,22,33,44]]
print(list_2d)


# In[15]:


for i in range(len(list_2d)):
    for j in range(len(list_2d[i])):
        print("{}행{}열: {}".format(i, j, list_2d[i][j]), end='\t')
    print()


# In[16]:


for i, row in enumerate(list_2d):
    for j, data in enumerate(row):
        print("{}행{}열: {}".format(i,j,data), end='\t')
    print()


# In[21]:


#2~9단까지 구구단 전체 출력
'''
2*1=2  3*1=3  4*1=4  ... 9*1=9
2*2=4  3*2=6  4*2=8  ... 9*2=18
...
2*9=18 3*9=27 4*9=36 ... 9*9=81
'''
for i in range(1,10):
    for j in range(2,10):
        print("{}*{}={}".format(j,i, i*j), end='\t')
    print()
print()
for i in range(1,10):
    for j in range(2,10):
        print("{}x{}={:2}".format(j, i, j*i), end='\t') #자릿수 지정하면 숫자는 오른쪽 정렬
    print()


# # 4절. 중첩루프 탈출

# In[31]:


#아래 예제에서 break는 안쪽 반복문을 빠져나옴
for a in range(0,3):          #a=0,1,2
    for b in range(1,3):      #b=1,2
        if a==b:
            break;
        print(a,b)


# ## 4.1 플래그를 이용한 중첩루프 탈출

# In[32]:


#braek를 만나면 바깥쪽 반복문까지 탈출하는 방법1. 플래그 이용
break_out_flag=False
for a in range(0,3):
    for b in range(1,3):
        if a==b:
            break_out_flag=True
            break
        print(a,b)
    if break_out_flag:
        break


# ## 4.2 예외처리를 이용한 중첩루프 탈출

# In[33]:


#braek를 만나면 바깥쪽 반복문까지 탈출하는 방법2. Exception 이용
class BreakOutLoop(Exception): pass

for a in range(0,3):
    try:
        for b in range(1,3):
            if a==b:
                raise BreakOutLoop
            print(a,b)
    except BreakOutLoop:
        break


# In[34]:


try:
    for a in range(0,3):
        for b in range(1,3):
            if a==b:
                raise BreakOutLoop
            print(a,b)
except BreakOutLoop:
    pass #pass: 아무일도 하지 않음


# # 5. 연습문제

# In[36]:


#1. 양의 정수를 입력 받아 홀수인지 짝수인지를 판별하는 프로그램을 작성하세요. 양의 정수가 아니면 숫자를 다시 입력 받아야 합니다.
num = 1
while True:
    num = int(input('양의 정수를 입력하세요'))
    if num <= 0:
        continue
    elif num%2==1:
        print('입력하신 수는 홀수입니다')
    else:
        print('입력하신 수는 짝수입니다')
        break


# In[38]:


#2. 1~50까지 자연수 중 3의 배수의 총합을 출력하는 프로그램을 작성하세요
sum=0
for i in range(1,51):
    if i%3==0:
        sum += i
else:
    print('1~50까지 자연수 중 3의 배수의 총합:', sum)
    
i=0
sum=0
while i<=50:
    if i%3==0:
        sum += i
    i += 1
else:
    print("1~50까지 자연수 중 3의 배수의 총합:", sum)


# In[56]:


#3. 아래 패턴의 별을 출력하는 프로그램을 작성하세요.
print('a')
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
print('b')
for i in range(1,6):
    print('{}'.format('*'*i))
print('c')
for i in range(5,0,-1):
    print('{}'.format('*'*i))
print('d')
for i in range(1,6):
    print('{:>5}'.format('*'*i))
print('e')
for i in range(5,0,-1):
    print('{:>5}'.format('*'*i))


# In[57]:


#1. 다음 코드는 1부터 30까지(30포함) 자연수 중에서 3의 배수의 총 합을 출력하는 프로그램입니다. 빈칸의 코드를 완성하시오.
sum = 0
for i in range(1,31):
    if i%3==0:
        sum=sum+i
    else:
        pass
print(sum)


# In[59]:


#2. 다음 코드의 실행결과가 “1 3 5 7 9”가 되도록 빈칸을 완성하시오
num = 0
while num <=10:
    if num%2==1:
        print(num, end=' ')
    num += 1


# In[60]:


#3. 다음 2차원 리스트의 모든 값을 출력하는 코드입니다. 빈칸을 완성하시오.
list2d=[[1,2,3],[4,5,6,7],[8,9]]
for row in list2d:
    for data in row:
        print(data, end=' ')
    print()


# In[61]:


#4. 다음 빈칸에 들어갈 함수 이름은?
colors={"red":'apple', "yellow":'banana'}
for i, v in enumerate(colors.values()):
    print(i,v)


# In[62]:


#5.  다음 코드의 실행결과는?
for i in range(0,2):
    for j in range(0,2):
        if i==j:
            break
        print(i,j)


# In[63]:


#6. 다음 코드의 실행 결과로 출력될 수 없는 것은?   #0, 1
for i in range(0,2):
    for j in range(0,2):
        print(i, j)
        if i==j:
            break


# In[64]:


#7. 다음 코드의 실행 결과는?
L = [3,4,5,6,7,8,9,10]
for i, data in enumerate(L):
    if(i%2==0):
        print(data, end=' ')

