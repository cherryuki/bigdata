# 2021-02-08 R_데이터 전처리_dplyr      ⓒcherryuki(ji) #
# # # 5장-2. dplyr 전처리 예제(연습문제) # # #

#혼자 해보기1
# (1) dplyr 패키지 이용
library(dplyr)
# (2) apply 계열 함수 이용: tapply, by, summaryBy, aggregate
library(doBy)
mpg <-as.data.frame(ggplot2::mpg)
#Q1.
mpg %>% 
  mutate(displ_range=ifelse(displ<=4, 'less4', ifelse(displ>=5, 'more5', '4-5'))) %>% 
  group_by(displ_range) %>% 
  summarise(avg_hwy=mean(hwy)) %>% 
  filter(displ_range %in% c('less4', 'more5') )
mpg$displ_range <- (ifelse(mpg$displ<=4, 'less4', ifelse(mpg$displ>=5, 'more5', 'NA')))
head(mpg)
tapply(mpg$hwy, mpg$displ_range, mean)[c(1,2)]
by(mpg$hwy, mpg$displ_range, mean)[c('less4','more5')]
summaryBy(hwy~displ_range, mpg)[c(1,2),]
aggregate(mpg$hwy, by=list(mpg$displ_range), mean)[c(1,2),]

#Q2.
mpg %>% 
  filter(manufacturer %in% c('audi', 'toyota')) %>% 
  group_by(manufacturer) %>% 
  summarise(avg_cty=mean(cty))
tapply(mpg$cty, mpg$manufacturer, mean)[c('audi','toyota')]
by(mpg$cty, mpg$manufacturer, mean)[c('audi','toyota')]
summaryBy(cty~manufacturer, mpg)[c(1,14),]
aggregate(mpg$cty, by=list(mpg$manufacturer), mean)[c(1,14),]

#Q3.
mpg %>% 
  filter(manufacturer %in% c('chevrolet', 'ford', 'honda')) %>% 
  group_by(manufacturer) %>% 
  summarise(avg_hwy=mean(hwy))
tapply(mpg$hwy, mpg$manufacturer, mean)[c('chevrolet', 'ford', 'honda')]
by(mpg$hwy, mpg$manufacturer, mean)[c('chevrolet', 'ford', 'honda')]
summaryBy(hwy~manufacturer, mpg)[c(2,4,5),]
aggregate(mpg$hwy, by=list(mpg$manufacturer), mean)[c(2,4,5),]

#혼자 해보기2
#Q1. 
mpg2 <- mpg %>% 
  select(class, cty)
names(mpg2)
mpg2 <- data.frame(mpg$class, mpg$cty)
head(mpg2)

#Q2.
table(mpg2$class)
mpg2 %>% 
  filter(class %in% c('suv', 'compact')) %>% 
  group_by(class) %>% 
  summarise(avg_cty=mean(cty))
table(mpg2$mpg.class)
tapply(mpg2$mpg.cty, mpg2$mpg.class, mean)[c('compact','suv')]
by(mpg2$mpg.cty, mpg2$mpg.class, mean)[c('compact','suv')]
summaryBy(mpg.cty~mpg.class, mpg2)[c(2,7),]
aggregate(mpg2$mpg.cty, by=list(mpg2$mpg.class), mean)[c(2,7),]

#Q3.
mpg %>% 
  filter(manufacturer=='audi') %>% 
  arrange(-hwy) %>% 
  head(5)
audi<-mpg[mpg$manufacturer=='audi',]
head(audi[order(-audi$hwy),],5)
head(orderBy(~-hwy, data=audi),5)

#혼자 해보기3
#Q1.
mpg_copy <- mpg %>% 
  mutate(total=cty+hwy)

mpg_copy <-data.frame(mpg)
mpg_copy$total <-mpg_copy$cty+mpg_copy$hwy
head(mpg_copy)

#Q2.
mpg_copy %>% 
  mutate(avg=total/2)
mpg_copy$avg <-mpg_copy$total/2
head(mpg_copy)

#Q3.
mpg_copy %>% 
  arrange(-(cty+hwy)/2) %>%  
  head(3)
head(orderBy(~-avg, data=mpg_copy),3)
head(mpg_copy[order(-mpg_copy$avg),],3)

#Q4.
mpg %>% 
  mutate(total=cty+hwy,
         avg=total/2) %>% 
  arrange(-avg) %>% 
  head(3)

##혼자 해보기4
#Q1. 
table(mpg$class)
mpg %>% 
  group_by(class) %>% 
  summarise(avg_cty=mean(cty))
tapply(mpg$cty, mpg$class, mean)
by(mpg$cty, mpg$class, mean)
summaryBy(cty~class, data=mpg)
aggregate(mpg$cty, by=list(mpg$class), mean)

#Q2.
mpg %>% 
  group_by(class) %>% 
  summarise(avg_cty=mean(cty)) %>% 
  arrange(-avg_cty)
sort(tapply(mpg$cty, mpg$class, mean), decreasing = T)
sort(by(mpg$cty, mpg$class, mean), decreasing = T)
result <-summaryBy(cty~class, mpg)
result[order(result$cty.mean, decreasing = T),]
orderBy(~-cty.mean, result)
result <-aggregate(mpg$cty, by=list(mpg$class), mean)
result[order(result$x, decreasing = T),]
orderBy(~-x, result)

#Q3.
mpg %>% 
  group_by(manufacturer) %>% 
  summarise(avg_hwy=mean(hwy)) %>% 
  arrange(desc(avg_hwy)) %>% 
  head(3)
head(sort(tapply(mpg$hwy, mpg$manufacturer, mean), decreasing = T),3)
head(sort(by(mpg$hwy, mpg$manufacturer, mean), decreasing = T),3)
head(orderBy(~-hwy.mean, data=summaryBy(hwy~manufacturer, data=mpg)),3)
head(orderBy(~-x, data=aggregate(mpg$hwy, by=list(mpg$manufacturer), mean)),3)

#Q4.
mpg %>% 
  filter(class=='compact') %>% 
  group_by(manufacturer) %>% 
  summarise(n_compact=n()) %>% 
  arrange(-n_compact)
class_compact <- mpg[mpg$class=='compact',]
sort(table(class_compact$manufacturer), decreasing = T)
compact <- subset(mpg, mpg$class=='compact')
sort(table(compact$manufacturer), decreasing = T)

# 혼자 해보기5
mpg <-as.data.frame(ggplot2::mpg)
colnames(mpg)
mpg$fl
table(mpg$fl)
head(mpg)
fuel <-data.frame(fl=c('c','d','e','p','r'),
                  kind=c('CNG', 'diesel', 'ethanol E85', 'premium', 'regular'),
                  price_fl=c(2.35,2.38,2.11,2.76,2.22))
#Q1.
mpg$price_fl <- left_join(mpg, fuel, by="fl")[,'price_fl']
#Q2.
mpg[1:5,c('model', 'fl', 'price_fl')]
mpg %>% 
  mutate(price_fl=(left_join(mpg, fuel, by="fl")$price_fl)) %>% 
  select('model', 'fl', 'price_fl') %>% 
  head(5)

# 혼자 해보기6
table(mpg$drv) #4(4륜구동), f(전륜구동), r(후륜구동)
mpg <- as.data.frame(ggplot2::mpg) # mpg 데이터 불러오기
mpg[c(10, 14, 58, 93), "drv"] <- "k" # drv 이상치 할당
mpg[c(29, 43, 129, 203), "cty"] <- c(3, 4, 39, 42) # cty 이상치 할당

#Q1.
table(mpg$drv) #이상치 k 확인
mpg$drv <-ifelse(mpg$drv %in% c('4', 'f', 'r'), mpg$drv, NA)
mpg$drv <-ifelse(mpg$drv!='4'&mpg$drv!='f'&mpg$drv!='r', NA, mpg$drv)

#Q2.
boxplot(mpg$cty) #정상 범위 벗어난 이상치 확인
result <-boxplot(mpg$cty)$stats
result
mpg$cty <-ifelse(mpg$cty<result[1]|mpg$cty>result[5], NA, mpg$cty)
mpg$cty <-ifelse(mpg$cty %in% c(result[1]:result[5]), mpg$cty, NA)
boxplot(mpg$cty)

#Q3.
mpg %>% 
  filter(drv %in% c('4', 'f', 'r')) %>% #NA도 나오게 하려면 filter 없애면 됨
  mutate(cty=ifelse(is.na(cty), median(cty), cty)) %>% 
  group_by(drv) %>% 
  summarise(avg_cty=mean(cty, na.rm=T))
mpg %>% 
  filter(drv %in% c('4', 'f', 'r')) %>% #NA도 나오게 하려면 filter 없애면 됨
  group_by(drv) %>% 
  summarise(avg_cty=mean(cty, na.rm=T))

#분석 도전
midwest <-as.data.frame(ggplot2::midwest)
#Q1. 
midwest$junior_ratio <-(midwest$poptotal-midwest$popadults)/midwest$poptotal*100
#Q2.
midwest %>% 
  mutate(junior_ratio=(poptotal-popadults)/poptotal*100) %>% 
  arrange(desc(junior_ratio)) %>% 
  select('county', 'junior_ratio') %>% 
  head(5)
#Q3.
midwest$junior_grade <-ifelse(midwest$junior_ratio>=40, 'large',
                              ifelse(midwest$junior_ratio<30, 'small', 'middle'))
table(midwest$junior_grade)
midwest %>% 
  mutate(junior_grade=ifelse(junior_ratio>=40, 'large', 
                             ifelse(junior_ratio<30, 'small', 'middle'))) %>% 
  group_by(junior_grade) %>% 
  select(county) %>% 
  summarise(n_county=n())
#Q4.
midwest$asian_ratio <-midwest$popasian/midwest$poptotal*100
midwest %>% 
  mutate(asian_ratio=popasian/poptotal*100) %>% 
  arrange(-asian_ratio) %>% 
  tail(10) %>% 
  select(c('state', 'county', 'asian_ratio'))
midwest %>% 
  mutate(asian_ratio=popasian/poptotal*100) %>% 
  arrange(asian_ratio) %>% 
  head(10) %>% 
  select(c('state', 'county', 'asian_ratio'))
