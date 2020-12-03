package com.lec.loop;
//1~10까지의 홀수의 합은 25
public class Q3_for {
	public static void main(String[] args) {
		int sum = 0;
//		for(int i=1; i<11; i+=2) {//i=i+2
//			sum += i; //sum=sum+i
//		}
		for(int i=1; i<11; i++) {
			if(i%2==1) {
				sum += i;
			}
		}
		System.out.println("1~10까지의 홀수의 합은"+sum);
	}
}
