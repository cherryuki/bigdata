# 2021-02-03 R_R프로그래밍      ⓒcherryuki(ji) #
# # # 4장. R 프로그래밍; 제어문, function # # #

# 1. 제어문
# 1.1 조건문
# (1) if문
num <- 9
if(num%%2==0) {
  print(paste(num, "은 짝수"))
} else {
  cat(num, "은 홀수")
}

# (2) ifelse() 함수
# "num%%2==0" "짝수":"홀수"
ifelse(num%%2==0, "짝수", "홀수")
(nums <-c(10, 9, 17, 5, 20))
result <- ifelse(nums%%2==0, "짝수","홀수")
result
m <-matrix(c(nums, result),ncol=5, byrow=TRUE,
           dimnames=list(c('수', '홀짝'), c('1회', '2회', '3회', '4회', '5회')))
m

# (3) switch() 함수
switch(2, "red", "green", "blue")
x <- switch(4, "red", "green", "blue")
x #NULL (0넣어도 NULL)

#사용자로부터 color값을 입력받아 해당 color 출력
?readline
color <- as.integer(readline(prompt="원하는 색(red:1, green:2, blue:3)?"))
class(color) #as.numeric() or as.integer()
switch(color, "red", "green", "blue")

color <-readline(prompt = "원하는 색(red, green, blue)?")
colorValue <-switch(color, "red"=1, "green"=2, "blue"=3)
cat('선택한 색상: ', color, '의 색상 값은 ',colorValue)

#Q. 점수(50~100)를 입력받아 학점을 계산하는 프로그램 구현
# 100: perfect, 90점대: A, 80점대: B, 70점대: c, 60점대: D, 50점대: F
score <- as.numeric(readline(prompt="점수(50~100)를 입력하세요: "))
grade <-switch(as.integer(score/10)-4, "F", "D", "C", "B", "A", "Perfect")
grade

getGrade <-function() {
  score <- as.numeric(readline(prompt="점수(50~100)를 입력하세요: "))
  grade <-switch(as.integer(score/10)-4, "F", "D", "C", "B", "A", "Perfect")
  cat('점수는 ', score, '점, 학점은 ', grade)
}
getGrade()

# 1.2 반복문; for, while, repeat
# (1) for문
1:10
seq(1:10)
seq(10)

x<-c(2, 5, -8, 10, 3)
for(val in x) {
  cat(val, '\t')
}
count <-0
for(val in x) {
  if(val%%2==0) {
    count = count+1;
  }
}
count

#10회 반복
for(val in 1:10) {
  cat(val, "안녕 ")
}

#Q. factorial 계산 함수를 작성
#결과: 5!=120
factorial(5) #5*4*3*2*1 

fact <-function(n) {
  if(n<0) {
    print("양수를 입력해주세요")
  } else if(n==0) {
    cat("0 ! = 1")
  } else {
    result <-1
    for(val in n:1) {
      result=result*val
    }
    cat(n, "! =", result)
  }
}
fact(-2)
fact(0)
fact(3)
fact(5)

rm(list=ls()) #만든 변수 전부 삭제
#getwd() #현재 working 디렉토리
#setwd("C:/Bigdata/source/7_R")
#getwd()
source('fact.R', encoding='utf-8')
fact(3)

# (2) while
i<-1
while(i<6) {
  +print(i)
  i=i+1
}

# (3) repeat: 반복
i<-1
repeat{
  if(i>6) break
  print(i)
  i<-i+1
}

# (4) break, next(자바에서의 continue)
x <-1
while(x<10) {
  x <-x+1
  #if(x==5) break;
  if(x==3) next;
  cat(x,'\t')
}

# 2. 연산자
# 논리연산자 &, &&, |, ||
TRUE & TRUE
TRUE && TRUE
x <-c(TRUE, FALSE, T, T, F)
y <-c(T, T, F, T, F)
x&y #각 요소별 확인: TRUE FALSE FALSE  TRUE FALSE
x&&y #첫번째 요소만 확인: TRUE
x | y
x || y

# 중위 연산자
5+8
'+'(5, 8)
'%add%' <-function(x,y) {
  return(x+y)
}
'%add%'(5,2)
5%add%2
c <-c(10, 23, 30)
10 %in% c
strings <-c("Hello", "world", "R")
'R' %in% strings #TRUE
strings %in% 'R' #FALSE FALSE  TRUE

#%o% : 벡터의 외적(outer)
#%*% : 백터의 내적(or 행렬의 곱)
a <-c(2,3,4)
b <-c(10,20,30)
a %o% b
a <-c('1', '2', '3')
b <-c('a', 'b', 'c')
outer(a,b, FUN=paste)

matrix.a <- matrix(1:6, nrow=3) #3행2열
(matrix.b <-matrix(1:6, nrow=3, ncol=2)) #3행2열
#matrix.a %*% matrix.b #3*2 3*2 곱셈 불가능
#solve(matrix.a) #정방행렬X 불가능

# 3. 함수
pow <-function(x,y) {
  return(x^y)
}
pow(2,5)

# 가변인자 함수: total(), total(1), total(2,3,4)
total <-function(...) {
  args <-list(...)
  sum <-0
  for(i in args) {
    sum <-sum+i
  }
  return(sum)
}
total()
total(1)
total(2, 3, 5)

# 재귀호출: 자기자신을 호출하는 함수->재귀함수(Recursive Function)
fact <-function(num) {
  if(num<0) {
    return() 
  } else if(num==0||num==1) {
    return(1)
  } else {
    return(num*fact(num-1))
  }
}
#fact(3) -> 6(3!)을 리턴
#fact(3) = 3*fact(2) = 3*2*fact(1) = 3*2*1
#fact(num) = num*fact(num-1) (단, num>1)
fact(-1)
fact(0)
fact(1)
fact(3)

# 4. R환경
environment() #<environment: R_GlobalEnv>
ls() 
f <-function(f_x) {
  g <-function(g_x) {
    print('g함수 안')
    print(environment())
    print(paste('g함수 영역에서의 변수들', ls()))
  }
  g(5)
  print('f함수 안')
  print(environment())
  cat('f함수 영역에서의 변수들', ls())
}
f(1)
f()

#Q. 소수 체크
#if문과 for문을 이용하여 매개변수가 소수인지 아닌지 
#TRUE, FALSE를 return하는 함수를 작성하고 호출

is.primeNum <-function(num) {
  if(num<1) {
    return(FALSE)
  } else {
    result <-0
    count <-0
    for(val in num:1) {
      result = num%%val
      if(result==0) {
        count=count+1
      }
    }
    if(count==2) {
      return(TRUE)
    } else {
      return(FALSE)
    }
  }
}
is.primeNum(-3)
is.primeNum(0)
is.primeNum(1)
is.primeNum(2)
is.primeNum(5)
is.primeNum(23)
