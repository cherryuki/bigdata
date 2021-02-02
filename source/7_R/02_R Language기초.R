# 2021-02-01 R_R Language 기초      ⓒcherryuki(ji) #
# # # 2장. R Language 기초 # # #

## 01. 도움말 기능
# 1.1 도움말: ?, help()
iris
edit(iris)
?iris #도움말 출력
help(iris) #도움말 출력

# 1.2 검색 기능
??iris
help.search('iris')

# 1.3 패키지 도움말
library(help='datasets')

# 1.4 함수 도움말
methods(as) #형변환 함수들
as.integer(1.25)
?as.integer
example(as.integer) #예제 출력

data <-c(10,20,30)
mean(data)
?mean
example(mean)

# 1.5 정보
edit(iris)
attributes(iris)

# 1.6 주석과 자동 완성
# 주석: #
# 자동완성: TAB
R.version

## 02. 패키지
# R내 기본 패키지 외 패키지 다운로드 가능
# R내 기본 패키지: c>Program Files R>R-4.0.3>library 폴더들
# 2.1 패키지 설치
# 설치: install.package("패키지명")
# 설치된 패키지를 메모리에 로드: library("패키지명")
# 패키지 내 데이터나 함수들 사용
# 패키지 언로드: detach("package:패키지명", unload=TRUE)
detach("package:datasets", unload=TRUE)
iris
install.packages("arules")
library("arules")
?apriori
detach("package:arules", unload=TRUE)

# 데이터의 경우 메모리에 패키지 로드없이 사용 가능
data(iris, package="datasets")
iris

# 변수들 전부 삭제
ls()
rm(list=ls())

## 03. 변수
# 변수: 특수문자('.', '_') 사용 가능
# 할당: <-, <<-
result <-0 #전역변수 result
class(result) #타입: numeric
add <-function(a,b) {
  #result <-a+b #지역변수
  result <<-a+b #전역변수에 할당
  return(result)
}
add(10,20)
result #전역변수

# 변수목록 조회
x <-10
y <-10
(z<-x+y)
ls() #변수들 출력(시스템 히든 변수는 제외)
?ls
ls(all.names=TRUE) #히든변수 포함(히든변수는 .으로 시작)
?.Random.seed

## 04. 출력
result
print(result)
(z <- z+10)
paste('Hello', 'World') #"Hello World"
paste('result 값은', result)
#print('result 값은'+result) #에러
paste('Hello', 'world', sep=', ') #"Hello, World"
1:3
paste(c(1,2,3), c('하나', '둘', '셋'), sep='은 ')
paste(c(1,2,3), c('하나', '둘', '셋'), sep='은 ', collapse=', ')

month.name
(nth <-paste(1:12, c('st', 'nd', 'rd', rep('th',9)), sep=''))
paste(month.name, nth)
paste(month.name, nth, sep='은 ', collapse='; ')

## 06. 확장자
# ~.R: R 스크립트 파일(R실행코드 저장)
# ~.RData: R작업공간
# ~.Rhistory: 콘솔창에 실행한 R명령어들의 history

# 문제1) kor에 '한국', '일본', '미국'
     #usa에 'Korea', 'Japan', 'America'
     #출력은 한국:Korea, 일본:Japan, 미국:America

(kor <- c('한국', '일본', '미국'))
(usa <-c('Korea', 'Japan', 'America'))
paste(kor, usa, sep=':', collapse=', ')
(str <- paste(kor, usa, sep=':', collapse=', '))
str
cat(str)

# 문제2) MASS::Cars93 (패키지::데이터) 데이터 출력
data(Cars93, package="MASS")
Cars93 #안되면: 패키지 로드 필요
library(MASS) #안되면: 패키지 설치하기
install.packages("MASS")
library(MASS)
Cars93
edit(Cars93)
head(Cars93) #1~6행까지만 