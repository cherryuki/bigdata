#!/usr/bin/env python
# coding: utf-8

# **21-02-23 python 03_자료형과 연산자 (c)cherryuki (ji)**

# <font size="5" color="red"><b>ch03. 데이터 구조</b></font>

# # 1절. 리스트

# ## 1.1 리스트 생성
# - []를 이용해서 생성, 여러개 값을 하나의 변수에 저장, 관리할 수 있음(list()함수로도 리스트 생성 가능)
# - index: 각 요소의 위치 (첫 인덱스:0, 마지막 인덱스:-1)
# - 슬라이싱: 부분 데이터셋을 추출하는 것. 인덱스를 이용해서 쓰기와 읽기 가능

# In[1]:


fruits = ['banana', 'apple', 'orange', 'grape']
type(fruits)


# In[2]:


print(fruits)


# In[3]:


print(fruits[0])


# In[4]:


for fruit in fruits:
    print(fruit)


# In[5]:


#range(from, to, by); from부터 to 바로 앞까지 by씩 증가되면서 만들어진 list
    #from 생략시 0부터, by 생략시 1씩 증가
list(range(6))


# In[6]:


list(range(0, 10, 2))


# In[7]:


list(range(10, -1, -2))


# In[8]:


for i in range(5):
    print(i, end='\t')


# In[9]:


#0번째: banana, ... len(fruits): fruits 요소의 개수
for idx in range(len(fruits)):
    print('{}번째: {}'.format(idx, fruits[idx]))


# In[10]:


numbers=[1,2,3,True,'5']
numbers


# - 1차원 리스트: 변수명 = []
# - 2차원 리스트: 변수명 = [[], ...]
# - []안에 []를 넣으면 차원이 증가

# In[11]:


#2차원 리스트: 리스트 안에 리스트
#[]안에 []를 넣으면 차원이 증가
numbers_2d = [[1,2,3,4,5],
              [10,20,30,40,50],
              [1,3,5,7,9],
              [2,4,6,8,10]]
print(numbers_2d)


# In[12]:


numbers_2d[1][0]


# In[14]:


for row in numbers_2d:
    for data in row:
        print(data, end='\t')
    print() #개행


# In[16]:


for i in range(len(numbers_2d)):
    for j in range(len(numbers_2d[i])):
        print('{}행{}열: {:>2}'.format(i, j, numbers_2d[i][j]), end='\t')
    print()


# ## 1.2 기본정보 조회

# In[17]:


numbers=[1,2,3,4,5]
numbers_2d = [[100,2,3,4,5],
              [10,20,30,40,50],
              [1,3,5,7,9],
              [2,4,6,8,10]]


# In[18]:


#요소 수
print('numbers의 요소수:', len(numbers))
print('numbers_2d의 요소수:', len(numbers_2d))


# In[19]:


print('numbers_2d[0]의 요소 수:', len(numbers_2d[0]))


# In[20]:


#최소값 min, 최대값 max
min(numbers), max(numbers)


# In[21]:


#2차원 리스트에서 mxa()함수는 부분 리스트 중 첫 요소가 가장 큰 값을 갖는 리스트를 반환
#min()함수는 부분 리스트 중 첫 요소가 가장 작은 값을 갖는 리스트를 반환
min(numbers_2d), max(numbers_2d)


# ## 1.3 요소(데이터) 추가
# - +; 두 리스트를 연결
# - *; 리스트를 곱한 수 만큼 반복
# - append(); 요소를 맨 뒤에 추가
# - extend(); 리스트를 요소별로 맨 뒤에 추가
# - insert(index, data); 지정된 index 위치에 삽입

# In[22]:


numbers=[1,2,3,4,5]
numbers = numbers+numbers #리스트 연결
numbers


# In[23]:


numbers=[1,2,3]
print(numbers*3) #리스트 반복


# In[24]:


print('ABC'*3)


# In[25]:


#append() 함수 이용
numbers=[1,2,3]
numbers.append(4) #요소 맨 뒤에 추가
numbers


# In[26]:


#extend()함수 이용
numbers=[1,2,3]
num = [4,5,6]
numbers.extend(num)
numbers


# In[28]:


numbers.extend([7])
numbers


# In[29]:


numbers.extend('Hello')
numbers


# In[30]:


#insert(idx, 추가할 데이터); idx번째 인덱스에 추가할 데이터 삽입
numbers=[1,2,3,4,5]
numbers.insert(1, 'xx')
numbers


# ## 1.4 인덱싱
# - count(); 리스트에서 데이터의 개수 반환
# - index(); 해당 요소의 첫번째 위치 반환
# - index(a, b); a번째 인덱스 이후부터 처음나오는 b의 인덱스 반환
# - [index]; 인덱스를 이용한 접근

# In[31]:


numbers=[1,2,3,[1,2,3],1,2,3]
numbers_2d = [[1,2,3], [1,2,3]]
print(numbers)
print(numbers_2d)


# In[32]:


numbers.count(2)


# In[33]:


numbers.count(9)


# In[34]:


numbers.count([1,2,3])


# In[35]:


numbers_2d.count([1,2,3])


# In[36]:


#0번째 인덱스부터 처음 나오는 2의 인덱스
numbers.index(2)


# In[37]:


#4번째 인덱스 이후부터 처음 나오는 2의 인덱스
numbers.index(2,4)


# In[38]:


print(numbers.count(9)) #없으면 0 반환
print(numbers.index(9)) #index함수는 없는 값을 찾으면 에러 발생


# In[39]:


len(numbers)


# In[40]:


numbers[7] #인덱스의 범위를 벗어나면 에러 발생


# ## 1.5 원하는 리스트 내용만 추출; 리스트 슬라이싱 - 인덱스보다 많이 사용
# - [from:to:by]; from부터 to 바로 앞까지 by씩 증가하는 index 아이템 추출
# - from, to, by 생략 가능. 음수 인덱스 가능(맨 처음:0, 맨 마지막:-1)

# In[41]:


numbers=[1,2,3,4,5]
numbers[2:9] #2번째부터 9번 인덱스 바로 앞까지(해당 인덱스가 없을 경우 끝까지)


# In[42]:


numbers[::-1] #거꾸로


# In[43]:


numbers[::]


# In[44]:


numbers[-5:-1]


# In[45]:


numbers[-1:-5] #-1부터 -5 바로 전까지 by(1)씩 인덱스를 전진하며 액세스 = []


# In[46]:


numbers_2d=[[1,2,3], [10,20,30], [11,12,13], [21,22,23]]
numbers_2d[1:3]


# In[47]:


numbers_2d[0][1:3]


# In[48]:


#람다식을 이용해서 list의 원하는 데이터 액세스
numbers=[1,3,5,9,10,12,13,18,19,20,7]
#모든 데이터 가져오기
#for data in numbers:
#    print(data)
[data for data in numbers]


# In[49]:


#짝수 데이터만 가져오기
for x in numbers:
    if x%2==0:
        print(x)
[x for x in numbers if x%2==0]


# In[50]:


#10이상의 데이터만 가져오기
[x for x in numbers if x>=10]


# In[52]:


#과일의 글씨가 5글자 이상인 과일만 추출
fruits = ['orange', 'apple', 'mango', 'kiwi']
[f for f in fruits if len(f)>=5]


# In[53]:


#리스트의 세제곱을 추출하라
L=[1,2,3,4,5]
[l**3 for l in L ]


# In[54]:


#리스트 값의 2배 수를 추출하라
L=[1,2,3,4,5]
[l*2 for l in L]


# ## 1.6 요소 수정하기; 인덱싱으로 데이터 수정
# - 지정한 인덱스 위치의 데이터를 다른 데이터로 바꿈
# - 지정한 범위의 리스트 항목을 다른 항목들로 통째로 바꿈(슬라이싱으로 데이터 수정)
# - 바꾸려는 항목이 더 많거나 더 적어도 일괄적으로 변경 가능

# In[55]:


numbers = [0,1,2,3,4,5,6,7,8,9]
numbers


# In[56]:


numbers[2] = 222
numbers


# In[57]:


#부분리스트를 통째로 바꿈(by없이 슬라이싱)
numbers[0:5] = [999, 999, 999]
numbers


# In[58]:


numbers[0:5] = [1,1,1,1,1,1,1]
numbers


# In[59]:


numbers = [0,1,2,3,4,5,6,7,8,9]
numbers[0:5] = numbers[5:] #0번째부터 5번 바로 앞까지의 값을 5번째 이후 값으로 대체
numbers


# In[60]:


#슬라이싱에서 by가 포함될 경우 1:!매핑되므로 데이터의 개수가 일치해야 함
numbers=[0]*10
print('수정전:', numbers)
numbers[::2]=[1,1,1,1,1] #by가 있을 경우 하나씩 매핑되므로 수의 개수 일치해야 함
print('수정후:', numbers)


# ## 1.7 삭제하기
# - pop(); 가장 마지막 요소 반환 및 삭제
# - pop(n); n번째 요소 반환 및 삭제
# - remove(data); 해당 데이터가 삭제
# - del xx[n]; 지정한 위치 항목 삭제, 변수 삭제
# - clear(); 모든 항목 삭제 (결과: []) #del 변수[:]와 동일한 결과

# In[61]:


numbers=[0,1,2,3,4,5,6,7,8,9]
print(numbers)
print(numbers.pop())
print(numbers)


# In[62]:


print(numbers.pop(2))
print(numbers)


# In[63]:


numbers_2d=[[1,2,3],[10,20,30],[100,100,100]]
print('pop전:', numbers_2d)
print(numbers_2d.pop())
print('pop후:', numbers_2d)


# In[64]:


numbers_2d=[[1,2,3],[10,20,30],[100,110,120]]
print(numbers_2d[2].pop())
print(numbers_2d)


# In[67]:


numbers=[0,1,2,3,4,5,6,7,8,9]
print(numbers.remove(4)) #remove는 반환값 없음: None
print(numbers)


# In[68]:


numbers.remove(999) #없는 데이터를 remove할 경우 error


# In[69]:


print(numbers)
del numbers[2] #지정 위치 항목 삭제
print(numbers)


# In[70]:


del numbers #변수 삭제
print(numbers) #변수 삭제되었으므로 찾을 수 없음(에러)


# In[71]:


numbers=[0,1,2,3,4]
del numbers[:] #clear()와 동일한 결과
numbers #빈 리스트만 남음: []


# In[72]:


numbers=[0,1,2,3,4]
print('clear전:', numbers)
numbers.clear() #del numbers[:]와 동일
print('clear후:', numbers)


# ## 1.8 정렬
# - sort(); 기본 오름차순 정렬(reverse=True: 내림차순 정렬)
# - reverse(); 역순으로 나열
# - [::-1]; 역순으로 출력
# - sort(), reverse()는 원본 데이터를 변경, [::-1]은 원본 데이터 변경X

# In[73]:


numbers=[6,2,7,10,4,5,8,3,9,1]
numbers.sort() #오름차순 정렬. sort()실행 후 리스트 바뀜
numbers


# In[74]:


numbers=[6,2,7,10,4,5,8,3,9,1]
numbers.sort(reverse=True) #내림차순 정렬, sort()실행 후 리스트 바뀜
numbers


# In[75]:


numbers=[6,2,7,10,4,5,8,3,9,1]
print(numbers[::-1]) #역순 출력, 리스트 순서 변경X
print(numbers)


# In[76]:


numbers=[0,1,2,3,4,5,6,7]
numbers.reverse() #리스트를 역순으로 나열, reverse()실행 후 리스트 바뀜
numbers


# In[77]:


numbers=[0,1,2,3,4,5,6,7]
numbers = numbers[::-1] #reverse()함수와 같은 명령
numbers


# ## 1.9 리스트 복제
# - =; 주소를 복사해 같은 객체를 참조(둘 중에 하나를 변경하면 다른 것도 변경)
# - copy(); 복제된 새로운 객체를 생성(주소값이 다름)

# In[78]:


numbers=[5,3,7,1,0,2]
old_numbers = numbers #numbers에 있는 주소 값이 old_numbers로(같은 주소)
numbers.sort() #numbers: 오름차순 정렬된 데이터
print('old_numbers:', old_numbers)
print('numbers(정렬 후):', numbers)
print('old_numbers 주소:', id(old_numbers))
print('numbers주소:', id(numbers))


# In[79]:


#복제
numbers=[5,3,7,1,0,2]
new_numbers = numbers.copy() #new_numbers에 numbers 데이터를 복제(다른 주소)
numbers.sort() #numbers: 오름차순 정렬된 데이터
print('정렬 전:', new_numbers)
print('정렬 후:', numbers)
print('new_numbers 주소:', id(new_numbers))
print('numbers주소:', id(numbers))


# In[80]:


city = ['서울', '부산', '대구', '대전', '광주', '울산']
city.sort()
city


# In[81]:


' '.join(city)


# # 2절. 튜플
# - 리스트와 유사하지만, 읽기 전용으로 수정이 필요없는 데이터 타입에서 사용
# - 튜플에 데이터 추가, 수정, 삭제 불가(제공되는 함수도 많지 않음)
# - ()이용해서 생성

# In[82]:


city = ('서울', '부산', '대전', '대구', '광주')
type(city)


# In[83]:


'-'.join(city)


# In[84]:


l = ['서울'] #요소가 하나 있는 리스트
print(type(l))
print(l)


# In[88]:


t = ('서울') #()안에 요소를 하나만 넣으면 튜블이 아닌 문자로 인식
print(type(t)) #str
print(t)
print(len(t)) #2


# In[87]:


t = ('서울',) #요소가 하나 있는 튜플 만들 때는 , 필요(t='서울', 과 동일)
print(type(t)) #tupple
print(t)
print(len(t)) #1


# In[89]:


numbers=1,2,3 #여러개 값이 나열될 때 자동적으로 튜플로 처리
type(numbers)


# In[90]:


numbers.remove(2) #수정 불가능(에러)


# In[91]:


min(numbers), max(numbers), len(numbers)


# In[92]:


numbers=(1,2,1,2,3)
numbers.count(2)


# In[93]:


numbers.index(1) #'1'의 첫번째 인덱스 반환. 없는 값이면 에러 발생


# In[94]:


data=(0,1,2,3,4,(5,6))
data[2:5]


# In[95]:


data[::-1]


# In[96]:


data[5:9:2]


# In[97]:


data[-1:-5:-1]


# In[98]:


data=((1,2,30),(10,0,0))
max(data), min(data) #첫번째 요소만 비교


# In[99]:


len(data)


# In[100]:


data=(1,2,3)
data+data


# In[101]:


data=('서울', 2, True)
data*3


# In[102]:


del data #튜플 데이터(요소)를 지정해서 지우는 것은 불가능 하나 변수 삭제는 가능


# # 3절. 딕셔너리
# - 중괄호{}를 이용해서 딕셔너리 생성
# - 키(key)와 값(value)의 쌍으로 구성된 자료구조(cf. 자바 hashmap과 유사)
# - 키는 유일한 값(중복허용X), 키에 리스트는 사용 불가(튜플은 사용 가능)
# - 값은 중복 가능하며 모든 데이터 타입 가능
# - 없는 키의 값을 참조시 에러 발생
# - 인덱스를 이용한 데이터 참조는 불가능

# In[103]:


dic = {'key1':'value', 'key2':'value'}
dic


# In[104]:


len(dic) #데이터 구조의 요소 개수:2


# In[105]:


my_favorite = {'fruit':'apple', 'number':1, 'sport':'golf'}
my_favorite['fruit'] #인덱스를 이용한 참조는 불가능:my_favorite[0]


# In[106]:


my_favorite.get('fruit')


# In[107]:


my_favorite['fruit']='strawberry'
my_favorite


# In[108]:


#키: 문자, 숫자, 튜플 (중복 불가)
#값: 모든 문자 타입 (중복 허용)
my_dic1 = {1:'Hello', 2:'World', 1:'Python'}
my_dic1 #가장 마지막 요소로 적용됨


# In[109]:


my_dic1['people'] = ['공유', '한지민'] #my_dic1에 요소 추가
#my_dic1.append({'people':['공유', '한지민']}) 불가능
my_dic1['study'] = ['python', 'hadoop'] #추가
my_dic1[1]='Hi' #수정
my_dic1


# In[110]:


del my_dic1['study']
my_dic1


# In[111]:


my_dic2 = {'name':'Kong', 'name':'Yoo', 'age':43}
my_dic2


# In[112]:


#키 목록의 True는 1, False는 0과 같은 값으로 간주
my_dic3 = {1:'Hello', True:'World', False:'Python', 0:'Hadoop'}
my_dic3


# In[113]:


my_dic3[True] #True=1로 간주 됨


# In[114]:


my_list=['Kong', 23, '010-0000-0000']
my_tupple = ('Kong', 23, '010-0000-0000')


# In[115]:


for data in my_list:
    print(data, end='\t')
print()
for data in my_tupple:
    print(data, end='\t')
print()
for idx in range(len(my_list)):
    print('{}번째: {}'.format(idx, my_list[idx]), end='\t')
print()
for idx in range(len(my_tupple)):
    print('{}번째: {}'.format(idx, my_tupple[idx]), end='\t')


# In[116]:


my_dic = {'name':'Kong', 'age':23, 'tel':'010-0000-00000'}
for key in my_dic:
    print('{}:{}'.format(key, my_dic[key]), end='\t')


# In[117]:


my_dic.keys() #키 목록 반환


# In[118]:


my_dic.values() #값들만 반환


# In[119]:


my_dic.items() #튜플로 이루어진 (키, 값)들을 반환


# In[120]:


for item in my_dic.items():
    print(item, end='\t')


# In[121]:


for key, value in my_dic.items():
    print("{}:{}".format(key, value), end='\t')


# **in 연산자**; key가 있는지 여부를 리턴

# In[122]:


my_favorite = {'fruit':'apple', 'number':1, 'sport':'golf'}
'golf' in my_favorite 


# In[123]:


'sport' in my_favorite


# - 할당과 복제

# In[124]:


#할당
my_favorite
new_my_favorite = my_favorite #할당(주소 복사)
print('new_my_favorite:', new_my_favorite)
print('my_favorite:', my_favorite)


# In[125]:


my_favorite['number'] = '다 좋아'
print('new_my_favorite:', new_my_favorite)
print('my_favorite:', my_favorite)
print('new_my_favorite 주소:', id(new_my_favorite))
print('my_favorite 주소:', id(my_favorite))


# In[126]:


#복제
my_favorite = {'fruit':'apple', 'number':1, 'sport':'golf'}
new_my_favorite = my_favorite.copy() #복제
print('new_my_favorite:', new_my_favorite)
print('my_favorite:', my_favorite)


# In[127]:


my_favorite['number'] = '다 좋아'
print('new_my_favorite:', new_my_favorite)
print('my_favorite:', my_favorite)
print('new_my_favorite 주소:', id(new_my_favorite))
print('my_favorite 주소:', id(my_favorite))


# # 4절. 셋
# - 중복을 허용하지 않는 집합(순서X, 인덱스를 통한 접근 불가)
# - {}나 set()함수를 이용하여 생성
# <br> - set(딕셔너리 타입의 변수); 딕셔너리 변수의 키만 셋에 추가
# - 집합 연산자(&:교집합, |:합집합, -:차집합)

# In[129]:


fruits = {'apple', 'orange', 'banana', 'apple', 'melon'}
fruits #중복허용X 중복된 데이터 하나만 남음


# In[130]:


s1 = set([1,2,3,1])
s1


# In[131]:


s1.add(4)
s1.add(1)
s1


# In[132]:


s1.add((5,6,7)) #튜플 자체가 추가됨(add 함수는 리스트나 딕셔너리 타입은 불가능)
s1


# In[133]:


s1={1,2,3,4}
s1.update([5,6,7,8,9]) #요소로 하나씩 추가됨
s1


# In[134]:


s1.update({'name':'Kong'}) #딕셔너리는 key만 추가됨
s1


# In[135]:


s1.remove('name') #특정 요소만 삭제 가능(없는 요소일 경우 에러)
s1


# In[136]:


s1 = {0, False, True, 1} #False와 0, True와 1은 같은 값으로 간주
s1


# In[137]:


s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}
s1, s2


# In[138]:


#합집합
s1 | s2


# In[139]:


#교집합
s1 & s2


# In[140]:


#차집합
s1-s2


# # 5절. enumerate
# - 반복자(iterator) 또는 순서(sequence) 객체로 반복문 사용시 인덱스 처리 지원
# - enumerate(객체) 사용: 객체를 (0, 객체[0]), (1, 객체[1]), ... 형식으로 반환

# In[141]:


names = {'jimin', 'jia', 'yoo'}
for name in names:
    print(name, end='\t')


# In[142]:


list(enumerate(names))


# In[143]:


#셋에 사용
for index, name in enumerate(names):
    print("{}번째: {}".format(index, name))


# In[144]:


#리스트에 사용시
L = ['kong', 'han', 'lee']
for idx in range(len(L)):
    print("{}번째 이름: {}".format(idx, L[idx]))
print()
for idx, data in enumerate(L):
    print("{}번째 이름: {}".format(idx, data))
print()


# In[145]:


#딕셔너리에 사용
dic = {"name":"Kong", "age":43, "address":"Seoul"}
for idx, key in enumerate(dic):
    print("{}번째: {}은 {}".format(idx, key, dic[key]))
print()


# In[147]:


#딕셔너리에 사용. items()함수 사용시
list(enumerate(dic.items()))
for idx, (key, value) in enumerate(dic.items()):
    print("{}번째: {}은 {}".format(idx, key, value))


# In[148]:


numbers_2d = [[1,2,3,4,5], [10,20,30,40], [1,3,5], [2,]]
len(numbers_2d[3])


# In[150]:


numbers=[0,1,2,3,4,5,6,7,8,9]
numbers[::2]=numbers[5:]
print(numbers)


# # 연습문제

# In[157]:


numbers= [1,2,3,4,5,6,7,8,9,10]


# In[158]:


#1. 숫자100을 맨 뒤에 추가하세요
numbers.append(100)
numbers


# In[159]:


#2. 다음 리스트를 numbers리스트 맨 뒤에 추가하세요 data = [200, 300, 400, 500]
data = [200,300,400,500]
numbers.append(data)
#numbers.extend(data) #리스트 요소를 추가할 경우
numbers


# In[160]:


#3.처음 다섯 개 숫자만 출력하세요
numbers[:5]


# In[161]:


#4. 리스트에서 짝수 번째 데이터만 출력하세요
numbers[::2]


# In[162]:


#5. 짝수번째 데이터를 모두 0으로 바꾸세요
numbers[::2] = [0]*len(numbers[::2])
numbers


# In[163]:


#6. 데이터를 역순으로 나열(내림차순 정렬X)
print(numbers[::-1])
numbers.reverse()
numbers


# In[164]:


member_info = {"name":"홍길동", "age":20, "address":"서울시 마포구","score":90}


# In[165]:


#7. address값을 출력하세요
member_info['address']


# In[166]:


#8. score를 출력하고 memeber_info 딕셔너리에서 삭제하세요
member_info.pop('score')


# In[168]:


member_info


# In[169]:


member_info['address']='서울시 서대문구'
member_info


# In[172]:


for key in member_info:
    print('key:{}, value:{}'.format(key, member_info[key]))
print()
for idx, key in enumerate(member_info):
    print('{}번째: {}은 {}'.format(idx, key, member_info[key]))
print()
for idx, (key, value) in enumerate(member_info.items()):
    print('{}번째: {}은 {}'.format(idx, key, value))


# In[173]:


#객관식 연습문제
L1 = ("orange", "apple", "banana", "kiwi")
new_list=[i for i in L1 if len(i)>5]
print(new_list)


# In[174]:


print(list(range(10)))
print(list(range(5, 10)))
print(list(range(10,0,-1)))
print(list(range(10,20,2)))


# In[175]:


numbers_2d = [[1,2,3,4,5], [10,20,30,40], [1,3,5], [2,]]
len(numbers_2d[3])


# In[176]:


numbers=[1,2,3,4,5]
numbers.extend([10,20,30,40,50])
numbers


# In[177]:


numbers=list(range(10))
numbers[::2]=[0]*len(numbers[::2])
print(numbers)


# In[178]:


numbers=[0,1,2,3,4,5,6,7,8,9]
numbers[::2] = numbers[5:]
print(numbers)


# In[181]:


my_dic={"a":10, "b":20, "c":30}
print(my_dic['a'])
print(list(my_dic.items())[0][1])
print(list(my_dic.values())[0])
print(my_dic.get('a'))

