#!/usr/bin/env python
# coding: utf-8

# **21-03-25 자연어처리 01_NLTK 자연어 처리 패키지 (c)cherryuki (ji)**

# # ch01. NLTK 자연어 처리 패키지
# - 텍스트 마이닝(Text Mining); 비정형 문서 데이터로부터 문서별 단어의 행렬을 만든 후, 여러가지 분석기법과 데이터 마이닝 기법을 사용하여 Insight를 얻거나 의사결정을 지원하기 위해 사용
# - 비정형 데이터(문서) -> 말뭉치(Corpus) -> 구조화된 문서 -> 분석(분류, 군집, 연관, 감성 등)

# ## 1. NLTK 패키지

# In[2]:


import nltk


# In[3]:


#아래 경로 중 하나에 다운로드 받아야 함(다른 곳X)
##book 선택 후 -> 경로 지정(d:/nltk_data) -> 다운로드
#c:/nltk_data
#d:/nltk_data
#e:/nltk_data
#c:/Users/컴퓨터이름/nltk_data
#c:/Users/컴퓨터이름/anaconda3/nltk_data
#c:/Users/컴퓨터이름/anaconda3/share/nltk_data
#c:/Users/컴퓨터이름/anaconda3/lit/nltk_data
#c:/Users/컴퓨터이름/AppData/nltk_data
nltk.download()
#원하는 말뭉치만 다운 받을 수 있음
#nltk.download("book") 


# In[4]:


from nltk.book import *


# In[5]:


#말뭉치(corpus) 리스트
nltk.corpus.gutenberg.fileids()


# In[6]:


emma = nltk.corpus.gutenberg.raw('austen-emma.txt')
print(emma[:20])


# In[7]:


len(emma)


# In[8]:


#sent_tokenize(); 문장 단위로 나눈 list 반환
from nltk.tokenize import sent_tokenize
sent_tokens = sent_tokenize(emma)
print('문장 수:', len(sent_tokens))
print('%r' %(sent_tokens[10]))


# In[9]:


#word_tokenize(); 단어 단위로 쪼갠 list 반환
from nltk.tokenize import word_tokenize
word_tokenize(sent_tokens[10])


# In[10]:


#print(sent_tokens[0])
#토큰화할 때 정규표현식 이용: ReqexpTokenizer 클래스 이용
from nltk.tokenize import RegexpTokenizer
ret = RegexpTokenizer('[\w]+')
print(ret.tokenize(sent_tokens[10]))
#[\w]=[0-9a-zA-Z]


# ## 2. 형태소(의미가 있는 가장 작은 말의 단위) 분석
# - 어간 추출(Stemming)
# - 원형 복원(Lemmatizing)
# - 품사 부착(Part Of Speech Tagging)

# In[11]:


words=['sending', 'cooking', 'files', 'lives', 'crying', 'dying']


# In[12]:


#어간 추출(1); PorterStemmer
from nltk.stem import PorterStemmer
pst = PorterStemmer()
pst.stem(words[0])


# In[13]:


[pst.stem(word) for word in words]


# In[14]:


#어간 추출(2); LancasterStemmer
from nltk.stem import LancasterStemmer
lst = LancasterStemmer()
[lst.stem(word) for word in words]


# In[15]:


#어간 추출(3); RegexpStemmer
from nltk.stem import RegexpStemmer
rst = RegexpStemmer('ing')
[rst.stem(word) for word in words]


# In[16]:


#어간 추출을 하면 의미가 달라질 수 있어 원형 복원을 함
words2 = ['cooking', 'believes']
[lst.stem(word) for word in words2]


# In[17]:


#원형 복원
from nltk.stem.wordnet import WordNetLemmatizer
wl = WordNetLemmatizer()
[wl.lemmatize(word) for word in words2]


# In[18]:


[wl.lemmatize(word, pos='v') for word in words2]


# In[19]:


#품사 태깅(POS Tagging)
from nltk.tag import pos_tag
tagged_list = pos_tag(word_tokenize(sent_tokens[10]))
print(word_tokenize(sent_tokens[10]))
print('\n품사 태깅 결과')
print(tagged_list)


# ## 퀴즈: emma 소설 안에서
# 1. 특수문자가 들어가지 않은 3글자 이상의 단어만 추출해서 품사 태깅하기
# 2. Emma 단어의 품사 태깅이 어떤 품사들로 되어 있는지 모두 출력하기
# 3. 내가 원하는 품사(명사)의 단어만 뽑아 등장하는 명사의 종류 갯수를 출력하기

# In[20]:


#1.
ret = RegexpTokenizer('[\w]{3,}')
emma_tags = pos_tag(ret.tokenize(emma))


# In[21]:


emma_tags[:10]


# In[22]:


len(emma_tags)


# In[23]:


emma_tags[0][0], emma_tags[0][1]


# In[24]:


#2. 
pos = set()
cnt = 0
for emma_t in emma_tags:
    if emma_t[0] == 'Emma':
        cnt+=1
        pos.add(emma_t[1])
print(cnt)
print(pos)


# In[26]:


import pandas as pd
pos_cnt = pd.Series([0]*len(pos), index=list(pos))
for emma_t in emma_tags:
    if emma_t[0]=='Emma':
        pos_cnt[emma_t[1]] += 1
pos_cnt


# In[28]:


#3.
noun_list = [emma_t[0] for emma_t in emma_tags if emma_t[1]=='NN']
print('명사가 나온 횟수:', len(noun_list))
print('명사 종류:', len(set(noun_list)))
print('한 단어가 나오는 평균 빈도수:', len(noun_list)/len(set(noun_list)))


# In[29]:


noun_list = []
for emma_t in emma_tags:
    if emma_t[1]=='NN':
        noun_list.append(emma_t[0])
len(noun_list)


# In[30]:


#특수문자 제외한 3글자 이상의 전체 단어들
words = ret.tokenize(emma)


# In[31]:


from nltk import Text
emma_text = Text(words)
emma_text


# In[32]:


emma_text.plot(20)


# In[33]:


noun_text = Text(noun_list)
noun_text.plot(20)


# In[34]:


noun_text.dispersion_plot(['thing', 'idea', 'sort', 'Emma']) #Emma를 NN으로는 총 7번 밖에 없음


# In[35]:


nnp_list = [t[0] for t in emma_tags if t[1]=='NNP']
len(set(nnp_list)), len(nnp_list)


# In[36]:


from nltk import FreqDist
FreqDist(nnp_list)


# In[ ]:




