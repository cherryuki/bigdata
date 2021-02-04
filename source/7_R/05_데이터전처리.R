# 2021-02-04 R_데이터 전처리      ⓒcherryuki(ji) #
# # # 5장. 데이터 전처리; 제어문, function # # #

# 1. 파일 입출력
# 1.1 시스템 인코딩 조회
Sys.getlocale() #Korea.949(CP949)

# 1.2 write.table(); 데이터를 파일에 저장
iris
class(iris)
write.table(iris, file="outData/iris.csv", sep=",", row.names=FALSE)
InsectSprays
write.table(InsectSprays, file='outData/insect.csv', sep=',')

# 1.3 read.table(); 파일을 읽어 데이터프레임 형태로 저장
irisData <-read.table("outData/iris.csv", sep=',', header=TRUE, encoding='UTF-8', stringsAsFactors = TRUE)
#stringsAsFactors=TRUE: 문자열 모두 팩터로 잡힘(자주 안씀)

head(irisData)
tail(irisData)
str(irisData)
irisData$Species <-as.factor(irisData$Species)
irisData$Species <-factor(irisData$Species, levels=c("setosa", "versicolor", "virginica"))
irisData$Species
str(irisData$Species)
nrow(irisData)
summary(irisData)

# 1.4 write.csv(); csv파일 형식으로 저장
write.csv(iris, file="outData/iris1.csv")
write.csv(iris, file="outData/iris1.csv", quote=FALSE)

# 1.5 read.csv(); csv파일 읽기
#newData <-read.csv(file.choose()) #탐색기 열림
newData <-read.csv('outData/iris1.csv', header=TRUE, stringsAsFactors = TRUE)
head(newData)
tail(newData)
str(newData)
summary(newData)

# 1.6 cat(); 분석 결과등을 저장할 때
irisSummary <-summary(newData)
class(irisSummary)
irisSummary[1,]
nrow(irisSummary)
cat('iris 요약:', '\n', file='outData/irisSummary.txt')
for(i in 1:nrow(irisSummary)) {
  cat(irisSummary[i,], '\n', file='outData/irisSummary.txt', append=T)
}

# 2. apply계열 함수 적용
# 2.1 apply
#iris데이터의 열별평균(합계, 분산, 표준편차, 최소값, 최대값, 중앙값)
#apply(대상자료, 1or2, 함수) 1:행별 함수 수행, 2: 열별 함수 수행
head(iris[,1:4])
head(iris[,-5])
apply(iris[,1:4], 1, mean)#행별 평균
apply(iris[,-5], 2, mean)#열별 평균
#setosa종과 versicolor종과 virginica종을 분류하고 각각의 열별 평균 구하기
apply(subset(iris, iris$Species=='setosa', select=-5), 2, mean)
apply(subset(iris, iris$Species=='versicolor', select=-c(5)),2, mean)
apply(subset(iris, iris$Species=='virginica', select=c(-5)),2, mean)

apply(iris[,1:4], 2, FUN=mean)   #열별 평균
apply(iris[,1:4], 2, FUN=sd)     #열별 표준편차
apply(iris[,1:4], 2, FUN=sum)    #열별 합계
apply(iris[,1:4], 2, FUN=median) #열별 중앙값
apply(iris[,-5], 2, FUN=min)    #열별 최소값
apply(iris[,-5], 2, FUN=max)    #열별 최대값

#InsectSPrays에서 count의 표준 편차
apply(InsectSprays['count'],2, FUN=sd)

name <-c('김', '이', '박', '강', '윤')
kor <-c(90, 50, 70, 60, 100)
eng <-c(100,40,50,60,70)
mat <-c(90,91,50,64,80)
student <-data.frame(name, kor, eng, mat)
student
apply(student[,-1], 1, mean) #학생별 평균
apply(student[,-1], 2, mean) #과목별 평균

#2.2 lapply: list apply(결과도 list)
x <- list(a=1:10, beta=exp(-3:3), logical=c(T,F,F,T))
#지수함수: exp(a:b) e의 a승부터 e의 b승까지 출력
x
lapply(x, mean)
lapply(x, quantile) #4분위수
lapply(x, quantile, 1:3/4)

# 2.3 sapply: lapply와 유사하나 결과를 행렬이나 벡터로 반환
sapply(x, mean)
sapply(x, quantile)
sapply(x, quantile, 1:3/4)

fivenum(0:10)
i39 <-sapply(c(3:9), seq)
i39
sapply(i39, fivenum)
lapply(i39, fivenum)

#Q. iris데이터를 lapply와 sapply를 이용하여 Sepal.Length~Petal.Width까지의 평균
irisList <- as.list(iris[,1:4])
irisList
lapply(irisList, mean)
sapply(irisList, mean)

lapply(iris[,-5], mean)
sapply(iris[,-5], mean)

# 2.4 vapply: sapply와 유사하나 FUN의 모든 값이 FUN.VALUE와 호환되는지 확인
vapply(irisList, mean, numeric(1))
vapply(i39, fivenum,
       FUN.VALUE = c(numeric(1), numeric(1), numeric(1), numeric(1), numeric(1)))
cities <-c('Seoul', 'Busan', 'New York', 'Tokyo')
nchar(cities[1])
sapply(cities, nchar)
lapply(cities, nchar)
vapply(cities, nchar, FUN.VALUE=numeric(1))

# 2.5 mapply: sapply와 유사하나 다수의 인자를 함수에 전달
rep(c(1:3), 3)
x <-c(1,2,3,4)
mean(x)
mapply(rep, x=1:4, times=4:1) #rep(1,times=4) rep(2,times=3) rep(3,times=2) rep(4, times=1)
mapply(rep, x=1:4, each=4:1) #rep(1, each=4) rep(2, each=3) rep(3, each=2) rep(4, each=1)

rm(list=ls())
#직업별 수입
job <-c(3,3,5,2,2,3,5,3,4,4,6,3)
income <-c(4897,6509,4183,0,3894,0,3611,6454,4975,8780,0,4362)
cust <-data.frame(job, income)
cust
income.avg <-c(862, 0, 3806, 3990, 3891, 3359, 3556, 2199)
names(income.avg) <-0:7
income.avg
zero2mean <-function(job, income) {
  #return(ifelse(income==0, income.avg[as.character(job)], income))
  if(income==0) {
    return(income.avg[as.character(job)])
  }else {
    return(income)
  }
}

#mapply(zero2mean, cust$job, cust$income)
cust$income2 <- mapply(zero2mean, cust$job, cust$income)
cust

# 3. 데이터 그룹화 함수 적용
# 3.1 tapply: 그룹별 처리를 위한 apply함수
tapply(iris$Sepal.Length, iris$Species, mean) #종별 꽃받침 길이의 평균
tapply(iris$Sepal.Length, iris$Species, sd) #종별 꽃받침 길이의 표준편차
boxplot(iris$Sepal.Length~iris$Species) #분포도(시각화)

cust
#직업별
cust$job <-factor(cust$job, levels=0:7) #as.factor로만 하면 현재 없는 직업번호가 누락 됨
str(cust)
tapply(cust$income2, cust$job, mean) #직업별 평균(없는 값: NA로 나옴)
tapply(cust$income2, cust$job, FUN=mean, default = -1) #default=NA대체값

datasets::InsectSprays
head(InsectSprays)
tail(InsectSprays)
str(InsectSprays)

# spray의 종류에 따른 살충효과를 점검
tapply(InsectSprays$count, InsectSprays$spray, mean)
nrow(InsectSprays)
tapply(InsectSprays$count, InsectSprays$spray, sd)
boxplot(InsectSprays$count~InsectSprays$spray)

#tapply(InsectSprays$count, InsectSprays, FUN=c(mean, sd)) #불가능 ->summaryBy로 가능
#tapply(iris[,1:2], iris[,5], sum) #불가능 -> by로 가능

# 3.2 by: 그룹화 처리를 위한 apply(함수 2개 이상 가능)
by(iris[,1:2], iris[,5], sum)
by(iris[,1:2], iris[,5], min)
by(iris[,1:4], iris$Species, summary) #종별 summary 가능

#cust의 직업별 평균을 income과 income2 한번에 #mean은 불가능
by(cust[,c('income', 'income2')], cust$job, summary)

# 3.3 doBy 패키지
install.packages('doBy')
library(doBy) #따옴표 생략 가능
summaryBy(Sepal.Length+Sepal.Width~Species, iris) #함수명 defalut:mean
summaryBy(Sepal.Length+Sepal.Width+Petal.Length+Petal.Width~Species, iris, FUN=sd)
summaryBy(Sepal.Length+Sepal.Width+Petal.Length+Petal.Width~Species, 
          iris, FUN=c(mean, sd))

#Q. emp.csv 파일의 데이터를 받아 부서별 급여, 상여금을 비교
emp <-read.csv(file="inData/emp.csv", header=T)
emp
str(emp)
emp$deptno <-factor(emp$deptno, levels=seq(10,40,10))
names(emp)
tapply(emp$sal, emp$deptno, FUN=mean)
tapply(emp$comm, emp$deptno, FUN=mean, na.rm=T)
summaryBy(sal+comm~deptno, emp, FUN=mean, na.rm=T) #na.rm=T 결측치 제외

# (2) orderBy 정렬
orderBy(~Sepal.Length, data=iris) #오름차순 정렬
orderBy(~-Sepal.Length, data=iris) #내림차순 정렬(-)
orderBy(~Species+Sepal.Length, data=iris) #Species, Sepal.Length 오름차순
orderBy(~Species-Sepal.Length, data=iris) #Species, Sepal.Length 내림차순
#종별, Sepal.Length 오름차순으로 정렬한 데이터 'Sepal.Length', 'Sepal.Width', 'Species' 출력
orderBy(~Species+Sepal.Length, data=iris[, c('Sepal.Length', 'Sepal.Width', 'Species')])

head(orderBy(~Species+Sepal.Length, data=iris))
tail(orderBy(~Species+Sepal.Length, data=iris))

#Q1. emp데이터셋에서 월급이 적은 순으로 ename, sal 추출
orderBy(~sal, data=emp[,c('ename', 'sal')])
#Q2. 월급이 적은 순 5명만 ename, sal
head(orderBy(~sal, data=emp[,c('ename', 'sal')]),5)

# (3) sampleBy
sampleBy(~Species, data=iris, frac=0.1) #group별 10%씩 표본 추출(비복원 임의 추출)
sampleBy(~Species, data=iris, frac=0.1, replace=T) #복원 임의 추출(중복된 데이터 뽑힐 수 있음)
sampleBy(~Species, data=iris, frac=0.1, systematic=T) #계층적 추출

#벡터 샘플링
idx <-sample(1:150, 10)
idx
iris[idx,] #전체에서 10개 임의 추출 #nrow[data]*0.7: 70%임의 추출시

# 4. Formula: ~, +, -, :, * 등
## lm() 선형회귀식 도출 함수(독립변수, 종속변수 연속적 변수에서 사용)
x <- c(1,2,3,4,5) #공부 시간(독립변수)
y <- c(20,41,59,81,98) #점수(종속변수) -회귀분석
y1 <- c('F', 'F', 'F', 'P', 'P') #당락여부(종속변수) -로지스틱 회귀; glm()

fit <-lm(y~x)
fit
plot(x,y, col='blue')
lines(x, x*19.6+1.0, col='red')
abline(fit, lty='dashed')

# 독립변수가 2개
x1<-c(1,2,3,4,5) #공부시간
x2<-c(10,20,3,4,5) #기출문제 푼 수
y <-c(50, 70, 63, 84, 95) #종속변수
fit <-lm(y~x1+x2) #x1과 x2사이의 상관관계가 없다는 전제 필요
fit

#cars
cars
?cars #속도에 따른 제동거리를 회귀식으로 도출
fit <-lm(cars$dist~cars$speed)
fit <-lm(dist~speed, data=cars)
fit
plot(cars)
plot(cars$speed, cars$dist, col='green')
lines(cars$speed, cars$speed*3.932-17.579, col="blue")
abline(fit, lty="dotted")

# 5. 데이터 분리
# 5.1 split
