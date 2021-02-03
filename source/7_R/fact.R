# 2021-02-03 R_R프로그래밍_팩토리얼 함수     ⓒcherryuki(ji) #

fact <-function(n) {
  if(n<0) {
    print("양수를 입력해주세요")
  } else if(n==0) {
    cat("0 ! = 1")
  } else {
    result <-1
    for(val in n:1) {
      result=result*val
    }
    cat(n, "! =", result)
  }
}