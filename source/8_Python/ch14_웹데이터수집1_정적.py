#!/usr/bin/env python
# coding: utf-8

# **21-03-17 python 14_웹데이터수집1 - 정적 (c)cherryuki (ji)**

# # ch14 웹데이터 수집(정적)

# # 1절. BeautifulSoup과 parser
# - pip install beautifulsoup4 ; 아나콘다 설치하면 자동 설치되는 패키지 7500개에 포함
# - pip install requests_file
# - 공식 사이트: https://www.crummy.com/software/BeautifulSoup/
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# In[1]:


import requests
from requests_file import FileAdapter


# In[2]:


s = requests.Session()
s.mount("file://", FileAdapter())
response = s.get("file:///C:/Bigdata/source/8_Python/data/ch14_sample.html")
response #<Response [200]> 으로 나오면 성공. (cf. [404]: 파일 찾지 못한 것)


# **<상태 코드>**
# - 100번 영역: 정보 전송
# - 200번 영역: 성공
#  - 200: 성공 / 201: POST 요청 처리 / 204: 전송할 데이터 없음
# - 300번 영역: 리다이렉션
# - 400번 영역: 클라이언트 측 오류
#  - 401: 사용자 인증 / 403: 접근권한 없음 / 404: 요청한 URL 없음 / 406: not acceptable
# - 500번 영역: 서버측 오류

# In[3]:


if response.status_code == 200:
    print("Success")
elif response.status_code == 404:
    print("Not Found")


# In[4]:


if response:
    print("Sucess")
else:
    print("Not Found")


# In[5]:


response.content


# In[6]:


# html 문서 파싱
from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
soup


# In[7]:


# select_one: 조건에 만족하는 첫번째 것 하나만 가져옴
el = soup.select_one("h1")
print("el =>", el)
print("el.text =>", el.text)
print("el.string =>", el.string)
print("el.attrs =>", el.attrs)
print("el의 class속성 =>", el.attrs['class'])
print("el.name =>", el.name)


# In[8]:


#select; 조건에 만족하는 것 전부를 리스트로 가져옴
el = soup.select(".greeting")
el


# In[9]:


el = soup.select("h1")
print('el =>', el)
print('el의 text들 =>', [e.text for e in el])
print('el의 string들 =>', [e.string for e in el])
print('el의 속성들 =>', [e.attrs for e in el]) 
print('el의 class들 =>', [e.attrs['class'] for e in el])
print('el의 name들 =>', [e.name for e in el])


# In[10]:


soup.select("h1, p")


# In[11]:


soup.select("div")


# In[12]:


soup.select("div b") #후손 선택자(div 밑에 있는 b 전부)


# In[13]:


soup.select("div > b") #자손 선택자(div 바로 밑에 있는 b만)


# In[14]:


soup.select("div.contents")


# In[16]:


soup.select("h1.greeting.css")[0]


# In[18]:


soup.select_one("h1.greeting.css")


# In[19]:


soup.select("h1.css")


# # 2절 정적 웹 데이터 수집(정적 웹크롤링)
# ## 2.1 requests 모듈(GET 요청)

# In[20]:


import requests
response = requests.get("http://api.github.com")
response


# In[22]:


if response.status_code == 200:
    print("sucess")
elif response.status_code == 404:
    print("존재하지 않는 url입니다")
elif response.status_code == 406:
    print("not acceptable(파이썬 웹크롤링 허용X)")


# In[23]:


if response:
    print("Sucess")
else :
    print("An error has occurred")


# In[24]:


response.content


# In[25]:


response.json()


# ## 2.2 BeautifulSoup 모듈을 활용한 웹데이터 수집
# - HTML, XML 등 Markup 언어를 crawling하기 위한 대표적인 모듈
# - https://www.crummy.com/software/BeautifulSoup/
# 
# **1) 환율정보 가져오기(네이버 금융>시장 지표)** <br>
# - https://finance.naver.com/marketindex/

# In[27]:


from bs4 import BeautifulSoup
from numpy import round
url = "https://finance.naver.com/marketindex/"
marketindex = requests.get(url)
soup = BeautifulSoup(marketindex.content, 'html.parser')
price = soup.select_one("div.head_info > span.value")
print(price)
print(price.text)
print(round(float(price.text.replace(',','')),1))


# In[28]:


price = soup.select("div.head_info > span.value")
for p in price:
    print(p.text, end='\t')
print()
for i in range(len(price)):
    print(price[i].text, end='\t')


# In[29]:


title = soup.select("h3.h_lst > span.blind")
for i in range(len(price)):
    print("{} {}".format(title[i].text, price[i].text))


# In[30]:


# price: div.head_info > span.value
# 단위(원, 달러): div.head_info > sapn > span.blind
# 상승, 하락: div.head_info > span.blind
unit = soup.select("div.head_info > span > span.blind")
unit = [u.text for u in unit]
unit


# In[31]:


unit.insert(7, '') #7번 인덱스에 ''추가 (단위 없음)
unit


# In[32]:


status = soup.select("div.head_info > span.blind")
[s.text for s in status]


# In[33]:


for idx in range(len(price)):
    print("{}: {}{} - {}".format(title[idx].text, price[idx].string, unit[idx], status[idx].text))


# **2) 네이버 영화 랭킹 출력하기** 
# 
# - https://movie.naver.com/movie/sdb/rank/rmovie.nhn
# - 1위 영화제목 : 영화소개 url
# - 감독 및 배우
# - OO 감독 / OO 주연 / OO 주연

# In[34]:


import requests
from bs4 import BeautifulSoup
url = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
movie_ranking = requests.get(url)
soup = BeautifulSoup(movie_ranking.content, 'html.parser')
title_list = soup.select("div.tit3 > a")
len(title_list)


# In[35]:


for idx in range(len(title_list)):
    print("{:2d}위 {}".format(idx+1, title_list[idx].attrs['title']))
    #print("{:2d}위 {}".format(idx+1, title_list[idx].text))


# In[37]:


#10위 까지만 (13위, 19위, 21위 등 역할 없는 곳에서 에러 발생)
for idx in range(10):
    print("{:2d}위 {}".format(idx+1, title_list[idx].text))
    link = 'https://movie.naver.com/'+title_list[idx].attrs['href']
    soup2 = BeautifulSoup(requests.get(link).content, 'html.parser')
    people = soup2.select("li a.tx_people")
    staffs = soup2.select("dl.staff > dt")
    roles = soup2.select("dl.staff > dd")  #0번째(감독)은 역할X
    print("감독 및 배우")
    for i in range(len(people)):
        if i==0:
            print("{}: {}".format(staffs[i].text, people[i].text), end=' / ')
        else :
            print("{}: {}({})".format(staffs[i].text, people[i].text, roles[i-1].text), end=' ')
    print('\n')


# **3) 이번주 로또 번호 출력**
# 
# - 구글에서 로또로 검색 후 첫 사이트(https://dhlottery.co.kr/gameResult.do?method=byWin)
# - OO회
# - 당첨번호:
# - 보너스번호:

# In[38]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
el_no = soup.select_one("div.win_result > h4 > strong")
el_win_nums = soup.select("div.win p > span.lrg")
el_bonus = soup.select_one("div.bonus p > span.lrg")


# In[39]:


print("{}".format(el_no.text))
print("당첨번호:", end=' ')
for idx in range(len(el_win_nums)):
    print("{}".format(el_win_nums[idx].text), end=' ')
print()
print("보너스번호: {}".format(el_bonus.text))


# In[40]:


print('{}'.format(el_no.text))
print("당첨번호:", [int(el.text) for el in el_win_nums])
print("보너스번호: {}".format(int(el_bonus.text)))


# **4) 크롤링 막아놓은 사이트 크롤링**

# In[41]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.melon.com/chart/index.htm"
html = urlopen(url)
#HTTP Error 406: Not Acceptable


# In[46]:


import requests
from bs4 import BeautifulSoup
url = "https://www.melon.com/chart/index.htm" #크롤링 막아놓음
#크롤링 막혀있는 경우 headers 시도해보기
headers = {'User-agent':'Mozilla/5.0'}
html = requests.get(url, headers=headers)
soup = BeautifulSoup(html.content, 'html.parser')
titles = soup.select("div.ellipsis.rank01 > span > a")
print(titles[0].text)
singers = soup.select("div.ellipsis.rank02 > span") #가수 2명 있는 것 주의!
print(singers[0].text)
len(titles), len(singers)


# In[47]:


for idx in range(len(titles)):
    print("{:3d}위 | {} | {}".format(idx+1, titles[idx].text, singers[idx].string))


# ## 2.3 정규표현식을 활용한 웹데이터 수집
# ### 정규표현식 참조
# - https://ko.wikipedia.org/wiki/%EC%A0%95%EA%B7%9C_%ED%91%9C%ED%98%84%EC%8B%9D
# - https://www.nextree.co.kr/p4327/
# - 정규표현식 연습장: https://regexr.com/
# ### 간략문법
# - \d ; 숫자. [0-9]와 동일
# - \D ; 숫자가 아닌 것
# - \s ; 공백(white space)
# - \w ; 영문자나 숫자
# - \W ; 영문자나 숫자가 아닌 문자
# - . ; 문자 하나
# <pre>
#  + ; 1번 이상 반복
#  * ; 0번 이상 반복
#  {n, m} ; n~m회 반복
#  ? ; {0, 1} 의미
# </pre>
# ### 정규표현식 예
# - 메일 패턴: \w+@\w+[\\.\w]+\w+
# - 전화번호 패턴: .?\d{2,3}.?\d{3,4}.?\d{4}
# - ip주소 정규표현식: [0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}
# - 주민번호 정규표현식: [0-9]{6}-[0-4]\d{6}

# In[48]:


print(r"hello\nWorld") #정규표현식 앞에 r을 붙이면 \그대로 출력


# In[49]:


print("hello\nWorld")


# In[50]:


import re
parsing_string = """010-9999-9999
01-65478
(02)716-1004
sp@naver.com
ko@abc.co.kr
<html>
    <tag>abe</tag>
</html>
"""


# In[52]:


mail_result = re.findall(r'\w+@\w+[\.\w]+\w+', parsing_string)
mail_result


# In[53]:


tel_result = re.findall(r'.?\d{2,3}.?\d{3,4}.?\d{4}', parsing_string)
tel_result


# In[56]:


tag_text = re.search(r'<tag>(.+)</tag>', parsing_string)
tag_text.group(1)


# **예제) 전국날씨 RSS 데이터 가져오기**
# - https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108

# In[59]:


import re, urllib.request
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
target = urllib.request.urlopen(url)
contents = target.read().decode('utf-8')
# re.DOTALL; 정규표현식의 .이 줄바꿈 문자를 포함하게 함
locations = re.findall(r'<location wl_ver="3">.+?</location>', contents, re.DOTALL) #여러줄일 경우 ?, re.DOTALL 필요
for loc in locations:
    province = re.search(r'<province>(.+)</province>', loc)
    city = re.search(r'<city>(.+)</city>', loc)
    print(province.group(1), '지역의 ', city.group(1))
    data = re.findall(r'<data>.+?</data>', loc, re.DOTALL) #여러줄일 경우 ?, re.DOTALL 필요
    for item in data:
        tmEf = re.search('<tmEf>(.+)</tmEf>', item).group(1)
        wf = re.search('<wf>(.+)</wf>', item).group(1)
        tmn = re.search('<tmn>(.+)</tmn>', item).group(1)
        tmx = re.search('<tmx>(.+)</tmx>', item).group(1)
        print("\t날짜 시간:{}, 날씨:{}, 최저:{}도, 최고:{}도".format(tmEf, wf, tmn, tmx))


# In[60]:


#get 요청
import requests
from bs4 import BeautifulSoup
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
html = requests.get(url)
soup = BeautifulSoup(html.content, "html.parser")
locations = soup.select("location")
for loc in locations:
    province = loc.select_one("province").text
    city = loc.select_one("city").text
    print(province, '지역의', city)
    data = loc.select("data")
    ampm = "오전"
    for item in data:
        tmEf = item.select_one('tmEf').text[:10]
        wf = item.select_one('wf').text
        tmn = item.select_one('tmn').text
        tmx = item.select_one('tmx').text
        print("\t날짜:{} {}, 날씨:{}, 기온:{}~{}도".format(tmEf, ampm, wf, tmn, tmx))
        if ampm == '오전':
            ampm = '오후'
        else :
            ampm = '오전'


# In[ ]:


#html = urlopen(url)
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
html = urlopen(url)
soup = BeautifulSoup(html, "html.parser")
locations = soup.select("location")
for loc in locations:
    province = loc.select_one("province").text
    city = loc.select_one("city").string
    print(province, '지역의', city)
    data = loc.select("data")
    ampm = '오전'
    for item in data:
        tmEf = item.select_one('tmEf').text[:10]
        wf = item.select_one('wf').text
        tmn = item.select_one('tmn').text
        tmx = item.select_one('tmx').text
        print('\t날짜:{} {}, 날씨:{}, 기온:{}~{}도'.format(tmEf, ampm, wf, tmn, tmx))
        if ampm == '오전':
            ampm = '오후'
        else :
            ampm = '오전'

