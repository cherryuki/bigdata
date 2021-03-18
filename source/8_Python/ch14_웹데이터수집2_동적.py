#!/usr/bin/env python
# coding: utf-8

# **21-03-18 python 14_웹데이터수집2 - 동적 (c)cherryuki (ji)**

# # ch14 웹데이터 수집(동적)

# # 3절. Selenium
# - https://selenium-python.readthedocs.io/
# - 아나콘다 prompt에서 pip install selenium
# - 크롬 드라이브 다운(크롬 버전 확인): https://sites.google.com/a/chromium.org/chromedriver/downloads

# In[4]:


from selenium import webdriver
driver = webdriver.Chrome('C:/Bigdata_자료/src/Selenium/chromedriver.exe')


# In[5]:


#지정한 url로 이동
driver.get('http://python.org')


# In[6]:


#Search(입력창)
elem = driver.find_element_by_name('q')
elem.clear() #입력창 내용 지우기
elem.send_keys("pycon") #입력창에 pycon 입력


# In[7]:


from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.RETURN) #Enter키 Keys.ENTER도 동일 


# In[8]:


result_list = driver.find_elements_by_css_selector("form h3 > a")
for result in result_list:
    print('%s - %s' %(result.text, result.get_attribute('href')))


# In[9]:


#브라우저 종료
driver.close()


# **맞춤법 검사기(네이버 맞춤법 검사기 이용)**

# In[10]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time


# In[12]:


driver = webdriver.Chrome('C:/Bigdata_자료/src/Selenium/chromedriver.exe')
driver.get('https://www.naver.com/')


# In[13]:


elem = driver.find_element_by_id("query")
elem.clear()
elem.send_keys("맞춤법 검사기")
elem.send_keys(Keys.ENTER)
#elem.send_keys(Keys.RETURN) #Enter키 누르기


# In[14]:


elem_text = driver.find_element_by_class_name("txt_gray")
elem_text.clear()
elem_text.send_keys("안영하세요")
elem_button = driver.find_element_by_class_name("btn_check")
elem_button.click()


# In[15]:


soup = BeautifulSoup(driver.page_source, 'html.parser')
result = soup.select_one('p._result_text').text
result


# In[16]:


driver.close()


# **한 번에 실행되도록 수정**
# - time.sleep(n); n초 동안 기다려주는 작업 필요

# In[17]:


driver = webdriver.Chrome('C:/Bigdata_자료/src/Selenium/chromedriver.exe')
driver.get('https://www.naver.com')
elem = driver.find_element_by_id("query")
elem.clear()
elem.send_keys("맞춤법 검사기")
elem.send_keys(Keys.ENTER)
time.sleep(1) #기다려주는 작업 필요
elem_text = driver.find_element_by_class_name("txt_gray")
elem_text.clear()
elem_text.send_keys("안영하세요")
elem_button = driver.find_element_by_class_name("btn_check")
elem_button.click()
time.sleep(2) #기다려주는 작업 필요 (맞춤법 검사 중입니다. 잠시만 기다려주세요.가 나오지 않게 설정)
soup = BeautifulSoup(driver.page_source, 'html.parser')
result = soup.select_one("p._result_text").text
print(result)
#기다려주는 작업 없으면 result 제대로 프린트 되지 않음
driver.close()


# **text파일을 맞춤법 검사 후 text파일로 저장**

# In[19]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
with open('data/ch14_맞춤법검사용.txt', 'r', encoding='utf8') as f:
    text = f.read()
len(text) #825
ready_list = []
while len(text) > 500:
    temp_str = text[:500]
    last_space_idx = temp_str.rfind(' ') #번역처럼 문장 단위로 나눌 경우 '.'
    ready_list.append(text[:last_space_idx])
    text = text[last_space_idx:] #ready_list에 append한 부분은 없앰
ready_list.append(text)
#print(len(ready_list))

driver = webdriver.Chrome('C:/Bigdata_자료/src/Selenium/chromedriver.exe')
driver.get('https://www.naver.com')
elem = driver.find_element_by_id("query")
elem.clear()
elem.send_keys("맞춤법 검사기")
elem.send_keys(Keys.ENTER) 
time.sleep(1) #기다려주는 작업 필요

elem_text = driver.find_element_by_class_name("txt_gray")
results=""
for ready in ready_list:
    elem_text.send_keys(Keys.CONTROL, 'a') #Ctrl+a; 텍스트 모두 선택
    elem_text.send_keys(ready)
    elem_button = driver.find_element_by_class_name("btn_check")
    elem_button.click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    result = soup.select_one("p._result_text").text
    results += result.replace('.', '.\n')
#results
with open('data/ch14_checked.txt', 'w', encoding='utf-8') as f:
    f.write(results)
driver.close()
#맞춤법 검사기 완벽하지 않음(일부러 틀린 내용들 중 바뀌지 않은 내용들 있는 것 확인)
#파일은 저작권문제로 확인 후 삭제완료


# In[ ]:




