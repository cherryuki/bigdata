package com.lec.oper;
//산술 연산자(+,-,*,/,%;나머지 연산)
public class Ex01_oper {
	public static void main(String[] args) {
		int n1 = 33, n2=10;
		int result;
		double resultDouble;
		result = n1 + n2;
		System.out.printf("%d %c %d = %d\n", n1, '+', n2, result);
		result = n1 - n2;
		System.out.printf("%d %c %d = %d\n", n1, '-', n2, result);
		result = n1 * n2;
		System.out.printf("%d %c %d = %d\n", n1, '*', n2, result);
		result = n1 / n2;
		System.out.printf("%d %c %d = %d\n", n1, '/', n2, result);
		resultDouble = n1 / (double)n2;
		System.out.printf("%d %c %d = %.1f\n", n1, '/', n2, resultDouble);
		result = n1 % n2;
		System.out.printf("%d %c %d = %d\n", n1, '%', n2, result);
		//나머지 연산자의 쓰임새
		if (n1%2==0)
			System.out.println("짝수");
		else
			System.out.println("홀수");
	}//main함수 끝
}//class 끝

