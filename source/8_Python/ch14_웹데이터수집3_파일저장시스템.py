#!/usr/bin/env python
# coding: utf-8

# ## 1. yes24의 베스트셀러 정보를 제공하는 사이트에서 베스트셀러 정보를 수집해서 파일에 저장하세요.
# - http://www.yes24.com/24/category/bestseller
# - 순위, 책이름, 저자 및 출판사, 가격

# In[1]:


import requests
from bs4 import BeautifulSoup
url = "http://www.yes24.com/24/category/bestseller"
html = requests.get(url)
soup = BeautifulSoup(html.content, 'html.parser')
titles = soup.select("p.image > a img")
titles = [title.attrs['alt'] for title in titles]
writers = soup.select("p.aupu")
writers = [writer.text for writer in writers]
price = soup.select("p.price > strong")
price = [p.text for p in price]

results = ""
for idx in range(len(titles)):
    #print('{:2d}위: {}, {}, "{}"'.format(idx+1, titles[idx], writers[idx], price[idx]))
    result = '{:2d}위: {}, {}, "{}"'.format(idx+1, titles[idx], writers[idx], price[idx])
    results += result + '\n'
with open('data/ch14_01_yes24.txt', 'w', encoding='utf-8') as f:
    f.write(results)


# In[ ]:


# 순위: ol > li class=num1 이면 1위 num2면 2위 식 -> 구할 필요 없음!! 순서대로 1~40위
# 책제목: p.image > a img alt 
# 저자 및 출판사: p.aupu > a 
# 가격: p.price > strong 


# ## 2. 영어번역 자동화 프로그램을 구현하시오. 텍스트 파일을 카카오 번역기를 통해 영어로 번역된 텍스트를 파일로 출력하는 동적 웹크롤링 프로그램을 구현하시오.
# -  https://translate.kakao.com/

# In[2]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
with open('data/ch14_02_한글원본.txt', 'r', encoding='utf-8') as f:
    text = f.read()
#len(text)
ready_list = []
while len(text)>5000:
    temp_str = text[:5000]
    last_dot_index = temp_str.rfind('.')
    ready_list.append(text[:last_dot_index+1]) #점 포함시키기 위해 +1
    text = text[last_dot_index+1:]
ready_list.append(text)

driver = webdriver.Chrome('C:/Bigdata_자료/src/Selenium/chromedriver.exe')
driver.get('https://translate.kakao.com/')
popup_button = driver.find_element_by_css_selector("a.btn_close")
popup_button.click()
textarea = driver.find_element_by_id("query")
results = ""
for ready in ready_list:
    textarea.send_keys(Keys.CONTROL, 'a')
    textarea.send_keys(ready)
    button = driver.find_element_by_id("btnTranslate")
    button.click()
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    result = soup.select_one("p#result").text
    results += result
#print(results)
with open('data/ch14_02_자동화영어번역본.txt', 'w', encoding='utf-8') as f:
    f.write(results)
#time.sleep(3)
driver.close()
#파일은 저작권 문제로 확인 후 삭제완료


# In[ ]:


#입력창 id = query
#번역하기 버튼 id: btnTranslate
#번역결과 id: p의 result

