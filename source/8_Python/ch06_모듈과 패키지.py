#!/usr/bin/env python
# coding: utf-8

# **21-02-25 python 06_모듈과 패키지   (c)cherryuki (ji)**

# # <font color="red">ch06. 모듈과 패키지</font>

# # 1절. 모듈 사용하기
# - 파이썬 모듈: 파이썬 정의와 문장을 담고 있는 파일(함수, 변수, 클래스가 있는 *.py 파일)
# - 200여개의 파이썬 모듈이 파이썬 인터프리터에 포함

# # 1.1 import 하는 방법
# (1) import 모듈명; 모듈 안의 함수들은 모듈명.함수()로 사용 가능 <font color="green">#모듈명. +Tab키: 내장 함수 확인 가능</font> <br>
# (2) from 모듈명 import 함수명 <br>
# 　 from 패키지명 import 모듈명 <font color="green">#패키지는 디렉토리, 모듈은 .py파일</font> <br>
# 　 from 패키지명.모듈명 import 함수명<br>
# (3) import 모듈명 as 별칭; 모듈명을 메모리에 로드하고 별칭으로 사용 <font color="green">#별칭.함수() 로 사용 가능</font><br>
# (4) from 모듈명 import 함수명 as 별칭 <font color="green">#별칭() 로 사용 가능</font><br>
# 　 from 패키지명 import 모듈명 as 별칭
# - dir(모듈명); 모듈 안에 있는 변수, 함수, 클래스 등을 list로 출력

# In[3]:


#1. import 모듈명; 모듈 안의 함수들은 모듈명.함수()로 사용 가능
import time #time 모듈 안 함수, 변수, 클래스 사용 가능
time.ctime() #모듈명. +Tab키: 내장 함수 확인 가능


# In[4]:


time.time() #unixtime(1970년 이후 밀리세컨)


# In[6]:


del time #time모듈을 메모리에서 unload


# In[7]:


#2. from 모듈명 import 함수명
#   from 패키지명 import 모듈명 (패키지는 디렉토리, 모듈은 .py파일)
#   from 패키지명.모듈명 import 함수명
from time import ctime
ctime()


# In[8]:


del ctime #메모리에 있는 ctime함수를 unload


# In[9]:


# import 모듈명 as 별칭
import time as t
t.ctime()


# In[12]:


#4. from 모듈명 import 함수명 as 별칭
#   from 패키지명 import 모듈명 as 별칭
from time import ctime as ct
ct() #ctime()으로 하면 에러 발생


# In[13]:


del ct


# In[14]:


import time #numpay, pandas 등 자주 사용(필요할 때만 로드해서 사용)


# In[15]:


dir(time) #time안에 있는 변수, 함수, 클래스 등을 list로 출력


# In[17]:


import math
print(dir(math))


# In[18]:


import sys
print(dir(sys))


# - import A; A모듈을 가져옴
# - import A as B; A모듈을 B이름으로 가져옴
# - from A import B; A모듈 안에 B함수(A패키지 안에 B모듈)를 가져옴
# - from A import B as C; A모듈 안에 B함수(A패키지 안에 B모듈)를 C이름으로 가져옴
# - from A.B import C; A패키지 안에 B모듈 안에 C함수를 가져옴
# - from A.B import C as D; A패키지 안에 B모듈 안에 C함수를 D이름으로 가져옴

# # 2절. 사용자 정의 모듈
# - 함수나 클래스 등을 파이썬 파일에 저장해서 모듈을 만들고 재사용할 수 있음
# - 모듈을 가져오는 순서: (1) 내장 모듈 (2) sys.path 변수에 저장된 경로

# In[19]:


import sys
sys.path #맨 첫 폴더: 현재 폴더


# In[20]:


sys.path.append('C:\\Bigdata\\source\\pylib') #역슬래시(\) 2개 or 슬래시(/) 1개


# In[21]:


sys.path #맨 마지막에 추가된 것 확인 가능


# In[22]:


import fibonacci


# In[23]:


fibonacci.fibo_print(100)


# In[24]:


temp = fibonacci.fibo_return(100)
temp


# In[25]:


import fibonacci as fibo
fibo.fibo_print(10)
print(fibo.fibo_return(10))


# In[26]:


del fibo


# In[27]:


from fibonacci import fibo_print, fibo_return


# In[28]:


fibo_print(200)
temp = fibo_return(300)
temp


# In[29]:


del fibo_print, fibo_return


# In[30]:


import fibonacci


# In[32]:


from importlib import reload #reload: 패키지나 모듈을 다시 load시키는 함수
reload(fibonacci)


# In[33]:


get_ipython().system(' python C:\\\\Bigdata\\\\source\\\\pylib\\\\fibonacci.py 500')


# In[34]:


import py_compile
py_compile.compile('C:\\Bigdata\\source\\pylib\\fibonacci.py')


# In[35]:


get_ipython().system(' python -m py_compile "C:\\\\Bigdata\\\\source\\\\pylib\\\\fibonacci.py"')


# In[36]:


get_ipython().system(' python C:\\\\Bigdata\\\\source\\\\pylib\\\\__pycache__/fibonacci.cpython-38.pyc 100')


# # 3절. 패키지
# - 모듈 이름이 A.B; A패키지 안에 B서브 모듈
# - 다중 모듈 패키지  ex) numpy, pandas, ...

# In[37]:


import sys
#sys.path.append('C:\\Bigdata\\source\\pylib')
import sample_pac #상위 패키지를 import한다고 하위 패키지 import 되지 않음


# In[1]:


#커널 재시작한 경우 sys.path 추가 필요
import sys
sys.path.append('C:\\Bigdata\\source\\pylib')


# In[38]:


import sample_pac.ab.a #하위 패키지를 import하면 상위 패키지 import됨
sample_pac.ab.a.hello()


# In[39]:


from sample_pac.ab import a
a.hello()


# In[40]:


from sample_pac.ab.a import hello
hello()


# In[2]:


from sample_pac.ab import * 
#sample_pac/ab/__init__.py파일에 __all__ = ['a', 'b'] 기재되어 있어야 a.hello(), b.world() 사용 가능


# In[42]:


a.hello()


# In[43]:


b.world()


# In[2]:


from sample_pac.cd import c #c에서 a사용 중이므로 ab패키지도 import 됨


# In[3]:


c.nice()


# <pre>
# <특수 속성들>
#  __init__.py
#  __all__; *로 import할 경우 import할 파일 지정 가능
#  __name__
#  __path__
#  __file__
# </pre>

# In[5]:


sys.path


# In[6]:


from mypkg import foo


# In[7]:


foo.foo_hello()


# In[8]:


from mypkg import bar


# In[9]:


bar.bar_hello()


# # 4절. 패키지 설치 및 삭제

# In[11]:


#아나콘다 관리자권한 실행 후> pip install objgraph 입력
import objgraph
objgraph.show_most_common_types() #메모리 사용량 출력


# In[14]:


#아나콘다 관리자 권한 실행 후> conda list objgraph 입력
#아나콘다 관리자권한 실행 후> pip uninstall objgraph 입력 


# In[1]:


import objgraph

