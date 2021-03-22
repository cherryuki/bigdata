#!/usr/bin/env python
# coding: utf-8

# **21-03-22 ML_DL 05_tensorflow ver1_머신러닝 (c)cherryuki (ji)**

# # 05. 머신러닝 with tensorflow
# ## 1. tensroflow ver2.x에서 ver1 사용하기

# In[1]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
#ver1로 사용하기


# In[2]:


#tensor=data(상수, 변수) 연산
#node1 상수 tensor 선언
node1 = tf.constant('Hello, TensorFlow')
#graph(computational graph 생성)
sess = tf.Session()
#print(node1)
print(sess.run(node1)) #b가 의미하는 것: byte literals
#https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal 
print(sess.run(node1).decode())


# In[3]:


#간단한 수학연산 수행(computation graph)
node1 = tf.constant(10, dtype=tf.float32)
node2 = tf.constant(20, dtype=tf.float32)
#node3 = node1+node2
node3 = tf.add(node1, node2)
#computational graph실행
sess = tf.Session()
print(sess.run([node1, node2, node3]))


# ### Tensorflow
# <ol>
#     <li>그래프 정의</li>
#     <li>sess = tf.Session()을 실행</li>
#     <li>sess.run()을 통해 값을 확인할 수 있음</li>
# </ol>

# In[4]:


import numpy as np
node1 = tf.constant(np.array([1,2,3]), dtype=tf.int16)
node2 = tf.cast(node1, dtype=tf.float32)
sess = tf.Session()
print(sess.run(node1))
print(sess.run(node2))


# In[5]:


data = [1., 2., 3., 4.]
m = tf.reduce_mean(data) #reduce_mean(); 평균값 연산
sess = tf.Session()
print(sess.run(m))


# ## 2. tensorflow ver1을 이용한 linear regression을 구현
# - 독립변수 x가 1개

# In[7]:


#tensro graph 정의

#train data set
#x = np.array([1,2,3])
#y = np.array([1,2,3])
x = [1,2,3]
y = [1,2,3]

#Weight & bias(처음에는 랜덤값을 세팅했다가 학습과정에서 변경)
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#Hypothesis(가설)
H = W*x+b

#Cost function(최소 제곱법)
cost = tf.reduce_mean(tf.square(H-y))

#cost function minimize(목적: cost함수가 최소가 되는 W와 b를 찾는 것)
'''
cost함수는 제곱의 평균인 2차 함수이므로 곡선. 곡선 위의 미분값이 줄어드는 방향으로 학습
'''
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

#Session; runnder 생성
sess = tf.Session()

#Variable 노드 초기화
sess.run(tf.global_variables_initializer())

#6000번 학습(tensorflow ver2. fit()함수)
"""
for step in range(1,6001):
    sess.run(train)
    if step%300 == 0:
        print("{:4d}번째 cost:{}, W:{}, b:{}".format(step, sess.run(cost), 
                                                sess.run(W), sess.run(b)))
"""
for step in range(1, 6001):
    _, cost_val, W_val, b_val = sess.run([train, cost, W, b])
    if step%200==0:
        print("{:4d}번째 cost:{}, W:{}, b:{}".format(step, cost_val, W_val, b_val))


# In[8]:


sess.run([W, b])


# In[9]:


W_, b_ = sess.run([W,b])


# In[10]:


print("최종적으로 나온 회귀식: H = {}*x+{}".format(W_[0], b_[0]))


# In[12]:


x = [1,2,3]
y = [1,2,3]

#Weight & bias(처음에는 랜덤값을 세팅했다가 학습과정에서 변경)
W = tf.Variable(100.0, name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#Hypothesis(가설)
H = W*x+b

#Cost function(최소 제곱법)
cost = tf.reduce_mean(tf.square(H-y))

#cost function minimize(목적: cost함수가 최소가 되는 W와 b를 찾는 것)
'''
cost함수는 제곱의 평균인 2차 함수이므로 곡선. 곡선 위의 미분값이 줄어드는 방향으로 학습
'''
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

#Session; runnder 생성
sess = tf.Session()

#Variable 노드 초기화
sess.run(tf.global_variables_initializer())

#4000번 학습(tensorflow ver2. fit()함수)
for step in range(1, 4001):
    cost_val, W_val, b_val = sess.run([cost, W, b])
    if step%200==1:
        print("{:4d}번째 cost:{}, W:{}, b:{}".format(step, cost_val, W_val, b_val))
    sess.run(train)


# ## 2.1 predict를 하기 위한 placeholder 노드

# In[13]:


#placeholder 이용
a = tf.placeholder(dtype=tf.float32)
b = tf.placeholder(tf.float32)
#ab = tf.add(a+b)
ab = a+b
sess = tf.Session()
sess.run(ab, feed_dict={a:10, b:20})


# In[14]:


sess.run(ab, feed_dict={a:[1,2,3], b:[10,10,10]})


# In[15]:


sess.run(ab, feed_dict={a:np.array([1,2,3]),
                       b:np.array([10,10,10])})


# In[17]:


#그래프 실행단계에서 값을 던져줌
node1 = tf.placeholder(tf.float32)
node2 = tf.placeholder(tf.float32)
adder_node = node1+node2
sess = tf.Session()
result = sess.run(adder_node, feed_dict={node1:input("node1값은? "),
                                        node2:input("node2값은? ")})
print(result)


# In[19]:


#training data set(H=2x+3)
x_data = [1,2,3]
y_data = [5,7,9]

#placeholder 설정
x = tf.placeholder(dtype=tf.float32)
y = tf.placeholder(dtype=tf.float32)

#Weight & bias
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#Hypothesis
H = W*x+b

#cost function
cost = tf.reduce_mean(tf.square(H-y))

#경사하강법
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

#Session & Variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#학습
for step in range(1,6001):
    _, cost_val_, W_val, b_val = sess.run([train, cost, W, b],
                                         feed_dict={x:x_data, y:y_data})
    if step%200==0:
        print("{:4d}번째 cost:{}, W:{}, b:{}".format(step, cost_val, W_val, b_val))


# In[20]:


sess.run([W,b])


# In[21]:


#예측해보기(predict)
sess.run(H, feed_dict={x:5})


# In[22]:


sess.run(H, feed_dict={x:np.array([1,10,20])})


# ## 2.2 scale이 다른 데이터들의 linear regression을 구현

# In[23]:


#training data set
x_data = [1,2,5,8,10]
y_data = [5,15,68,80,95]

#placeholder를 설정
x = tf.placeholder(dtype=tf.float32, shape=None)
y = tf.placeholder(dtype=tf.float32, shape=None)

#Weight & bias
W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#Hypothesis
H = W*x+b

#cost function
cost = tf.reduce_mean(tf.square(H-y))

#train
train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)
#optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
#train = optimizer.minimize(cost)

#Session & Variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#학습
for step in range(1, 6001):
    _, cost_val, W_val = sess.run([train, cost, W], feed_dict={x:x_data, y:y_data})
    if step%200==0:
        print("{}번째 cost:{}, W:{}".format(step, cost_val, W_val))


# In[24]:


sess.run([W,b])


# In[25]:


#예측을 할 수는 있으나 cost 너무 큰 값이나 신뢰할 수 없음
sess.run(H, feed_dict={x:10})


# In[ ]:


"""
예측이 제대로 안되는 이유: GradientDescentOptimizer에서 
local 최소값을 만나면 global 최소값이 따로 있어도 멈춤
"""


# ## 3. 독립변수 x가 여러개인 linear regression
# - scale이 다른 x, y값

# In[34]:


#trining data set(np.array나 list로 생성)
x_data = np.array([[73,80,75],
                   [93,88,93],
                   [89,91,90],
                   [96,98,100],
                   [73,66,70]])
y_data = np.array([[152],[185],[180],[196],[142]])
#np.c_[x_data, y_data]

#placeholder
X = tf.placeholder(shape=[None, 3], dtype=tf.float32)
Y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

#Weight & bias
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#Hypothesis
#H = X@W+b
H = tf.matmul(X, W) + b

#cost function
cost = tf.reduce_mean(tf.square(H-Y))

#train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost) 
#learning_rate=0.01=1e-2 -> cost: nan 으로 나와서 1e-5로 조정

#session & Variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#학습
for step in range(1, 30001):
    _, cost_val = sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
    if step%3000==0:
        print("{}번째 cost:{}".format(step, cost_val))


# ## 4. Ozone량 예측 예제
# - 독립변수 x가 3 => Multi-variable Linear Regression

# In[35]:


import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import pandas as pd


# In[47]:


#training data set 생성
#data load -> 결측치 처리 -> 독립변수, 종속변수 분리
data = pd.read_csv('./data/ozone.csv', sep=',')

#data를 바로 학습할 수 없음. 데이터 정제 작업 필요
data = data.dropna(how='any') #결측치가 한 열이라도 있는 행 모두 제거
data.isna().sum()

#필요한 columns만 추출
data = data.iloc[:, 0:4]
data.head()

#training data set
x_data = data.iloc[:, 1:].values #values -> DataFrame을 numpy배열로 바꿔줌
y_data = data[['Ozone']].values.reshape(-1, 1)
#y_data = data['Ozone'].values.reshape(-1,1) 
x_data.shape, y_data.shape #(111,3), (111,1)

#tensorflow 구현
#1. placeholder
X = tf.placeholder(shape=[None,3], dtype=tf.float32)
Y = tf.placeholder(shape=[None,1], dtype=tf.float32)

#2. Weight&bias 설정
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#3. Hypothsis
# H = X@W+b
H = tf.matmul(X,W)+b

#4. cost함수
cost = tf.reduce_mean(tf.square(H-Y))

#5. train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost)

#6. session&variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#7. 학습
for step in range(1, 6001):
    _, cost_val = sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
    if step%300==0:
        print("{:4d}번째 cost:{}".format(step, cost_val))


# In[48]:


data[1:2]


# In[49]:


sess.run(H, feed_dict={X:np.array([[118, 8, 72]])})


# ## scale 맞추는 방법: normalization(많이 사용), standardization(표준화)

# In[ ]:


"""
scale 맞추는 방법: normalization, standardization
                  X - Xmin
normalization = -------------
                 Xmax - Xmin

상기 식을 사용하거나, sklearn 라이브러리(sklearn.preprocessing.MinMaxScaler) 사용
                    X - Xmean(평균)
standardization = -------------------
                     Xstd(표준편차)
상기 식을 사용하거나, sklearn 라이브러리(sklearn.preprocessing.StandardScaler) 사용
"""


# In[50]:


#training data set 생성
#data load -> 결측치 처리 -> 독립변수, 종속변수 분리
data = pd.read_csv('./data/ozone.csv', sep=',')

#data를 바로 학습할 수 없음. 데이터 정제 작업 필요
data = data.dropna(how='any') #결측치가 한 열이라도 있는 행 모두 제거
data.isna().sum()

#필요한 columns만 추출
data = data[['Ozone', 'Solar.R', 'Wind', 'Temp']]
data.head()

### scale 조정(standardization) ###
#                     X - Xmean(평균)
# standardization = -------------------
#                      Xstd(표준편차)

data['Ozone'] = (data['Ozone']-data['Ozone'].mean()) / data['Ozone'].std()
data['Solar.R'] = (data['Solar.R']-data['Solar.R'].mean()) / data['Solar.R'].std()
data['Wind'] = (data['Wind']-data['Wind'].mean()) / data['Wind'].std()
data['Temp'] = (data['Temp']-data['Temp'].mean()) / data['Temp'].std()

#training data set
x_data = data.iloc[:,1:].values 
y_data = data[['Ozone']].values.reshape(-1,1)

#tensorflow 구현
#1. placeholder
X = tf.placeholder(shape=[None, 3], dtype=tf.float32)
Y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

#2. Weight & bias 설정
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#3. Hypothesis
# H = X @ W + b
H = tf.matmul(X, W) + b

#4. cost함수
cost = tf.reduce_mean(tf.square(H-Y))

#5. train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost)

#6. session & variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#7. 학습
for step in range(1, 60001):
    _, cost_val = sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
    if step%3000==0:
        print("{:5d}번째 cost:{}".format(step, cost_val))


# In[51]:


#predict 하려면 scale이 맞춰진 데이터로 predict를 하고 결과를 다시 scale조정


# In[53]:


#data load -> 결측치 처리 -> 독립변수, 종속변수 분리
data = pd.read_csv('./data/ozone.csv', sep=',')

#data를 바로 학습할 수 없음. 데이터 정제 작업 필요
data = data.dropna(how='any') #결측치가 한 열이라도 있는 행 모두 제거
data.isna().sum()

#필요한 columns만 추출
data = data[['Ozone', 'Solar.R', 'Wind', 'Temp']]

#training data set
x_data = data[['Solar.R','Wind','Temp']].values #values -> DataFrame을 numpy배열로 바꿔줌
y_data = data[['Ozone']].values.reshape(-1,1)
print("scale조정 전 데이터(상위 3행):\n", np.c_[x_data[:3], y_data[:3]])

### scale 조정 (1) sklearn.preprocessing.MinMaxScaler ###
from sklearn.preprocessing import MinMaxScaler
scale_x = MinMaxScaler() #scale_x: x_data를 scale조정할 객체
#x_data에 대한 설정을 잡는 부분; x_data 3개 컬럼에 대한 max, min 설정
scale_x.fit(x_data)
x_data = scale_x.transform(x_data) #scale 조정된 x_data

scale_y = MinMaxScaler()
scale_y.fit(y_data)
y_data = scale_y.transform(y_data) #scale 조정된 y_data
print('scale조정 후 데이터(상위 3행):\n', np.c_[x_data[:3], y_data[:3]])

#tensorflow 구현
#1. placeholder
X = tf.placeholder(shape=[None, 3], dtype=tf.float32)
Y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

#2. Weight & bias 설정
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#3. Hypothesis
# H = X @ W + b
H = tf.matmul(X, W) + b

#4. cost함수
cost = tf.reduce_mean(tf.square(H-Y))

#5. train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost)

#6. session & variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#7. 학습
for step in range(1, 60001):
    _, cost_val = sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
    if step%3000==0:
        print("{:5d}번째 cost:{}".format(step, cost_val))


# In[56]:


#8. prediction
input_data = np.array([[118., 8.,72.]])
scale_input_data = scale_x.transform(input_data)
print('원 데이터 : ', input_data)
print('scale 조정된 데이터 :', scale_input_data)


# In[57]:


predict_value = sess.run(H, feed_dict={X:scale_input_data})
scale_y.inverse_transform(predict_value)


# In[58]:


#data load -> 결측치 처리 -> 독립변수, 종속변수 분리
data = pd.read_csv('./data/ozone.csv', sep=',')

#data를 바로 학습할 수 없음. 데이터 정제 작업 필요
data = data.dropna(how='any') #결측치가 한 열이라도 있는 행 모두 제거
data.isna().sum()

#필요한 columns만 추출
data = data[['Ozone', 'Solar.R', 'Wind', 'Temp']]
data.head()

### scale 조정 (2); data를 한꺼번에 scale조정시 prediction이 어려워짐
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# scaler.fit(data)
# data = pd.DataFrame(scaler.transform(data), columns=['Ozone', 'Solar.R', 'Wind', 'Temp'])
# display(data.head())
# type(data)

#training data set
x_data = data.iloc[:,1:].values #values -> DataFrame을 numpy배열로 바꿔줌
y_data = data[['Ozone']].values.reshape(-1,1)

print('조정 전:\n', np.c_[x_data[:3], y_data[:3]])
### scale 조정 (2); x_data, y_data scale을 따로따로 - prediction 가능
from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
scaler_x.fit(x_data)
x_data = scaler_x.transform(x_data)

scaler_y = StandardScaler()
scaler_y.fit(y_data)
y_data = scaler_y.transform(y_data)
print('조정 후:\n', np.c_[x_data[:3], y_data[:3]])

#tensorflow 구현
#1. placeholder
X = tf.placeholder(shape=[None, 3], dtype=tf.float32)
Y = tf.placeholder(shape=[None, 1], dtype=tf.float32)

#2. Weight & bias 설정
W = tf.Variable(tf.random_normal([3,1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

#3. Hypothesis
# H = X @ W + b
H = tf.matmul(X, W) + b

#4. cost함수
cost = tf.reduce_mean(tf.square(H-Y))

#5. train
train = tf.train.GradientDescentOptimizer(learning_rate=1e-5).minimize(cost)

#6. session & variable 초기화
sess = tf.Session()
sess.run(tf.global_variables_initializer())

#7. 학습
for step in range(1, 60001):
    _, cost_val = sess.run([train, cost], feed_dict={X:x_data, Y:y_data})
    if step%3000==0:
        print("{:5d}번째 cost:{}".format(step, cost_val))


# In[59]:


input_data = np.array([[118, 8, 72]])
scaled_input_data = scaler_x.transform(input_data)
scaler_y.inverse_transform(sess.run(H, feed_dict={X:scaled_input_data}))


# In[61]:


sess.run([W,b])


# ## 5. Logistic Regression = Binary classification(2개 그룹)
# ### Logistic Regression이 필요한 이유(기존의 liner regression으로는 안되는 경우)

# In[63]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

x = np.array([1,2,5,8,10,30])
y = np.array([0,0,0,1,1,1])
lm = stats.linregress(x,y)
print('w값:', lm[0], 'b값:', lm[1])
plt.scatter(x,y)
plt.plot(x, x*lm[0]+lm[1], 'r')


# In[ ]:




