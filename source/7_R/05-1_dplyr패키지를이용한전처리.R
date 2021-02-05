# 2021-02-05 R_데이터 전처리_dplyr      ⓒcherryuki(ji) #
# # # 5-1. dplyr 패키지를 이용한 전처리 # # #
# 1. 외부파일 read/write
# 1.1 엑셀파일 읽어오기 readxl 패키지 이용
install.packages('readxl')
library(readxl) #require(readxl)
getwd()
exam <-read_excel("inData/exam.xlsx")
class(exam)
exam <-as.data.frame(exam)
head(exam)
nrow(exam)
exam[21,] <-data.frame(id=21, class=1, math=90, english=80, science=99)
tail(exam)
exam$tot <-exam$math+exam$english+exam$science #파생변수 추가
mean(exam$tot)
exam$grade <-ifelse(exam$tot>=mean(exam$tot), '상', '하') #파생변수
table(exam$grade)
apply(exam[,3:6], 2, mean)

#데이터 파일에 컬럼명이 없는 경우
data <-read_excel("inData/data_ex.xls", col_names=FALSE)
data
colnames(data) <-c('id', 'gender', 'age', 'area')
data

# 1.2 데이터 쓰기(파일(csv)로 쓰기 vs. 변수만 쓰기)
write.csv(exam, "outData/exam.csv", row.names = TRUE) #파일로 쓰기(행번호 포함)
save(exam, file='outData/exam.rda') #exam변수를 파일로 저장
rm(list=ls(all.names=TRUE)) #모든 변수 삭제
load('outData/exam.rda') #환경창에서도 확인 가능
exam

# 2. 데이터 파악하기
mpg <-as.data.frame(ggplot2::mpg)
#head() 앞부분 6열, tail() 뒷부분 6열
#View() 뷰 창에서 데이터 확인용(=edit())
#dim() 차원, str() 구조, summary() 요약
head(mpg)
tail(mpg)
edit(mpg)
View(mpg)
dim(mpg)
str(mpg)
summary(mpg) #최소값, 1사분위수, 중위수, 평균, 3사분위수, 최대값

# 변수명 바꾸기(cty->city, hwy->highway)
install.packages("dplyr")
library(dplyr)
mpg <-rename(mpg, city=cty)
mpg <-rename(mpg, highway=hwy)
colnames(mpg)
head(mpg)

# 파생변수 (계산식으로)
mpg$total <-(mpg$city+mpg$highway)/2
head(mpg)
# 파생변수 (조건식으로)
mean(mpg$total)
median(mpg$total)
mpg$test <-ifelse(mpg$total>mean(mpg$total), "pass", "fail")
table(mpg$test) #빈도표 출력
boxplot(mpg$total)
hist(mpg$total) #변수가 반드시 숫자여야 함(histogram)
?qplot
library(ggplot2)
qplot(mpg$test) #막대 그래프

# 플롯 비교
boxplot(mpg$total)  #(1) 박스 플롯
hist(mpg$total)     #(2) 히스토그램
install.packages("vioplot")
library(vioplot)
vioplot(mpg$total, col="blue") #(3)바이올린 플롯

par(mfrow=c(1,3)) #시각화 그래프를 1행 3열로 출력
boxplot(mpg$total)
hist(mpg$total)
vioplot(mpg$total, col='green')
par(mfrow=c(1,1)) #플롯 공간 원상복귀

#연습문제
#문제1. 데이터 파악하기
midwest <-as.data.frame(ggplot2::midwest)
head(midwest)
str(midwest)
summary(midwest)
#문제2. poptotal을 total로, popasian을 asian으로 변수명 수정
midwest <-rename(midwest, c(total=poptotal, asian=popasian))
colnames(midwest)
#문제3. total, asian 변수를 이용해 "전체 인구 대비 아시아 인구 백분율" 파생변수를 만들고, 히스토그램
midwest$ratio_asian <-(midwest$asian/midwest$total*100)
midwest[1:10, c('total', 'asian', 'ratio_asian')]
hist(midwest$ratio_asian)
boxplot(midwest$ratio_asian)
#문제4. 아시아 인구 백분율 전체 평균
mean(midwest$ratio_asian)
midwest$asian_group <-ifelse(midwest$ratio_asian>mean(midwest$ratio_asian), 'large', 'small')
head(midwest)
dim(midwest)
head(midwest[,c('total', 'asian', 'ratio_asian', 'asian_group')])
#문제5. large, small 지역 빈도표 확인
table(midwest$asian_group)
qplot(midwest$asian_group)
nrow(midwest)

# 3. 파악한 데이터를 dplyr 패키지를 이용하여 전처리 및 분석하기
#filter(), select(), arrange(), mutate(), summarise(), group_by(), left_join(), bind_rows()
#데이터 변질없이 분석 가능
# 3.1 조건에 맞는 데이터 추출하기: filter() '%>%'의 단축키: ctrl+shift+m
exam <-read.csv("inData/exam.csv", header=T)
exam
exam %>% #dplyr패키지는 %>% 기호를 이용해서 함수들을 나열하는 방식 코딩
  filter(class==1)
exam %>% 
  filter(class==1|class==2|class==3)
exam %>% 
  filter(class %in% c(1,2,3))
#class가 1이고 english가 80이상인 데이터 추출
exam1 <- exam %>% 
  filter(class==1 & english>=80)
#데이터 변질없이 추출 가능. 다시 사용할 예정이라면 변수 등에 저장 필요
exam1

# 3.2 필요한 변수 추출하기: select()
exam %>% 
  select(class, english, math) #추출하고자 하는 변수만 select
exam %>% 
  select(-math) #-변수만 제외하고 전부 출력
#class가 1과 2의 행 중에서 영어, 수학 데이터만 출력
exam %>% 
  filter(class %in% c(1,2)) %>% 
  select(english, math)
# class가 1, 2, 3행에서 영, 수 데이터만 앞 5개 추출
exam %>% 
  filter(class %in% c(1,2,3) ) %>% 
  select(english, math) %>% 
  head(5) #6개일 경우 숫자 없이 head까지만 써도 가능

# 3.3 정렬하기: arrange()
exam %>% arrange(math)        #오름차순 정렬
exam %>% arrange(desc(math))  #내림차순 정렬
exam %>% arrange(-math)       #내림차순 정렬
#class 오름차순, class가 같은 경우 math 내림차순 정렬
exam %>% arrange(class, -math) 
exam %>% arrange(class, desc(math))

# id가 1부터 10인 학생의 영어, 수학 성적을 영어성적 기준으로 오름차순 정렬하고 top6명만
exam %>% 
  filter(id %in% c(1:10)) %>% 
  select(english, math) %>% 
  arrange(english) %>% 
  head

## 파생변수 추가: mutate
exam %>% 
  mutate(total=math+english+science)
head(exam) #실제 exam에 추가된 것 X
exam %>% 
  mutate(total=math+english+science) %>% 
  filter(total>=200)
# 파생변수를 한 번에 2개 이상 추가해서 분석
exam %>% 
  mutate(total=math+english+science,
         avg=round(total/3)) %>% 
  head
#추가한 파생변수는 dplyr 코드에 바로 활용 가능
exam %>% 
  mutate(total=math+english+science,
         avg=round(total/3)) %>% 
  select(-id) %>% 
  arrange(desc(total)) %>% 
  head(3)

# 3.5 요약하기: summarise()
exam %>% 
  summarise(mean_math=mean(math))
exam %>% 
  summarise(mean_math=mean(math),
            mean_eng=mean(english))
exam %>% 
  summarise(mean_math=mean(math),
            mean_eng=mean(english),
            sd_math=sd(math),
            sd_eng=sd(english))

# 3.5 집단별로 요약하기: group_by() + summarise()
exam %>% 
  group_by(class) %>% 
  summarise(mean_math=mean(math),
            n=n(),
            max_eng=max(english)) %>% 
  arrange(mean_math)

# 클래스별 수학, 영어, 과학의 평균
exam %>% 
  group_by(class) %>% 
  summarise(mean_math=mean(math),
            mean_eng=mean(english),
            mean_sci=mean(science))
library(doBy)
summaryBy(math+english+science~class, exam)

#mpg 회사별로 "suv 자동차의 도시 및 고속도로 통합 연비 평균을 구해 내림차순으로 정렬하고 1~5위까지 출력)
mpg <-as.data.frame(ggplot2::mpg)
nrow(mpg)
table(mpg$class)
head(mpg)
mpg %>% 
  filter(class=='suv') %>% 
  group_by(manufacturer) %>% 
  mutate(avg=(cty+hwy)/2) %>% 
  summarise(avg_manuf=mean(avg)) %>% 
  arrange(-avg_manuf) %>% 
  head(5)
