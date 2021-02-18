# 2021-02-17 R_ 사례연구(시각화 예제)      ⓒcherryuki(ji) #
# # # 11장. 빅데이터 분석결과 시각화 사례연구 # # #

# 1. ‘한국복지패널데이터’(SPSS, koweps_hpc10_2015_beta5.sav)를 로드 후 변수명 변경
rm(list=ls(all.names=TRUE)) #기존 변수 삭제
install.packages("foreign") 
library(foreign) #read.spss()함수 사용 위함
library(dplyr) #전처리
library(doBy) #전처리
library(ggplot2) #시각화
library(readxl) #엑셀 파일

getwd()
raw_welfare <-read.spss(file='inData/Koweps/Koweps_hpc10_2015_beta1.sav',
                        to.data.frame=T) #to.data.frame = T 설정 안하면 리스트 형태로 받아옴
                        #한글 깨질 경우: reencode='utf-8' 
nrow(raw_welfare)
View(raw_welfare)
welfare <- raw_welfare
dim(welfare)
welfare <-rename(welfare, gender=h10_g3, #성별
                 birth=h10_g4, #출생년도
                 marriage=h10_g10, #혼인 상태
                 religion=h10_g11, #종교
                 code_job=h10_eco9, #급여
                 income=p1002_8aq1, #직종코드
                 code_region=h10_reg7) #지역코드
welfare <- welfare %>% 
  select(gender, birth, marriage, religion, code_job, income, code_region)
colnames(welfare)
head(welfare)
dim(welfare)
View(welfare)

# 2. 상기 data.frame변수를 이용하여 성별에 따른 월급차이가 있는지 분석
table(welfare$gender, useNA="ifany")
table(is.na(welfare$gender))
welfare$gender <-factor(welfare$gender)
welfare$gender <-ifelse(welfare$gender==1, 'male', 'female')
welfare$gender <-factor(welfare$gender, levels=c('male', 'female'))
table(welfare$gender)

welfare %>% 
  group_by(gender) %>% 
  summarise(ratio=n()/nrow(welfare)*100) #성별 비율
welfare %>% 
  group_by(gender) %>% 
  summarise(ratio=n()/nrow(welfare)*100) %>% 
  ggplot(aes(x=gender, y=ratio)) +
  geom_col(aes(fill=gender)) +
  theme(legend.position = "none") #범례 없애기

gender.ratio <- welfare %>% 
  group_by(gender) %>% 
  summarise(ratio=n()/nrow(welfare)*100)
pie(gender.ratio$ratio, 
    labels=paste(gender.ratio$gender, round(gender.ratio$ratio, 1), '%'),
    clockwise=T)
ggplot(gender.ratio, aes(x="", y=ratio, fill=gender)) +
  geom_bar(stat="identity") +
  coord_polar("y")

boxplot(welfare$income)
summary(welfare$income)
table(is.na(welfare$income))
bp <-boxplot(welfare$income)$stat
table(welfare$income<=bp[1], useNA="ifany") #하위 이상치 벗어난 값
table(welfare$income>bp[5], exclude=NULL) #상위 이상치를 벗어난 값이 5%이상이므로 이상치 처리X
welfare$income <-ifelse(welfare$income<=bp[1], NA, welfare$income)

qplot(welfare$income, xlim=c(0,1000))
ggplot(data=welfare, aes(income)) +
  geom_histogram() +
  coord_cartesian(xlim=c(0,1000))
summaryBy(income~gender, data=welfare, FUN=c(mean, sd), na.rm=T)

#na.omit 함수 사용해서 아래 방법으로 처리하기도 함(결측치가 많은 경우)
temp <-welfare[, c('income', 'birth')]
temp <-na.omit(temp)
summary(temp)
summaryBy(income~birth, temp, FUN=c(mean, sd))

welfare %>% 
  filter(!is.na(income)) %>% 
  ggplot(aes(x=gender, y=income, col=gender)) +
  geom_point(position="jitter", col="yellow", alpha=0.3) +
  geom_violin() +
  geom_boxplot(notch=T, width=0.5, alpha=0.3, fill="forestgreen") +
  coord_cartesian(ylim=c(0, 1000)) +
  geom_rug()

var.test(income~gender, data=welfare)
# p-value가 0.05보다 작음 -> 등분산성 성립X
t.test(income~gender, data=welfare, var.equal=F)
# p-value가 0.05미만으로 성별에 따른 월급차이가 없다는 가설을 기각함

# 3. 나이와 월급의 관계를 분석하여 몇 살 때 월급을 가장 많이 받는지 시각화
boxplot(welfare$birth)
b <-boxplot(welfare$birth)$stat
table(welfare$birth<b[1]|welfare$birth>b[5]) #이상치 없음
boxplot(welfare$income)
table(is.na(welfare$birth))
table(is.na(welfare$income)) #결측치 많음
welfare$age <-2015-welfare$birth+1

ggplot(welfare, aes(age)) +
  geom_histogram()

welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean.income=mean(income)) %>% 
  ggplot(aes(x=age, y=mean.income)) +
  geom_bar(stat="identity")

welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean.income=mean(income)) %>% 
  ggplot(aes(x=age, y=mean.income)) +
  geom_line() +
  coord_cartesian(xlim=c(20, 60))

fit <-lm(income~age, data=welfare)
anova(fit)
#F값이 0.05미만으로 나이에 따른 월급 차이가 없다는 가설을 기각함

welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age) %>% 
  summarise(mean.income=mean(income)) %>% 
  arrange(-mean.income) %>% 
  head

# 4. 연령대에 따른 월급의 차이가 있는지, 있으면 어떤 연령대가 월급이 가장 많은지 분석
welfare$agegrade <- ifelse(welfare$age<=30, 'young', 
                           ifelse(welfare$age<=60, 'middle', 'old'))
welfare$agegrade <-factor(welfare$agegrade, levels=c('young', 'middle', 'old'))
table(welfare$agegrade)
ggplot(welfare, aes(x=agegrade)) +
  geom_bar()

welfare %>% 
  filter(!is.na(income)) %>% 
  ggplot(aes(x=agegrade, y=income)) +
  geom_boxplot(aes(fill=agegrade), notch=T) +
  coord_cartesian(ylim=c(0, 1000)) +
  scale_fill_manual(values=heat.colors(3))

result <-aov(income~agegrade, data=welfare)
summary(result)
#F값이 0.05미만으로 연령대에 따라 월급 차이가 없다는 가설을 기각함

# 5. 성별에 따른 월급의 차이는 연령대 별로 다른지 분석
table(is.na(welfare))
colSums(is.na(welfare)) #code_job, income에 결측치 있음
summaryBy(income~agegrade+gender, data=welfare, FUN=c(mean, sd), na.rm=T)
welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(agegrade, gender) %>% 
  summarise(income.mean=mean(income),
            income.sd=sd(income),
            income.n=n())
welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(agegrade, gender) %>% 
  summarise(income.mean=mean(income),
            income.sd=sd(income),
            income.n=n()) %>% 
  ggplot(aes(x=agegrade, y=income.mean, fill=gender)) +
  geom_bar(stat="identity", position="dodge")

#연령대 별로 나눠서 비교
library(gridExtra)
young <- ggplot(subset(welfare, agegrade=='young'), aes(x=gender, y=income)) +
  geom_point(position="jitter", col="tan3", alpha=0.3) +
  geom_violin() +
  geom_boxplot(aes(fill=gender), notch=T, width=0.6, alpha=0.5) +
  theme(legend.position="none")
middle <- ggplot(subset(welfare, agegrade=='middle'), aes(x=gender, y=income)) +
  geom_point(position="jitter", col="tan3", alpha=0.3) +
  geom_violin() +
  geom_boxplot(aes(fill=gender), notch=T, width=0.6, alpha=0.5) +
  theme(legend.position = "none")
old <- ggplot(subset(welfare, agegrade=='old'), aes(x=gender, y=income)) +
  geom_point(position="jitter", col="tan3", alpha=0.3) +
  geom_violin() +
  geom_boxplot(aes(fill=gender), notch=T, width=0.6, alpha=0.5) +
  theme(legend.position = "none")
grid.arrange(young, middle, old, ncol=3)

# 6. 나이에 따른 월급 변화를 성별을 분리하여 시각화
welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age, gender) %>% 
  summarise(mean.income=mean(income),
            sd.income=sd(income),
            median.income=median(income),
            min.income=min(income),
            max.income=max(income),
            n=n())

welfare %>% 
  filter(!is.na(income)) %>% 
  group_by(age, gender) %>% 
  summarise(mean.income=mean(income)) %>% 
  ggplot(aes(x=age, y=mean.income, col=gender)) +
  geom_line()
ggsave('outData/사례연구소스_ex06.png')

# 7. 직업별 월급의 차이가 나는지 분석하고, 
#만약 월급의 차이가나면 어떤 직업이 월급이 가장 많은지 상위 10개 직업군만 시각화
library(readxl)
job <-read_excel('inData/Koweps/Koweps_Codebook.xlsx', sheet=2)
head(job)
welfare <-left_join(welfare, job, by='code_job')
head(welfare)

welfare %>% 
  filter(!is.na(income)&!is.na(job)) %>% 
  group_by(job) %>% 
  summarise(mean.income=mean(income),
            sd.income=sd(income),
            n=n()) %>% 
  arrange(-mean.income) %>% 
  head(10)

welfare %>% 
  filter(!is.na(income)&!is.na(job)) %>% 
  group_by(job) %>% 
  summarise(mean.income=mean(income),
            sd.income=sd(income),
            n=n()) %>% 
  arrange(desc(mean.income)) %>% 
  head(10) %>% 
  ggplot(aes(x=reorder(job, mean.income), y=mean.income)) + #reorder(a, b) b의 내림차순으로 a정렬
  geom_col() +
  coord_flip() + #coord_flip(); x축과 y축 위치 바꾸기(가로 막대 그래프)
  labs(title="상위 소득 10개 직업군",
       x="직업", y="평균 소득")
ggsave('outData/사례연구소스_top10.png')

welfare %>% 
  filter(!is.na(income)&!is.na(job)) %>% 
  group_by(job) %>% 
  summarise(mean.income=mean(income)) %>% 
  arrange(-mean.income) %>% 
  tail(10) %>% 
  ggplot(aes(y=reorder(job, mean.income), x=mean.income)) +
  geom_col() +
  labs(title="하위 소득 10개 직업군",
       x="평균 소득", y="직업")

# 8. 성별로 어떤 직업이 가장 많을지 분석하시오.
welfare %>% 
  filter(!is.na(job)&gender=='female') %>% 
  group_by(job) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(10)

welfare %>% 
  filter(!is.na(job)&gender=='male') %>% 
  group_by(job) %>% 
  summarise(n=n()) %>% 
  arrange(-n) %>% 
  head(10)

f_job <-welfare %>% 
  filter(!is.na(job)&gender=='female') %>% 
  group_by(job) %>% 
  summarise(n=n()) %>% 
  arrange(desc(n)) %>% 
  head(10) %>% 
  ggplot(aes(y=reorder(job, n), x=n)) +
  geom_col() +
  labs(title="여성 최빈 직업(상위10)",
       y="직업", x="여성 수")
m_job <- welfare %>% 
  filter(!is.na(job)&gender=='male') %>% 
  group_by(job) %>% 
  summarise(n=n()) %>% 
  arrange(-n) %>% 
  head(10) %>% 
  ggplot(aes(y=reorder(job, n), x=n)) +
  geom_col() +
  labs(title="남성 최빈 직업(상위10)",
       y="직업", x="남성 수")
grid.arrange(f_job, m_job, ncol=2)

# 9. 종교 유무에 따른 이혼률을 분석하시오.
colSums(is.na(welfare))
table(is.na(welfare$religion))
str(welfare)
table(welfare$religion, useNA="ifany") #1,2(num)

welfare$religion <-factor(ifelse(welfare$religion==1, '종교-유', '종교-무'))
ggplot(welfare, aes(x=religion, fill=religion)) +
  geom_bar()

table(welfare$marriage, useNA = "ifany")
welfare$marrige_group <- ifelse(welfare$marriage==1, "기혼",
                                ifelse(welfare$marriage==3, "이혼", NA))
table(welfare$marrige_group, useNA="ifany")
table(welfare$religion, welfare$marrige_group)
table(welfare$religion, welfare$marrige_group, useNA="ifany") #결측치 포함
welfare %>% 
  filter(!is.na(religion)&!is.na(marrige_group)) %>% 
  group_by(religion, marrige_group) %>% 
  summarise(n=n())

temp <- welfare %>% 
  filter(!is.na(religion)&!is.na(marrige_group)) %>% 
  group_by(religion, marrige_group) %>% 
  summarise(n=n()) %>% 
  group_by(religion) %>% 
  mutate(total=sum(n),
         ratio=n/total*100)
temp
ggplot(temp, aes(x=religion, y=ratio, fill=marrige_group)) +
  geom_col(position="dodge")

var.test(data=temp, n~religion)
#p-value가 0.05 이상으로 종교 유무에 따른 이혼률 차이가 없다는 가설을 기각할 수 없음

# 10. 지역별 연령대 비율을 분석하시오. 노년층이 많은 지역 출력
colSums(is.na(welfare))
table(is.na(welfare$religion))
table(is.na(welfare$age))

region <- data.frame(code_region=1:7, region=c('서울', '수도권(인천/경기)', '부산/경남/울산',
                                               '대구/경북', '대전/충남', '강원/충북', 
                                               '광주/전남/전북/제주도'))

region
head(welfare)
table(welfare$code_region, useNA="ifany")
welfare <- left_join(welfare, region, by='code_region')
table(welfare$region, useNA = "ifany")

temp <- welfare %>% 
  group_by(region, agegrade) %>% 
  summarise(n=n()) %>% 
  group_by(region) %>% 
  mutate(total=sum(n),
         ratio=n/total*100) 
ggplot(temp, aes(x=region, y=ratio, fill=agegrade)) +
  geom_col(position = "dodge") +
  aes(stringr::str_wrap(region, 6), ratio) +
  labs(x="region")

#노년층 비율이 높은 지역순
temp %>% 
  filter(agegrade=='old') %>% 
  arrange(-ratio)

#노년층(수) 많은 지역순
temp %>% 
  filter(agegrade=='old') %>% 
  arrange(-n) %>% 
  ggplot(aes(x=region, y=n, fill=region)) +
  geom_col() +
  aes(stringr::str_wrap(region, 6), n) +
  labs(x="지역", y="노년층 인구") +
  geom_label(aes(label=n), fill="white", nudge_y=1.1) + #막대 그래프에 y축 라벨 표시(1)
  theme(legend.position = "none") +
  scale_fill_manual(values=topo.colors(10))

temp %>% 
  filter(agegrade=='old') %>% 
  arrange(-n) %>% 
  ggplot(aes(x=region, y=n, fill=region)) +
  geom_col() +
  aes(stringr::str_wrap(region, 6), n) +
  labs(x="지역", y="노년층 인구") +
  geom_text(aes(label=n), vjust=-0.2) + #막대 그래프에 y축 라벨 표시(2)
  theme(legend.position = "none") +
  scale_fill_manual(values=topo.colors(10))
