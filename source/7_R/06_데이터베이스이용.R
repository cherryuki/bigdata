# 2021-02-09 R_데이터 베이스 이용      ⓒcherryuki(ji) #
# # # 6장. 데이터 베이스 이용 # # #
# SQL문으로 데이터 프레임과 DB 테이블 이용
rm(list=ls(all.names=T)) #변수 모두 삭제

# 6.1 SQL문을 이용한 데이터 프레임 처리
install.packages('sqldf')
#참고하는 패키지 많음 fastmap, bit, cachem, ... RSQLite, DBI 등 의존
library(sqldf)
sqldf("select * from iris")

# 중복행 제거하여 한번만 출력(iris종 출력): distinct
sqldf("select distinct Species from iris")
names(table(iris$Species))
library(dplyr)
iris %>% 
  group_by(Species) %>% 
  summarise()

# 행 제한 조건 설정(vriginica 종만 출력)
sqldf("select * from iris where species=='virginica'") #' '안에 기재
iris[iris$Species=='virginica',]
iris %>% 
  filter(Species=='virginica')

# virginica 종이면서 Sepal.Length가 7.5 초과하는 것만
sqldf('select * from iris where Species=="virginica" and "Sepal.Length">7.5')
sqldf('select * from iris where Species=="virginica" and `Sepal.Length`>7.5')
# 컬럼명에 . 있을경우 경우: ``(backtick)로 감싸는 것을 추천

# 종별 Sepal.Length 합을 출력
sqldf("select Species, sum(`Sepal.Length`) from iris group by Species")

tapply(iris$Sepal.Length, iris$Species, sum)
by(iris$Sepal.Length, iris$Species, sum)
library(doBy)
summaryBy(Sepal.Length~Species, iris, FUN=sum)
aggregate(iris$Sepal.Length, by=list(iris$Species), sum)

# 정렬(Sepal.Length 1~5등, 6~10등) #0부터 시작: limit
sqldf("select * from iris order by `Sepal.Length` limit 5") #0번째부터 5개
sqldf("select * from iris order by `sepal.length` desc limit 5, 5") #5번째부터 5개
#limit m, n :m번째부터 n개 추출(0번부터 시작), desc: 내림차순

#sql함수(mySQL함수) 사용: Petal.Length와 Petal.Width의 평균과 표준편차
sqldf("select avg(`Petal.Length`) as avg_PL, avg(`Petal.Width`) as `avg_PW`,
      stdev(`Petal.Length`) as 'sd_PL', stdev(`Petal.Width`) sd_PW from iris")
apply(iris[,c('Petal.Length', 'Petal.Width')], 2, mean)
apply(iris[,c(3:4)],2,sd)
apply(iris[,c(3:4)], 2, mean); apply(iris[,c(3:4)], 2, sd)

#종에 따른 Petal.Length, Petal.Width의 평균과 표준편차
sqldf("select Species, avg(`Petal.Length`) as avg_PL, avg(`Petal.Width`) as `avg_PW`,
      stdev(`Petal.Length`) as 'sd_PL', stdev(`Petal.Width`) sd_PW from iris
      group by Species")
summaryBy(Petal.Length+Petal.Width~Species, iris, FUN=c(mean, sd))

sqldf("select round(avg(`Petal.Length`),2) avg_PL from iris")
iris %>% 
  summarise(avg=round(mean(Petal.Length),2))

# 조인
getwd()
#setwd('C:/Bigdata/source/7_R') #작업 디렉토리 변경(절대 경로 입력)
getwd() #변경된 작업 디렉토리 확인
emp <-read.csv('inData/emp.csv', header=T)
colnames(emp)
head(emp)
dept <-read.csv("inData/dept.csv")#header 있을 경우 생략 가능, 없으면 반드시 header=F 입력 
dept
#사번, 이름, 직책, 급여, 부서번호, 부서이름
sqldf("select empno, ename, job, sal, e.deptno, dname 
        from emp e, dept d 
        where e.deptno=d.deptno")
#사번, 이름, 부서번호, 부서이름
sqldf("select empno, ename, e.deptno, dname
        from emp e join dept d on e.deptno=d.deptno") #join 테이블명 on 조인 조건

rm(list=ls())
# 2. 오라클 데이터 베이스 연결
# 0단계: 자바 설치 및 환경 설정(JAVA_HOME), 작업디렉토리(getwd())에 ojdbc6.JAR 복사
# 1단계: 패키지 설치 및 로드: RJDBC
install.packages('RJDBC')
library(RJDBC)
# 2단계: 드라이버 클래스 로드
drv <-JDBC("oracle.jdbc.OracleDriver", classPath="ojdbc6.jar")
drv
# 3단계: 데이터 베이스 연결
con <- dbConnect(drv, "jdbc:oracle:thin:@127.0.0.1:1521:xe", "scott", "tiger")
con
# 4단계: SQL전송+결과(데이터 프레임) 받기
#(1) SQL전송(select문)+결과 받기
emp <- dbGetQuery(con, "select * from emp")
emp
class(emp)
summary(emp)
tail(emp)
emp[1:2, "EMPNO"]
#(2) 테이블 전체 조회
dept <-dbReadTable(con, "dept")
dept
# 5단계: DB데이터 수정; SQL(update, insert, delete) 전송
dbSendUpdate(con, "INSERT INTO DEPT VALUES (60, 'MARKETING', 'TOKYO')")
dbSendUpdate(con, "UPDATE DEPT SET LOC='SEOUL KOREA' WHERE DEPTNO=50")
dbSendUpdate(con, 'DELETE DEPT WHERE DEPTNO>40')
# 6단계: DB연결 해제
dbDisconnect(con)
# 드라이버 언로드: DB연결 해제시 자동 언로드 됨
dbUnloadDriver(drv)
detach("package:RJDBC", unload=TRUE)

# 3. MySQL 데이터 베이스 연결
# 0단계: MySQL Workbench 실행-> 아래 입력 후 실행
# ALTER USER '아이디'@'localhost' IDENTIFIED WITH mysql_native_password BY '비밀번호';
# ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'mysql';
# 1단계: 패키지 설치 및 로드:RMySQL
install.packages("RMySQL")
library(RMySQL)
# 2단계: 드라이버 클래스 로드
drv <-dbDriver("MySQL")
drv
# 3단계: 데이터 베이스 연결
con <-dbConnect(drv, host="127.0.0.1", dbname="kimdb", user="root", password="mysql")
con
# 4단계: SQL전송+결과(데이터 프레임) 받기
rs <-dbSendQuery(con, "select * from personal")
personal <-fetch(rs, n=-1)
personal
class(personal)

# 6단계: db 연결 해제
dbDisconnect(con)
dbUnloadDriver(drv)
personal
rm(list=ls())
