#!/usr/bin/env python
# coding: utf-8

# **21-03-26 자연어처리 03_연관분석 (c)cherryuki (ji)**

# # Ch03. 연관분석
# ## 1. 연관분석 개요
# - 데이터들 사이에서 '자주 발생하는 속성'을 찾는 것
# - 활용분야: 상품진열, 사기보험 적발, 카탈로그 디자인, 신상품 카테고리 구성, ...
# - 연관성 분석 관련 지표: 지지도, 신뢰도, 향상도
#   - 지지도(Support): 조건 결과 항목 / 전체
#   - 신뢰도(Confidence): 조건 결과 항목 / 조건 항목
#   - 향상도(Lift): 우연히 발생한 규칙 여부(상관관계)
#     - 향상도 = 조건결과 신뢰도 / 결과 지지도
#     - 향상도<1: 음의 상관관계, 향상도=1: 상관관계 없음, 향상도>1: 양의 상관관계
# <pre>
# [조건] => [결과]　지지도　신뢰도　향상도
# 주스  =>  콜라     0.4       1      1/1 -> 상관X
# </pre>

# In[1]:


#트랜잭션 데이터 가져오기
import csv
transaction = []
with open('data/cf_basket.csv', 'r', encoding='utf8') as cf:
    csvdata = csv.reader(cf)
    transaction = list(csvdata)


# In[2]:


transaction


# ## 2. 연관분석
# - 아나콘다에서 pip install apyori
# 
# ### 2.1 연관 규칙 조회

# In[4]:


from apyori import apriori
rules = apriori(transaction, min_support=0.2, min_confidence=0.1)
rules = list(rules)
len(rules)


# In[5]:


rules[17]


# In[6]:


rules[0]


# ### 2.2 연관 규칙 평가

# In[7]:


print('조건 \t => \t 결과 \t\t지지도 \t신뢰도 \t향상도')
for row in rules:
    support = row[1]
    ordered_st = row[2]
    for item in ordered_st:
        #lhs = ', '.join(x for in item[0])
        lhs = [x for x in item[0]]
        #rhs = ', 'join(x for x in item[1])
        rhs = [x for x in item[1]]
        confidence = item[2]
        lift = item[3]
        lift = item[3]
        if lift !=1:
            print(lhs, '=>', rhs, '\t{:5.3f}\t{:5.3f}\t{:5.3f}'.format(support, confidence, lift) )
        


# ## 3. 뉴스기사 연관 분석 실습
# ### 3.1 뉴스 RSS 이용해서 기사 검색후 연관분석

# In[2]:


import requests
from bs4 import BeautifulSoup
rss_url = 'https://rss.joins.com/joins_money_list.xml'
money_response = requests.get(rss_url)
money_soup = BeautifulSoup(money_response.content, 'xml')
link_list = money_soup.select('item > link')
# link_list = [l.text for l in link_list]
len(link_list)


# In[4]:


from konlpy.tag import Kkma
kkma = Kkma()
news = []
for link in link_list:
    news_response = requests.get(link.text)
    news_soup = BeautifulSoup(news_response.content, 'html.parser')
    content = news_soup.select_one('div#article_body').text
    nouns_list = list(filter(lambda word: len(word)>1, kkma.nouns(content)))
    news.append(nouns_list)


# In[5]:


len(news)


# In[6]:


from apyori import apriori
rules = apriori(news, min_support=0.3, min_confidence=0.2)
result = list(rules)


# In[7]:


result[0]


# In[8]:


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


# In[50]:


result_df


# In[56]:


result_df[(result_df.lhs.str.contains('한국')) &
          (result_df.rhs.str.contains('전망'))].sort_values(by=['lift'], 
                                                        ascending=False)


# In[ ]:




