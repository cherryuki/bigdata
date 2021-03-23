#!/usr/bin/env python
# coding: utf-8

# **21-03-23 ML_DL 06_tensorflow ver2_딥러닝 (c)cherryuki (ji)**

# # 06. tensorflow_ver2_keras
# ## 1. XOR Problem

# In[1]:


import numpy as np
from tensorflow.keras.models import Sequential #모델 객체 생성시
from tensorflow.keras.layers import Dense #layer 쌓을 때 필요한 함수
import matplotlib.pyplot as plt


# In[3]:


#1. data set
x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],  [1],  [1],  [0]]

#2. 모델 구성
model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu'))
model.add(Dense(20, activation='relu')) #은닉층부터는 input_dim 기재X
model.add(Dense(10, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
#입력2, 출력10: Weight 20(2*10)개, bias: 10개 -> 30(파라미터)
#입력10, 출력20: Weight 200(10*20)개, bias:20개 -> 220(파라미터)
print(model.summary()) #파라미터의 개수 출력

#3. 모델 학습과정
model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])
#model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=['accuracy']) 
#model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['accuracy']) 
#loss: mse, binary_crossentropy, crossentropy

#4. 학습하기
fit_hist = model.fit(x_data, y_data, epochs=100, verbose=2)


# In[4]:


fit_hist.history.keys()


# In[5]:


for acc in fit_hist.history['binary_accuracy']:
    print(acc, end='\t')


# In[7]:


plt.plot(fit_hist.history['loss'])
plt.show()


# In[8]:


#입력 스타일은 [[0, 0]]
while True:
    input_list = input('space로 분리해서 0이나 1을 2개 입력(종료:9)').strip().split() #space를 기준으로 분리
    input_data = list(map(int, input_list))
    print(input_data)
    if input_data[0] == 9:
        break;
    input_data = [input_data]
    #input_data = np.array(input_data).reshape(1,2)
    print("입력값:", input_data)
    print("예측값:", int(model.predict(input_data).round()))


# ## 2. AND Problem

# In[9]:


#1. data set
x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],  [0],  [0],  [1]]

#2. 모델 구성
and_model = Sequential()
and_model.add(Dense(32, input_dim=2, activation='relu'))
and_model.add(Dense(1, activation='sigmoid'))

print(and_model.summary()) #파라미터의 개수 출력

#3. 모델 학습과정
and_model.compile(loss='mse', optimizer='adam', metrics=['binary_accuracy'])

#4. 학습하기
and_fit_hist = and_model.fit(x_data, y_data, epochs=300, verbose=0)


# In[10]:


and_fit_hist.history.keys()


# In[12]:


for acc in and_fit_hist.history['binary_accuracy']:
    print(acc, end='\t')


# In[13]:


plt.plot(and_fit_hist.history['loss'])
plt.show()


# In[14]:


#입력 스타일은 [[0, 0]]
while True:
    input_list = input('space로 분리해서 0이나 1을 2개 입력(종료:9)').strip().split() #space기준으로 분리
    input_data = list(map(int, input_list))
    print(input_data)
    if input_data[0] ==9:
        break;
    input_data = [input_data]
    #input_data = np.array(input_data).reshape(1,2)
    print('입력값:', input_data)
    print('예측값:', int(and_model.predict(input_data).round()))


# ## 3. OR Problem

# In[22]:


#1. data set
x_data = [[0,0],[0,1],[1,0],[1,1]]
y_data = [[0],  [1],  [1],  [1]]

#2. 모델 구성
or_model = Sequential()
or_model.add(Dense(32, input_dim=2, activation='relu'))
or_model.add(Dense(1, activation='sigmoid'))
print(or_model.summary())

#3. 학습과정
or_model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

#4. 학습하기
or_fit_hist = or_model.fit(x_data, y_data, epochs=300, verbose=0)


# In[23]:


for acc in or_fit_hist.history['accuracy']:
    print(acc, end='\t')


# In[24]:


plt.plot(or_fit_hist.history['loss'])
plt.show()


# In[25]:


while True:
    input_list = input('space로 분리해서 0이나 1을 2개 입력(종료:9)').strip().split() #space기준으로 분리
    input_data = list(map(int, input_list))
    print(input_data)
    if input_data[0] ==9:
        break;
    input_data = [input_data]
    #input_data = np.array(input_data).reshape(1,2)
    print('입력값:', input_data)
    print('예측값:', int(or_model.predict(input_data).round()))


# In[ ]:




