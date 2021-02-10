# 2021-02-09 R_데이터 처리 성능 향상      ⓒcherryuki(ji) #
# # # 7장. 데이터 처리 성능 향상 # # #
# ①plyr패키지(apply계열), ②데이터 구조변경(melt, cast), ③데이터 테이블 #

# 1. plyr(플라이어) 패키지: 데이터 분할, 함수 적용 등을 사용하는 함수 포함
 #apply(), lapply(), sapply() 보강할 수 있음
install.packages("plyr")
library(plyr)
#xyply(.data, .group, ...) ex:adply, ddply
apply(iris[,1:4], 2, mean)
apply(iris[,1:4], 2, function(col){mean(col)})
sapply(iris[,1:4], mean)
sapply(iris[,1:4], function(col){round(mean(col),2)})
x <-data.frame(v1=c(4,9,16),
               v2=c(16,81,196))
x
apply(x, 2, function(col){sum(sqrt(col))})
apply(x, 2, function(col){mean(sqrt(col))})
#adply == apply(iris[,1:4], 2, sum), sapply()... 유사
adply(.dat=iris[,1:4], .margins = 2, function(col){sum(col)})
##ddply == summaryBy(Sepal.Length+Sepal.Width~Speices, iris, FUN=mean) 유사
ddply(.data=iris, .(Species), function(group){
  data.frame(SL.mean=mean(group$Sepal.Length),
             SW.mean=mean(group$Sepal.Width))
})

#summarise: 뒤에 나오는 변수들만 출력
#transform: 기존 데이터와 뒤에 나오는 변수들 같이 출력
ddply(iris, .(Species), summarise, SLmean=mean(Sepal.Length), SWmean=mean(Sepal.Width))
ddply(iris, .(Species), transform, SLmean=mean(Sepal.Length), SWmean=mean(Sepal.Width))

dfx <-data.frame(group=c(rep('A',8), rep('B', 15), rep('C',6)),
                 gender=sample(c('M','F'), size=29, replace=TRUE), #replace=TRUE: 복원 임의 추출
                 age=round(runif(29, min=18, max=54))) #runif 난수 실수 발생 
round(runif(29, min=18, max=54))
dfx
ddply(dfx, .(group, gender), summarise, mean=round(mean(age),2), sd=round(sd(age),2))
library(doBy)
summaryBy(age~group+gender, dfx, FUN=c(mean, sd)) #소숫점 지정 불가능

# 2. 데이터 구조 변경(melt, cast 함수)
View(airquality)
install.packages("reshape2")
library(reshape2)
airquality.melt <-melt(airquality, id=c('Month', 'Day'), na.rm=T) #na.rm=T 결측치 제외
View(airquality.melt)
airquality[airquality$Month==5&airquality$Day==1,]
subset(airquality, Month==5&Day==1)
#melt를 통해 바뀐 구조
airquality.melt[airquality.melt$Month==5&airquality.melt$Day==1,]
subset(airquality, Month==5&Day==5) #결측치有 Ozone:NA, Solar.R:NA
subset(airquality.melt, Month==5&Day==5) #결측치 부분은 나오지 않음

#melt된 데이터를 원상 복구: dcast vs. acast
airquality.dc <-dcast(airquality.melt, Month+Day~variable)
head(airquality.dc) #Month, Day 가 1,2열로 출력
head(airquality)

airquality.ac <-acast(airquality.melt, Month+Day~variable)
head(airquality.ac) #Month_Day가 행 이름으로 출력
airquality.ac['5_1',]
airquality.ac['5_5',]

# 3. 데이터 테이블: 짧고 유연한 구문 사용 위해 데이터 프레임에서 상속 받음
flights_df <-read.csv('inData/flights14.csv')
head(flights_df)
class(flights_df)

install.packages('data.table') #fread():csv파일을 데이터 테이블로 받는 함수
library(data.table)
flights_dt <-fread('inData/flights14.csv')
View(flights_dt)
class(flights_dt) #data.table, data.frame


# 2021-02-10 R_데이터 처리 성능 향상      ⓒcherryuki(ji) #

#연습문제
#(1) data.frame 이용(flights_df)
#(2) data.table 이용(flights_dt); 보다 간편하고 속도도 빠름

#1. origin이 JFK이고 month가 5월인 모든 행을 resul에 얻는다
colnames(flights_df)
library(dplyr)
resul <- flights_df %>% 
  filter(origin=='JFK'  & month==5)
resul <-subset(flights_dt, subset=(origin=='JFK'&month==5))
head(result)

resul <-flights_dt[origin=='JFK'&month==5]
resul

#2. 처음 두 행을 resul에 얻는다
resul <- flights_df[c(1:2),]
resul <-flights_dt[1:2]

#3. origin으로 오름차순, dest로 내림차순으로 정렬하여 출력
flights_df %>% 
  arrange(origin, desc(dest)) 
flights_df[order(flights_df$origin, desc(flights_df$dest)),]
flights_dt[order(origin, -dest)]

#4. arr_delay열만 출력
flights_df %>% 
  select(arr_delay) 
flights_df$arr_delay #벡터형태로 출력
flights_df[,'arr_delay', drop=F] #데이터 프레임 형태로 출력
subset(flights_df, select=arr_delay) #데이터 프레임 형태로 출력

flights_dt[,arr_delay] #벡터 형태로 출력
subset(flights_dt,select=arr_delay) #데이터프레임형태로 출력

#5. year열부터 dep_time열까지 출력
flights_df %>% 
  select(c('year':'dep_time')) 
flights_df[, 1:4]
subset(flights_df, select=c('year', 'month', 'day', 'dep_time'))
flights_dt[, 1:4]
flights_dt[, year:dep_time]
subset(flights_dt, select=c(year:dep_time))

#6. year열과 dep_time열 출력
flights_df %>% 
  select(c('year', 'dep_time')) 
flights_df[, c('year', 'dep_time')]
flights_dt[, year, dep_time] #출력 순서는 다름
flights_dt[, .(year, dep_time)]
flights_dt[, list(year, dep_time)]
flights_dt[, c('year', 'dep_time')]

#7. arr_delay열과 dep_delay열을 출력하되 열이름을 delay_arr과 delay_dep로 변경
flights_df %>% 
  mutate(delay_arr=arr_delay,
         delay_dep=dep_delay) %>% 
  select(c('delay_arr', 'delay_dep'))
df <- data.frame(delay_arr=flights_df$arr_delay, delay_dep=flights_df$dep_delay)
head(df)

flights_dt[, .(delay_arr=arr_delay, delay_dep=dep_delay)]

#8. 지연시간(arr_delay, dep_delay모두 0미만인 비행이 몇 번인지 출력
flights_df %>% 
  filter(arr_delay<0 & dep_delay<0 ) %>% 
  summarise(n = n())
nrow(subset(flights_df, arr_delay<0&dep_delay<0))
nrow(flights_df[flights_df$arr_delay<0&flights_df$dep_delay<0,])

flights_dt[arr_delay<0&dep_delay<0, .(.N)] #.N:개수
flights_dt[arr_delay<0&dep_delay<0, .(cnt=.N)]
#8-1. 지연시간의 합이 0 미만인 비행이 몇 번인지 출력
nrow(flights_df[flights_df$arr_delay+flights_df$dep_delay<0,])
flights_dt[arr_delay+dep_delay<0, .(.N)]

#9. 6월에 출발 공항이 JFK인 모든 항공편의 도착지연 및 출발지연 시간의 평균을 계산
flights_df %>% 
  filter(month==6&origin=='JFK') %>% 
  summarise(avg_arrdelay=mean(arr_delay),
            avg_depdelay=mean(dep_delay))
apply(subset(flights_df, month==6&origin=='JFK', select=c('arr_delay', 'dep_delay')), 2, mean)

flights_dt[month==6&origin=='JFK', .(mean(arr_delay), mean(dep_delay))]

#10. 9번의 결과에 title에 mean_arr, mean_dep로 출력
flights_df %>% 
  filter(month==6&origin=='JFK') %>% 
  summarise(mean_arr=mean(arr_delay),
            mean_dep=mean(dep_delay))
df <-apply(subset(flights_df, origin=='JFK', select=c('arr_delay', 'dep_delay')), 2, mean)
names(df) <- c('mean_arr', 'mean_dep')
df
flights_dt[month==6&origin=='JFK', .(mean_arr=mean(arr_delay), mean_dep=mean(dep_delay))]

#11. JFK 공항의 6월 운항 횟수
flights_df %>% 
  filter(month==6) %>% 
  summarise(n=n())
nrow(subset(flights_df, month==6))

flights_dt[month==6, .(.N)]

#12. JFK 공항의 6월 운항 데이터 중 arr_delay열과 dep_delay열을 출력
flights_df %>% 
  filter(origin=='JFK'&month==6) %>% 
  select(c('arr_delay', 'dep_delay'))
subset(flights_df, origin=='JFK'&month==6, select=c('arr_delay', 'dep_delay'))

flights_dt[origin=='JFK'&month==6, .(arr_delay, dep_delay)]
flights_dt[origin=='JFK'&month==6, list(arr_delay, dep_delay)]

#13. JFK 공항의 6월 운항 데이터 중 arr_delay열과 dep_delay열을 제외한 모든 열 출력
flights_df %>% 
  filter(origin=='JFK'&month==6) %>% 
  select(-c('arr_delay', 'dep_delay')) 
subset(flights_df, origin=='JFK'&month==6)[,c(-5,-7)]
subset(flights_df, origin=='JFK'&month==6)[,-c(5,7)]

flights_dt[origin=='JFK'&month==6, -c('arr_delay', 'dep_delay')]

#14. 출발 공항(origin)별 비행 수 출력 (JFK 81483 LGA 84433 EWR 87400)
table(flights_df$origin)
flights_df %>% 
  group_by(origin) %>% 
  summarise(n=n())

flights_dt[, .(.N), .(origin)]
flights_dt[, .(.N), by=.(origin)]
flights_dt[, .(.N), keyby=.(origin)] #origin 오름차순(E->J->L순)

#15. 항공사코드(carrier)가 AA에 대해 출발공항별 비행횟수 계산
flights_df %>% 
  filter(carrier=='AA') %>% 
  group_by(origin) %>% 
  summarise(n=n())
table(subset(flights_df, carrier=='AA')[,c('origin')])
table(subset(flights_df, carrier=='AA', select=origin))

flights_dt[carrier=='AA', .(.N), .(origin)]

#16. origin, dest별로 비행횟수 출력
table(flights_df$origin)
table(flights_df$dest)
table(flights_df$origin, flights_df$dest)
table(flights_df$cancelled) #취소 건수: 0

flights_dt[, .(.N), .(origin, dest)]

#17. 항공사코드(carrier)가 AA에 대해 origin, dest별로 비행횟수 출력
table(subset(flights_df, carrier=='AA', select=c('origin', 'dest')))

flights_dt[carrier=='AA', .(.N), .(origin, dest)]

#18. 항공사 코드가 AA에 대해, origin, dest, 월별 평균arr_delay, 평균 dep_delay 출력
flights_df %>% 
  filter(carrier=='AA') %>% 
  group_by(origin, dest, month) %>% 
  summarise(mean(arr_delay), mean(dep_delay))
library(doBy)
summaryBy(arr_delay+dep_delay~origin+dest+month, subset(flights_df, carrier=='AA'), FUN=mean)

flights_dt[carrier=='AA', .(avg_arr=mean(arr_delay), avg_dep=mean(dep_delay)), .(origin, dest, month)]

#19. dep_delay>0가 참이거나 거짓, arr_delay>0가 참이거나 거짓인 각각의 비행횟수
flights_df %>% 
  mutate(dep_n=ifelse(dep_delay>0, TRUE, FALSE),
         arr_n=ifelse(arr_delay>0, TRUE, FALSE)) %>% 
  summarise(table(dep_n), table(arr_n)) #1행 false, 2행 true
df <- data.frame(dep_n=ifelse(flights_df$dep_delay>0, TRUE, FALSE),
                 arr_n=ifelse(flights_df$arr_delay>0, TRUE, FALSE))

table(flights_df$dep_delay>0, flights_df$arr_delay>0)
flights_dt[, .(.N), by=.(dep_delay>0, arr_delay>0)]

#20. Origin==“JFK”에 대해 월별 최대 출발 지연 시간 출력(month로 정렬)
flights_df %>% 
  filter(origin=='JFK') %>% 
  group_by(month) %>% 
  summarise(max(dep_delay)) %>% 
  arrange(month)
df <- subset(flights_df, origin=='JFK', select=c('month', 'dep_delay'))
tapply(df$dep_delay, df$month, max)

flights_dt[origin=='JFK', .(max_dep=max(dep_delay)), .(month)]
