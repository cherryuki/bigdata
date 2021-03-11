#!/usr/bin/env python
# coding: utf-8

# **21-03-10 python 13_데이터 시각화(matplotlib) (c)cherryuki (ji)**

# # ch13. 데이터 시각화

# # 1절. 시각화 개요
# - 시각화 라이브러리: matplotlib, seaborn, folium(지도 시각화), ...
# - matplotlib: 파이썬에서 가장 많이 사용하는 시각화 라이브러리. 판다스에서도 내부적으로 matplotlib 사용
# - seaborn: matplotlib을 기반으로 다양한 색, 테마, 차트 기능을 추가한 라이브러리

# # 2절. Matplotlib
# ## 2.1 패키지 import 및 기본 설정
# - https://matplotlib.org/stable/api/pyplot_summary.html
# - %matplotlib inline; 주피터 노트북이 실행되는 브라우저에서 시각화
# - %config InlineBackend.figure_format = 'retina'; 그래프의 해상도를 높임
#   - 'retina', 'jpge', 'svg', 'pdf' 등 설정 가능(기본값: 'png')

# In[1]:


import matplotlib
import matplotlib.pyplot as plt


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "inlineBackend.figure_format = 'retina'")


# In[4]:


matplotlib.__version__


# - Matplotlib으로 그래프 그리는 단계 <br>
# 1) 데이터 준비<br>
# 2) 그래프 (공간) 생성<br>
# 3) 그래프 함수로 그래프 그리기<br>
# 4) 그래프 커스터마이징<br>
# 5) 그래프 출력 및 저장<br>

# In[5]:


import matplotlib.pyplot as plt
plt.plot([1,2,3,4]) #하나만 기재시 y로 인지 plot([x], y, [fmt], ...)
plt.ylabel('some numbers')


# ## 2.2 그래프 객체

# In[6]:


fig = plt.figure()


# - fmt = '[marker][line][color]' 　ex) 'o--g'
# - fmt = '[color][marker][line]'　 ex) 'go--'

# In[7]:


plt.figure(figsize=(8,3))
plt.plot([1,2,3,4],[2,4,6,6], 'go--') #go--; green, circle marker, -- dashed line #o--g로 기재해도 동일
plt.show() #그래프만 출력


# ## 2.3 그래프 영역 나누기
# ### 1) subplot() 함수로 서브플롯 추가

# In[8]:


import numpy as np
x = np.arange(0,10,0.01)
x.shape


# In[10]:


plt.subplot(2,1,1) #2행1열의 subplot생성 후 첫번째 subplot에 plot을 그림(#plt.subplot(211)로 적어도 동일)
plt.plot(x, np.sin(x))
plt.subplot(223) # 2,2,3 으로 적은 것과 동일
plt.plot(x, np.cos(x))
plt.subplot(2,2,4)
plt.plot(x, np.sin(x)*np.cos(x))
plt.show() #그래프만


# In[12]:


plt.subplot(311) #3행 (1행) 1열 1번째 자리
plt.subplot(334) #3행 (2행) 3열 4번째 자리 (2행의 첫번째 자리)
plt.subplot(326) #3행 (3행) 2열 6번째 자리 (3행의 두번째 자리) 


# In[ ]:


#경고 메시지 안보이게(에러 메시지는 보임)
import warnings
warnings.filterwarnings(action='ignore')
#경보 메시지 보이게
warnings.filterwarnings(action='defalut')


# ### 2) subplots() 함수로 서브플롯 추가하기

# In[14]:


x = np.arange(0,10,0.01)
x.shape


# In[15]:


#방법1(2행 2열 서브플롯); subplot() 이용
plt.subplot(2,2,1); plt.plot(x, np.sin(x))
plt.subplot(2,2,2); plt.plot(x, np.cos(x))
plt.subplot(2,2,3); plt.plot(x, np.tanh(x))
plt.subplot(2,2,4); plt.plot(x, np.sin(x)*np.cos(x))
plt.show()


# In[18]:


#방법2(2행 2열 서브플롯); subplots() 이용
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10,6))
axes[0,0].plot(x, np.sin(x), color='r', linewidth=5)
axes[0,0].plot([0,1,2,3], [-1,-0.5,0,0.5], 'k:') #k: black, :(dotted line) #그래프 위에 겹쳐 그리는 것 가능
axes[0,1].plot(x, np.cos(x), 'c--') #c: cyan(청록), --(dashed line)
axes[1,0].plot(x, np.tanh(x), 'g') #g: green
axes[1,1].plot(x, np.sin(x)*np.cos(x), '-.') # -.(dash-dot line)


# In[19]:


#방법3(2행2열 서브플롯)
x = np.arange(0,7,0.01)
x.shape


# In[20]:


# def sin_cos(x):
#    return np.sin(x)*np.cos(x)
# fun_list = [np.sin, np.cos, np.tanh, sin_cos]
fun_list = [np.sin, np.cos, np.tanh, lambda x:np.sin(x)*np.cos(x)]
fmt_list = ['k:', 'c--', 'g', 'r-.']


# In[22]:


fig, axes = plt.subplots(2,2, figsize=(10,6))
#2차원 axes를 list(axes.flat)로 이용하면 중첩 for문 사용하지 않아도 됨
for i, ax in enumerate(axes.flat):
    ax.plot(x, fun_list[i](x), fmt_list[i])


# In[23]:


fig, axes = plt.subplots(ncols=4, figsize=(12,3))
for i,ax in enumerate(axes):
    ax.plot(x, fun_list[i](x), fmt_list[i])


# In[25]:


fig, axes = plt.subplots(nrows=4, figsize=(10,10)) #figsize 전체 그래프 공간 크기(그래프별 사이즈X)
for i, ax in enumerate(axes):
    ax.plot(x, fun_list[i](x), fmt_list[i])


# ## 2.4 다양한 그래프 그리기
# **1) pyplot 함수들: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html**<br>
# **2) matplotlib.pyplot.plot(); 선 그래프**

# In[26]:


np.random.randn(4,10) #4행10열 난수 발생(평균 0, 표준편차1)


# In[28]:


fig, axes = plt.subplots(2,2, figsize=(8,5))
fig.suptitle("figure sample plots")
axes[0,0].plot([1,2,3,4], 'ro-') #r: red, o: 동그라미, -: 실선 
axes[0,1].plot(np.random.randn(4,10), np.random.randn(4,10), 'cs-.') #c:cyan, s:네모, -.:dashed-dot
axes[1,0].plot(np.linspace(0,5,50), np.cos(np.linspace(0,5))) #linspcae 생략시 num=50
axes[1,1].plot([3,6], [3,5], 'b^:') #b: blue, ^:세모, : dot
axes[1,1].plot([4,5], [5,4], 'kx--') #k: black, x:x, --:dash
plt.show()


# ### 3) pandas.DataFrame.plot()
# plot(x=None, y=None, kind='line', figsize=None, title=None, grid=None, xlim, ylim, ...)
# 
# - kind: line, scatter, bar, barh(수평바), hist, box, density=kde, area, pie
# - figsize: tuple(인치 단위)
# - xlim, ylim: list/tuple

# In[29]:


import seaborn as sns
iris_df = sns.load_dataset('iris')
iris_df.head()


# In[30]:


iris_df.plot(figsize=(12,4))
plt.legend(bbox_to_anchor=(1.01,1), loc=2, borderaxespad=0.) #범례 위치 조정
plt.show()


# In[31]:


iris_df.plot(kind="box", figsize=(10,5), title="IRIS boxplot", 
            ylabel="y-value", grid=True, fontsize=20, rot=10)
plt.show()


# In[32]:


#iris_df에서 상관관계가 가장 높은 두 변수의 scatter plot을 그리시오
iris_df.corr()


# In[33]:


iris_df.plot(x="petal_length", y="petal_width", kind="scatter")
plt.show()


# In[35]:


iris_df.groupby(iris_df['species']).plot(kind="box", subplots=True, #서브플롯으로
                                        sharey=True, #y축 공유
                                        layout=(3,4),
                                         figsize=(8,6))
plt.show()


# ### 4) pyplot.scatter(); 산점도
# - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

# In[36]:


np.random.seed(2021) #난수발생 고정 위함
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (np.random.rand(N)*30)**2
plt.scatter(x,y, s=area, #마커의 크기
                 c=colors, alpha=0.5) #alpha: 투명도(0~1)
plt.show()


# np.random.rand(N) <br>
# <font color="0.16813959">0.16813959 색깔</font>
# <font color="0.46352234">0.46352234 색깔</font>
# <font color="0.93477117">0.93477117 색깔</font>
# <font color="0.50995722">0.50995722 색깔</font>
# <font color="0.29097608">0.29097608 색깔</font>
# <font color="0.44418679">0.44418679 색깔</font>
# <font color="0.75679187">0.75679187 색깔</font>

# ## 2.5 다양한 그래프 그리기 예
# 1) fill(), fill_between(), scatter() <br>
# 2) bar(), axvline(), axhline(), ... <br>
# 3) hist(), boxplot(), violineplot() <br>

# In[40]:


x = np.linspace(0,10)
y = np.cos(x)
fig, axes = plt.subplots(2,2)
axes[0,0].scatter(x,y,s=5, c='r', marker='o')
axes[0,1].fill(x,y,c='b')
axes[1,1].fill_between(x,y, color='y')
#axes[1,1].plot([-1,5],[-1,1],'ko-.')


# In[44]:


fig, axes = plt.subplots(2,2)
axes[0,0].bar([1,2,3], [3,4,5], color='g')
axes[0,0].plot([1,2,3],[3,4,5], 'r')
axes[0,1].bar([0.5,1,2.5], [0,1,2])
axes[0,1].plot([0.5,1,2.5], [0,1,2], 'b')
axes[1,0].axvline(0.5)
axes[1,1].axhline(0.75, color='0.7')
plt.show()


# In[45]:


fig, axes = plt.subplots(2,2)
#빈도표
axes[0,0].hist(iris_df['sepal_length'], bins=20, color='y')
#누적 빈도표(cumulative=True)
axes[0,1].hist(iris_df['sepal_length'], bins=20, cumulative=True)
axes[1,0].hist(iris_df['sepal_length'], bins=10, orientation='horizontal')
axes[1,1].hist(iris_df['sepal_length'], bins=10, histtype='step')
plt.show()


# In[47]:


fig, axes = plt.subplots(1,2)
axes[0].boxplot(iris_df['sepal_length'])
axes[1].violinplot(iris_df['sepal_length'])
plt.show()


# ## 2.6 그래프 커스터마이징
# 1) linestyle, linewidth

# In[48]:


x = np.linspace(0,10,100)
y = np.cos(x)


# In[49]:


fig, axes = plt.subplots(2,2) 
#ls: line style
axes[0,0].plot(x,y,linewidth=2, color='y')
axes[0,1].plot(x,y,ls='dotted', linewidth=5, color='c')
axes[1,0].plot(x,y,ls='--', linewidth=2, color='purple')
axes[1,1].plot(x,y,ls='-', c='m')


# 2) text(), annotate()

# In[52]:


fig, axes = plt.subplots(1,2, figsize=(8,4))
axes[0].scatter(x,y,marker='.')
axes[0].text(2,0, '샘플 텍스트', style='italic')
axes[1].scatter(x,y,marker='*', color='y')
axes[1].annotate('Sine', xy=(5,0.5), #화살표가 가리킬 위치
                         xytext=(2,0.75), #글자위치
                         arrowprops=dict(arrowstyle='->',  #화살표 스타일
                                        connectionstyle='angle3'))
plt.show()


# In[51]:


#한글 폰트 설정
plt.rc('font', family='Malgun Gothic') #Windows
#plt.rc('font', family='AppleGothic') #Mac
plt.rc('axes', unicode_minus=False) #축


# In[54]:


#원하는 한글 폰트 지정
import matplotlib.font_manager as fm
font_path = 'C:/Windows/Fonts/HMFMOLD.TTF'
font_prop = fm.FontProperties(fname=font_path, size=15)
fig, axes = plt.subplots(1,2, figsize=(8, 4))
plt.suptitle("메인 타이틀", fontproperties=font_prop) #폰트 지정
axes[0].scatter(x,y, marker='.')
axes[0].text(2,0,'샘플 텍스트', style='italic')
axes[1].scatter(x,y, marker='*', color='y')
axes[1].annotate('Sine', xy=(5,0.5), #화살표가 가리킬 위치 
                         xytext=(2,0.75), #글자가 있을 위치
                         arrowprops=dict(arrowstyle='->', #화살표 스타일
                                        connectionstyle='angle3'))
plt.show()


# In[53]:


print(matplotlib.matplotlib_fname())
#아래 경로의 파일에서 font.family: 원하는 폰트 지정 (#제거) 후 주피터 노트북 다시 실행


# 3) 수학기호 <br>
# - https://matplotlib.org/2.0.2/users/mathtext.html

# In[55]:


fig, ax = plt.subplots()
ax.scatter(x,y, marker='.')
ax.set_title(r'$sigma_i = 15$', fontsize=30)
ax.text(2.5, 0.5, r'$\sum_{i=0}^\infty X_i$', fontsize=25)


# **21-03-11 python 13_데이터 시각화(matplotlib) (c)cherryuki (ji)**

# In[1]:


#주피터노트북 재부팅 후 설정
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
#한글 설정
plt.rc('font', family='Malgun Gothic')
plt.rc('axes', unicode_minus=False) #y축
#경고 메시지 안보이게
import warnings
warnings.filterwarnings(action='ignore')
#경고 메시지 보이게
#warnings.filterwarnings(action='default')


# 4) 축과 눈금<br>
# - https://matplotlib.org/3.1.0/api/axis_api.html
# - plt.subplots_adjust(); 서브플롯간의 간격변경

# In[5]:


import numpy as np
x = np.linspace(0,10,100)
y = np.cos(x)
fig, axes = plt.subplots(2,2,figsize=(10,5))
#plt.subplots_adjust(); 서브플롯간의 간격변경
plt.subplots_adjust(hspace=0.4, wspace=0.3) #hspace는 상하 여백 wspace 좌우 여백
axes[0,0].scatter(x, y, marker='.')
axes[0,0].set(title='An Example Axes', ylabel='y축', xlabel='x축',
             xlim=[0,12], ylim=[-2,2]) #축 범위 변경

axes[0,1].scatter(x,y, marker='*', c='b')
axes[0,1].set_xlim(0,5)
axes[0,1].set_xlabel('x축 0~5')
axes[0,1].set_ylim(-1.5,1.5)
axes[0,1].set_ylabel('y축 -1.5~1.5')

axes[1,0].scatter(x,y,marker='^', c='c')
#축 눈금 위치
axes[1,0].set_xticks(range(0,11,3))
axes[1,0].set_xticklabels([-99,3,'6개','아무값'])
axes[1,0].set_yticks([-2,0,1,2])
axes[1,0].set_yticklabels(['-2개', '제로', 1, 'Max'])

#한번에 셋팅 가능
axes[1,1].scatter(x,y,c='g')
axes[1,1].set(xticks=[0,2,3.5,5,7], xticklabels=['Min', 2, 3.5, 5, 'Max'],
             title='test')
axes[1,1].grid(True)
axes[1,1].spines['top'].set_visible(False)
axes[1,1].spines['bottom'].set_position(('outward',10)) #밑에 공간 10만큼 띄우기
plt.show()


# 5) 축 공유

# In[6]:


import numpy as np
x = np.arange(0,10)
y1 = 0.5*x**2 #0.5*(x**2)
y2 = -1*y1


# In[7]:


fig, ax1 = plt.subplots() #1행1열(기본값 nrows=1, ncols=1)

ax1.plot(x, y1, 'g^:')
ax1.set(xlabel = 'X data', ylabel='y1 data', title='축 공유')

ax2 = ax1.twinx() #x축을 공유하는 ax2
ax2.plot(x, y2, 'bv--')
ax2.set_ylabel('y2 data', color='b')

ax3 = ax1.twiny() #ax1과 x축을 공유하는 ax3
ax3.plot(-x,y1, 'rD-.')
ax3.set_xlabel('-x data', color='r')

plt.show()


# 6) 범례 표시

# In[8]:


x = np.arange(0,10)
y = 0.2 * x**2


# In[9]:


fig, ax = plt.subplots(figsize=(8,4))
ax.plot(x,y, 'g', label='GREEN')
ax.plot(x,-y, 'b', label='BLUE')
ax.legend()
plt.legend(loc='center right', bbox_to_anchor=(1.0, 0.5), ncol=1)
plt.savefig('data/ch13_graph1.png') #그래프를 파일로 저장
plt.show()


# - 그래프 양식참고(범례 위치 조정 등)
# - https://stackoverflow.com/questions/30490740/move-legend-outside-figure-in-seaborn-tsplot

# In[ ]:




