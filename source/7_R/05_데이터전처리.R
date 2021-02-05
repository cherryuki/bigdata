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
iris.species <-split(iris, iris$Species) #list형태
iris.species
iris.species['virginica']
head(iris.species$'versicolor')
iris.sepal <- split(iris, iris$Sepal.Length>5) #TRUE, FALSE로 나뉨
iris.sepal
iris.sepal['FALSE']
head(iris.sepal$'FALSE')

#5.2 subset
#Q1. setosa종 중 Sepal.Length, Petal.Length 열 출력
subset(iris, subset=(iris$Species=='setosa'), select=c('Sepal.Length', 'Petal.Length'))
#Q2. setosa종 중 Sepal.Length, Sepal.Width, Petal.Length, Petal.Width 열 출력
subset(iris, subset=(iris$Species=='setosa'), select=c(1:4))
subset(iris, subset=(iris$Species=='setosa'), select=(-5))
subset(iris, subset=(iris$Species=='setosa'), select=c(-5))
subset(iris, subset=(iris$Species=='setosa'), select=-c(5))
#Q3. setosa 중 Sepal.Length가 4이상인 데이터
subset(iris, subset=(iris$Species=='setosa' &iris$Sepal.Length>=4))

# 6. 데이터 합치기
# 컬럼합치기 cbind()
# 행 합치기 rbind()
# 병합하기 merge()
# 6.1 cbind
student.a <-data.frame(name=c('kim', 'kong'), score=c(100, 90))
student.a
student.b <-data.frame(id=c(100,101), gender=c('f', 'm'))
student.b
(student <-cbind(student.a, student.b))

# 6.2 rbind
student.a <-data.frame(name=c('kim', 'kong'), score=c(100,90))
student.b <-data.frame(name=c('park', 'han'), score=c(100,85))
(student <-rbind(student.a, student.b))

# 6.3 merge
student.a <-data.frame(name=c('kim', 'lee'), kor=c(100, 90))
student.b <-data.frame(name=c('kim', 'lee'), mat=c(100,80), eng=c(90,80))
(student <-merge(student.a, student.b))

student.a <-data.frame(name=c('kim', 'yun'), kor=c(100, 90))
student.b <-data.frame(name=c('kim', 'lee'), mat=c(100, 80), eng=c(90, 80))
(student <-merge(student.a, student.b)) 
(student <-merge(student.a, student.b, all=T)) 
#all=T를 붙이면 없는 항목 NA (기본값 F: 결측치 있는 데이터는 출력X)

# 7. 데이터 정렬
# sort() 정렬된 데이터 반환
# order() 정렬된 데이터의 index 반환
data <-c(10, 30, 100, 1, 5)
sort(data) #오름차순 정렬
sort(data, decreasing=T) #내림차순 정렬
sort(iris$Sepal.Length)

names(data) <-c('1번째', '2번째', '3번째', '4번째', '5번째')
data
sort(data)
order(data) #정렬된 데이터의 색인
data[order(data)] #sort(data)와 동일
#iris데이터를 Sepal.Length를 기준으로 내림차순 정렬
sort(iris$Sepal.Length, decreasing = T)
order(iris$Sepal.Length, decreasing = T)
iris[order(iris$Sepal.Length, decreasing = T),]
orderBy(~-Sepal.Length, data=iris)

#iris데이터를 Sepal.Length(내림차순), Sepal.width(오름차순) 
#내림차순:-
order(-iris$Sepal.Length+iris$Sepal.Width)
iris[order(-iris$Sepal.Length+iris$Sepal.Width), 1:2]

#emp 데이터셋에서 월급이 많은 순으로 ename, sal을 추출
order(-emp$sal)
emp[order(-emp$sal), c('ename', 'sal')]
#월급이 많은 top5명의 ename, sal을 추출
head(emp[order(-emp$sal), c('ename', 'sal')], 5)
#월급이 적은 top5명의 ename, sal을 추출
tail(emp[order(-emp$sal), c('ename','sal')],5)

# 8. 데이터 프레임 이름 생략하기
# 8.1 with절, within절
iris.temp <-iris
iris.temp[c(1,3), 1] <-NA
head(iris.temp)
#종별 중앙값
split(iris.temp$Sepal.Length, iris.temp$Species) #결과는 list
(mps<-sapply(split(iris.temp$Sepal.Length, iris.temp$Species), median, na.rm=T))
(mps <-tapply(iris.temp$Sepal.Length, iris.temp$Species, median, na.rm=T))
mps
mps['setosa']
iris.temp$Sepla.Length2 <-ifelse(is.na(iris.temp$Sepal.Length), mps[iris.temp$Species], iris.temp$Petal.Length)
head(iris.temp)
iris.temp$Sepla.Length2 <-NULL

#with절은 Sepal.Length의 결측치가 대치된 결과값을 반환
#within절은 Sepla.Length의 결측치가 대치된 데이터 프레임 셋 반환
iris.with <-with(iris.temp, {#iris.temp 생략
  mps <-tapply(Sepal.Length, Species, median, na.rm=T) 
  Sepal.Length <-ifelse(is.na(Sepal.Length), mps[Species], Sepal.Length)
})
head(iris.with)

iris.within <-within(iris.temp, {#iris.temp 생략
  mps <-tapply(Sepal.Length, Species, median, na.rm=T) 
  Sepal.Length <-ifelse(is.na(Sepal.Length), mps[Species], Sepal.Length)
})
head(iris.within)
head(iris.temp)

# 8.2 attach(), detach() 함수
attach(iris) #이 부분 아래는 iris$ 생략해도 되는 구간
summary(Species)
tapply(Petal.Length, Species, mean)
detach(iris) #attach 기능 해제

# 9. 데이터 집계
# 9.1 table
table(iris$Species) #factor 변수 쓰기(팩터 변수가 아니면 집계 무의미)
table(emp$deptno)

head(InsectSprays)
#InsectSprays 데이터셋에서 spray별 집계
table(InsectSprays$spray)

#emp데이터 셋에서 deptno별 집계
str(emp)
#emp$deptno <-factor(emp$deptno, levels=seq(10,40,10))
table(emp$deptno)

# 9.2 aggregate: 데이터를 하위 집합으로 분할하고 요약 통계 계산
aggregate(iris[,1:4], by=list(iris[,5]), mean)

#보험회사의 고객들이 보험금을 청구하는 데이터에서 고객별 입원일 조회
#보험회사의 고객들이 보험금을 청구하는 데이터에서 고객별 입원일 조회
cust_id <-c(1005, 1002, 1003, 1004, 1005, 1001, 1005, 1002, 1003, 1005)
hosp_day <-c(2, 3, 20,5, 13, 0, 8, 2, 3, 1)
length(cust_id)
length(hosp_day)
data <-data.frame(cust_id, hosp_day)
day_per_cust <-aggregate(data$hosp_day, by=list(data$cust_id), sum)
day_per_cust
names(day_per_cust) <-c('cust_id', 'hosp_day')
day_per_cust
order(day_per_cust$hosp_day)
day_per_cust[order(day_per_cust$hosp_day),]

#아래가 다 같은 결과
aggregate(data$hosp_day, by=list(data$cust_id), sum) #대상열 하나이상 가능
tapply(data$hosp_day, data$cust_id, sum) #대상열 하나만 가능
summaryBy(hosp_day~cust_id, data=data, FUN=c(sum, mean)) #FUN 2개 이상도 가능

# 10. 조건으로 색인 찾기: which()
subset(iris, iris$Species=='setosa') #조건으로 데이터 추출
which(iris$Species=='setosa') #조건으로 색인 추출
iris[which(iris$Species=='setosa'),] #조건 이용해서 데이터 출력

which.max(iris$Sepal.Length)
iris[which.max(iris$Sepal.Length),] #Sepal.Length가 가장 큰 row를 출력
iris[which.min(iris$Sepal.Length),] #Sepla.Length가 가장 작은 row 출력