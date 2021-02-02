# 2021-02-03 R_데이터 종류 및 구조      ⓒcherryuki(ji) #
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

# 9. 배열