package com.lec.ex06_wrapper;
//20-12-15_API(wrapper)		ⓒcherryuki(ji)

//스트링 -> 정수
//정수 -> 스트링
public class Ex03 {
	public static void main(String[] args) {
		System.out.println("스트링을 정수: Integer.parseInt(문자열)");
		int i = Integer.parseInt("123");
		int j = Integer.parseInt("010");
		System.out.println(i);
		System.out.println(j);
		System.out.println("정수를 스트링: String.valueOf(정수)");
//		String monthString = ""+12;
		String monthString = String.valueOf(12);
		System.out.println(monthString);
//		String tel = String.valueOf(010);//0을 앞에 붙이며 8진수로 계산됨 = 8
//		System.out.println(tel);
	}
}
