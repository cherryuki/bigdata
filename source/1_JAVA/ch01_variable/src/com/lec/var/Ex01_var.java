package com.lec.var;

public class Ex01_var {
	public static void main(String[] args) {
		//변수선언 방법
		//1.자료형 변수명;
		int num1; //선언만 하고 값 할당은 안 함
		num1 = 10;
		System.out.println("num1="+num1);
		//2.자료형 변수명 = 값;
		char c1 = '씨';
		System.out.println("c1="+c1);
		// 3.자료형 변수명1, 변수명2, ...변수명n; 
		boolean b1, b2, b3;
		b1 = true; b2=false; b3 = true;
		System.out.print("b1="+b1+"\t b2="+b2+"\t b3="+b3+"\n");
		//4.자료형 변수명1=값1, 변수명2=값,...변수명n=값n;
		long l1 = 2200000000L;
		float f1=1.19f, f2=2.22f, f3;
		System.out.println("f1="+f1+"\t f2="+f2);
		System.out.printf("f1 = %3.1f, f2 = %4.1f\n",f1, f2);
		//%f:실수, %d:정수, %c:문자, %s:문자열, %x-16진수
		System.out.println("프로그램 끝");
	}// 프로그램 끝
} //class 끝
