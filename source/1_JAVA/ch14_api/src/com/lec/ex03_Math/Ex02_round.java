package com.lec.ex03_Math;
//20-12-15_API(Math)		ⓒcherryuki(ji)
public class Ex02_round {
	public static void main(String[] args) {
		System.out.println("소수점 첫째자리에서 올림, 반올림, 버림");//기준: 소수점 첫째자리(일의 자리까지)
		System.out.println("9.23을 올림: "+Math.ceil(9.23));//10.0 (double타입 리턴)
		System.out.println("9.23을 반올림: "+Math.round(9.23));//9 (round만 정수타입 리턴)
		System.out.println("9.23을 버림: "+Math.floor(9.23));//9.0 (double타입 리턴)
		
		System.out.println("소수점 둘째자리에서(한자리까지) 올림, 반올림, 버림");
		System.out.println("9.15를 올림: "+Math.ceil(9.15*10)/10);
		System.out.println("9.15를 반올림: "+Math.round(9.15*10)/10.0);
		//round는 int를 반환하므로 나눌 때 double로 나눠야 함(10.0)
		System.out.println("9.15를 버림: "+Math.floor(9.15*10)/10);
		
		System.out.println("십의 자리에서(백의 자리까지) 올림, 반올림, 버림");
		//double형으로 나눠야 함! (100이 아닌 100.0으로 나눠야 함)
		System.out.println("175를 올림: "+Math.ceil(175/100.0)*100);
		System.out.println("175를 반올림: "+Math.round(175/100.0)*100);
		System.out.println("175를 버림: "+Math.floor(175/100.0)*100);
	}
}
