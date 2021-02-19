# 2021-02-19 R_웹 데이터 수집      ⓒcherryuki(ji) #
# # # 13장. 웹 데이터 수집(웹크롤링) # # #
# 1. 정적 웹크롤링: 단일 페이지 크롤링 (rvest 패키지 사용)
install.packages("rvest")
library(rvest)

#네이버 영화 평점, 리뷰
#영화제목 class="movie color_b"
#영화 평점: <div class="list_netizen_score"> 밑에 <em> </em>
#리뷰를 가져오기 위해서 <td class="title> 가져와서 점수(<em>)을 기준으로 뒷 부분

url <-'https://movie.naver.com/movie/point/af/list.nhn'
text <-read_html(url, encoding='CP949')
text
#영화 제목; .movie
nodes <-html_nodes(text, '.movie')
nodes
title <-html_text(nodes)
title

#해당 영화 페이지
movieInfo <-html_attr(nodes, 'href')
movieInfo <-paste0(url, movieInfo) #paste0; space 없이 붙여줌
movieInfo

#평점; .list_netizen_score em
nodes <-html_nodes(text, ".list_netizen_score em")
nodes
point <-html_text(nodes)
point

#영화 리뷰; .title
nodes <-html_nodes(text, '.title')
nodes
review <-html_text(nodes, trim=TRUE)
review <-gsub('\t', '', review)
review <-gsub('\n', '', review)
review

strsplit(review, '중[0-9]{1,2}')
review <-unlist(strsplit(review, '중[0-9]{1,2}'))[seq(2,20,2)]
review <-gsub('신고', '', review)
review

page <-cbind(title, movieInfo)
page <-cbind(page, point)
page <-cbind(page, review)
View(page)

#csv파일로 out
write.csv(page, "outData/movie_review.csv")
write.csv(page, "outData/movie_review.csv", row.names=F)

#여러 페이지 정적 웹크롤링
home <- 'https://movie.naver.com/movie/point/af/list.nhn'
site <- 'https://movie.naver.com/movie/point/af/list.nhn?&page='
movie.review <-NULL

for(i in 1:100) {
  url <-paste0(site, i);
  text <-read_html(url, encoding='CP949')
  #영화제목; .movie
  nodes <-html_nodes(text, '.movie')
  title <-html_text(nodes)
  #해당 영화 페이지
  movieInfo <-html_attr(nodes, 'href')
  movieInfo <-paste0(home, movieInfo)
  #평점; .list_netizen_score em
  nodes <-html_nodes(text, ".list_netizen_score em")
  point <-html_text(nodes)
  #영화 리뷰; .title
  nodes <-html_nodes(text, '.title')
  review <-html_text(nodes, trim=TRUE)
  review <-gsub('\t', '', review)
  review <-gsub('\n', '', review)
  review <- unlist(strsplit(review, '중[0-9]{1,2}'))[seq(2,20,2)]
  review <- gsub('신고', '', review)
  page <-cbind(title, movieInfo)
  page <-cbind(page, point)
  page <-cbind(page, review)
  movie.review <-rbind(movie.review, page)
}

View(movie.review)
write.csv(movie.review, 'outData/movie_review100page.csv', row.names=F)

#1~100페이지까지 크롤링한 영화들 중 평점이 높은 10개를 시각화
movie <-as.data.frame(movie.review, stringsAsFactors = F)
str(movie)
movie$point <-as.numeric(movie$point)

library(dplyr)
library(ggplot2)

movie %>% 
  group_by(title) %>% 
  summarise(avg.point=mean(point),
            sum.point=sum(point)) %>% 
  arrange(desc(avg.point, sum.point)) %>% 
  head(10)

#평점이 최소 5개 이상인 영화 들 중에서 평점이 높은 10개
more5 <-movie %>% 
  group_by(title) %>% 
  summarise(n=n()) %>% 
  filter(n>=5)
more5[order(-more5$n),]

movie %>% 
  filter(title %in% more5$title) %>% 
  group_by(title) %>% 
  summarise(avg.point=mean(point)) %>% 
  arrange(desc(avg.point)) %>% 
  head(10)

movie %>% 
  filter(title %in% more5$title) %>% 
  group_by(title) %>% 
  summarise(avg.point=mean(point)) %>% 
  arrange(desc(avg.point)) %>% 
  head(10) %>% 
  ggplot(aes(x=avg.point, y=reorder(title, avg.point))) +
  geom_col() +
  labs(title="평점이 높은 top10 영화",
       subtitle="(평점 최소 5개 이상인 영화 대상)",
       x="평점", y="영화 제목") +
  geom_text(aes(label=round(avg.point,1)), col="white", hjust=1.2)

library(stringr)
#영화 리뷰 내용만 뽑아 최빈단어 10개, 워드 칼라우드 시각화
library(KoNLP)
useNIADic()
movie$review
review <-movie$review
review <-str_replace_all(review, '\\W', ' ')
review <-str_replace_all(review, '[ㄱ-ㅎ]', ' ')
review <-str_replace_all(review, '  ', ' ')

nouns <-extractNoun(review)
head(nouns)
wordcount <-table(unlist(nouns))
df_word <-as.data.frame(wordcount, stringsAsFactors = F)
head(df_word)

df_word <-rename(df_word, word=Var1, freq=Freq)
df_word <-df_word %>% filter(nchar(word)>1)

top10 <-df_word %>% 
  arrange(-freq) %>% 
  head(10)
ggplot(top10, aes(x=freq, y=reorder(word, freq))) +
  geom_bar(stat="identity")

library(wordcloud)
display.brewer.all()

set.seed(1234)
pal <-brewer.pal(8, 'Set2')
wordcloud(words=df_word$word,
          freq=df_word$freq,
          min.freq=5,
          max.words=200,
          random.order = F,
          rot.per=0.1,
          scale=c(3, 0.3),
          color=pal)


# 2. 동적 웹 크롤링(selenium 패키지 이용): 스크롤 다운, 로그인 이후, 버튼, ...
#특정 폴더 생성후 3개의 파일을 다운받아 압축을 풀고 셀레니움 서버 가동
##java -Dwebdriver.gecko.driver="geckodriver.exe" -jar selenium-server-standalone-3.141.59.jar -port 4445
##CMD창은 셀레니움 폴더에서 열고, 윗줄 복사해서 붙여 넣은 뒤 엔터 + CMD창 끄지 않고 작업해야함

# 필요한 패키지 다운로드와 로드
install.packages("RSelenium")
library(httr)
library(rvest)
library(RSelenium)

###셀레니움 동적 웹 크롤링 준비 완료
#예제1. 특정 부분에 text를 입력한 후 엔터한 결과를 크롤링(검색창)
remDr <-remoteDriver(port=4445L, #포트번호
                     browserName='chrome') #사용할 브라우저
remDr$open()
remDr$navigate('https://www.youtube.com')
webElem <-remDr$findElement(using='css', '#search')
webElem$sendKeysToElement(list('과학 다큐 비욘드', key='enter'))

#현재 페이지의 html 소스 가져오기
html <-remDr$getPageSource()[[1]]
html <-read_html(html)

#'#video-title' css 안의 text 가져오기
youtube_title <-html %>%  html_nodes('#video-title') %>% html_text()
head(youtube_title)

youtube_url <- html %>%  html_nodes('#video-title') %>% html_attr('href')
head(youtube_url)

youtube_url <- ifelse(is.na(youtube_url), '',
                      paste0('https://www.youtube.com'), youtube_url)

#제목만 text파일로 out
write.table(youtube_title,
            file='outData/과학다큐비욘드결과.txt',
            sep='',
            row.names=F,
            quote=F)
result <-cbind(youtube_title, youtube_url)
write.csv(result, filte="outData/과학다큐비욘드결과.csv",
          row.names=F)

#예제2. n번 마우스 스크롤 다운한 크롤링(댓글)
remD <-remoteDriver(port=4445L,
                    browserName='chrome')
remD$open() #서버를 통해 브라우저 open
remD$navigate('https://youtu.be/tZooW6PritE')

btn <- remD$findElement(using='css selector',
                        value='.html5-main-video')
btn$clickElement() #메인 동영상 플레이 멈춤

#마우스 스크롤 다운
remD$executeScript("window.scrollTo(0,500)")
remD$executeScript("window.scrollTo(0,1000)")
remD$executeScript("window.scrollTo(1000,1500)")
remD$executeScript("window.scrollTo(1000,2000)")
remD$executeScript("window.scrollTo(0,3000)")
remD$executeScript("window.scrollTo(0,5000)")

#현재 페이지의 html 소스 가져오기
html <-remD$getPageSource()[[1]]
html <-read_html(html)

comments <-html %>% html_nodes('#content-text') %>%  html_text()
comments[1:10]

write.table(comments, file="outData/댓글.txt",
            sep=',',
            #row.names=F,
            quote=F)
