#!/usr/bin/env python
# coding: utf-8

# **21-03-25 ML_DL 12_CNN mnist(손글씨 데이터) (c)cherryuki (ji)**

# # 12. CNN mnist(손글씨 데이터)

# In[1]:


import tensorflow as tf
from tensorflow.keras.datasets import mnist
import tensorflow.keras.utils as utils
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dropout
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


#1. 데이터셋 생성
width=28; height=28
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#정규화 작업(1차원으로 바꾸고, scale 조정)
x_train = x_train.reshape(60000, width*height).astype('float32') / 255.0
x_test = x_test.reshape(10000, width*height).astype('float32') / 255.0

#훈련셋:검증셋 분리(5:1)
x_val = x_train[50000:]
y_val = y_train[50000:]
x_train = x_train[:50000]
y_train = y_train[:50000]

#원 핫 인코딩
y_train = utils.to_categorical(y_train)
y_val = utils.to_categorical(y_val)
y_test = utils.to_categorical(y_test)


# In[3]:


plt_row=5
plt_col=5
plt.rcParams['figure.figsize']=(10,10)
plt.rc('font', family='Malgun Gothic') #한글 폰트 설정
f, axarr = plt.subplots(plt_row, plt_col)

for i in range(plt_row*plt_col):
    sub_plt = axarr[i//5, i%5] #(0,0)~(5,5)
    sub_plt.imshow(x_test[i].reshape(width, height))
    sub_plt.axis('off') #축 제거
    sub_plt.set_title('실제: '+str(np.argmax(y_test[i])))


# ## 1. DNN(Deep Neural Network, 다중 퍼셉트론)
# ### 07. 딥러닝 기초 mnist(손글씨 데이터) 참조

# In[4]:


#1. 데이터셋 생성
width = 28; height=28
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#정규화 작업(1차원으로 바꾸고, scale조정)
x_train = x_train.reshape(60000, width*height).astype('float32') / 255.0
x_test = x_test.reshape(10000, width*height).astype('float32') / 255.0

#훈련셋:검증셋 분리(5:1)
x_val = x_train[50000:]
y_val = y_train[50000:]
x_train = x_train[:50000]
y_train = y_train[:50000]

#원 핫 인코딩
y_train = utils.to_categorical(y_train)
y_val = utils.to_categorical(y_val)
y_test = utils.to_categorical(y_test)

#2. 모델 구성
model = Sequential()
model.add(Dense(256, input_dim=width*height, activation='relu'))
model.add(Dense(512, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

#3. 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#4. 모델 학습시키기
early_stopping = EarlyStopping(patience=10)
hist = model.fit(x_train, y_train, epochs=30, batch_size=32,
                validation_data=(x_val, y_val),
                callbacks=[early_stopping])

#5. 학습과정 표시하기
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

#6. 모델 평가하기
score = model.evaluate(x_test, y_test, batch_size=32)
print('\n\nloss:', score[0], ' metrics["accuracy"]:', score[1])

#7. 모델 사용하기(예측)
yhat = model.predict(x_test, batch_size=32)

plt_row = 5
plt_col = 5
plt.rcParams['figure.figsize'] = (10,10)
plt.rc('font', family='Malgun Gothic') #한글 폰트 설정
f, axarr = plt.subplots(plt_row, plt_col)

for i in range(plt_row*plt_col):
    sub_plt = axarr[i//plt_row, i%plt_col]
    sub_plt.imshow(x_test[i].reshape(width, height))
    sub_plt.axis('off') #축 제거
    title = '실제: '+ str(np.argmax(y_test[i])) + ' 예측: '+ str(np.argmax(yhat[i]))
    sub_plt.set_title(title)


# In[5]:


#틀린 것만 나오게(최대 100개)
yhat = model.predict(x_test, batch_size=32)

plt_row=10
plt_col=10
plt.rcParams['figure.figsize'] = (20,20) #전체 사이즈
plt.rc('font', family='Malgun Gothic')
f, axarr = plt.subplots(plt_row, plt_col)

i=0; cnt=0
while cnt < (plt_row*plt_col):
    if np.argmax(y_test[i])==np.argmax(yhat[i]):
        i+=1
        continue
    sub_plt = axarr[cnt//plt_row, cnt%plt_col]
    sub_plt.imshow(x_test[i].reshape(width, height))
    sub_plt.axis('off') #축 제거
    title = '실제: '+ str(np.argmax(y_test[i])) + ' 예측: '+ str(np.argmax(yhat[i]))
    sub_plt.set_title(title)
    i+=1
    cnt+=1


# ## 2. CNN(Convolutional Neural Network)
# - 컨볼루션 레이어 -> 깊은 컨볼루션 레이어

# In[8]:


#1. 데이터셋 생성
width = 28; height=28
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#정규화 작업(1차원으로 바꾸고, scale조정)
x_train = x_train.reshape(60000, width, height, 1).astype('float32') / 255.0
x_test = x_test.reshape(10000, width, height, 1).astype('float32') / 255.0

#훈련셋:검증셋 분리(5:1)
x_val = x_train[50000:]
y_val = y_train[50000:]
x_train = x_train[:50000]
y_train = y_train[:50000]

#원 핫 인코딩
y_train = utils.to_categorical(y_train)
y_val = utils.to_categorical(y_val)
y_test = utils.to_categorical(y_test)

#2. 모델 구성
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(width, height, 1)))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256, input_dim=width*height, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(10, activation='softmax'))

#3. 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#4. 모델 학습시키기
early_stopping = EarlyStopping(patience=10)
hist = model.fit(x_train, y_train, epochs=20, batch_size=32,
                 validation_data=(x_val, y_val),
                 callbacks=[early_stopping])


#5. 학습과정 표시하기
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

#6. 모델 평가하기
score = model.evaluate(x_test, y_test, batch_size=32)
print('\n\nloss:', score[0], ' metrics["accuracy"]:', score[1])

#7. 모델 사용하기(예측)
yhat = model.predict(x_test, batch_size=32)

plt_row = 10
plt_col = 10
plt.rcParams['figure.figsize'] = (15,15) #전체 사이즈
plt.rc('font', family='Malgun Gothic') #한글 폰트 설정
f, axarr = plt.subplots(plt_row, plt_col)

i=0; cnt=0
while (cnt < (plt_row*plt_col)) and (i<len(yhat)):
    if np.argmax(y_test[i])==np.argmax(yhat[i]):
        i+=1
        continue
    sub_plt = axarr[cnt//plt_row, cnt%plt_col]
    sub_plt.imshow(x_test[i].reshape(width, height))
    sub_plt.axis('off') #축 제거
    title = '실제: '+ str(np.argmax(y_test[i])) + ' 예측: '+ str(np.argmax(yhat[i]))
    sub_plt.set_title(title)
    i+=1
    cnt+=1


# In[ ]:




