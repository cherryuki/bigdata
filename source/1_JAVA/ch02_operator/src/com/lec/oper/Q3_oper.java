package com.lec.oper;

import java.util.Scanner;
//����, ����, ���� ������ �Է¹޾� ������ ����� ���
public class Q3_oper {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("���� ����: ");
		int kor = sc.nextInt();
		System.out.print("���� ����: ");
		int eng = sc.nextInt();
		System.out.print("���� ����: ");
		int mat = sc.nextInt();
		int tot = kor + eng + mat; //����
		double avg = tot/3.0; //���
//		double avg = (double)tot/3;
		System.out.printf("����: %3d\n", kor);
		System.out.printf("����: %3d\n", eng);
		System.out.printf("����: %3d\n", mat);
		System.out.printf("����: %3d,\t���: %.2f\n", tot, avg);
		sc.close();
	}
}
