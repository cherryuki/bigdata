#!/usr/bin/env python
# coding: utf-8

# **21-03-26 자연어처리 02_한글 형태소 분석 (c)cherryuki (ji)**

# # Ch02. 한글 형태소 분석
# ## 1. 자연어 처리
# - 자연어(사람들이 일상적으로 사용하는 언어, NLP) 처리
# - 자연어 처리 분야
#   - 자연어 이해: 형태소 분석 -> 의미 분석 -> 대화 분석
#   - 자연어 생성: 대화 분석 -> 다음 문장이나 단어 출력
# - 활용 분야: 맞춤법 검사, 번역기, 검색 엔진, 키워드 분석 등
# 
# ## 2. 자연어 처리 절차
# - 전처리: 단어, 어절 추출
# - 분석 후보 생성: 형태소(의미를 가진 최소 단위) 분리, 원형 복원, 품사 태깅
# - 제약조건(불용어 처리) 규칙 확인
# - 분석
# 
# ## 3. 한글 형태소 분석 엔진
# - KoNLPy: 파이썬용 자연어 처리기(JPype1 패키지 의존)
#   - https://konlpy.org/en/latest/
#   - https://pypi.org/project/JPype1/#files (JPype1-1.2.1-cp38-cp38-win_amd64.whl)
#   - KOMORAN: 자바로 만든 형태소 분석기(JAVA_HOME 시스템 변수)
#     - https://shineware.tistory.com/entry/KOMORAN-ver-24
#   - HanNanum: 자바로 만든 형태소 분석기(JAVA_HOME 시스템 변수)
#     - http://semanticweb.kaist.ac.kr/home/index.php/HanNanum
#   - Kkma: 서울대학교 연구실
#     - http://kkma.snu.ac.kr/documents/index.jsp
# - KoNLP: R용 자연어 처리기
#   - https://github.com/haven-jeon/KoNLP

# In[1]:


#아나콘다에서 pip install JPype1
#다운로드 안될 경우 !pip install JPype1-1.2.1-cp38-cp38-win_amd64.whl
#KoNLPy 패키지 install: 아나콘다에서 pip install konlpy


# In[2]:


get_ipython().system(' pip install JPype1-1.2.0-cp38-cp38-win_amd64.whl')


# In[2]:


text = """아름답지만 다소 복잡하기도한 한국어는 전세계에서 13번째로 많이
사용되는 언어입니다."""


# ### 3.1 HanNanum

# In[5]:


from konlpy.tag import Hannanum
han = Hannanum()
han.analyze(text)  #Hannanum (ntags=69)


# ### 형태소 분석 및 품사 태깅
# - Korean POS tags comparison chart: https://docs.google.com/spreadsheets/d/1OGAjUvalBuX-oZvZ_-9tEfYD2gQe7hTGsgUpiiBSXI8/edit#gid=0

# In[6]:


#형태소 분석만
print(han.morphs(text))


# In[7]:


#품사 태깅
print(han.pos(text, ntags=9)) #han.pos()의 기본값 ntags=9


# In[8]:


print(han.pos(text, ntags=22)) #han.post()의 ntags는 9, 22 중 선택 가능 (26, 69는 불가능)


# In[9]:


#text중에 형용사(PA)만 추출
tagged_text = han.pos(text, ntags=22)
[t[0] for t in tagged_text if t[1]=='PA']


# In[10]:


#명사만 추출할 경우: han.nouns()
han.nouns(text)


# ### 3.2 Kkma

# In[11]:


from konlpy.tag import Kkma
kkma = Kkma(max_heap_size=1024) #힙 메모리 사이즈 증가시킬 때 사용
print(kkma.morphs(text))#형태소 분석만


# In[12]:


#품사 태깅
print(kkma.pos(text)) #kkma(ntags=56)


# In[13]:


#보통명사(NNG)만 추출
tagged_text = kkma.pos(text)
[t[0] for t in tagged_text if t[1]=='NNG']


# In[14]:


#명사만 추출할 경우: kkma.nouns()
kkma.nouns(text)


# ### 3.3 Komoran

# In[3]:


from konlpy.tag import Komoran
komoran = Komoran(max_heap_size=1024) #heap memory; 변수 저장하는 메모리
print(komoran.morphs(text)) #형태소 분석만


# In[4]:


#품사 태깅
print(komoran.pos(text)) #ntags=42


# In[5]:


#일반명사(NNG)만 추출
tagged_text = komoran.pos(text)
[t[0] for t in tagged_text if t[1]=='NNG']


# In[6]:


#명사만 추출할 경우: komoran.nouns()
print(komoran.nouns(text))


# ## 4. 말뭉치(Corpus)
# - C:\Users\컴퓨터이름\anaconda3\Lib\site-packages\konlpy\data\corpus 위치에 data저장되어 있음

# In[7]:


print(r'Hello\nWorld') #r: raw data
print('Hello\nWorld')


# In[8]:


from konlpy.corpus import kolaw
data = kolaw.open('constitution.txt').read()
print(len(data))
print(data[:100])


# In[10]:


from konlpy.corpus import kobill
data1 = kobill.open('1809890.txt').read()[:1000] #1809890.txt - 1809899.txt 가능
data1


# ## 5. 워드 클라우드

# In[11]:


type(data)


# In[12]:


i = 20
print("i={:d}".format(i))
print("i=%d"%(i))


# In[13]:


#명사만 추출
word_list = komoran.nouns("%r" %data) # \n포함한 명사만 추출할 때 %r 이용
print("명사 출현 수:", len(word_list))
print("출현 명사 종류:", len(set(word_list)))
print("단어당 평균 출현 빈도:", len(word_list)/len(set(word_list)))
print(type(word_list))


# In[14]:


word_list[:10]


# In[15]:


#워드 클라우드 만들기 위해 리스트를 하나의 문장 형태로 변경
text = ' '.join(word_list)
text[:10]


# In[16]:


#아나콘다 prompt에서 pip install wordcloud


# In[17]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from wordcloud import WordCloud


# In[18]:


#아무런 설정 없이 기본값으로만 워드클라우드 생성
wordc = WordCloud()
wordc.generate(text)


# In[19]:


plt.figure()
plt.imshow(wordc, interpolation='bilinear') #한글 깨짐


# In[20]:


wordc = WordCloud(background_color='white', max_words=300,
                 font_path='c:/Windows/Fonts/malgun.ttf',
                 relative_scaling=0.2)
wordc.generate(text)


# In[21]:


plt.figure(figsize=(10,5))
plt.imshow(wordc, interpolation='bilinear')
plt.axis('off') #축 제거


# In[22]:


#일반 명사만 추출
tagged_data = komoran.pos(data)
nng_list = [t[0] for t in tagged_data if t[1]=='NNG']
print('일반명사 출현 수:', len(nng_list))
print('출현 일반명사 종류:', len(set(nng_list)))
print('단어당 평균 출현 빈도:', len(nng_list)/len(set(nng_list)))
print(type(nng_list))

#워드 클라우드 위한 형태 변경(리스트 -> 하나의 문장 형태)
nng_text = ' '.join(nng_list)

#워드 클라우드 작업
wordc = WordCloud(background_color='white',
                 max_words=300, #최대로 나올 수 있는 단어 수
                 font_path='c:/Windows/Fonts/malgun.ttf',
                 relative_scaling=0.2)
wordc.generate(nng_text)

#워드 클라우드 그리기
wordc.generate(nng_text)
plt.figure(figsize=(10,5))
plt.imshow(wordc, interpolation='bilinear')
plt.axis('off')


# ### 5.1 불용어 처리(불용어 사전 + 불용어 추가)
# - 워드 클라우드 생성시 제외시킬 단어 지정

# In[23]:


from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
from wordcloud import STOPWORDS
print(list(ENGLISH_STOP_WORDS)[:10]) #불용어 사전(영어)
print(list(STOPWORDS)[:10]) #불용어 사전(영어)


# In[24]:


#불용어 처리(불용어 사전+불용어 추가); 불용어 추가시에는 반드시 set()으로 추가해야함
불용어 = STOPWORDS | ENGLISH_STOP_WORDS | set(['대통령', '법관'])
#불용어 사전(영어)이 필요 없을 경우 아래와 같이 설정하는 것도 가능
불용어 = set(['대통령', '법관'])


# In[26]:


#워드 클라우드 작업
wordc = WordCloud(background_color='white',
                 max_words=300,
                 font_path='c:/Windows/Fonts/H2PORM.TTF',
                 relative_scaling=0.2,
                 stopwords=불용어) #워드 클라우드에서 불용어 제외시키기
wordc.generate(nng_text)

#워드 클라우드 그리기
wordc.generate(nng_text)
plt.figure(figsize=(10,5))
plt.imshow(wordc, interpolation='bilinear')
plt.axis('off')


# ### 5.2 마스킹
# - 워드 클라우드를 지정된 마스크 이미지에 맞도록 처리

# In[27]:


import os
os.getcwd() 


# In[28]:


#마스킹; 워드 클라우드를 지정된 마스크 이미지에 맞도록 표시
from PIL import Image
import numpy as np
img = Image.open('data/south_korea.png').convert('RGBA')
#png 파일: 'RGBA'로 jpg 파일: 'RGB'로 convert
mask = Image.new('RGB', img.size, (0,0,0))
mask.paste(img)
plt.imshow(mask)
mask=np.array(mask) #넘파이 배열로 바꾸기


# In[29]:


wordcloud = WordCloud(background_color='white',
                     max_words=500,
                     font_path='C:/Windows/Fonts/malgun.ttf',
                     relative_scaling=0.1,
                     mask=mask) #마스크 된 부분에만 글자 나오게
wordcloud.generate(nng_text)
plt.figure(figsize=(5,8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')


# In[30]:


#워드 클라우드 저장
wordcloud.to_file('data/ch02_south_korea.png')


# In[31]:


img = Image.open('data/test3.png').convert('RGBA')
mask = Image.new('RGB', img.size, (0,0,0))
mask.paste(img)
plt.imshow(mask)
mask = np.array(mask) #넘파이 배열로 바꾸기

wordcloud = WordCloud(background_color='white',
                     max_words=500,
                     font_path='C:Windows/Fonts/malgun.ttf',
                     relative_scaling=0.1,
                      stopwords = 불용어,
                      mask=mask)
wordcloud.generate(nng_text)
plt.figure(figsize=(5,7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')


# ## 6. 단어 빈도수 계산

# In[32]:


import nltk
import matplotlib.pyplot as plt
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina' #그래프 선명하게")
plt.rc('font', family='Malgun Gothic') #한글 폰트 설정
word_list = komoran.nouns(data)
nltk.Text(word_list).plot(10)


# ## 7. 워드 임베딩(Word Embedding)
# - 단어간 유사성 도출

# In[33]:


#뉴스 기사 link들 list 가져오기 (RSS이용: https://fs.jtbc.joins.com//RSS/economy.xml)
import requests
from bs4 import BeautifulSoup
rss_url = 'https://fs.jtbc.joins.com//RSS/economy.xml'
jtbc_economy = requests.get(rss_url)
economy_soup = BeautifulSoup(jtbc_economy.content, 'xml')
link_list = economy_soup.select('item > link')
link_list = [link.text for link in link_list]
link_list


# In[36]:


#뉴스 기사들 명사들만 추출해서 워드 임베딩하기 편하게 만들기
from konlpy.tag import Kkma
kkma = Kkma()
news = []
for link in link_list:
    news_response = requests.get(link)
    news_soup = BeautifulSoup(news_response.content, 'html.parser')
    news_title = news_soup.select_one('h3#jtbcBody') #기사 제목
    news_content = news_soup.select_one('div#articlebody > div.article_content') #기사 내용 (div 생략 가능)
    content = news_title.text + ' ' + news_content.text
    news.append(kkma.nouns(content))


# In[37]:


print(news[0])


# In[38]:


#리스트별 명사 개수
print([len(n) for n in news])


# In[39]:


#워드 임베딩하기
##아나콘다 prompt에서 conda install gensim 
##pip로 설치해서 넘파이에러 발생시 넘파이 패키지 삭제 후 다시 설치하기 (pip uninstall numpy ->  pip install numpy) 
from gensim.models import Word2Vec
model = Word2Vec(news, size=100, window=5, min_count=2, workers=-1) #min_count=num; num번 이상 나온 단어만


# In[40]:


model.wv.most_similar('코로나')


# In[41]:


model.wv.most_similar('코로나', topn=5)


# In[ ]:




