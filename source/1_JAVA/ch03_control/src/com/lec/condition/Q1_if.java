package com.lec.condition;

import java.util.Scanner;
//사용자로부터 가위(0), 바위(1), 보(2) 중 입력 받고
//컴퓨터도 가위(0), 바위(1), 보(2) 중 하나를 선택해서 승자를 출력
public class Q1_if {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("가위(0), 바위(1), 보(2) 중 하나를 입력하세요: ");
		int you = sc.nextInt();
		if (you == 0) {
			System.out.println("You: 가위");
		} else if (you == 1) {
			System.out.println("You: 바위");
		} else if (you == 2) {
			System.out.println("You: 보");
		} else {
			System.out.println("잘못 입력하셨습니다");
			System.exit(0);
		}
		sc.close();
		int computer = (int) (Math.random() * 3); // 0~3미만 정수
		if (computer == 0) {
			System.out.println("컴퓨터: 가위");
		} else if (computer == 1) {
			System.out.println("컴퓨터: 바위");
		} else {
			System.out.println("컴퓨터: 보");
		}
		if ((you + 2) % 3 == computer) {
			System.out.println("당신 승리");
		} else if (you == computer) {
			System.out.println("무승부");
		} else {
			System.out.println("컴퓨터 승리");
		}
//	if(you==0) {
//	if(computer==0) {
//		System.out.println("무승부");
//	}else if(computer==1) {
//		System.out.println("컴퓨터 승리");
//	}else {
//		System.out.println("당신 승리");
//	}
//}else if(you==1) {
//	if(computer==0) {
//		System.out.println("당신 승리");
//	}else if(computer==1) {
//		System.out.println("무승부");
//	}else {
//		System.out.println("컴퓨터 승리");
//	}
//}else if(you==2) {
//	if(computer==0) {
//		System.out.println("컴퓨터 승리");
//	}else if(computer==1) {
//		System.out.println("당신 승리");
//	}else {
//		System.out.println("무승부");
//	}//computer if문
//}// you if문
	}// main함수
}// class
