#!/usr/bin/env python
# coding: utf-8

# **21-03-24 ML_DL 09_DNN 와인감별 (c)cherryuki (ji)**

# # 09. DNN 와인 등급 감별

# In[1]:


import pandas as pd #read_csv, #get_dummies: 원핫인코딩
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.callbacks import EarlyStopping
import tensorflow.keras.utils as utils #원핫 인코딩
import matplotlib.pyplot as plt


# In[2]:


#1. 데이터셋 생성
raw_data = pd.read_csv('data/winequality-red.csv', sep=';')
raw_data.head()


# In[3]:


raw_data.info()


# In[4]:


raw_data.describe().T


# In[5]:


raw_data.isna().sum()


# In[6]:


Input_data = raw_data.iloc[:, :-1]
Target = raw_data.iloc[:, -1]
print(Target.unique()) #총 6종류(3~8등급)


# ### 원 핫 인코딩 방법(2가지)
# 1) utils.to_categorical() <br>
# 2) pd.get_dummies().to_numpy()

# In[7]:


#1. 데이터셋 
raw_data = pd.read_csv('data/winequality-red.csv', sep=';')
raw_data.head()
Input_data = raw_data.iloc[:, :-1]
Target = raw_data.iloc[:, -1]
#scale 조정
scaler = StandardScaler()
scaler.fit(Input_data)
scaled_input = scaler.transform(Input_data)
scaled_input = pd.DataFrame(scaled_input)

#1)one-hot 인코딩:utils.to_categorical()
label_target = utils.to_categorical(Target)

#데이터셋 분할(훈련셋:테스트셋=7:3)
X_train, X_test, Y_train, Y_test = train_test_split(scaled_input, label_target,
                                                   test_size=0.3, random_state=3)
print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)

#2. 모델 구성
model = Sequential()
model.add(Dense(units=256, input_dim=11, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(units=720, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(units=128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(units=9, activation='softmax'))

#3. 학습과정 설정
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

#4. 학습 시키기
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(patience=25)
hist = model.fit(X_train, Y_train, epochs=100, batch_size=5,
                validation_split=0.3, verbose=2, callbacks=[early_stopping])

#5. 모델학습과정 표시하고 평가하기
#학습과정 표시하기
fig, loss_ax = plt.subplots()
loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'g', label='val loss')
loss_ax.set_xlabel('epochs')
loss_ax.set_ylabel('loss')

acc_ax = loss_ax.twinx() #x축을 공유하는 acc_ax
acc_ax.plot(hist.history['accuracy'], 'b', label='train accuracy')
acc_ax.plot(hist.history['val_accuracy'], 'r', label='val accuracy')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()


# In[8]:


#6. 모델 평가
loss_and_matrics = model.evaluate(X_test, Y_test, batch_size=16)
print()
print('loss:', loss_and_matrics[0])
print('accuracy:', loss_and_matrics[1])


# In[10]:


#7. 모델 사용하기
pred = model.predict(X_test).argmax(axis=1)
#pred = np.argmax(model.predict(X_test), axis=1)
real = np.argmax(Y_test, axis=1)
ct = pd.crosstab(pred, real)
ct.index.name='predict'
ct.columns.name='real'
ct


# In[15]:


#1. 데이터셋 
raw_data = pd.read_csv('data/winequality-red.csv', sep=';')
raw_data.head()
Input_data = raw_data.iloc[:, :-1]
Target = raw_data.iloc[:, -1]
#데이터 전처리; scale 조정, 원 핫 인코딩
scaler = StandardScaler()
scaler.fit(Input_data)
scaled_input = scaler.transform(Input_data)
scaled_input = pd.DataFrame(scaled_input)
#2)one-hot 인코딩: pd.get_dummies()
label_target2 = pd.get_dummies(Target).to_numpy()
X_train2, X_test2, Y_train2, Y_test2 = train_test_split(scaled_input, label_target2,
                                                   test_size=0.3, random_state=5)

#2. 모델 구성
model = Sequential()
model.add(Input(11))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(720, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(6, activation='softmax'))

#3. 학습과정 설정
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])

#4. 학습 시키기
early_stopping = EarlyStopping(monitor='val_loss', patience=20)
hist = model.fit(X_train2, Y_train2, epochs=100, batch_size=10,
                validation_split=0.3, verbose=2, callbacks=[early_stopping])

#5. 모델학습과정 표시하고 평가하기
#학습과정 표시하기
fig, loss_ax = plt.subplots()
loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'g', label='val loss')
loss_ax.set_xlabel('epochs')
loss_ax.set_ylabel('loss')

acc_ax = loss_ax.twinx() #x축을 공유하는 acc_ax
acc_ax.plot(hist.history['accuracy'], 'b', label='train accuracy')
acc_ax.plot(hist.history['val_accuracy'], 'r', label='val accuracy')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()


# In[16]:


#6. 모델 평가
loss_and_matrics = model.evaluate(X_test2, Y_test2, batch_size=16)
print()
print('loss:', loss_and_matrics[0])
print('accuracy:', loss_and_matrics[1])


# In[17]:


#7. 모델 사용하기
pred = model.predict(X_test2).argmax(axis=1)+3
#model.predict_classes(X_test2)+3
real = np.argmax(Y_test2, axis=1)+3


# In[18]:


ct = pd.crosstab(pred, real)
ct.index.name='predict'
ct.columns.name='real'
ct


# In[ ]:




