#!/usr/bin/env python
# coding: utf-8

# **21-03-23 ML_DL 07_딥러닝기초 mnist(손글씨 데이터) (c)cherryuki (ji)**

# # 07. 딥러닝 기초 mnist(손글씨 데이터)

# In[2]:


from tensorflow.keras.datasets import mnist #mnist 데이터셋
import tensorflow.keras.utils as utils #원핫인코딩
from tensorflow.keras.models import Sequential #모델
from tensorflow.keras.layers import Dense, Activation #model.add 시
from matplotlib import pyplot as plt
import numpy as np


# In[3]:


#1. 데이터셋 준비하기
##훈련셋, 검증셋 분리
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()


# In[3]:


X_train.shape, Y_train.shape, X_test.shape, Y_test.shape


# In[4]:


X_train[0]


# In[5]:


plt.imshow(X_train[0])


# In[6]:


Y_train[0]


# In[7]:


#훈련셋과 검증셋 분리(X_train, Y_train을 검증셋과 훈련셋으로 분리)
X_val = X_train[50000:]
Y_val = Y_train[50000:]
X_train = X_train[:50000]
Y_train = Y_train[:50000]


# In[8]:


#훈련셋; model 학습시 사용
X_train.shape, Y_train.shape


# In[9]:


#검증셋; model 학습시 사용
len(X_val), len(Y_val)


# In[10]:


#시험셋(test set); model 평가시 사용
len(X_test), len(Y_test)


# In[11]:


#1차원으로 바꾸고, scale 맞춰야 함
#normalize하기 위해 색상값(255.0)으로 나눔 #28*28=784
X_train = X_train.reshape(50000, 784).astype('float32') / 255.0
X_val = X_val.reshape(10000, 28*28).astype('float32') / 255.0
X_test = X_test.reshape(10000, 28*28).astype('float32') / 255.0


# In[12]:


X_train.shape, X_val.shape, X_test.shape


# In[13]:


#훈련셋과 검증셋 700개, 300개씩 가져옴
train_rand_idx = np.random.choice(50000, 700)
val_rand_idx = np.random.choice(10000, 300)

X_train = X_train[train_rand_idx]
Y_train = Y_train[train_rand_idx]
X_val = X_val[val_rand_idx]
Y_val = Y_val[val_rand_idx]


# In[14]:


plt.imshow(X_train[0].reshape(28,28))


# In[15]:


Y_train[0]


# In[16]:


Y_train.shape, Y_val.shape, Y_test.shape


# In[17]:


#원 핫 인코딩(라벨링 전환)
#1 -> 0 1 0 0 0 0 0 0 0 0
#9 -> 0 0 0 0 0 0 0 0 0 9
Y_train = utils.to_categorical(Y_train)
Y_val = utils.to_categorical(Y_val)
Y_test = utils.to_categorical(Y_test)


# In[18]:


Y_train[0]
#데이터 전처리 완료


# ## 1. 과적합(Overfitting) 발생

# In[21]:


#2. 모델 구성하기
model = Sequential()
model.add(Dense(units=2, input_dim=784, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#3. 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='sgd', 
              metrics=['accuracy'])

#4. 모델 학습시키기
hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10, validation_data=(X_val,Y_val), verbose=0)


# In[22]:


#5. 모델 학습과정 표시 및 평가
hist.history.keys()


# In[27]:


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
#학습 데이터에서는 어느정도 loss도 줄고 accuracy도 증가하나 
##검증 데이터에서는 결과 좋지 못한 편(과적합 발생)


# In[28]:


#모델 평가하기
loss_and_metrics = model.evaluate(X_test, Y_test, batch_size=32)


# In[29]:


print("loss:", loss_and_metrics[0])
print("accuracy:", loss_and_metrics[1])


# In[33]:


#6. 모델 저장 및 로드하기
model.save('model/mnist.h5')


# In[31]:


model.summary()


# In[34]:


#모델 로드
from tensorflow.keras.models import load_model
model2 = load_model('model/mnist.h5')
model2.summary()


# In[36]:


plt.imshow(X_train[5].reshape(28,28))


# In[37]:


model2.predict(X_train[5].reshape(1,28*28)).argmax()


# In[43]:


plt.imshow(X_val[2].reshape(28,28))


# In[44]:


model2.predict(X_val[2].reshape(1,784)).argmax()


# In[46]:


model2.predict_classes(X_val[2].reshape(1,784))


# **21-03-24 ML_DL 07_딥러닝기초 mnist(손글씨 데이터) (c)cherryuki (ji)**

# ## 콜백함수
# - epoch 실행할 때마다 자동으로 실행되는 함수

# In[5]:


import tensorflow as tf
class CustomHistory(tf.keras.callbacks.Callback):
    def __init__(self):
        self.epoch = 0
        self.train_loss=[]
        self.val_loss=[]
        self.train_acc=[]
        self.val_acc=[]
    def on_epoch_end(self, batch, logs={}):
        self.train_loss.append(logs.get('loss'))
        self.val_loss.append(logs.get('val_loss'))
        self.train_acc.append(logs.get('accuracy'))
        self.val_acc.append(logs.get('val_accuracy'))
        if self.epoch%10 == 0:
            print("epoch:{:3d}, loss:{}, val_loss:{}".format(self.epoch, 
                                                          logs.get('loss'), logs.get('val_loss')))
        self.epoch +=1
            
#1. 데이터셋 준비하기
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
#훈련셋과 검증셋 분리(X_train, Y_train을 검증셋과 훈련셋으로 분리)
X_val = X_train[50000:]
Y_val = Y_train[50000:]
X_train = X_train[:50000]
Y_train = Y_train[:50000]
#1차원으로 바꾸고, scale 맞춰야 함
#normalize하기 위해 색상값(255.0)으로 나눔 #28*28=784
X_train = X_train.reshape(50000, 784).astype('float32') / 255.0 
X_val = X_val.reshape(10000, 784).astype('float32') / 255.0
X_test = X_test.reshape(10000, 784).astype('float32') / 255.0
#훈련셋과 검증셋 700개, 300개씩 가져옴
train_rand_idx = np.random.choice(50000, 700)
val_rand_idx = np.random.choice(10000, 300)
X_train = X_train[train_rand_idx]
Y_train = Y_train[train_rand_idx]
X_val = X_val[val_rand_idx]
Y_val = Y_val[val_rand_idx]
#라벨링 처리(원 핫 인코딩)
#1 => 0 1 0 0 0 0 0 0 0 0 
#9 => 0 0 0 0 0 0 0 0 0 1
Y_train = utils.to_categorical(Y_train)
Y_val = utils.to_categorical(Y_val)
Y_test = utils.to_categorical(Y_test)

#2. 모델 구성하기
model = Sequential()
model.add(Dense(units=2, input_dim=784, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#3. 모델학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

#4. 모델 학습시키기
custom_hist = CustomHistory()
hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10,
                 validation_data=(X_val, Y_val), verbose=0,
                 callbacks=[custom_hist])


# ## 2. Early Stopping
# ### 2-1. 성급한 조기종료: EarlyStopping()
# - val_loss값이 늘어나면 epoch를 다 수행하지 않고 조기 종료

# In[7]:


(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
#훈련셋과 검증셋 분리(X_train, Y_train을 검증셋과 훈련셋으로 분리)
X_val = X_train[50000:]
Y_val = Y_train[50000:]
X_train = X_train[:50000]
Y_train = Y_train[:50000]
#1차원으로 바꾸고, scale 맞춰야 함
#normalize하기 위해 색상값(255.0)으로 나눔 #28*28=784
X_train = X_train.reshape(50000, 784).astype('float32') / 255.0 
X_val = X_val.reshape(10000, 784).astype('float32') / 255.0
X_test = X_test.reshape(10000, 784).astype('float32') / 255.0
#훈련셋과 검증셋 700개, 300개씩 가져옴
train_rand_idx = np.random.choice(50000, 700)
val_rand_idx = np.random.choice(10000, 300)
X_train = X_train[train_rand_idx]
Y_train = Y_train[train_rand_idx]
X_val = X_val[val_rand_idx]
Y_val = Y_val[val_rand_idx]
#라벨링 처리(원 핫 인코딩)
#1 => 0 1 0 0 0 0 0 0 0 0 
#9 => 0 0 0 0 0 0 0 0 0 1
Y_train = utils.to_categorical(Y_train)
Y_val = utils.to_categorical(Y_val)
Y_test = utils.to_categorical(Y_test)

#2. 모델 구성하기
model = Sequential()
model.add(Dense(units=2, input_dim=784, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
#3. 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='sgd', 
              metrics=['accuracy'])
#4. 모델 학습시키기
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping()
hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10,
                validation_data=(X_val, Y_val), verbose=1,
                callbacks=[early_stopping]) #val_loss가 늘어나게 되면 학습 조기종료 시킴(성급한 조기종료)

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
##val_loss가 증가하면 바로 학습이 종료됨(성급한 조기종료)


# ### 2-2. 적절한 조기종료: EarlyStopping(patience = num)
# - patience: 개선 없다고 바로 종료하지 않고 개선이 없는 에포크를 얼마나 기다려줄 지 지정
# - 개선이 없는 에포크가 num번째 지속될 경우 학습 종료

# In[9]:


(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
#훈련셋과 검증셋 분리(X_train, Y_train을 검증셋과 훈련셋으로 분리)
X_val = X_train[50000:]
Y_val = Y_train[50000:]
X_train = X_train[:50000]
Y_train = Y_train[:50000]
#1차원으로 바꾸고, scale 맞춰야 함
#normalize하기 위해 색상값(255.0)으로 나눔 #28*28=784
X_train = X_train.reshape(50000, 784).astype('float32') / 255.0 
X_val = X_val.reshape(10000, 784).astype('float32') / 255.0
X_test = X_test.reshape(10000, 784).astype('float32') / 255.0
#훈련셋과 검증셋 700개, 300개씩 가져옴
train_rand_idx = np.random.choice(50000, 700)
val_rand_idx = np.random.choice(10000, 300)
X_train = X_train[train_rand_idx]
Y_train = Y_train[train_rand_idx]
X_val = X_val[val_rand_idx]
Y_val = Y_val[val_rand_idx]
#라벨링 처리(원 핫 인코딩)
#1 => 0 1 0 0 0 0 0 0 0 0 
#9 => 0 0 0 0 0 0 0 0 0 1
Y_train = utils.to_categorical(Y_train)
Y_val = utils.to_categorical(Y_val)
Y_test = utils.to_categorical(Y_test)

#2. 모델 구성하기
model = Sequential()
model.add(Dense(units=2, input_dim=784, activation='relu'))
model.add(Dense(units=10, activation='softmax'))
#3. 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='sgd', 
              metrics=['accuracy'])
#4. 모델 학습시키기
from tensorflow.keras.callbacks import EarlyStopping
early_stopping = EarlyStopping(patience=20) #patience=수 만큼 val_loss 오를 수 있음
hist = model.fit(X_train, Y_train, epochs=1000, batch_size=10,
                validation_data=(X_val, Y_val), verbose=1,
                callbacks=[early_stopping])

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


# In[10]:


#6. 모델 평가하기
loss_and_matrics = model.evaluate(X_test, Y_test, batch_size=32)
print()
print('loss_and_metrics:', loss_and_matrics)


# ## 3. 상기 모델(DNN)의 accuracy 늘리기
# <ol>
# <li>많은 데이터 확보</li>
# <li>레이어</li>
# <li>활성화 함수: 은닉층에는 주로 relu, elu <br>
#     output layer에는 sigmoid(이진분류), softmax(다중분류)</li>
# <li>optimizer, epoch 등을 조정</li>
# </ol>

# In[11]:


#1. 데이터셋 준비하기
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()
#훈련셋과 검증셋 분리(X_train, Y_train을 검증셋과 훈련셋으로 분리)
X_val = X_train[50000:]
Y_val = Y_train[50000:]
X_train = X_train[:50000]
Y_train = Y_train[:50000]
#1차원으로 바꾸고, scale 맞춰야 함
#normalize하기 위해 색상값(255.0)으로 나눔 #28*28=784
X_train = X_train.reshape(50000, 784).astype('float32') / 255.0 
X_val = X_val.reshape(10000, 784).astype('float32') / 255.0
X_test = X_test.reshape(10000, 784).astype('float32') / 255.0
#훈련셋과 검증셋 700개, 300개씩 가져옴 ###데이터 양 늘리기 위해 주석 처리###
# train_rand_idx = np.random.choice(50000, 700)
# val_rand_idx = np.random.choice(10000, 300)
# X_train = X_train[train_rand_idx]
# Y_train = Y_train[train_rand_idx]
# X_val = X_val[val_rand_idx]
# Y_val = Y_val[val_rand_idx]
#라벨링 처리(원 핫 인코딩)
#1 => 0 1 0 0 0 0 0 0 0 0 
#9 => 0 0 0 0 0 0 0 0 0 1
Y_train = utils.to_categorical(Y_train)
Y_val = utils.to_categorical(Y_val)
Y_test = utils.to_categorical(Y_test)

#2. 모델 구성하기
model = Sequential()
model.add(Dense(units=256, input_dim=784, activation='relu'))
model.add(Dense(units=512, activation='relu'))
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

#3. 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', 
              metrics=['accuracy'])
#4. 모델 학습시키기
from tensorflow.keras.callbacks import EarlyStopping
#early_stopping = EarlyStopping() #성급한 조기종료
early_stopping = EarlyStopping(patience=10) #patience=수 만큼 val_loss 오를 수 있음
hist = model.fit(X_train, Y_train, epochs=20, batch_size=10,
                validation_data = (X_val, Y_val), verbose=1,
                callbacks=[early_stopping])


# In[12]:


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


# In[13]:


#6. 모델 평가하기
loss_and_matrics = model.evaluate(X_test, Y_test, batch_size=32)
print()
print('loss_and_metrics:', loss_and_matrics)


# In[15]:


#7. 모델 사용하기
idx = np.random.choice(X_test.shape[0],5)
xhat = X_test[idx]
yhat = model.predict(xhat)


# In[16]:


np.argmax(yhat,axis=1) #예측값


# In[17]:


np.argmax(Y_test[idx], axis=1) #실제 값


# In[19]:


for i in range(len(yhat)):
    print(i, "번째 실제값:", np.argmax(Y_test[idx[i]]), '\t예측값:', np.argmax(yhat[i]))


# In[20]:


#8. 모델 저장하기
model.save('model/mnist.h5')


# In[21]:


#9. 모델 재사용하기
from tensorflow.keras.models import load_model
model2 = load_model('model/mnist.h5')
model2.predict_classes(xhat)


# In[ ]:




