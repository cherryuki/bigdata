#!/usr/bin/env python
# coding: utf-8

# **python 타겟팅_웹크롤링 및 전처리 워드클라우드, 연관분석 (c)cherryuki (ji)**

# # Project (2021-04-01~2021-04-07)
# ## 01. 자료수집
# ### 1) 뉴스 기사 웹크롤링('대체식품', '대체육' 타겟팅)
# - 식음료신문
# - 농수축산식품(식품, 이슈플러스)
# - 식품외식경제
# - 식품저널뉴스

# In[1]:


#식음료신문: http://www.thinkfood.co.kr/news/articleList.html?page=2&total=3642&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=%EB%8C%80%EC%B2%B4&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm
#div.list-titles > a 기사링크
#기사제목: div.list-titles > a > strong 
#기사 페이지 기사 제목: div.article-head-title
#기사 내용: article.article-veiw-body
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
result_df = pd.DataFrame(None, columns = ['title', 'link', 'date', 'news'])
num=1
index=0
for num in range(1, 11):
    url = 'http://www.thinkfood.co.kr/news/articleList.html?page='+str(num)+'&total=158&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=대체식품&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    link_list = soup.select('div.list-titles > a')
    link_list = ['http://www.thinkfood.co.kr'+link.attrs['href'] for link in link_list]
    date_list = soup.select('div.list-dated')
    date_list = [date.text for date in date_list]
    date_list = ' '.join(date_list)
    date_list = re.findall(r'\d{4}-\d{2}-\d{2}', date_list)
    title_list = soup.select('div.list-titles > a > strong')
    title_list = [title.text for title in title_list]
    for i in range(len(date_list)):
        html = requests.get(link_list[i])
        news_soup = BeautifulSoup(html.content, 'html.parser')
        news_list = news_soup.select('article.article-veiw-body')
        news_list = [news.text for news in news_list]
        result_df.loc[index] = [title_list[i], link_list[i], date_list[i], news_list]
        index+=1
    num+=1


# In[2]:


#대체육
#http://www.thinkfood.co.kr/news/articleList.html?page=2&total=116&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=%EB%8C%80%EC%B2%B4%EC%9C%A1&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm

result_df1 = pd.DataFrame(None, columns = ['title', 'link', 'date', 'news'])
num=1
index=0
for num in range(1, 8):
    url = 'http://www.thinkfood.co.kr/news/articleList.html?page='+str(num)+'&total=116&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=%EB%8C%80%EC%B2%B4%EC%9C%A1&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    link_list = soup.select('div.list-titles > a')
    link_list = ['http://www.thinkfood.co.kr'+link.attrs['href'] for link in link_list]
    date_list = soup.select('div.list-dated')
    date_list = [date.text for date in date_list]
    date_list = ' '.join(date_list)
    date_list = re.findall(r'\d{4}-\d{2}-\d{2}', date_list)
    title_list = soup.select('div.list-titles > a > strong')
    title_list = [title.text for title in title_list]
    for i in range(len(date_list)):
        html = requests.get(link_list[i])
        news_soup = BeautifulSoup(html.content, 'html.parser')
        news_list = news_soup.select('article.article-veiw-body')
        news_list = [news.text for news in news_list]
        result_df1.loc[index] = [title_list[i], link_list[i], date_list[i], news_list]
        index+=1
    num+=1


# In[3]:


result_df.to_csv('data/0_대체식품_식음료식문.csv', sep=',')


# In[4]:


result_df1.to_csv('data/0_대체육_식음료식문.csv', sep=',')


# In[5]:


#식품외식경제: http://www.foodbank.co.kr/news/articleList.html?page=1&total=40&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=%EB%8C%80%EC%B2%B4%EC%8B%9D%ED%92%88&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm&sc_multi_code=
#기사제목: div.list-titles > a 텍스트
#기사 링크: div.list-titles > a href
#날짜: div.list-dated \d{4}-\d{2}-\d{2}
#기사 내용: #article-view-content-div
result_df2 = pd.DataFrame(None, columns = ['title', 'link', 'date', 'news'])
num=1
index=0
for num in range(1, 2):
    url = 'http://www.foodbank.co.kr/news/articleList.html?page='+str(num)+'&total=40&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=대체식품&sc_word2=&sc_andor=&sc_order_by=E&view_type=sm&sc_multi_code='
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    link_list = soup.select('div.list-titles > a')
    link_list = ['http://www.foodbank.co.kr'+link.attrs['href'] for link in link_list]
    date_list = soup.select('div.list-dated')
    date_list = [date.text for date in date_list]
    date_list = ' '.join(date_list)
    date_list = re.findall(r'\d{4}-\d{2}-\d{2}', date_list)
    title_list = soup.select('div.list-titles > a > strong')
    title_list = [title.text for title in title_list]
    for i in range(len(date_list)):
        html = requests.get(link_list[i])
        news_soup = BeautifulSoup(html.content, 'html.parser')
        news_list = news_soup.select('#article-view-content-div')
        news_list = [news.text for news in news_list]
        result_df2.loc[index] = [title_list[i], link_list[i], date_list[i], news_list]
        index+=1
    num+=1


# In[6]:


result_df2.to_csv('data/0_대체식품_식품외식경제.csv', sep=',')


# In[7]:


#대체육, 대체식품
#농수축산신문(식품): https://www.aflnews.co.kr/news/articleList.html?page=1&total=97&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=1999-05-20&sc_edate=2021-04-03&sc_serial_number=&sc_word=%EB%8C%80%EC%B2%B4%EC%8B%9D%ED%92%88&box_idxno=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_order_by=E&view_type=sm
#기사제목: h4.titles > a 텍스트
#기사 링크: h4.titles > a href
#기사 내용: #article-view-content-div
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
result_df3 = pd.DataFrame(None, columns = ['title', 'link', 'date', 'news'])
num=1
index=0
for num in range(1,4):
    url = 'https://www.aflnews.co.kr/news/articleList.html?page='+str(num)+'&total=97&sc_section_code=&sc_sub_section_code=&sc_serial_code=&sc_area=A&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=1999-05-20&sc_edate=2021-04-03&sc_serial_number=&sc_word=%EB%8C%80%EC%B2%B4%EC%8B%9D%ED%92%88&box_idxno=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_order_by=E&view_type=sm'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    link_list = soup.select('h4.titles > a')
    link_list = ['http://www.aflnews.co.kr'+link.attrs['href'] for link in link_list]
    title_list = soup.select('h4.titles > a')
    title_list = [title.text for title in title_list]
    date_list = soup.select('span.byline')
    date_list = [date.text for date in date_list]
    date_list = ' '.join(date_list)
    date_list = re.findall(r'\d{4}.\d{2}.\d{2}', date_list)
    for i in range(len(date_list)):
        html = requests.get(link_list[i])
        news_soup = BeautifulSoup(html.content, 'html.parser')
        news_list = news_soup.select('article#article-view-content-div')
        news_list = [news.text for news in news_list]
        result_df3.loc[index] = [title_list[i], link_list[i], date_list[i], news_list]
        index+=1
    num+=1


# In[8]:


result_df3.to_csv('data/0_대체식품_대체육_농수축산신문.csv', sep=',')


# In[9]:


#식품저널뉴스(전체): https://www.foodnews.co.kr/news/articleList.html?page=1&total=82&box_idxno=&sc_area=A&view_type=sm&sc_word=%EB%8C%80%EC%B2%B4%EC%8B%9D%ED%92%88
#기사제목: h4.titles > a 텍스트
#기사 링크: h4.titles > a href
#날짜 span.byline \d{4}.\d{2}.\d{2}
#기사 내용: #article-view-content-div
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
result_df4 = pd.DataFrame(None, columns = ['title', 'link', 'date', 'news'])
num=1
index=0
for num in range(1, 5):
    url = 'https://www.foodnews.co.kr/news/articleList.html?page='+str(num)+'&total=82&box_idxno=&sc_area=A&view_type=sm&sc_word=대체식품'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    link_list = soup.select('h4.titles > a')
    link_list = ['http://www.aflnews.co.kr'+link.attrs['href'] for link in link_list]
    title_list = soup.select('h4.titles > a')
    title_list = [title.text for title in title_list]
    date_list = soup.select('span.byline')
    date_list = [date.text for date in date_list]
    date_list = ' '.join(date_list)
    date_list = re.findall(r'\d{4}.\d{2}.\d{2}', date_list)
    for i in range(len(date_list)):
        html = requests.get(link_list[i])
        news_soup = BeautifulSoup(html.content, 'html.parser')
        news_list = news_soup.select('#article-view-content-div') 
        news_list = [news.text for news in news_list]
        result_df4.loc[index] = [title_list[i], link_list[i], date_list[i], news_list]
        index+=1
    num+=1


# In[10]:


result_df4.to_csv('data/0_대체식품_식품저널뉴스.csv', sep=',')


# In[11]:


#식품저널뉴스(전체): https://www.foodnews.co.kr/news/articleList.html?page=1&total=82&box_idxno=&sc_area=A&view_type=sm&sc_word=%EB%8C%80%EC%B2%B4%EC%8B%9D%ED%92%88
#기사제목: h4.titles > a 텍스트
#기사 링크: h4.titles > a href
#날짜 span.byline \d{4}.\d{2}.\d{2}
#기사 내용: #article-view-content-div
import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
result_df5 = pd.DataFrame(None, columns = ['title', 'link', 'date', 'news'])
num=1
index=0
for num in range(1, 3):
    url = 'https://www.foodnews.co.kr/news/articleList.html?page='+str(num)+'total=53&box_idxno=&sc_area=A&view_type=sm&sc_word=대체육'
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')
    link_list = soup.select('h4.titles > a')
    link_list = ['http://www.aflnews.co.kr'+link.attrs['href'] for link in link_list]
    title_list = soup.select('h4.titles > a')
    title_list = [title.text for title in title_list]
    date_list = soup.select('span.byline')
    date_list = [date.text for date in date_list]
    date_list = ' '.join(date_list)
    date_list = re.findall(r'\d{4}.\d{2}.\d{2}', date_list)
    for i in range(len(date_list)):
        html = requests.get(link_list[i])
        news_soup = BeautifulSoup(html.content, 'html.parser')
        news_list = news_soup.select('#article-view-content-div') 
        news_list = [news.text for news in news_list]
        result_df5.loc[index] = [title_list[i], link_list[i], date_list[i], news_list]
        index+=1
    num+=1


# In[12]:


result_df5.to_csv('data/0_대체육_식품저널뉴스.csv', sep=',')


# In[13]:


len(result_df), len(result_df1), len(result_df2), len(result_df3), len(result_df4), len(result_df5)


# In[14]:


df = pd.concat([result_df,result_df1,result_df2,result_df3,result_df4,result_df5], ignore_index=True)
df


# In[15]:


df.to_csv('data/00_대체식품_대체육_신문기사.csv', sep=',')


# ### 2) 전처리

# In[16]:


df = df.loc[:, ['title', 'date', 'news']]
df.shape


# In[17]:


#연도, 월 칼럼 추가
df['date'] = df['date'].str.replace('.', '-')
df['year'] = df['date'].apply(lambda x:int(x.split('-')[0]))
df['month'] = df['date'].apply(lambda x:int(x.split('-')[1]))
df.head()


# In[18]:


type(df['news'][0]), type(df['title'][0])


# In[19]:


df['news_nouns'] = df['news']
df['news_nouns'] = [''.join(x) for x in df['news_nouns']]
df['news_nouns']


# In[20]:


df['content'] = df['title']+df['news_nouns']
df['content']


# In[21]:


df[[type(x)==list for x in df['news_nouns']]]


# In[25]:


for i in range(len(df)):
    df.iloc[i,6] = df.iloc[i,6].replace('\t', ' ')


# In[26]:


df.iloc[:,6]


# In[39]:


df.to_csv('data/00_대체식품_대체육_신문기사_전처리1.csv', sep=',')


# In[40]:


import pandas as pd
#df.to_csv('00_대체식품_대체육_신문기사.csv', sep=',')
df1 = pd.read_csv('data/00_대체식품_대체육_신문기사_전처리1.csv')
df1


# In[41]:


from konlpy.tag import Komoran
komoran = Komoran()
df1['content'] = df1['title']+df1['news']


# In[42]:


df1[[type(x)==float for x in df1['title']]]
df1 = df1.dropna()


# In[43]:


df1['content_nouns'] = df1['content'].apply(lambda x:komoran.nouns(x))


# In[44]:


df1.columns


# In[45]:


df1 = df1.loc[:, ['title', 'date', 'news', 'year', 'month', 'content', 'content_nouns']]
df1


# In[46]:


df1.to_csv('data/00_대체식품_대체육_신문기사_전처리완료.csv', sep=',')


# # 02. 연관분석

# In[47]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
from konlpy.tag import Komoran
from wordcloud import WordCloud
plt.rc("font", family="Malgun Gothic") 
komoran = Komoran(max_heap_size=2048)
from nltk import Text
from konlpy.tag import Okt
okt = Okt()


# In[48]:


#df1.to_csv('00_대체식품_대체육_신문기사_전처리완료.csv', sep=',')
df1 = pd.read_csv('data/00_대체식품_대체육_신문기사_전처리완료.csv')


# In[49]:


df1 = df1.drop(['Unnamed: 0', 'date'], axis=1)


# In[50]:


df1


# In[51]:


#일반명사, 고유명사만 추출
df_list=[]
for i in range(len(df1)):
    tagged_text = komoran.pos(df1.loc[i, 'content'])
    for tagged in tagged_text:
        if len(tagged[0])>1:
            if (tagged[1]=='NNG') | (tagged[1]=='NNP'):
                df_list.append(tagged[0])


# In[52]:


len(df_list)


# In[53]:


#단어 빈도수 계산하는 함수
def word_count(word_list):
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


# In[54]:


dic1 = word_count(df_list)
df_word = pd.DataFrame.from_dict([dic1])


# In[55]:


df_word = pd.DataFrame.from_dict([dic1])
df_word = df_word.T
df_word = df_word.sort_values(by=0, ascending=False)
df_word.reset_index(inplace=True)
df_word.columns=['word', 'frequency']


# In[56]:


#df_word.to_csv('data/00_대체식품_대체육_신문기사_단어빈도수.csv', sep=',')
df_word


# In[57]:


df_word2 = df_word[df_word['frequency']>=5]


# In[58]:


df_word2.head(20)


# In[59]:


import seaborn as sns
ax = sns.barplot(x='word', y='frequency', data=df_word2[:20])


# In[60]:


temp = df1['content_nouns']
temp


# In[61]:


temp_list=[]
for t in temp:
    temp = t.replace('[','').replace(']', '').replace("'", '')
    temp = temp.split(", ")
    temp_list.append(temp)


# In[62]:


type(temp_list[0])


# In[63]:


import random
sample_list = random.sample(temp_list, 30)


# In[64]:


type(sample_list[0])


# In[65]:


list1 = df_word2.loc[5:14, 'word']
list1 = list1.reset_index()
list1 = list1['word']


# In[66]:


df_word2[5:15]


# In[67]:


total_list=[]
for temp in temp_list:
    t = [ word for word in list1 if word in temp ]
    if len(t)>0:
        total_list.append(t)


# In[68]:


len(total_list)


# In[69]:


from apyori import apriori
rules = apriori(total_list, min_support=0.3, min_confidence=0.2)
result = list(rules)
len(result)


# In[70]:


import pandas as pd
result_df = pd.DataFrame(None,
                        columns = ['lhs', 'rhs', 'support', 'confidence', 'lift'])
index = 0
for row in result:
    support = row[1]
    ordered_st = row[2]
    for item in ordered_st:
        lhs = ', '.join(x for x in item[0])
        rhs = ', '.join(x for x in item[1])
        confidence = item[2]
        lift = item[3]
        result_df.loc[index] = [lhs, rhs, support, confidence, lift]
        index += 1


# In[71]:


result_df


# In[72]:


result_df[result_df['lift']!=1]


# In[73]:


result_df[result_df['lift']!=1].sort_values(by='lift', ascending=False).head(10)


# In[74]:


result_df[result_df['lift']!=1].sort_values(by=['support', 'confidence'], ascending=False).head(10)


# In[75]:


a = result_df[result_df['lift']>1.2].sort_values(by=['lift', 'support', 'confidence'], ascending=False).head(10)
a


# In[76]:


df_word2.head(20)[['word']]


# In[77]:


df_word[df_word['word']=='환경']


# # 03. 워드 클라우드

# In[78]:


from wordcloud import STOPWORDS
불용어 = set(['기사', '금지', '체육', '기자', '업체', '배포', '무단', '저작권', '전재', '이번', '신문','사용',
          '식품', '음료', '우리나라', '한국', '제품', '최근', '국내', '판매', '산업', '올해', '소비자', 
          '기업', '시장', '경우', '대표', '대체', '사업', '정부', '외식', '관련', '기존'])
wordcloud = WordCloud(background_color='white',
                max_words=300,
                 font_path='c:/Windows/Fonts/H2PORM.TTF',
                 relative_scaling=0.2,
                 stopwords=불용어) #워드 클라우드에서 불용어 제외시키기


# In[79]:


#워드 클라우드 그리기
temp1 = ' '.join(df_list)
wordcloud.generate(temp1)
plt.figure(figsize=(10,10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
wordcloud.to_file('data/wordcloud_대체식품0.jpg')


# In[80]:


df_list[:10]


# In[81]:


temp = df1['content_nouns']


# In[82]:


temp_list=[]
for t in temp:
    temp = t.replace('[','').replace(']', '').replace("'", '')
    temp = temp.split(", ")
    temp_list.append(temp)


# In[83]:


len(temp_list)


# # 04. 워드 임베딩

# In[84]:


from gensim.models import Word2Vec
model = Word2Vec(temp_list, size=500, window=5, min_count=2, workers=-1)


# In[85]:


model.wv.most_similar('식품')


# In[86]:


model.wv.most_similar('대체')


# In[87]:


model.wv.most_similar('환경')


# In[88]:


model.wv.most_similar('건강')


# In[ ]:




