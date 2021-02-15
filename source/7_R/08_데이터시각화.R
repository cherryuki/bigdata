# 2021-02-10 R_데이터 시각화      ⓒcherryuki(ji) #
# # # 8장. 데이터 시각화 # # #
#시각화: 원본 데이터, 분석된 결과 데이터를 그래프로 표현. 
#사용자에게 효과적으로 정보전달하는 것이 목적

#R의 그래픽 시스템
# (1) base graphics system - 전통적인 함수 이용
    # 그래프 종류별 함수가 각기 달라 정교한 그래프 이용시 노력 필요
# (2) grid graphics system - base graphics system 한계 극복을 위해 탄생한 패키지(ggplot2)
    # 유연한 그래프 환경 제공

#ex.
library(ggplot2)
ggplot(data=mtcars, aes(x=wt, y=mpg)) +
  geom_point() +
  labs(title="그래프 첫 예제") +
  geom_smooth()

# 1.2 그래프 함수
 # 고수준 그래프 함수: plot, barplot, boxplot, hist, pie, ...
  # 그래프 함수를 호출할 때마다 그래프 영역에 새로운 그래프를 그림(매번 초기화 후 다시 그림)
 # 저수준 그래프 함수: lines, abline(회귀라인), point, text, ...
  # 이미 그려진 그래프 위에 점, 선, 텍스트, 장식 등을 더하기 위해 사용

# 1.3 그래프 파라미터: bty(박스 유형), ...
# (1) par(): 그래프를 조정하거나 특성을 지정, par()함수의 리턴값은 실행 전 특성
?cars #차의 속도와 제동거리
plot(cars)
oldPar <-par(bty='L')
plot(cars)
plot(iris)
par(oldPar) #oldPar 설정으로 복귀
plot(cars) #고수준 그래프; 새로 그림
#fit <- lm(cars$dist~cars$speed)
fit <-lm(dist~speed, data=cars)
fit
abline(fit, col=2) #저수준 그래프; 추가

#par함수의 다른 파라미터 사용
x <-1:100
y1 <-rnorm(100) #표준정규분포(평균0, 표준편차1) 실수 100개 임의추출
y2 <-rnorm(100)+100 #평균 100, 표준편차 1인 수(정규분포) 100개 임의 추출

oldPar <-par(mar=c(5,5,5,5)) #그래프 여백(margin) mar=c(하,좌,상,우) defalut c(5,4,4,2)+0.1
?par
plot(x,y1, pch=0, type="b", col="springgreen3",
     ylim=c(-8,2), yaxt="n", bty="n", ylab="")
  #pch; 점모양 0:네모, 1:원, 2:세모, 3:십자, 4:x, 5:다이아몬드 등
  #type; p:점, l:선, b:점&선, o:점&선 겹치게, h:히스토그램 s:계단모양 n:좌표 찍지 않음
  #col; 1:black, 2:red, 3:green, 4:blue, 5:cyan, 6:purple, 7:yellow, 8:gray
  #ylim, xlim; y축 눈금, x축 눈금 조정
  #yaxt; y축 눈금 yaxt="n"; y축 눈금 없애기
  #bty; 박스타입 o, L, 7, c, u, n(박스 없음)
axis(side=2, at=c(-2,0,2)) #저수준 함수는 그래프 영역에 그래프가 있는 상태에서만 사용 가능
  #side; 1하 2좌 3상 4우
  #at; 위치
mtext("green line(y1)", side=2, line=2, at=0, col=3)
?points
colors()

par(new=TRUE) #기존 그래프 영역을 지우지 않고 덧그림(고수준 함수도 적용)
plot(x, y2, pch=1, type='b', col='tan3', yaxt='n', ylim=c(98,108), ylab='', bty='n')
axis(side=4, at=c(98,100,102))
mtext("tan line(y2)", side=4, line=2, at=100, col="tan3")

par(oldPar) #그래프 영역 설정 원상 복구

# 2. 고수준 그래프 함수
# 2.1 plot: type에 따라 여러 유형의 그래프를 그림. 산점도 그래프 함수
plot(cars, main="Speed and Stopping Distance of Cars",
     xlab="speed(mph)", ylab="stopping distances(ft)", las=1)
  #las; 축 눈금 라벨 방향 0: 축과 평행, 1:평행, 2:축과 수직, 3:수직
?plot
#2행3열로 그래프 영역 분리하고 type 속성에 따른 그래프 그리기
oldPar <-par(mfrow=c(2,3))
plot(cars, type="p", main="p타입") #일반적 산점도(점이 산발적)
plot(cars, type="l", main="l타입") #추세선
plot(cars, type="b", main="b타입") #점, 선 겹치지 않게
plot(cars, type="o", main="o타입") #점, 선 겹치게
plot(cars, type="s", main="s타입") #계단 타입
plot(cars, type="n", main="n타입") #좌표 찍히지 않음

par(oldPar)
# 2.2 barplot; 막대 그래프
VADeaths
barplot(VADeaths, main="버지니아주 사망률", font=2,
        border="red", legend=rownames(VADeaths),
        angle=c(10, 30, 50, 70, 120),
        density=50, col=terrain.colors(5), beside=T)
  #legend; 오른쪽 상단 범례
  #angle; 막대 그래프에 칠할 빗금 각도
  #density; 막대 그래프 안에 칠할 선 수(밀도)
  #beside; 기본 값 F: 누적 막대그래프, T: 옆으로 

# 2.3 boxplot: 사분위수 그래프
InsectSprays
boxplot(InsectSprays$count)
boxplot(count~spray, data=InsectSprays, col="steelblue")
tapply(InsectSprays$count, InsectSprays$spray, median)

# 2.4 hist: 히스토그램(도수 분포표)
x <-c(1,1,2,2,2,3,4,4)
hist(x)
h <-hist(x, breaks=0:4, las=1)
  #breaks; 구간(눈금 구간)
h
text(h$mids, h$counts, h$counts)
text(h$mids, h$counts, h$counts, adj=c(0.5, -.2), col="1")
text(h$mids, h$counts, h$counts, adj=c(0,0), col='red')
text(h$mids, h$counts, h$counts, adj=c(1,0), col='blue')
text(h$mids, h$counts, h$counts, adj=c(0,1), col='green')
text(h$mids, h$counts, h$counts, adj=c(1,1), col='orange')
  #adj; 위치 재조정

islands #1만 평방 마일을 초과하는 주요 대륙 넓이 정보
class(islands)
is.vector(islands)
hist(sqrt(islands), breaks=c(2,35,70,100,140))

# 2.5 pie
pie.sales <-c(0.1, 0.3, 0.2, 0.15, 0.1, 0.15)
sum(pie.sales)
names(pie.sales) <-c("c","java","python","R","oracle","hadoop")
pie.sales
pie(pie.sales) #반시계 방향으로
pie(pie.sales, clockwise = T, #시계방향
    col=c('red', 'orange', 'yellow', 'green', 'blue', 'purple'))
pie(pie.sales, clockwise = T, col=topo.colors(6))

# 2.6 mosaicplot
?Titanic
class(Titanic) #table
Titanic
mosaicplot(Titanic, color=T)
mosaicplot(~Sex+Age+Survived, data=Titanic, color=T)

# 3. 저수준 그래프 함수
# 3.1 points
plot(-4:4, -4:4, type="n")
points(2,2, col="red")
rnorm(100) #평균0, 표준편차1인 표준정규분포 데이터 100개 난수 생성
points(rnorm(100), rnorm(100), col="tan3", pch=3)

# 3.2 lines
plot(cars, main="speed & distance")
fit <-lm(dist~speed, cars)
fit #y=3.932x-17.579
lines(cars$speed, 3.932*cars$speed-17.579, col="blue")

# 3.3 ablines: 회귀식 선
abline(fit, col="red", lty="dashed")
  #lty; 라인 타입(1:solid, 2:dashed, 3:dotted, 4:dotdash, 5:longdash, 6:twodash)
?abline
?par

# 3.4 text(x,y, 출력할 텍스트, 그 외 옵션들)
plot(1:5, 1:5, type="n")
text(3,3, 'A', adj=c(0,0), col="red")
text(2,4, expression(hat(beta)==(x^t*x)^{-1}*X^t*y), cex=2, adj=c(0,0))

# 4. ggplot2 패키지 함수
install.packages("ggplot2")
library(ggplot2)
# 1: 그래프 초기화(데이터셋, 변수 설정) - 그래프 표현X
# 2: 그래프의 결과물에 대응하는 geom 함수
# 3: 제목, 부제목, 캡션, 축이름 등 부가요소를 추가
# +기호를 이용해서 함수들 연결방식으로 그래프 생성
ggplot(data=mtcars, aes(x=wt, y=mpg)) +
  geom_point(aes(size=mpg, color=cyl)) +
  labs(title="wt & Fuel consumption",
       x="weight(1,000lbs)",
       y="Fuel consumption(miles per gallon)",
       subtitle="(차량 무게와 연비와의 관계)",
       caption="source: mpg datasets")

# 4.1 산점도, 적합도, text, ...
#1. x축: iris$Petal.Width, y축: iris$Petal.Length 값을 나타내는 산점도, 종에 따라 다른 색
ggplot(data=iris, aes(x=Petal.Width, y=Petal.Length)) +
  geom_point(aes(color=Species)) +
  scale_color_manual(values=c('black', 'red', 'orange')) +
  labs(title="iris 데이터의 산점도",
       x='꽃잎 너비', '꽃잎 길이') +
  coord_cartesian(xlim=c(0,2)) + #출력 범위 설정
  geom_smooth()
#2. x축: iris$Petal.Width, y축: iris$Petal.Length 값을 나타내는 산점도 
#(단, Species에 따라 산점도의 점을 다른 색, 점의 크기는 Petal.Width의 크기가 클수록 큰 점)
ggplot(data=iris, aes(x=Petal.Width, y=Petal.Length)) +
  geom_point(aes(color=Species, size=Petal.Width))
#3. 태양 복사량과 오존량 상관관계 확인 위한 그래프
 # airquality$Ozone, airquality$Solar.R 과의 관계(월별 점의 색을 달리 표현)
ggplot(data=airquality, aes(x=Ozone, y=Solar.R)) +
  geom_point(aes(col=Month)) +
  labs(title="오존량과 태양 복사량의 관계",
       caption="source: airquality") +
  geom_smooth(method="lm")
?geom_smooth

ggplot(data=mtcars, aes(x=wt, y=mpg)) +
  geom_point(pch=23, color="yellow", bg="red", size=2, stroke=2) +
  geom_smooth(method="lm", color="red", size=2, linetype=2) +
  geom_text(label=rownames(mtcars), hjust=0, vjust=0, size=3, nudge_y=0.5) +
  labs(title="차량 무게와 연비와의 관계",
       x="차량 무게(1,000lbs)",
       y="연비(miles per gallon)",
       subtitle="(부제목)",
       caption="참조:datasets의 mtcats")
  #shape; par의 pch와 동일(pch부분에 shape으로 기재해도 동일)
  #size; 점 크기 
  #stroke; 테두리 두께

# 4.2 히스토그램
head(mtcars)
dim(mtcars)
str(mtcars)
mtcars$cyl <-factor(mtcars$cyl, levels=c(4,6,8),
                     labels=c('4 cylinders', '6 cylinders', '8 cylinders'))
head(mtcars)
str(mtcars$cyl)
ggplot(data=mtcars, aes(x=mpg)) +
  geom_histogram() +
  facet_grid(cyl~.) + #복수 패널에 그리기
  labs(title="실린더에 따른 연비 히스토그램",
       x="연비", y="횟수")
?facet_grid


# 2021-02-15 R_데이터 시각화      ⓒcherryuki(ji) #
#히스토그램은 연속형 자료형에서의 도수분포표(범주형 도수분포는 histogram불가능)
library(ggplot2)
ggplot(data=mtcars, aes(x=cyl)) +
  #geom_histogram() #cyl데이터는 연속형이 아니므로 사용 불가
  geom_bar() #범주형에서는 histogram 아닌 bar 사용

#ggplot2::mpg 데이터셋에서 displ 도수 분포표(class에 따라 그래프 색상 달리 표현)
str(mpg$displ)
ggplot(mpg, aes(x=displ)) +
  geom_histogram(aes(fill=class)) +
  theme(axis.text.x=element_text(color="red", size=15),
        axis.line=element_line(color="black", size=2),
        axis.text.y=element_blank(), #y축 눈금 숫자 사라짐
        panel.background = element_rect(fill="paleturquoise", linetype="dashed", color="blue"),
        plot.background = element_rect(fill="lightyellow"))

?geom_histogram
colors()

ggplot(mpg, aes(x=displ)) +
  geom_histogram(aes(fill=class),
                 binwidth = 0.1) + #binwidth: 빈(그래프 막대)의 너비
  labs(title="Histogram with Auto Bining",
       subtitle="(Engine Displacement across Vihival Classes)") +
  theme(legend.position = "bottom")

ggplot(mpg, aes(x=displ)) +
  geom_histogram(aes(fill=class),
                 bins=5, #빈의 개수 지정(지정 안하면 30), binwidth 지정시 bins 무시됨
                 col='black')

# 4.3 상자 도표(boxplot)
boxplot(iris$Sepal.Length)$stat #이상치 처리 위함
ggplot(iris, aes(y=Sepal.Length)) +
  geom_boxplot()

# 종별 Sepal.Length의 차이가 있는지 보고 싶을 때
tapply(iris$Sepal.Length, iris$Species, mean) #도표 표현
ggplot(iris, aes(y=Sepal.Length, x=Species)) + #시각화 표현
  geom_boxplot(aes(fill=Species), col="tan3") + #col=선, 점 색상
  scale_fill_manual(values=c('yellow', 'orange', 'red'))

library(RColorBrewer) #색 팔레트 사용 위함
display.brewer.all()
pal <-brewer.pal(8, 'Pastel1')
ggplot(iris, aes(y=Sepal.Length, x=Species)) +
  geom_boxplot(aes(fill=Species), col="dimgray") +
  scale_fill_manual(values=pal)

install.packages('gapminder')
library(gapminder)
table(gapminder$country)
dim(gapminder)

#대륙별 GDP 차이가 있는지
ggplot(gapminder, aes(x=continent, y=gdpPercap)) +
  geom_boxplot(aes(fill=continent)) +
  scale_fill_manual(values=pal) +
  coord_cartesian(ylim=c(0, 30000))

#교수별 직급별(조교수, 부교수, 정교수) 연봉이 상이한지
install.packages("car")
library(car)
Salaries
head(Salaries)
str(Salaries)

ggplot(Salaries, aes(x=rank, y=salary)) +
  geom_boxplot(aes(col=rank), fill="lightyellow", notch=T) +
  #notch=T; 중위수에 대해서 ,95% 신뢰구간 표현, 신뢰구간이 겹치는지 파악 위함
  geom_point(position='jitter', col="tan3", alpha=0.3, pch=2) +
  #position='jitter'; 산점도를 분산해서, alpha; 투명도(0~1)
  geom_rug(col="gray", sides="l") #관측값 밀도 상태 표현(데이터가 많을 수록 빽빽)

#mtcars 데이터 cyl개수에 따른 연비 mpg의 95% 중위수 신뢰구간을 표현한 상자 도표를 시각화
head(mtcars)
ggplot(mtcars, aes(x=cyl, y=mpg, fill=cyl)) +
  geom_boxplot(notch=T)
ggplot(mtcars, aes(cyl, x=mpg, fill=cyl)) +
  geom_boxplot(notch=T)

# 4.4 바이올린 도표; boxplot과 밀도도표를 합침
# 합창부 단원의 키와 성악부 part의 관계
singer <-lattice::singer
head(singer)
str(singer)

ggplot(data=singer, aes(x=voice.part, y=height)) +
  geom_boxplot()

ggplot(data=singer, aes(x=voice.part, y=height)) +
  geom_violin(fill='honeydew2') +
  geom_boxplot(width=0.3, fill='forestgreen')

# 4.5 밀도도표
head(mtcars)
#실린더수(cyl)에 따른 연비(mpg)의 밀도도표
ggplot(data=mtcars, aes(x=mpg, fill=cyl)) +
  geom_density() +
  labs(title="밀도 도표", x="Miles per Gallon") +
  theme(legend.position = c(0.9, 0.8)) #그래프 안에 넣을 때는 (0,0)~(1,1) 사이

# 4.6 추세선
economics
colnames(economics)
#시간(date)에 따른 실업률(unemploy)
ggplot(data=economics, aes(x=date, y=unemploy)) +
  geom_line() + #추세선
  geom_smooth() #적합도선

# 4.7 막대도표(geom_bar함수, geom_col함수)
#도수 분포표: 막대도표, 히스토그램 모두
  #히스토그램: 연속형 자료를 계급으로 나누어 계급별 도수(횟수) 나타냄
          #geom_histogram()
  #막대 그래프: 범주형 자료의 빈도를 나타냄
          #geom_bar(), geom_col()

#mpg 데이터셋에서 제조회사별로 빈도표 나타내기
head(mpg)
str(mpg)
ggplot(data=mpg, aes(x=manufacturer)) +
  geom_histogram() #불가능
ggplot(data=mpg, aes(x=manufacturer)) +
  geom_bar(stat="count") #stat="count": 빈도를 시각화(생략 가능)

str(mpg$class)
ggplot(data=mpg, aes(x=manufacturer, fill=class)) +
  geom_bar(stat='count') +
  theme(legend.position="top",
        axis.text.x=element_text(angle=60, vjust=0.6)) +
  scale_fill_manual(values=topo.colors(10)) +
  labs(title="제조사별 class 빈도표")

#다이아몬드 품질별 데이터
head(diamonds)
str(diamonds)
dim(diamonds)
table(diamonds$cut)
#다이아몬드 품질(cut)별 빈도수
ggplot(data=diamonds, aes(x=cut, fill=cut, col=cut)) +
  geom_bar(stat="count") + #col은 테두리 색
  scale_fill_manual(values=topo.colors(5)) +
  scale_color_manual(values=rainbow(5))

#다이아몬드 품질별 색상 개수
table(diamonds$cut, diamonds$color)
library(dplyr)
diamonds %>% 
  group_by(cut, color) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=cut, fill=color, y=n)) +
  geom_bar(stat="identity") #y값이 있는 경우: geom_col or geom_bar(state="identity")
?geom_bar
diamonds %>% 
  group_by(cut, color) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=cut, fill=color, y=n)) +
  geom_col()

#cut별, color별 막대 그래프
diamonds %>% 
  group_by(cut, color) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=cut, fill=color, y=n)) +
  geom_bar(stat="identity", position='dodge')
diamonds %>% 
  group_by(cut, color) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=cut, fill=color, y=n)) +
  geom_col(position="dodge")

#다이아몬드 품질별, table별 빈도수 시각화
diamonds %>% 
  group_by(cut, table) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=cut, fill=table, y=n)) + 
  geom_col()

diamonds %>% 
  group_by(cut, table) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=table, fill=cut, y=n)) +
  geom_col() +
  facet_wrap(~cut) + #cut별로 그래프 따로 그림: facet_wrap
  coord_cartesian(ylim=c(0,3000), xlim=c(50,70))

#다이아몬드 품질별 table의 종류 갯수
length(table(diamonds$table)) #127개
diamonds %>% 
  group_by(cut, table) %>% 
  summarise(n=n()) %>% 
  group_by(cut) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=cut, y=n, fill=cut)) +
  #geom_bar(stat="identity")
  geom_col() +
  labs(title="다이아몬드 품질별 table 종류 수",
       x="품질(cut)별", y="테이블 종류")

diamonds %>% 
  group_by(cut) %>% 
  summarise(n=n_distinct(table)) #cut별 table 종류 개수

# 4.8 그래프를 파일로 저장
# (1) basic 그래프, ggplot2 그래프 모두 저장 가능한 방법
jpeg('outData/08_iris.jpg') #iris.jpg 그림파일 생성
boxplot(iris$Sepal.Length)
dev.off()
png('outData/08_iris.png', width=300, height=150) #iris.png 파일 생성
ggplot(iris, aes(x=Sepal.Length, y=Sepal.Width)) +
  geom_point() +
  facet_wrap(~Species)
dev.off()

# (2) ggplot2 그래프에서만 저장할 수 있는 방법
ggplot(iris, aes(x=Petal.Width, y=Petal.Length, col=Species)) +
  geom_point(aes(size=Petal.Width), pch=2, alpha=0.5)
ggsave('outData/08_iris.jpg') #동일 파일명 있을경우 덮어씀

# 4.9 그래프 분할 출력(gridExtra)
oldPar <-par(mfrow=c(2,3)) #basic 그래프에서 사용(ggplot에는 적용X)
ggplot(iris, aes(x=Petal.Width, y=Petal.Length)) +
  geom_point()
par(oldPar)

install.packages("gridExtra")
library(gridExtra)
g1 <- ggplot(iris, aes(x=Petal.Width, y=Petal.Length)) +
  geom_point()
g2 <-ggplot(iris, aes(x=Sepal.Width, y=Sepal.Length)) +
  geom_point()
grid.arrange(g1, g2, ncol=2)

# 5. 산점도 행렬
plot(iris[-5])
pairs(iris[-5], panel=panel.smooth) #추세선(적합도선) 추가; panel=panel.smooth
