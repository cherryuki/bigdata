package com.lec.ex;

public class Ex01 {
	public static void main(String[] args) {
		int sum=0; //누적변수
		for(int i=1; i<=10; i++) {
			sum += i;
		}
		System.out.println("합은 "+sum);
		System.out.println((sum%2==0)? "짝수":"홀수");
		sum = 0; //누적변수
		for(int i=1; i<=50; i++) {
			sum += i;
		}
		System.out.println("합은 "+sum);
		System.out.println((sum%2==0)? "짝수":"홀수");
		sum=0; //누적변수
		for(int i=10; i<=50; i++) {
			sum += i;
		}
		System.out.println("합은 "+sum);
		System.out.println((sum%2==0)? "짝수":"홀수");
	}
}
