# 2021-02-18 R_텍스트 마이닝(워드 클라우드)      ⓒcherryuki(ji) #
# # # 12장. 텍스트 마이닝 # # #
# 텍스트 마이닝: 문자로 된 비정형 데이터로부터 가치있는 정보를 얻어내는 분석 기법
 ##텍스트 마이닝시 가장 먼저 할 일은 형태소 분석

install.packages("rJava")
install.packages("memoise")

install.packages("KoNLP") #availavle error
#별도로 KoNLP 0.80.2.tar.gz 파일 설치 필요 - 인터넷 이용

#R에서 우측 하단의 Packages -> install 도구를 이용해서 설치(수동 설치)시 필요한 패키지 설치
install.packages("devtools")

#KoNLP가 의존하는 패키지 설치
install.packages("hash")
install.packages("tau")
install.packages("Sejong")

#Packages -> install 도구 이용하여 KoNLP 패키지 설치
#C:/Users/Home/Documents/R/win-library/4.0/KoNLP/java에 'scala-library-2.11.8.jar' 설치하라는 문구

library(KoNLP)
Sys.getenv("JAVA_HOME") #없으면 환경변수 필요함 (제대로 나오면 이미 환경변수 되어 있는 것)

#사전 설정하기
useNIADic()
extractNoun('대한민국의 영토는 한반도와 그 부속 도서로 한다')
extractNoun('의미있는 하루 하루, 항상 감사한 하루가 되길')

# 1. 힙합 가사 텍스트 마이닝
# 1.1 텍스트 마이닝할 텍스트 로드(필요한 data 확보)
txt <-readLines('inData/hiphop.txt') #비정형 데이터
txt
head(txt)

# 1.2 특수문자 제거
#gsub(oldStr, newStr string)
#str_replace_all(string, oldStr, newStr)
library(stringr)
temp <-gsub('\\W', ' ', txt) #특수문자(\\W)를 space로 바꿈
txt <-str_replace_all(txt, '\\W', ' ')
table(temp==txt)

# 1.3 명사 추출
head(txt)
nouns <-extractNoun(txt) #명사만 추출하여 list형태로 반환
class(nouns)
head(unlist(nouns)) #벡터형태로 전환: unlist
table(unlist(nouns))
wordcount <-table(unlist(nouns)) #워드카운트; 단어별 빈도표
class(wordcount) #table
sort(wordcount)
df_word <-as.data.frame(wordcount, stringsAsFactors = F)
 #stringsAsFactors=F; 문자를 chr 타입으로 하기 위함(factor 타입X)
head(df_word, 10)
str(df_word)
library(dplyr)
df_word <-rename(df_word, word=Var1, freq=Freq)
str(df_word)
head(df_word)
nrow(df_word)
df_word <- df_word %>% 
  filter(nchar(word)>=2) #nchar(); 문자수 반환
df_word <-filter(df_word, nchar(word)>=2) #위와 동일한 결과
head(df_word)


#자주 사용되는 단어 빈도표 top20 만들기
top20 <-df_word[order(-df_word$freq), ][1:20,]
top20 <-df_word %>% 
  arrange(desc(freq)) %>% 
  head(20)
top20

#자주 사용되는 단어 top20 그래프 그리기
library(ggplot2)
ggplot(data=top20, aes(x=freq, y=reorder(word, freq))) +
  geom_col() +
  geom_text(aes(label=freq), hjust=1.2, col="white") +
  labs(title="힙합 가사에 자주 사용되는 단어 top20",
       x="출현 빈도", y="출현 단어")

#워드 클라우드
#1. 비정형 text 데이터 확보
#2. 패키지 설치 및 로드(KoNLP, wordcloud)
#3. 확보된 text 데이터 읽어고기
#4. 명사 추출
#5. 필요없는 데이터 삭제(특수문자, ㅋㅋ, kk, [0-9] 등)
#6. 워드 카운트 생성(단어 빈도표); table(unlist(단어))
#7. wordcloud함수 이용해서 워드칼라우드 생성

install.packages("wordcloud")
library(wordcloud) #컬러팔레트(RColorBrewer)도 같이 로드 됨

set.seed(1234) #난수 고정; 난수 생성 결과 일치 시키기 위함
round(runif(6, min=1, max=45))

display.brewer.all()
?wordcloud

pal <-brewer.pal(8, "Dark2")
set.seed(1234)
wordcloud(word=df_word$word, #출력될 단어
          freq=df_word$freq, #단어 빈도
          min.freq=2,        #최소 단어 빈도
          max.words=200,     #표현 단어 수
          random.order = F,  #고빈도 단어 중앙 배치
          rot.per=.1,        #회전 단어 비율
          scale=c(2,0.3),    #단어 크기 범위
          colors=pal)        #색깔 목록 지정

#색상 변경
pal <-brewer.pal(9, "Blues")[5:9]
wordcloud(words=df_word$word,
          freq=df_word$freq,
          min.freq = 2,
          max.words=200,
          random.order = F,
          ort.per=.1,
          scale=c(2,0.3),
          colors=pal) #pal대신 rainbow, topo.colors 등 사용 가능


# 2. 국정원 트윗 데이터 텍스트 마이닝
twitter <-read.csv("inData/twitter.csv",
                   header=T,
                   stringsAsFactors = F,
                   fileEncoding = 'UTF-8')
head(twitter)
View(twitter)
class(twitter)
twitter <-rename(twitter,
                 no=번호,
                 id=계정이름,
                 date=작성일,
                 tw=내용)
edit(twitter)

#필요 없는 문자, 단어 삭제하기
twitter$tw <-str_replace_all(twitter$tw, '\\W', ' ')
twitter$tw <-str_replace_all(twitter$tw, '[ㄱ-ㅎ]', ' ')
twitter$tw <-str_replace_all(twitter$tw, '  ', ' ') #스페이스 줄이기
head(twitter)

nouns <-extractNoun(twitter$tw)
head(nouns)
class(nouns)
wordcount <-table(unlist(nouns))
class(wordcount)
df_word <-as.data.frame(wordcount, stringsAsFactors = F)
df_word <-rename(df_word, word=Var1, freq=Freq)
str(df_word)
head(df_word)

#출현단어 중 2글자 이상만 분석
df_word <-filter(df_word, nchar(word)>1)

#최빈 단어 top20 출력, 그래프 
top20 <-df_word[order(df_word$freq, decreasing = T), ][1:20, ]
top20

df_word %>% 
  arrange(desc(freq)) %>% 
  head(20) %>% 
  ggplot(aes(x=freq, y=reorder(word, freq))) +
  geom_bar(stat="identity") +
  labs(x="빈도", y="출현 단어")

ggplot(top20, aes(x=freq, y=reorder(word, freq))) +
  geom_col() +
  labs(x="출현 빈도", y="출현 단어") +
  geom_text(aes(label=freq), hjust=1.2, col="white")
#coord_flip(); x축과 y축 바꾸기

#워드클라우드 그리기
set.seed(1234)
pal <-brewer.pal(9, "Blues")[5:9]
wordcloud(word=df_word$word,
          freq=df_word$freq,
          min.freq = 5,
          max.words = 300,
          random.order = F,
          rot.per=0.1,
          scale=c(3, 0.3),
          colors=pal)

sort(table(twitter$id))
# 150회 이상 트윗한 아이디의 게시물에 대해 최빈 top20개 단어를 출력, 시각화 하고 워드 클라우드를 완성
View(twitter)
more150Id <-twitter %>% 
  group_by(id) %>% 
  summarise(n=n()) %>% 
  filter(n>150)

more150 <- twitter %>% 
  filter(id %in% more150Id$id) %>% 
  select(id, tw)

table(more150$id)

more150$tw <-str_replace_all(more150$tw, '\\W', ' ')
more150$tw <-str_replace_all(more150$tw, '[ㄱ-ㅎ]', ' ')
more150$tw <-str_replace_all(more150$tw, '  ', ' ')

nouns <-extractNoun(more150$tw)
head(nouns)
class(nouns)

wordcount <-table(unlist(nouns))
class(wordcount)
df_word <-as.data.frame(wordcount, stringsAsFactors = F)
head(df_word)
df_word <-rename(df_word, word=Var1, freq=Freq)
str(df_word)
df_word <-filter(df_word, nchar(word)>1)
set.seed(1234)
wordcloud(word=df_word$word,
          freq=df_word$freq,
          min.freq = 5,
          max.words = 300,
          random.order = F,
          rot.per=0.1,
          sclae=c(3, 0.3),
          color=pal)

df_word %>% 
  arrange(-freq) %>% 
  head(20)

df_word %>% 
  arrange(-freq) %>% 
  head(20) %>% 
  ggplot(aes(x=freq, y=reorder(word, freq))) +
  geom_col() +
  geom_text(aes(label=freq), col="yellow", hjust=1.1) +
  labs(y="단어", x="출현 빈도 수",
       title="150회 이상 트윗한 아이디 게시물의 최빈 단어")
