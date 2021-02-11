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

#1. x축: iris$Petal.Width, y축: iris$Petal.Length 값을 나타내는 산점도, 종에 따라 다른 색
ggplot(data=iris, aes(x=Petal.Width, y=Petal.Length)) +
  geom_point(aes(color=Species))
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
