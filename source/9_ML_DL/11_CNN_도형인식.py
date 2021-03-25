#!/usr/bin/env python
# coding: utf-8

# **21-03-25 ML_DL 11_CNN 도형인식 (c)cherryuki (ji)**

# # 11_CNN 도형(삼각형, 사각형, 원) 인식
# ### CNN: Convolutional Neural Network

# In[1]:


import matplotlib.pyplot as plt
c0 = plt.imread('data/handwriting_shape/train/circle/circle001.png')
plt.imshow(c0)
print(c0.shape)
print(type(c0))


# In[2]:


import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D #필터링(; 패턴 특징 추출)
from tensorflow.keras.layers import MaxPool2D #풀링(최대풀링; 데이터(영상) 크기 줄여줌. 사소한 변화 무시)
from tensorflow.keras.layers import Flatten #2차원 영상 데이터를 1차원으로
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.preprocessing.image import ImageDataGenerator


# In[3]:


#1. 데이터 생성
train_datagen = ImageDataGenerator(rescale=1./255) #정규화 작업(scale 맞추기)
train_generator = train_datagen.flow_from_directory('data/handwriting_shape/train',
                                                   target_size=(24,24), batch_size=3,
                                                   class_mode='categorical')
#class_mode='categorical'; 다중분류 원핫 인코딩
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory('data/handwriting_shape/test',
                                                 target_size=(24,24),
                                                 batch_size=3,
                                                 class_mode='categorical') #다중분류 원핫 인코딩


# In[4]:


#2. 모델 구성
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(24,24,3)))
#input_shape=(행, 열, 채널 수)
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2))) #2*2에서 제일 큰 값만 뽑아 이미지 축소
model.add(Flatten()) #2차원 이미지데이터를 1차원으로
model.add(Dense(128, activation='relu'))
model.add(Dense(3, activation='softmax'))


# In[5]:


#3. 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[6]:


#4. 모델 학습 시키기
model.fit_generator(train_generator, steps_per_epoch=15,
                   epochs=50,
                   validation_data=test_generator,
                   validation_steps=5)


# In[7]:


#5. 모델 평가하기
score=model.evaluate_generator(test_generator, steps=5)
print('loss:', score[0])
print('accuracy:', score[1])


# In[8]:


#6. 예측하기
pred = model.predict_generator(test_generator)
print(test_generator.class_indices)
np.set_printoptions(formatter={'float':lambda x:"{:0.2f}".format(x)})
print(pred)
print(pred.argmax(axis=1))


# ## 상기 예제 accuracy 높이기
# 1. 데이터 확보, 데이터 양 늘리기(ImageDataGenerator)
# 2. 레이어 층

# In[9]:


#1. 데이터 생성
#데이터 부풀리기 - 이미지 회전 등
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=10,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.7, #0.7 라디안 밀림
                                   zoom_range=[0.9,2.2], # 0.9배~2.2배
                                   horizontal_flip=True, # 수평방향으로 뒤집기
                                   vertical_flip=True, # 수직방향으로 뒤집기
                                   fill_mode='nearest')#이미지를 회전, #이동하거나 축소할 때 공간을 채우는 방식

train_generator = train_datagen.flow_from_directory('data/handwriting_shape/train',
                                                   target_size=(24,24), batch_size=3,
                                                   class_mode='categorical')
test_datagen = ImageDataGenerator(rescale=1./255)
test_generator = test_datagen.flow_from_directory('data/handwriting_shape/test',
                                                 target_size=(24,24), batch_size=3,
                                                 class_mode='categorical')


# In[10]:


#2. 모델 구성
model = Sequential()
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=(24,24,3)))
model.add(Conv2D(32, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2))) #최대 풀링; 2*2에서 제일 큰 값만 뽑아 이미지 축소
model.add(Dropout(0.1)) #과적합 막는 목적
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.1))
model.add(Flatten()) #2차원 이미지데이터를 1차원으로
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.1))
model.add(Dense(3, activation='softmax'))

#3. 모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[12]:


#4. 모델 학습 시키기
model.fit_generator(train_generator, steps_per_epoch=15,
                   epochs=50,
                   validation_data=test_generator,
                   validation_steps=5)


# In[14]:


#5. 모델 평가하기
score=model.evaluate_generator(test_generator, steps=5)
print('loss:', score[0])
print('accuracy:', score[1])

#6. 예측하기
pred = model.predict_generator(test_generator)
print(test_generator.class_indices)
np.set_printoptions(formatter={'float':lambda x:"{:0.2f}".format(x)})
print(pred.argmax(axis=1))
print(pred)


# In[ ]:




