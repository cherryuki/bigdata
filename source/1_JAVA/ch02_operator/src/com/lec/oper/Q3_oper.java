package com.lec.oper;

import java.util.Scanner;
//국어, 영어, 수학 점수를 입력받아 총점과 평균을 출력
public class Q3_oper {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("국어 점수: ");
		int kor = sc.nextInt();
		System.out.print("영어 점수: ");
		int eng = sc.nextInt();
		System.out.print("수학 점수: ");
		int mat = sc.nextInt();
		int tot = kor + eng + mat; //총점
		double avg = tot/3.0; //평균
//		double avg = (double)tot/3;
		System.out.printf("국어: %3d\n", kor);
		System.out.printf("영어: %3d\n", eng);
		System.out.printf("수학: %3d\n", mat);
		System.out.printf("총점: %3d,\t평균: %.2f\n", tot, avg);
		sc.close();
	}
}
