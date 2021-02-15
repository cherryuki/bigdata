# 2021-02-15 R_마크다운      ⓒcherryuki(ji) #
# # # 9장. 마크다운(데이터 분석 보고서 - 데이터 시각화 예제) # # #

#ex01
library(ggplot2)
png('outData/09_ex01.png')
ggplot(cars, aes(x=speed, y=dist)) + 
  geom_point() +
  coord_cartesian(xlim=c(5,20), ylim=c(0,100)) +
  geom_smooth(method="lm")
dev.off()

#ex02
library(gapminder)
ggplot(gapminder, aes(x=gdpPercap, y=lifeExp, col=continent)) +
  geom_point()
ggsave('outData/09_ex02.png')

#ex03
library(dplyr)
gapminder %>% 
  group_by(continent) %>% 
  filter(lifeExp>70) %>% 
  summarise(n=n()) %>% 
  ggplot(aes(x=continent, fill=continent, y=n)) +
  geom_bar(stat="identity") +
  labs(title="연습문제 3.",
       subtitle="기대수명이 70을 초과하는 데이터 빈도(대륙별)",
       x="대륙", y="빈도")
ggsave('outData/09_ex03.png')

#ex04
gapminder %>% 
  filter(lifeExp>70) %>% 
  group_by(continent) %>% 
  summarise(n=n_distinct(country)) %>% 
  ggplot(aes(x=continent, fill=continent, y=n)) +
  geom_col() +
  labs(title="연습문제4.",
       subtitle="기대수명이 70을 초과하는 대륙별 나라 빈도",
       y="나라 빈도")
ggsave('outData/09_ex04.png')

#ex05
ggplot(gapminder, aes(x=continent, y=lifeExp)) +
  geom_boxplot(aes(col=continent)) +
  coord_cartesian(ylim=c(40, 80)) +
  labs(title="연습문제5.",
       subtitle="대륙별 기대수명의 사분위 수")
ggsave('outData/09_ex05.png')

#ex06
ggplot(gapminder, aes(x=gdpPercap, y=lifeExp)) +
  geom_point(aes(col=continent), alpha=0.5) +
  facet_wrap(~year) +
  scale_x_log10() +
  labs(title="연습문제6.",
       subtitle="GDP와 기대수명과의 관계")
ggsave('outData/09_ex06.png')

#ex07.
temp <-gapminder %>% 
  filter(substr(country, 1, 5)=='Korea')
temp$country <-factor(temp$country)
str(temp$country)
temp$country <-factor(temp$country, levels=c('Korea, Rep.', 'Korea, Dem. Rep.'))
temp %>% 
  ggplot(aes(x=year, y=gdpPercap)) +
  geom_point(aes(col=country, pch=country)) +
  labs(title="연습문제7.",
       subtitle="GDP의 변화(한국과 북한)") +
  scale_color_manual(values=c("red", "blue")) +
  scale_shape_manual(values=c(3, 16)) +
  theme(legend.position = c(0.2, 0.8))
ggsave('outData/09_ex07.png')

#ex08.
gapminder %>% 
  filter(country %in% c('China', 'Japan', 'Korea, Dem. Rep.', 'Korea, Rep.')) %>% 
  ggplot(aes(x=year, y=gdpPercap, col=country)) +
  geom_point() +
  geom_line() +
  labs(title="연습문제8.",
       subtitle="한중일 4개국의 GDP변화의 산점도와 추세선")
ggsave('outData/09_ex08.png')

#ex09.
library(gridExtra)
g1 <-gapminder %>% 
  filter(country %in% c('China', 'Japan', 'Korea, Dem. Rep.', 'Korea, Rep.')) %>% 
  ggplot(aes(x=year, y=pop, col=country)) +
  geom_point() +
  geom_line() +
  labs(title="연습문제9.",
       subtitle="한중일 4개국의 인구 변화 산점도와 추세선") +
  theme(legend.position = c(0.6, 0.4))
g2 <-gapminder %>% 
  filter(country %in% c('China', 'Japan', 'Korea, Dem. Rep.', 'Korea, Rep.')) %>% 
  ggplot(aes(x=year, y=pop, col=country)) +
  geom_point() +
  geom_line() +
  labs(title="연습문제9.",
       subtitle="한중일 4개국의 인구 변화 산점도와 추세선") +
  scale_y_continuous(labels=scales::comma) +
  theme(legend.position = c(0.6, 0.4))
grid.arrange(g1, g2, ncol=2)
ggsave('outData/09_ex09.png') #g2만 저장

#ex10.
ggplot(economics, aes(x=date, y=psavert)) +
  geom_line(col="red", size=2) +
  geom_smooth(col="red") +
  labs(title="연습문제10.",
       subtitle="개인저축률 시계열 그래프")
ggsave('outData/09_ex10.png')
