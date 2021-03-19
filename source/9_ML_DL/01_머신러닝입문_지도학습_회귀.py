#!/usr/bin/env python
# coding: utf-8

# **21-03-19 ML_DL 01_머신러닝 (c)cherryuki (ji)**

# ## 머신러닝: 지도학습- 분류, 회귀 / 비지도학습- 군집

# # 01. Linear Regression(선형 회귀)
# ## 1.1 기존의 프로그램 방식

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


#섭씨 온도(input data) 를 받아 화씨 온도(target data) 출력
def celsius_to_fahrenheit(x):
    return x*1.8+32


# In[4]:


input_c = int(input("섭씨온도는?"))
print("화씨 온도는", celsius_to_fahrenheit(input_c))


# ## 1.2 머신러닝 프로그램 방식
# 1. 데이터 셋 확보 및 생성
# 2. 데이터 전처리: 훈련데이터셋, 검증데이터셋, 시험데이터 셋, ...
# 3. 모델 구성
# 4. 모델 학습과정 설정
# 5. 모델 학습 시키기
# 6. 모델 평가(시험 데이터 셋)
# 7. 모델 사용(입력값 주고 예측값 받기)

# In[6]:


from tensorflow.keras.models import Sequential #3. 모델 생성시
from tensorflow.keras.layers import Dense #입력값과 출력값


# In[7]:


#1&2 데이터
data_C = np.array(range(100))
data_C #입력값(input data)


# In[8]:


data_F = celsius_to_fahrenheit(data_C)
data_F #목적값(target value)


# In[9]:


#3. 모델 구성
model = Sequential()
model.add(Dense(1, input_dim=1)) #input_dim=1: 독립변수 1개, 앞부분 숫자: target 데이터 개수(1개)

#4. 모델학습과정 설정
model.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
print(model.summary())


# In[10]:


#학습전 예측
print(model.predict([0]))


# In[12]:


model.save('model/before_learning.h5')


# In[13]:


#2. 컴퓨터에게 학습시키기 위해 normalize함(전체의 편차 줄이기. 이상적인 편차 0~1)
scaled_data_C = data_C/100.0
scaled_data_F = data_F/100.0
print(scaled_data_C, end='\n\n')
print(scaled_data_F)


# In[14]:


#4. 모델 학습시키기
hist = model.fit(scaled_data_C, scaled_data_F, epochs=1000, verbose=2)


# In[15]:


hist.history.keys()


# In[16]:


plt.plot(hist.history['loss'])
plt.show()


# In[17]:


model.predict([0.01])


# In[18]:


model.save('model/after_learning.h5')


# In[19]:


plt.scatter(x=scaled_data_C, y=scaled_data_F)


# ## 1.3 노이즈가 있는 데이터로 실습

# In[20]:


# 평균이 0이고 표준편차가 0.1인 데이터 100
#np.random.seed(123) #동일한 숫자 나오게 하고 싶을 때 시드 고정
noise = np.array(np.random.normal(0,0.1,100))
noised_scaled_data_F = scaled_data_F + noise


# In[21]:


plt.scatter(x=scaled_data_C, y=noised_scaled_data_F)
plt.show()


# In[22]:


#3. 모델 구성
model2 = Sequential()
model2.add(Dense(1, input_dim=1))

#4. 모델학습과정 설정
model2.compile(loss='mse', optimizer='rmsprop', metrics=['mae'])
print(model2.summary())


# In[23]:


#5. 모델 학습시키기
hist2 = model2.fit(scaled_data_C, noised_scaled_data_F, epochs=1000, verbose=2)


# In[24]:


print(model2.predict(np.array([0.01])))


# In[25]:


plt.plot(hist2.history['loss'])


# In[26]:


model2.save('model/noise_after_learning.h5')


# In[ ]:




