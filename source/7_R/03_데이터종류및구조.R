# 2021-02-02 R_데이터 종류 및 구조      ⓒcherryuki(ji) #
# # # 3장. R 데이터 종류 및 구조 # # #
  # 팩터(Factor), 벡터, 리스트, 행렬, 배열, 데이터프레임, 날짜, 특별한값(결측치, ..)

# 2. 기본 데이터 타입: character, numeric, logical
a <- "Hello\nR"
a <- "Hello
R"
class(a) #character
cat(a) #print와 사용법 동일, \n 수행
b <- 10.1
class(b) #numeric
strB <-as.character(b) #as.*(); *타입으로 형변환
class(strB) #character
c <-TRUE
class(c) #logical
is.logical(c) #methods(is) -> is.*(): 타입(형)이나 값을 물어보는 함수

str(a) #str(): R의 내부 구조를 간결하게 표시
str(b)
str(c)

# 3. 특별한 값(NULL, NA:결측치, NaN, Inf)
reuslt <-0
add <-function(a,b) {
  result <<-a*5+b #전역변수 result에 할당
  return(result)
}
(temp <-add(1,2)) #일반변수 temp에 할당
(temp <-add(a=1, b=2))
(temp <-add(b=10, a=5)) #35
add <-function(a,b) {
  result <<-a*5+b #전역변수 result에 할당
  return()
}
(temp <-add(a=1, b=3)) #NULL; Empty value
is.null(temp)

d <- c(2,4,NA,6,NaN,10/0) #vector(동일 자료형 집합)
d
#NA(결측치) 관련 함수
#is.na(d) #d가 결측치인지 아닌지 #NA가 있으면 TRUE <->complete.case(d)
#complete.cases(d) 
#na.omit(d) #결측치 제외
#na.pass(d) #NA여부 상관 없이 처리

?is.na
complete.cases(d)#TRUE  TRUE FALSE  TRUE FALSE  TRUE
na.omit(d)
na.pass(d)
mean(d) #평균값 계산시 NA가 있을 경우 NA
?mean
d<-c(2,3,4,5,NA,12)
mean(d, na.rm=TRUE)
boxplot(d)

# 4. 팩터(Factor): 범주형 데이터, 명명식(Norminal), 순서식(Ordinal)
gender1 <-c('남', '남', '여')
gender1[3]
class(gender1) #charactere
gender1[4] <-'넘'
gender1

gender <-factor(c('남','남','여'), levels=c('남','여'))
class(gender) #factor
gender[3]
gender  
str(gender)
str(gender1)
gender[4] <-'넘' #NA로 들어감
gender
level <-factor(c('좋음', '보통', '보통'), levels=c('싫음', '보통', '좋음'), ordered=T) #T=TRUE
level
level <-ordered(c('좋음','보통','보통'), levels=c('싫음', '보통', '좋음'))
level
level[4] <-'몰라' #<Na>
level
nlevels(level) #level변수의 범주 개수
nlevles(gender)
levels(level) #level변수의 범주들

gender1 <-c('남', '남', '여')
class(gender1)
gender1<-as.factor(gender1) #형변환 관련: 5장 전처리에서 다룰 예정
gender1

# 5. 구조형 변수와 복합형 변수; 변수 하나에 여러값을 가짐
 # (1) 구조형 변수: 동일 자료형 ex)벡터, 행렬(회귀식 용이), 배열
 # (2) 복합형 변수: 서로 다른 자료형 가질 수 있음 ex)리스트, 데이터프레임(csv), 데이터테이블

# 6. 벡터: 동일 자료형의 집합
data <-c(11,22,33,'TEST') #숫자, 문자 -> 문자
data <-c(11, 22, 33, TRUE) #숫자, logical ->숫자(T:1, F:0)
data <-c(TRUE, 'TEST') #logical, 문자 -> 문자
data <-c(1,2,3) #1 index부터 시작
data[4] <-40
data

# 행과 열 조회
NROW(data) #항목 개수
length(data) #항목 개수

data <-c(1:4)
names(data) <-c('A열', 'B열', 'C열', 'D열')
#특정한 값 조회
data[1] #첫번째 값 반환
data['A열'] #A열 값 반환
data[c(1,2)] #첫번째, 두번째 값 반환
data[c(1:2)] #첫번째부터 두번째까지 값 반환
data[c('A열', 'B열')] #A열 B열 값 반환
data[-2] #음수:2번째 제외
data[data>2] #2보다 큰 값만 반환
data[c(TRUE,FALSE,F,T)] #TRUE(T)인 열만 값 반환 = 1,4번째 값 반환

2%in%data #data에 2가 포함되어 있는지 여부 T/F

# Q1. 시험점수 변수를 만들어 출력하고 전체 평균을 구한 후 출력
# 80, 60, 70, 50, 90, 미응시
score <- c(80,60,70,50,90,NA)
print("시험점수는 아래와 같다\n")
print(paste('시험 점수는', score))
cat('시험 점수는 아래와 같다\n', score)
(avg <- mean(na.omit(score)))
(avg <-mean(score, na.rm=TRUE))

# Q2. 
# Lee, Kim, Yun, Park, Lim, Yi
names(score) <-c('Lee', 'Kim', 'Yun', 'Park', 'Lim', 'Yi')
names(score)
score
score[score>80] #NA도 출력됨
class(score) #class함수 이용시 벡터 요소 하나하나의 타입
is.vector(score)

# 6.1 character()
charArr <- character() #charArr legnth가 0인 벡터
is.vector(charArr)
length(charArr)
charArr <- character(5) #length가 5인 벡터
charArr
charArr[1] <-'안녕'; charArr[2]='R'; charArr[3]='복습중'
charArr[7] <-'테스트'
charArr

# 6.2 numeric()
intArr <-numeric()
class(intArr)
is.vector(intArr)
intArr[1]<-1
intArr[3]<-3
intArr

# 6.3 logical()
logiArr <-logical(2) #length가 2인 logical 벡터
logiArr[1] <-TRUE
logiArr[2] <-FALSE
logiArr[3] <-T
logiArr #TRUE FALSE  TRUE

# 6.4 seq()
?seq
a <-seq(from=1, to=10)
a <-seq(from=1, to=10, by=2)
a <-1:10
is.vector(a)
seq(10, -10, -2)
seq(0, 1, 0.1)
seq(1, 9, by=pi)

# 6.5 rep(); 반복객체를 만드는 함수
rep(1:4, 2) #1 2 3 4 1 2 3 4
rep(1:4, times=2) #1 2 3 4 1 2 3 4
rep(1:4, each=2) #1 1 2 2 3 3 4 4 
rep(1:4, c(1,2,3,4)) # 1 2 2 3 3 3 4 4 4 4 
rep(1:4, each=2, len=6) # 1 1 2 2 3 3 
rep(1:4, times=2, len=6) # 1 2 3 4 1 2 

# 6.6 벡터의 연산(+, -, *, /, 결합, 교집합, 합집합, 차집합, 비교연산)
a <-c(1,2,3)
b <-c(10,20,30)
a+b
a-b
a^b
b^a
a*b
a%%b #나머지 연산자
c(a,b) #벡터의 결합

a <-c(1,2,3)
b <-c('Hello', 'R')
c <-c(TRUE, FALSE)
(z<-c(a,b,c)) #문자로 결합됨
a <-append(a, c(4,5,6))
a <-append(a,7)
a[8]<-8
a

#벡터의 집합 연사: 합집합, 교집합, 차집합, 비교
a <-c(1,2,3,4,5,6)
b <-c(2,4,6,8,10,12)
union(a,b) #합집합
intersect(a,b) #교집합
setdiff(a,b) #차집합
setequal(a,b) #비교: FALSE
setequal(a,c(intersect(a,b), setdiff(a,b))) #TRUE

# 7. 리스트
student <-list(name='공유', age=43)
student
studentVector <-unlist(student)
studentVector
s <-c('공유', 43)
names(s) <-c('name', 'age')
s
student <-as.list(s) #as.list(); list형으로 형변환
student['name']
student$name
student[1] #$name [1] "공유"
student[[1]] #[1] "공유"
student$age <-NULL #student의 age제거
student
#항목 개수
NROW(student)
length(student)

# 8. 행렬
colMatrix <-matrix(1:15, nrow=5, ncol=3)
colMatrix
?matrix
colMatrix <-matrix(1:15, nrow=5, byrow=FALSE)
colMatrix
rowMatrix <-matrix(1:15, nrow=5, ncol=3, byrow=T,
                  dimnames=list(c('R1','R2','R3','R4','R5'),
                                c('C1','C2','C3')))
rowMatrix
dim(rowMatrix) #행과 열의 수
nrow(rowMatrix) #행 수
NROW(rowMatrix)
ncol(rowMatrix) #열 수
NCOL(rowMatrix)
dim(rowMatrix) <-c(5,3)
dim(rowMatrix)
rowMatrix
dimnames(rowMatrix)
rownames(rowMatrix)
colnames(rowMatrix)
#행이름과 열이름 수정
dimnames(rowMatrix) <-list(c('1월', '2월', '3월', '4월', '5월'), c('kim', 'lee', 'park'))
dimnames(rowMatrix)
rowMatrix

#행렬의 곱을 이용하여 선형회귀식 도출
x <-c(2,4)
y <-c(40,60)
X <-matrix(c(x, rep(1,NROW(x))), nrow=2, ncol=2, byrow=FALSE)
Y=matrix(y, ncol=1)
# X %*% ab = Y #행렬의 곱: %*%
# slove(X): X의 역행렬  # solve(X) %*% X %*% ab = solve(X) %*% Y
ab <- solve(X) %*% Y
ab
ab[1] #x의 기울기
ab[2] #y 절편
plot(x,y)
lines(x, x*ab[1]+ab[2])
lines(x,y)

x <- c(32, 64, 96, 118, 126, 144, 152.5, 158) #독립변수
y <- c(18, 24, 61.5, 49, 52, 105, 130.3, 125)
# plot(x,y, col-2, pch=19, ylim=c(0,150))

X <-matrix(c(x, rep(1, NROW(x))), ncol=2)
X
Y <-matrix(y, ncol=1)
Y
# X %*% ab = Y
# 전치행렬 곱해서 정방행렬
t(X)
t(X)%*%X #2*8%*%8*2 => 2*2 정방행렬
#solve(t(X) %*% X) %*% t(X) %*% X %*% ab =solve(t(X) %*% X) %*% t(X) %*% Y
ab = solve(t(X)%*%X)%*%t(X)%*%Y
ab
plot(x,y)
lines(x, x*ab[1]+ab[2])

#다변량에서 회귀분석 도출
x1 <-c(60, 65, 55) #몸무게
x2 <-c(5.5, 5.0, 6.0) #키
x3 <-c(1, 0, 1) #흡연유무
y <-c(66, 74, 78) #수명
X <-matrix(c(x1, x2, x3), ncol=3)
X #3*3정방행렬
Y <-matrix(y, ncol=1)
Y #3*1
#X%*%ab=Y
ab = solve(X)%*%Y
ab
# 80kg, 6.5ft, 금연시 예상 수명은?
80*ab[1]+6.5*ab[2]+0*ab[3]

#행렬 연산(+,-,*,/, %%, ..., %*%)
a <-matrix(1:4, nrow=2, ncol=2)
a
b <-matrix(seq(10,40,10), nrow=2, ncol=2)
b
a+b
a-b
b-a
a*b
a^b
b^a
a%%b
b%%a

## 행렬연산 중 행렬 곱(%*%)
payMatrix <-matrix(c(12000, 26000, 18000), ncol=3)
payMatrix #1행3열
dimnames(payMatrix) <-list(c('시간당 수당'), c('보검', '공유', '지민'))
workerMatrix <-matrix(c(c(5,4,9), c(7,3,2)), ncol=2)
workerMatrix #3행2열
dimnames(workerMatrix) <-list(c('보검', '공유', '지민'), c('1월', '2월'))
cost <-payMatrix%*%workerMatrix #1*3%*%3*2 => 1*2
rownames(cost) <-c('인건비')
cost

#9. 배열
dataArray <-array(1:24, dim=c(3,4,2)) #3행4열2면 3차원 배열
dataArray
dim(dataArray) #차원의 크기 조회
nrow(dataArray) #행수
NROW(dataArray)
ncol(dataArray) #열수
NCOL(dataArray)
length(dataArray) #요소 개수: 3*4*2
dimnames(dataArray) <-list(c('1행', '2행', '3행'),
                           c('1열', '2열', '3열', '4열'),
                           c('X면', 'Y면'))
dataArray
dim(dataArray) <-c(3,8) #3*4*2=3*8
dataArray
dim(dataArray) <-c(8,3) #reshape
attr(dataArray, 'dim') <-c(3,8) #reshape

# 10. 데이터 프레임 ★ ★ ★ ★ ★
student_id <-c('20211', '20212', '20213', '20214')
student_name <-c('Kong', 'Jia', 'Jimin', 'Eric')
student_eng <-c(70, 100, 80, 95)
student_kor <-c(80, 90, 85, 70)
student_gender <-c('남', '여', '여', '남')
student_data <-data.frame(student_id, student_name, 
                          student_eng, student_kor, student_gender)
student_data
#(2) 데이터 프레임에 열추가 및 삭제
student_data$mat <-c(100, 100, 99, 89) #열 추가
student_data
class(student_data$student_gender)
student_data$student_id<-NULL #열 삭제

#(3) 열의 형변환
student_data$student_gender <-as.factor(student_data$student_gender)
class(student_data$student_gender)
str(student_data) #구조 조회
summary(student_data)

#(4) 열이름 변경
student_data
install.packages("reshape")
library(reshape)
require("reshape")
student <-rename(student_data, c("student_name"="name"))
student <-rename(student, c("student_eng"="eng", 
                            "student_kor"="kor", "student_gender"="gender"))
student

names(student_data) <-c("name", "eng", "kor", "gender", "mat")
student_data

#(5) 데이터 프레임 합치기
#행으로 합치기 rbind
(newStudent <-rbind(student_data, student))
#열로 합치기 cbind
student
id = data.frame(student_id)
id
student <-cbind(id, student)
student
names(student) <-c("id", "name", "eng", "kor", "gender", "mat")
student

#부분 데이터 조회
student <-rbind(student, student) #2회 실행 -> 16행
nrow(student)
student[1,1] #1행 1열
student[1,'id']
student[1,] #1행 데이터
student[,1] #1열 데이터
student[c(1:3)] #1행부터 3행 데이터
student[, c(2,3,4,6)] #2,3,4,6 열 데이터
student[c(-2,-4,-6),] #,2,4,6행 제외한 모든 데이터
student[,c(-1,-5)] #1,5열 제외한 모든 데이터
student[c(1:3), c(-1,-5)] #1~3행까지 1열, 5열 제외한 데이터

#국어점수가 90점 이상인 데이터
subset(student, subset=(student$kor>=90))
subset(student, subset=(student$mat>=99))
subset(student, select=c(1,4)) #1열과 4열 데이터
subset(student, select=c(-1,-4)) #1열과 4열 제외한 데이터
#수학점수가 99점 이상인 여학생만 출력
subset(student, subset=(student$mat>99&student$gender=='여'))
#처음 5행만
student[c(1:5),]
head(student, 5)
#처음 3행만
head(student, 3)
edit(student)

emp <-read.csv(file.choose())
emp
head(emp)
class(emp)
#Q1. 직원 이름만 출력
emp[,2]
emp[,'ename']
emp$ename
#Q2. 직원 이름, job, sal
emp[,c('ename', 'job', 'sal')]
subset(emp, select=c('ename', 'job', 'sal'))
subset(emp, select=c(2,3,6))
#Q3. 이름이 KING인 직원의 empno, job, hiredate, sal
subset(emp, subset=(emp$ename=='KING'), select=c('empno', 'job', 'hiredate', 'sal'))
#Q4. sal이 2000이상인 직원의 empno, ename, sal
subset(emp, subset=(emp$sal>=2000), select=c('empno', 'ename', 'sal'))
#Q5. sal이 2000부터 3000사이인 직원의 ename, sal
subset(emp, subset=(emp$sal>=2000 & emp$sal<=3000), select=c('ename','sal'))

# 11. 타입 판별 및 타입 변환
head(emp)
tail(emp)
class(emp) #emp의 타입
str(emp) #emp 및 emp데이터 타입(구조)
emp$detno <-as.factor(emp$deptno) #int를 factor로 형변환
str(emp)
class(iris)
edit(iris)
str(iris)
iris$Species <-as.character(iris$Species) #factor를 character로 형변환
str(iris)
iris$Species <-as.factor(iris$Species) #character를 factor로 형변환
levels(iris$Species)

# 타입판별
class(iris$Species)
is.factor(iris$Species)
str(iris$Species)

# 12. 문자열과 날짜
name <-"Eric"
length(name) #요소 개수:1
nchar(name) #문자 개수:4

names <-c("Eric", "Larray", "Curly")
length(names) #3
nchar(names) #4 6 5

#하위 문자열 추출하기: substr
?substr
substr('ABCDEF', 1, 4) #1~4까지 추출: ABCD
substr('ABCDEF', 4, 10) #1~10까지 출력(없는 번째 문자는 ""처리)
substr(names, 1, 2) #names 안에 각각의 문자 1~2까지 추출

#names안에 각각의 이름 맨마지막 자리 앞글자, 맨 마지막 글자 추출
substr(names, nchar(names)-1, nchar(names))

#문자열 연결하기: paste, paste0
paste(names, 'loves', 'stars')
paste(names, 'loves', 'stars', sep='_')
paste(names, 'loves', 'stars', sep='_', collapse=', and ')
paste0(names, 'loves', 'stars')

# Q. paste 함수를 이용해서 아래 결과와 같이 출력
name <-c ('Yun', 'Lim', 'Lee'); hobby <- c('swim', 'sleep', 'eat')
# 결과: Yun의 취미는 swim이고, Lim의 취미는 sleep이고, Lee의 취미는 eat
paste(name, '의 취미는 ', hobby, collapse='이고, ')
paste(name, hobby, sep='의 취미는 ', collapse='이고, ')

#문자열 분할(구분자로 분할)
path <-'home/hadoop/data/speech.csv'
strsplit(path, '/')
customerInfo <-'jin@gmail.com,010-9999-8888,seoul Korea'
strsplit(customerInfo, ',')
strsplit(customerInfo, ',010-9999-8888,')
customers <-c('yun@naver.com,010-9999-6666,seoul Korea', 
              'lee@gmail.com,02-716-1006,pusan Korea', 
              'jin@hanmail.net,010-9999-8888,seoul Korea')
strsplit(customers, ',[0-9]{2,3}-[0-9]{3,4}-[0-9]{4},')

#문자열 대체: sub(oldStr, newStr, string)
          # gsub(oldStr, newStr, string)
s <- 'Curly is the smart one. Curly is funny, too.'
sub('Curly', 'Eric', s) #첫번째 것만 바뀜
gsub('Curly', 'Eric', s) #모두 바뀜

#외적: outer; 문자열의 모든 쌍별 조합 만듦
a <-c('aa', 'bb', 'cc')
b <-c('11', '22', '33')
outer(a,b,FUN="paste")
outer(a,b,FUN="paste", sep=" ~ ")
?outer

#날짜
today=Sys.Date()
class(today)
#%Y: 년도 4자리(2021), %y: 년도 2자리(21)
#%m: 월 2자리(02), %d:일 2자리(03)
thatday = as.Date("2021-04-30", '%Y-%m-%d')
thatday
today<thatday #TRUE
if(today<thatday) {
  cat('today보다 thatday가 나중')
} else {
  cat('today가 thatday보다 먼저')
}

#Q R데이터 종류 및 구조의 이해 실습
#1. iris데이터를 사용하여 data.frame의 특성 살펴보기
#1)
?iris
rm(list=ls()) #내가 만든 변수 모두 삭제
dim(iris)
dimnames(iris)
rownames(iris)
colnames(iris)
nrow(iris)
ncol(iris)
length(iris)
str(iris)
#2)
summary(iris)
head(iris$Sepal.Length, 10)
iris[c(1:10),'Sepal.Length']
iris[c(1:10),'Sepal.Length', drop=FALSE]
#3)
vir<-subset(iris, subset=(iris$Species=='virginica'))
set<-subset(iris, subset=(iris$Species=='setosa'))
#4)
rbind(set, vir)

#2. setosa종의 꽃받침의 폭과 길이 부분 데이터셋을 추출
subset(iris, subset=(iris$Species=='setosa'), select=c('Sepal.Width', 'Sepal.Length'))
#3. 작업내용에 따른 급여가 차등지급(행렬문제)
payMatrix <- matrix(c(12000, 26000, 18000), ncol=3)
payMatrix 
dimnames(payMatrix) <-list(c('시급'), c('A작업', 'B작업', 'C작업'))
workerMatrix <-matrix(c(c(5,4,9), c(7,3,2)), ncol=2)
workerMatrix
dimnames(workerMatrix) <-list(c('A작업', 'B작업', 'C작업'), c('갑', '을'))
# cost <- payMatrix %*% workerMatrix 3*1 3*2
cost <- payMatrix %*% workerMatrix
rownames(cost) <-c('급여')
cost
