# 2021-02-05 R_중간 점검(문제 풀이)      ⓒcherryuki(ji) #

#[문제1] 1부터 10사이의 벡터를 만들어서 v1 이라는 변수에 저장한다.
v1 <-c(1:10)
v2 <-v1*2
max_v <-max(v2)
min_v <-min(v2)
avg_v <-mean(v2)
sum_v <-sum(v2)
v3 <-v2[-5]
cat('v1\n',v1,'\nv2\n',v2,'\nv3\n',v3,
    '\nmax_v\n',max_v,'\nmin_v\n',min_v,'\navg_v\n',avg_v,'\nsum_v\n',sum_v)
v1; v2; v3; max_v; min_v; avg_v; sum_v;

#[문제2] 10 에서 38사이의 숫자 중에서 2씩 증가한 값으로 벡터를 생성하고
#3행 5열의 매트릭스를 만들어 m1 에 저장한다.(행 우선 저장)
#각 원소 값들에 +100 한 결과로 매트릭스 m2 를 만든다.
m1 <-matrix(seq(10,38, 2), nrow=3, byrow = T)
(m2 <-m1+100)

#[문제3] seq() 또는 rep() 함수를 이용하여 다음 결과가 나오도록 명령을 작성한다.
#(1) 1, 3, 5, 7, 9
seq(1, 9, 2)
#(2) 1, 1, 1, 1, 1
rep(1, 5)
#(3) 1, 2, 3, 1, 2, 3, 1, 2, 3
rep(c(1:3),3)
#(4) 1, 1, 2, 2, 3, 3, 4, 4
rep(c(1:4), each=2)

#[문제4] 1부터 10 까지 출력하는데 3씩 증가 되는 형태로(1 4 7 10)저장되는 벡터를 정의하여 
# v3 변수에 저장한다.(또한 각각 값마다 "A", "B", "C", D" 라는 이름을 부여한다.)
v3 <-seq(1,10,3)
names(v3) <-(c("A", "B", "C", "D"))
names(v3) <-LETTERS[1:4]
#LETTERS 알바펫 대문자, letters 알파벳 소문자

#[문제5] 1부터 100으로 구성되는 7개의 중복되지 않는 데이터를 추출하여 count 라는 백터를 만든다. 
count <- sample(1:100, 7)
week.korname <- c("일요일", "월요일", "화요일", "수요일", "목요일", "금요일", "토요일")
cat(paste(week.korname, count, sep=':'))
week.korname[which.max(count)]
week.korname[which.min(count)]
week.korname[count>50]

#[문제6]  다음과 같이 값이 구성되는 매트릭스를 정의하여 m1 에 저장한다.
n1 <-c(1:3)
n2 <-c(4:6)
n3 <-c(7:9)
m1 <-matrix(c(n1,n2,n3), nrow=3)

#[문제7] 다음과 같이 값이 구성되는 매트릭스를 정의하여 m2 에 저장한다.
#1~9 의 벡터를 이용하여 matrix를 생성하고 출력한다.
(m2 <- matrix(c(1:9), nrow=3, byrow=T))

#[문제8]  m2 를 가지고 다음과 같이 값이 구성되는 매트릭스를 정의하여 m3 에 저장하고 출력한다.
m3 <- matrix(m2, nrow=3, ncol=3, 
             dimnames=list(c('row1', 'row2', 'row3'), c('col1', 'col2', 'col3')))
m3
#[문제9] 다음과 같이 구성 되는 2행 3열 매트릭스 alpha를 생성한 후에
alpha <-matrix(letters[1:6], nrow=2)
(alpha2 <-rbind(alpha, letters[24:26]))
(alpha3 <-cbind(alpha, c('s','p')))

#[문제10] 다음과 같이 값이 구성되는 배열을 정의하여 a 라는 변수에 저장한다.
a <- array(c(1:24), dim=c(2,3,4))
a[2,3,4]
a[2,,]
a[,1,]
a[,,3]
(a+100)
a[,,4]*100
a[1,2:3,]
(a[2,,2] <-a[2,,2]+100)
(a[,,1] <-a[,,1]-2)
a <-a*10
rm(a)
#[문제11] 다음과 같이 값이 구성되는 데이터프레임을 정의하여 df1 에 저장한다.
df1 <-data.frame(x=(1:5), y=(seq(2,10,2)))
df1

#[문제12] 다음과 같이 값이 구성되는 데이터프레임을 정의하여 df2 에 저장한다.
df2 <- data.frame(col1=1:5, col2=letters[1:5], col3=6:10)
df2
#[문제13] c() 함수로 먼저 벡터를 생성한 다음 data.frame()사용해서 
#다음과 같이 구성되는 데이터 프레임 df3를 
#만들어 출력해 본다.(제품명이 팩터형이 되지 않게 한다.)
제품명 <-c('사과', '딸기', '수박')
가격 <-c(1800, 1500, 3000)
판매량 <-c(24, 38, 13)
df3 <-data.frame(제품명, 가격, 판매량)
str(df3)

#[문제14] 앞에서 만든 데이터 프레임을 이용해서 과일 가격 평균, 판매량 평균을 구하여 출력한다.
apply(df3[,2:3], 2, mean)

#[문제15] 다음 세 벡터를 이용하여 데이터프레임 df4를 생성하고, name 변수는 문자, gender 변수는 팩터, 
#math 변수는 숫자 데이터의 유형이라는 것을 확인하시오.
name <- c('Potter', 'Elsa', 'Gates', 'Wendy', 'Ben')
gender <- factor(c('M', 'F', 'M', 'F', 'M'))
math <- c(85, 76, 99, 88, 40)
df4 <- data.frame(name, gender, math)
str(df4)

df4$stat <-c(76, 73, 95, 82, 35)
df4$score <-df4$math+df4$stat
df4$grade <-ifelse(df4$score>=150, "A", ifelse(df4$score>=100, "B", ifelse(df4$score>=70, "C")))
df4
#[문제16] 다음과 같이 값이 구성되는 리스트를 정의하여 L1 에 저장한다.
L1 <-list(name='scott', sal=3000)

#[문제17] 다음과 같이 값이 구성되는 리스트를 정의하여 L2 에 저장한다.
L2 <-list('scott', c(100, 200, 300))

#[문제18] 다음 리스트에서 A를 "Alpha"로 대체한다.
L3 <-list(c(3,5,7), c('A', 'B', 'C'))
L3[[2]][1] <-'Alpha'
L3

#[문제19] 다음 리스트에서 첫 번째 원소(alpha)의 각 값에 10을 더하여 출력한다.
L4 <- list(alpha=0:4, beta=sqrt(1:5), gamma=log(1:5))
#sqrt(1): 루트1, log(1); log1 (base 지수e)
L4[1]$alpha+10

#[문제20] 다음 리스트는 math, writing, reading의 중간고사 및 기말고사 점수이다. 
#전체 평균을 계산하여 출력한다.
L5 <-list(math=list(95, 90), writing=list(90, 85), reading=list(85, 80))
mean(unlist(L5))

#[문제21] iris 데이터에서 다룰 기본 정보를 조회한다(기본정보조회)
#타입, 구조, 차원, 변수이름, 기본통계량(평균, 표준편차, 사분위수)
class(iris)
str(iris)
dim(iris)
colnames(iris)
summary(iris)

#[문제22] iris 데이터를 정렬한다
library(doBy)
orderBy(~-Petal.Length, iris)
iris[order(-iris$Petal.Length),]

#[문제 23] iris 데이터의 종별 데이터 개수 출력한다
table(iris$Species)

#[문제 24] 종별 Sepal.Length의 합을 출력한다.
tapply(iris$Sepal.Length, iris$Species, FUN=sum)

#[문제 25] Sepal.Length, Sepal.Width, Petal.Length, Petal.Width의 평균을 출력
#(Apply, lappy, sapply이용)
apply(iris[,1:4], 2, mean)
lapply(iris[,-5], mean)
sapply(iris[,1:4], mean)
#종별 Sepal.Length의 평균 출력
tapply(iris$Sepal.Length, iris$Species, mean)
summaryBy(Sepal.Length~Species, iris)

#[문제 26] 꽃받침의 길이(Sepal.Length)가 가장 긴 꽃의 종은 무엇인가요?
iris[which.max(iris$Sepal.Length),5]
iris[which.max(iris$Sepal.Length),'Species']
iris[which.max(iris$Sepal.Length),]$Species
