#!/usr/bin/env python
# coding: utf-8

# **21-03-19 ML_DL 03_딥러닝_분류분석 (c)cherryuki (ji)**

# # 03. 딥러닝 기초(분류 분석)

# In[1]:


import tensorflow.keras.utils as utils #분류분석시 원핫 인코딩
from tensorflow.keras.models import Sequential #모델 생성시
from tensorflow.keras.layers import Dense, Activation
import numpy as np


# ## 1. 데이터셋 준비
# - 학습 데이터(=훈련 데이터), 검증 데이터, 시험(TEST) 데이터

# In[2]:


#학습 데이터(=훈련 데이터)
X_train = np.array([1,2,3,4,5,6,7,8,9]*10)
Y_train = np.array([2,4,6,8,10,12,14,16,18]*10)
#검증 데이터, 테스트 데이터
X_val = np.array([1,2,3,4,5,6,7,8,9])
Y_val = np.array([2,4,6,8,10,12,14,16,18])


# In[3]:


Y_val


# In[4]:


#분류분석을 하기 위해 target데이터를 라벨링 전환(원 핫 인코딩)
Y_train = utils.to_categorical(Y_train, 19)
Y_val = utils.to_categorical(Y_val, 19)


# In[5]:


Y_val


# ## 2. 모델구성하기
# - 활성화 함수(activation function); 생물학적 뉴런에서 입력신호가 일정크기 이상일 때만 신호를 전달하는 메커니즘을 모방한 함수
# - Softmax, Sigmoid, tanh(x), Binary step, Gaussian, ReLU 등

# In[6]:


model = Sequential()
# 아래 숫자는 경험상 넣는 것?? 해보면서 조정 필요
model.add(Dense(units=38, input_dim=1, activation='sigmoid'))
model.add(Dense(units=64, activation='elu'))
model.add(Dense(units=32, activation='elu'))
model.add(Dense(units=19, activation='softmax')) #softmax: 모든 출력 결과의 합이 1


# ## 3. 모델 학습과정 설정

# In[7]:


model.compile(loss='categorical_crossentropy', optimizer='sgd',
             metrics=['accuracy'])


# ## 4. 모델 학습시키키

# In[8]:


hist = model.fit(X_train, Y_train, epochs=500, batch_size=10,
                verbose=2, validation_data=(X_val, Y_val))


# In[9]:


hist.history.keys()


# ## 5. 모델 학습과정 살펴보기(hist, 평가)

# In[15]:


import matplotlib.pyplot as plt
fig, loss_ax = plt.subplots(figsize=(8,5))
loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax = loss_ax.twinx() #loss_ax와 x축을 공유하는 acc_ax 생성
acc_ax.plot(hist.history['accuracy'], 'g', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'b', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuracy')
loss_ax.legend(loc='upper left')
acc_ax.legend(loc='center right')
plt.show()


# In[16]:


#모델 평가
score = model.evaluate(X_val, Y_val, batch_size=1)
score


# In[17]:


print('loss:', score[0])
print('accuracy:', score[1])


# ## 6. 모델을 이용해서 예측하기

# In[19]:


model.predict_classes(np.array([2]))


# In[21]:


model.predict(np.array([2])).argmax() #argmax(); 최대값이 있는 곳의 인덱스 리턴


# In[ ]:




