package com.lec.oper;
//����(��) ������: ����(==), �ٸ���(!=), ũ��(>), �۴�(<), ũ�ų� ����(>=), �۰ų� ����(<=)
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
