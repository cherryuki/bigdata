package com.lec.ex;

public class Ex02 {
	private static int sum(int to) {
		int result = 0; //누적해서 전달할 변수
		for(int i=1; i<=to; i++) {
			result += i;
		}
		return result;
	}
	private static int sum(int from, int to) {//from=1, to=100
		int result = 0; //누적해서 전달할 변수
		for(int i=from; i<=to; i++) {
			result += i;
		}
		return result;
	}
	private static String evenOdd(int value) {
		String result = value%2==0? "짝수":"홀수";
		return result;
	}
	public static void main(String[] args) {
		int sum = sum(10);
		System.out.println("합은 "+sum);
		System.out.println(evenOdd(sum));
		sum = sum(1,100);
		System.out.println("합은 " +sum);
		System.out.println(evenOdd(sum));
		sum = sum(50,100);
		System.out.println("합은 "+sum);
		System.out.println(evenOdd(sum));
	}
}
