package com.lec.ex;

import java.util.Scanner;

public class Ex03 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int su=-5;
		System.out.println(su+"의 절대값은 "+Arithmetic.abs(su));
		sc.close();
		
		Arithmetic ar = new Arithmetic(); //Arithmetic형 객체
		int sum = ar.sum(10,50); //10~50까지의 합
		System.out.println("합은 "+sum);
		System.out.println(ar.evenOdd(sum));
		System.out.println("*****************");
		sum=ar.sum(50); //0~50까지의 합
		System.out.println("합은 "+sum);
		System.out.println(ar.evenOdd(sum));
	}
}
