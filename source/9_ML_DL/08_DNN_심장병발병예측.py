#!/usr/bin/env python
# coding: utf-8

# **21-03-24 ML_DL 08_DNN 심장병발병예측 (c)cherryuki (ji)**

# # 08. DNN_심장병 발병예측
# ### DNN: Deep Neural Network

# In[1]:


import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import matplotlib.pyplot as plt


# In[2]:


#1. 데이터셋 생성
raw_data = pd.read_excel('data/heart-disease.xlsx')
raw_data.head()


# In[4]:


raw_data.describe()


# In[5]:


raw_data.info()


# In[6]:


raw_data[raw_data['chol']=='?']


# In[7]:


raw_data[raw_data['ca']=='?']


# In[8]:


raw_data[raw_data['hsl']=='?']


# In[9]:


clean_data = raw_data.replace('?', np.nan)
clean_data


# In[10]:


clean_data = clean_data.dropna() #NAN값이 있는 row를 제거
clean_data


# In[11]:


clean_data.isnull().sum()


# In[12]:


clean_data.info()


# In[13]:


clean_data.columns


# In[14]:


Input_data = clean_data.iloc[:, :-1]
Target = clean_data.iloc[:, [-1]]
Target


# In[15]:


#심장별 걸린 데이터 수
Target['heartDisease'].sum()


# In[16]:


#심장병 걸린 데이터 비율
Target['heartDisease'].mean()


# In[17]:


Input_data.head(2)


# In[18]:


#scale 조정
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(Input_data)
scaled_input = scaler.transform(Input_data)
scaled_input = pd.DataFrame(scaled_input)
scaled_input


# In[19]:


scaled_input.describe().T #평균 0, 표준편차 1에 가깝게 scale 조정 됨(StandardScaler)


# In[20]:


# 학습 데이터:테스트 데이터 = 7:3 으로 나누기
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(scaled_input, Target,
                                                   test_size=0.3, random_state=5) #seed값 세팅과 유사
print(X_train.shape, Y_train.shape, X_test.shape, Y_test.shape)


# In[21]:


#2. 모델 구성
model = Sequential()
model.add(Dense(units=500, input_dim=13, activation='tanh'))
#과적합을 해결하기 위한 Dropout
model.add(Dropout(0.1))
model.add(Dense(units=200, activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(units=100, activation='tanh'))
model.add(Dropout(0.1))
model.add(Dense(units=1, activation='sigmoid')) #이진분류 (0아니면1)
model.summary()


# **<metrics에 들어갈 수 있는 항목들; 성능평가지표>**
# - accuracy(정확도); 예측값과 실제값이 동일한 건수 / 전체 건수 (TP+TN / TP+FN+FP+TN)
# - Recall(재현율); 실제 True를 True라고 예측한 건수 / 실제 True인 전체 건수 (TP / TP+FN)
# - Precision(정밀도); 실제 True를 True라고 예측한 건수 / True로 예측한 전체 건수 (TP / TP+FP)

# In[22]:


#3. 학습과정 설정
from tensorflow.keras import metrics
model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
#model.compile(loss='categorical_crossentropy', optimizer='nadam', 
#                 metrics=[metrics.Recall()]) 
#metrics에 들어갈 수 있는 것들 - accuracy, Recall, Precision


# In[24]:


#4. 학습 시키기
hist = model.fit(X_train, Y_train, epochs=50, batch_size=50,
                validation_split=0.2, verbose=2)
#validation_split; train 데이터에서 일부(0.2)를 검증데이터로 사용
##(검증 데이터셋 없을 경우 사용하는 방법)


# In[25]:


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


# In[26]:


#6. 평가 및 예측
score = model.evaluate(X_test, Y_test, verbose=0)
print('model loss:', score[0])
print('model accuracy:', score[1])


# In[28]:


#7. confusion_matrix(성능 평가지표)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
pred = model.predict(X_test)
pred = (pred>0.5)
print(confusion_matrix(Y_test, pred), end='\n')
print('f1_score:', f1_score(Y_test, pred))


# In[ ]:




