package com.lec.oper;
//관계(비교) 연산자: 같다(==), 다르다(!=), 크다(>), 작다(<), 크거나 같다(>=), 작거나 같다(<=)
public class Ex02_oper {
	public static void main(String[] args) {
		int n1=10, n2=5;
		boolean result = n1 > n2;
		System.out.printf("%d %s %d = %b\n", n1, ">", n2, result);
		result = n1 >= n2;
		System.out.printf("%d %s %d = %b\n", n1, ">=", n2, result);
		result = n1 == n2;
		System.out.printf("%d %s %d = %b\n", n1, "==", n2, result);
		result = n1 <= n2;
		System.out.printf("%d %s %d = %b\n", n1, "<=", n2, result);
		result = n1 != n2;
		System.out.printf("%d %s %d = %b\n", n1, "!=", n2, result);
	}
}
