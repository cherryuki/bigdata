# 2021-02-05 R_데이터 전처리_dplyr      ⓒcherryuki(ji) #
# # # 5장-2. dplyr 패키지를 이용한 전처리 # # #
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

#########################################################
# 2021-02-08 R_데이터 전처리_dplyr      ⓒcherryuki(ji) #
# 4. 데이터 합치기
# 열합치기: cbind, left_join
# 행합치기: rbind, bind_rows
# cf. merge

# 4.1 열 합치기(가로 합치기)
test1 <-data.frame(id=c(1:5), midterm=c(70,80,90,95,100))
test2 <-data.frame(id=c(1:5), final=c(90,80,70,60,100),
                   teacherid=c(1,1,2,2,3))
teacher <-data.frame(teacherid=c(1:3),
                     techaername=c('Kim','Lee','Park'))
cbind(test1, test2) #5열(id가 중복되어서 나옴)
merge(test1, test2) #4열(id 1번)
library(dplyr)
left_join(test1, test2, by="id") #by를 기준으로 열 조인
#cbind(test2, teacher) 행 수가 달라서 불가능
merge(test2, teacher) #teacherid가 1열로 출력됨
left_join(test2, teacher, by="teacherid") #test2+teacher(원하던 조인)

test1 <-data.frame(id=c(1:5), midterm=c(70,80,90,95,100))
test2 <-data.frame(id=c(1:5), final=c(90,80,70,60,100),
                   teacherid=c(1,1,2,2,4)) #데이터 조작
teacher <-data.frame(teacherid=c(1:3),
                     techaername=c('Kim','Lee','Park'))
merge(test2, teacher, by="teacherid") #teacherid 4번 사라짐
merge(test2, teacher, by="teacherid", all=T) #all=T: NA포함된 열도 출력할 경우 

# 4.2 행 합치기(세로 합치기)
group_a <-data.frame(id=c(1:5), test=c(60, 70, 80, 90, 95))
group_b <-data.frame(id=c(6:10), test=c(90, 80, 95, 80, 90))
#두 데이터 프레임의 변수가 같을 경우: rbind, bind_rows 모두 사용 가능(결과 동일)
rbind(group_a, group_b)
bind_rows(group_a, group_b)

group_a <-data.frame(id=c(1:5), test1=c(60,70,80,90,95))
group_b <-data.frame(id=c(6:10), test2=c(90,95,85,80,90))
#두 데이터 프레임의 일부 변수가 다를 경우: bind_rows, merge(,all=T)만 가능(NA 출력)
#rbind(group_a, group_b) 불가능
bind_rows(group_a, group_b) #없는 항목은 NA로 출력
merge(group_a, group_b, all=T) #all=T 표기시 없는 항목들 NA로 출력

# 5. 데이터 정제하기 - 결측치(NA), 이상치
boxplot(ggplot2::mpg$hwy) #이상치
# 5.1 결측치 정제하기
df <-data.frame(name=c('Kim', 'Lim', "Park", "Yun", "Han"),
                gender=c('M','F',NA,'M','F'),
                score=c(5,4,3,4,NA),
                income=c(5000,3000,4000,3500,4000))
df
is.na(df) #결측치:TRUE
dim(df)
table(is.na(df))
table(is.na(df$gender))
table(is.na(df$score))

na.omit(df) #결측치가 하나라도 있으면 그 행 모두 제거
#간편(장점)하지만, 분석에 필요한 같은 행의 정보까지 손실(단점)

df %>% 
  filter(!is.na(score)) %>% 
  summarise(avg_score=mean(score))
mean(df$score, na.rm=T) #결측치 제외하고 평균값 계산: na.rm=T
tapply(df$score, df$gender, mean, na.rm=T)
library(doBy)
summaryBy(score~gender, df, FUN=mean, na.rm=T)

x <-c(1,1,2,2,3,3,3,4,4,5,5,100)
mean(x) #11.08333
median(x) #3 중앙값으로 대체하는 것이 안전

exam <-read.csv('inData/exam.csv', header = T) #헤더 없을 경우: header=FALSE 입력
exam
table(is.na(exam))
colnames(exam)
exam[c(3,8,15), 'math'] <-NA #인위적으로 math에 결측치 삽입
exam[1:2, 'english'] <-NA #인위적으로 english에 결측치 삽입
table(is.na(exam))
tapply(exam[,3], exam$class, mean, na.rm=T)
apply(exam[3:5], 2, mean, na.rm=T)
exam %>% 
  summarise(math=mean(math, na.rm=T),
            english=mean(english, na.rm=T),
            science=mean(science, na.rm=T))

#결측치를 중앙값으로 대체
#중앙값: median(객체, na.rm=T), 평균: mean(객체, na.rm=T) 
#소수점 처리를 위해 round() 이용시: round(meand(객체, na.rm=T))
exam$math
exam$math <-ifelse(is.na(exam$math), median(exam$math, na.rm=T), exam$math)
exam$math <-ifelse(is.na(exam$math), round(mean(exam$math, na.rm=T)), exam$math)

exam$english
exam$english <-ifelse(is.na(exam$english), round(median(exam$english, na.rm=T)), exam$english)
round(median(exam$english))
head(exam$english)

exam[c(1,3,8), 'math'] <-NA
exam[1:2, 'english'] <-NA
exam[1, 'science'] <-NA
head(exam)
#결측치 대체 방법1
median <-round(apply(exam[3:5], 2, median, na.rm=T))
median['math']; median['english']; median['science']
exam <-within(exam, {#결측치 대체하기 위한 블록
  math <-ifelse(is.na(math), median['math'], math)
  english <-ifelse(is.na(english), median['english'], english)
  science <-ifelse(is.na(science), median['science'], science)
})
head(exam)
table(is.na(exam)) #exam 안에 결측치(TRUE) 개수 확인
colSums(is.na(exam)) #변수별로 결측치 확인

#결측치 대체 방법2(dplyr패키지 이용)
colSums(is.na(exam))
median['math']; median['english']; median['science']
exam <- exam %>% 
  mutate(
    math=ifelse(is.na(math), median['math'], math),
    english=ifelse(is.na(english), median['english'], english),
    science=ifelse(is.na(science), median['science'], science)
  )
head(exam)

# 5.2 이상치 정제
 #논리적 이상치(ex: 성별에 남, 여가 아닌 값)
 #극단적인 이상치(정상 범위 기준에서 벗어난 값)
 #이상치는 결측치로 대체(이상치->결측치 대체->결측치를 중앙값or평균으로 대체 순)

# (1) 논리적 이상치
outlier <-data.frame(gender=c(1,2,1,3,2),
                     score=c(90,95,100,99,101))
table(outlier$gender)
#gender 1은 남, 2는 여, 3은 이상치 처리
outlier$gender <-ifelse(outlier==3, NA, outlier$gender)
outlier
outlier$gender <-ifelse(outlier$gender!=1&outlier$gender!=2, NA, outlier$gender)

#score가 100초과하는 경우 이상치 처리
outlier$score <-ifelse(outlier$score>100, NA, outlier$score)
outlier

# (2) 정상범위 기준을 많이 벗어난 이상치: 상하위 0.3% or 평균±3*표준편차
mpg <-as.data.frame(ggplot2::mpg)
mpg$hwy
mean(mpg$hwy)
sd(mpg$hwy)
boxplot(mpg$hwy)
result <-boxplot(mpg$hwy)$stats #boxplot의 통계치
result #12, 18, 24, 27, 37
result[1]; result[5]
mpg$hwy <-ifelse(mpg$hwy>result[5]|mpg$hwy<result[1], NA, mpg$hwy)
table(is.na(mpg$hwy)) #이상치를 결측치로 대체(NA:3)

summary(mpg$hwy) #12(Min), 18, 24, 23.44 27, 44(Max) #결측치 대체 전
