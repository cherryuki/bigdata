package com.lec.condition;

import java.util.Scanner;
//점수를 입력받아 학점을 출력
public class Q2_switch {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("점수를 입력하세요: ");
		int score = sc.nextInt();
		int temp = score==100? score-1:score;//100점일 경우를 위해 필요
		switch(temp/10) {
		case 9:
			System.out.println("A학점"); break;
		case 8:
			System.out.println("B학점"); break;
		case 7:
			System.out.println("C학점"); break;
		case 6:
			System.out.println("D학점"); break;
		case 5: case 4: case 3: case 1: case 0:
			System.out.println("F학점"); break;
		default:
			System.out.println("유효하지 않은 점수입니다"); break;
		}
	}
}
