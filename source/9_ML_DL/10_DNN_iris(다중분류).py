#!/usr/bin/env python
# coding: utf-8

# **21-03-24 ML_DL 10_DNN iris(다중분류) (c)cherryuki (ji)**

# # 10. DNN iris (다중분류)

# In[1]:


import seaborn as sns #아이리스 데이터
import pandas as pd #원핫인코딩
import numpy as np
from sklearn.model_selection import train_test_split #훈련셋과 테스트셋 분리
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, Dropout
import matplotlib.pyplot as plt


# In[6]:


#1. 데이터 셋
iris = sns.load_dataset('iris')
#display(iris.head())
iris_X = iris.iloc[:, :-1].to_numpy()
iris_Y = iris.iloc[:, -1]
#iris_Y 원핫 인코딩(문자이므로 pd.get_dummies()이용) 
##utils.to_categorical()은 숫자만 가능
iris_Y = pd.get_dummies(iris_Y).to_numpy()
# 1 0 0 -> setosa
# 0 1 0 -> versicolor
# 0 0 1 -> virginica
#훈련 데이터와 시험 데이터 분리
train_X,test_X, train_Y, test_Y = train_test_split(iris_X, iris_Y,
                                                  test_size=0.3, random_state=1)
train_X.shape, train_Y.shape, test_X.shape, test_Y.shape


# In[9]:


#ModelCheckpoint; 모델 저장하는 함수
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
import os
model_save_folder = './model/'
if not os.path.exists(model_save_folder):
    os.mkdir(model_save_folder) #절대 경로 필요
file = model_save_folder + 'iris-{epoch:03d}-val{val_accuracy:.4f}.h5'
early_stopping = EarlyStopping(patience=40)
checkpoint = ModelCheckpoint(filepath=file, monitor='val_accuracy',
                            verbose=1, save_best_only=True)

#2. 모델 구성
model = Sequential()
model.add(Dense(60, input_dim=4, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(30, activation='relu'))
model.add(Dense(3, activation='softmax')) #다중분류이므로 softmax 

#3. 학습 과정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#4. 학습
fit_hist = model.fit(train_X, train_Y, batch_size=50, epochs=300,
                    validation_split=0.2,
                    callbacks=[early_stopping, checkpoint])

#5. 모델 학습과정 표시
fig, loss_ax = plt.subplots()
loss_ax.plot(fit_hist.history['loss'], 'y', label='train loss')
loss_ax.plot(fit_hist.history['val_loss'], 'g', label='val loss')
loss_ax.set_xlabel('epochs')
loss_ax.set_ylabel('loss')

acc_ax = loss_ax.twinx() #x축을 공유하는 acc_ax
acc_ax.plot(fit_hist.history['accuracy'], 'b', label='train accuracy')
acc_ax.plot(fit_hist.history['val_accuracy'], 'r', label='val accuracy')
acc_ax.set_ylabel('accuracy')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')
plt.show()


# In[10]:


#6. 모델 평가
score = model.evaluate(test_X, test_Y, batch_size=10)
print('loss:', score[0])
print('accuracy:', score[1])


# In[11]:


model.predict(np.array([[6.0,3.4,4.5,1.6]])).argmax(axis=1) #versicolor


# In[12]:


#7. 예측
real = np.argmax(test_Y, axis=1) #실제 값
pred = model.predict(test_X).argmax(axis=1) #예측 값
np.all(pred==real) #100% 동일하면 True


# In[13]:


ct_result = pd.crosstab(pred, real)
ct_result.index.name='pred'
ct_result.columns.name='real'
ct_result


# In[ ]:




