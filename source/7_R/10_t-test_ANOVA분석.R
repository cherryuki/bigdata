# 2021-02-16 R_t-text 분석 vs. ANOVA분석      ⓒcherryuki(ji) #
# # # 10장. t-test 분석 vs. ANOVA 분석 # # #
# 두 그룹간 평균의 차이가 통계적으로 유의한지 검증: t-test분석
# 세 그룹 이상 집단의 평균 차이가 통계적으로 유의한지 검증: ANOVA분석(분산분석)

# 1. 두 그룹간 평균의 차이가 유의한지 분석
head(ToothGrowth)
ToothGrowth
table(ToothGrowth$supp)
# (1) 도표로 차이의 유의성 표현(tapply, by, summaryBy, aggregate, ... 평균, 분산)
# (2) 그래프로 시각화된 유의성 표현(바이올린 도표, 산점도, 상자 도표)
# (3) 통계적으로 유의한지 검증

###비타민의 종류가 기니피그 치아성장에 영향을 미치는지?
ToothGrowth <-rbind(ToothGrowth, ToothGrowth) #3번 -> 480행
nrow(ToothGrowth) #임의로 데이터 수 증가
table(is.na(ToothGrowth)) #결측치 여부 확인
colSums(is.na(ToothGrowth))

# (1) 차트
library(doBy)
summaryBy(len~supp, ToothGrowth, FUN=c(mean, sd))
library(dplyr)
ToothGrowth %>% 
  filter(!is.na(supp)&!is.na(len)) %>%  #결측치 처리
  group_by(supp) %>% 
  summarise(len.mean=mean(len),
            len.sd=sd(len))

# (2) 시각화
ToothGrowth %>% 
  group_by(supp) %>% 
  summarise(len.mean=mean(len)) %>% 
  ggplot(aes(x=supp, y=len.mean)) +
  geom_col(aes(fill=supp), width=0.7)

ggplot(data=ToothGrowth, aes(x=supp, y=len)) +
  geom_violin() +
  geom_point(position = "jitter", alpha=0.7, col="yellow") +
  geom_boxplot(aes(fill=supp), notch=T, width=0.3)

# (3) 통계적 분석
#일원표본 t-test
table(ToothGrowth$supp, useNA="ifany") #useNA="ifany";결측치 빈도까지 출력
table(ToothGrowth$supp, exclude=NULL) #exclude=NULL; 결측치 빈도까지 출력
a <- ToothGrowth[ToothGrowth$supp=='OJ', 'len']
b <- ToothGrowth[ToothGrowth$supp=='VC', 'len']
t.test(a-b)
t.test(a, b)
#p-value가 0.05보다 작은 경우: 귀무가설(; 두 그룹의 평균이 같다)을 기각함
#p-value가 0.05보다 큰 경우: 귀무가설을 기각하지 못함

#이원표본 t.test(등분산성 테스트 ->t.test 분석)
var.test(len~supp, data=ToothGrowth)
  #p-value가 0.05보다 작은 경우 귀무가설을 기각함 - 등분산성이 성립되지 않음
  #p-value가 0.05보다 큰 경우 귀무가설을 기각하지 못함 - 등분산성이 성립됨
#등분산성? 분산이 같음

t.test(len~supp, data=ToothGrowth, var.equal=F)
  #var.equal=F; 두 그룹의 등분산성이 성립되지 않는 경우
  #var.equal=T; 두 그룹의 등분산성이 성립되는 경우
# p-value가 0.05보다 작은 경우: 귀무가설을 기각
# p-value가 0.05보다 큰 경우: 귀무가설을 기각할 수 없음

rm(list=ls())
### 예제: datasets:sleep : extra(수면량), group(수면제 종류)
# 수면제 group에 따라 수면량의 변화가 있는지 분석하시오
sleep <-rbind(sleep, sleep) #4번 실행: 320행
nrow(sleep)
head(sleep)
str(sleep)
table(sleep$group, useNA="ifany")

# (1) 도표로 평균의 차이 나타내기
summaryBy(extra~group, data=sleep, FUN=c(mean, sd))
sleep %>% 
  group_by(group) %>% 
  summarise(extra.mean=mean(extra),
            extra.sd=sd(extra))

# (2) 평균, 표본의 차이 시각화 하기
sleep %>% 
  group_by(group) %>% 
  summarise(extra.mean=mean(extra)) %>% 
  ggplot(aes(x=group, y=extra.mean)) +
  geom_col(aes(fill=group))

ggplot(data=sleep, aes(x=group, y=extra)) +
  geom_violin(aes(fill=group)) +
  geom_point(position="jitter", alpha=0.5, col="green") +
  geom_boxplot(notch = T, width=0.5, alpha=0.7)

# (3) 통계적으로 유의미한 차이 있는지 분석하기
table(sleep$group, useNA="ifany")
sleep[sleep$group==1, 'extra']
sleep[sleep$group==2, 'extra']
t.test(sleep[sleep$group==1, 'extra']-sleep[sleep$group==2, 'extra'])
#p-value(2.2e-16)가 0.05보다 작다 -> 귀무가설을 기각함
t.test(sleep[sleep$group==1, 'extra'], sleep[sleep$group==2, 'extra'])
#p-value(8.009e-14)가 0.05보다 작다 -> 귀무가설을 기각함

var.test(extra~group, data=sleep)
# p-value가 0.05보다 큼: 귀무가설을 기각하지 못함 - 등분산성이 성립됨
t.test(extra~group, data=sleep, var.equal=T)
# p-value가 0.05보다 작음: 귀무가설(두 그룹의 평균이 같다)을 기각


# 2. 3개 이상의 집단간 평균의 차이를 비교할 때는 분산분석(ANOVA)
# (1) aov(): 독립변수가 범주형일 때 주로 사용
#iris데이터 셋에서 종에 따라 Sepal.Length의 평균이 다른지
#독립변수: Species (범주형), 종속변수: Sepal.Length (연속형)
ggplot(iris, aes(x=Species, y=Sepal.Length)) +
  geom_boxplot(aes(fill=Species), notch=T)
result <-aov(Sepal.Length~Species, data=iris) #Species: 범주형
summary(result)
#F값이 0.05보다 작으면 귀무가설을 기각
#F값이 0.05보다 크면 귀무가설을 기각할 수 없다

# (2) anova(): 독립변수가 연속형일 때 주로 사용
  #ggplot2::mpg 데이터셋에서 cyl에 따라 mpg의 평균이 다른지
  #독립변수: cyl (연속형), 종속변수: mpg (연속형)
str(mtcars$cyl) #num
table(mtcars$cyl, useNA="ifany") #cyl의 가지수와 결측치 확인

#cyl에 따른 그룹이 3개 이상, cyl변수 연속형 변수
fit <-lm(mpg~cyl, data=mtcars)
fit
anova(fit)
#F값이 0.05보다 작으면 귀무가설을 기각
#F값이 0.05보다 크면 귀무가설을 기각할 수 없다

### 예제: datasets::Orange ; 오렌지 나무의 종류, 연령, 둘레
#오렌지 나무의 연령에 따른 둘레의 평균이 상이한지 분석하시오.
table(Orange$age)
fit <-lm(circumference~age, data=Orange)
anova(fit)
#F값이 0.05보다 작으므로 연령에 따라 둘레의 평균 상이함

#aov 사용해도 동일한 결과
result <-aov(circumference~age, data=Orange)
summary(result)
