package com.lec.ex06_wrapper;
//20-12-15_API(wrapper)		ⓒcherryuki(ji)

//가변 인자 함수(매개 변수의 개수가 고정되어 있지 않음) cf)인자==매개 변수
public class Ex02 {
	public static void main(String[] args) {
		int total = valueSum("10", "20", "30", "40", "50");
		System.out.println("합계는 "+total);
	}
	private static int valueSum(String ... value) {
		int result =0; //누적 변수
		for(int i=0; i<value.length; i++) {
			result += Integer.parseInt(value[i]);
			//Integer.parseInt(str); str(문자열)을 int(정수)로 바꿔 줌
		}
		return result;
	}
}
