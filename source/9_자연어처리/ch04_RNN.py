#!/usr/bin/env python
# coding: utf-8

# **21-03-29 자연어처리 04_RNN (c)cherryuki (ji)**

# # ch04. RNN(순환 신경망)
# ## 1. 문맥을 이용하여 모델 만들기

# In[1]:


text = """경마장에 있는 말이 뛰고 있다
그의 말이 법이다
가는 말이 고와야 오는 말이 곱다
"""


# In[2]:


from keras_preprocessing.text import Tokenizer
t = Tokenizer()
t.fit_on_texts([text])
encoded = t.texts_to_sequences([text])[0]
print(encoded)
print(t.word_index)


# In[3]:


t.texts_to_sequences(['있다'])[0]


# In[4]:


t.texts_to_sequences(['경마장에 있는 말이 뛰고 있다'])[0]


# In[5]:


sequences = []
for line in text.split('\n'):
    encoded = t.texts_to_sequences([line])[0]
    print('원래 문장:', line)
    print('encoded 문장:', encoded)
    for i in range(0, len(encoded)-1):
        for j in range(i+2, len(encoded)+1):
            sequences.append(encoded[i:j])
#제대로 encode되었는지 확인
print()
for sequence in sequences:
    print('[', end=' ')
    for word_seq in sequence:
        for key, value in t.word_index.items():
            if value==word_seq:
                print("{}:{}".format(value, key), end=' ')
    print(']')


# In[7]:


print([len(s) for s in sequences])


# In[8]:


#sequences에 가장 많은 단어가 들어 있는 개수
maxlen = max([len(s) for s in sequences])
maxlen


# In[9]:


type(sequences), len(sequences)


# In[11]:


#sequences를 훈련가능한 데이터로 만들기
from tensorflow.keras.preprocessing.sequence import pad_sequences
sequences = pad_sequences(sequences=sequences, maxlen=maxlen,
                         padding='pre') #앞에 0을 붙임
type(sequences), len(sequences)


# In[12]:


sequences


# In[13]:


#독립변수(X)와 종속변수(Y) 분리
X = sequences[:, :-1]
Y = sequences[:, -1]
Y


# In[14]:


print(t.word_index)


# In[15]:


vocab_size=len(t.word_index)+1
vocab_size


# In[16]:


#종속변수(Y)를 원핫 인코딩
from tensorflow.keras.utils import to_categorical
Y = to_categorical(Y, num_classes = vocab_size)
Y


# In[17]:


X.shape, Y.shape, vocab_size


# In[18]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, SimpleRNN

#RNN 모델 생성
model = Sequential()
#희소행렬로 변환(10:벡터)
model.add(Embedding(vocab_size, 10, input_length=X.shape[1]))
model.add(SimpleRNN(32))
model.add(Dense(vocab_size, activation='softmax'))

#모델 학습과정 설정
model.compile(loss='categorical_crossentropy', optimizer='adam',
             metrics=['accuracy'])

#모델 학습 시키기
hist = model.fit(X, Y, epochs=200, verbose=2)


# In[19]:


#모델 평가
model.evaluate(X, Y)


# In[20]:


#학습과정 보기
import matplotlib.pyplot as plt
plt.plot(hist.history['loss'], color='r', label='loss')
plt.plot(hist.history['accuracy'], color='g', label='accuracy')
plt.legend()


# In[24]:


#'경마장에' 뒤에 나오는 단어를 model에 의해 추측
encoded = t.texts_to_sequences(['경마장에'])[0]
encoded = pad_sequences([encoded], maxlen=maxlen-1, padding='pre')
result = model.predict_classes(encoded)
print('예측 결과:', result[0])
for key, value in t.word_index.items():
    if result[0]==value:
        print('예측 단어:', key)
        break;


# In[26]:


import numpy as np
#사용자에게 입력받은 단어 다음 말 추측하기
word = input('입력단어: ')
encoded = t.texts_to_sequences([word])[0]
encoded = pad_sequences([encoded], maxlen=maxlen-1, padding='pre')
result = np.argmax(model.predict(encoded))
print('예측 결과:', result)
for key, value in t.word_index.items():
    if result==value:
        print('예측 단어:', key)
        break;


# ## 2. 다음 문맥 예측하기

# In[29]:


#'가는' 이후에 올 단어 5개 예측 => 가는 말이 고와야 오는 말이 곱다
# ----                 ---
def sentence_generation(model, t, current_word, n):
    init_word = current_word
    print("입력 단어 :", init_word)
    for i in range(1,n+1):
        encoded = t.texts_to_sequences([current_word])[0]
        encoded = pad_sequences([encoded], maxlen=maxlen-1, padding='pre')
        result = np.argmax(model.predict(encoded))
        for word, index in t.word_index.items():
            if index==result:
                print("{}번째 : {}:{}".format(i, word, result))
                current_word = current_word + ' ' + word
                break;
    return current_word


# In[31]:


sentence_generation(model, t, '경마장에 있는', 3)


# In[32]:


sentence_generation(model, t, '가는', 5)


# ## 3. LSTM

# In[35]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

#모델 생성
model = Sequential()
#희소행렬로 변환 (10:벡터)
model.add(Embedding(vocab_size, 10, input_length=X.shape[1]))
model.add(LSTM(32))
model.add(Dense(vocab_size, activation="softmax"))

#모델 학습과정 설정
model.compile(loss="categorical_crossentropy", optimizer="adam", 
              metrics=['accuracy'])

# 학습시키기
hist = model.fit(X, Y, epochs=250, verbose=2)


# In[ ]:




