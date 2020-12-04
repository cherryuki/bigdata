package com.lec.loop;

import java.util.Scanner;

//가위(0),바위(1),보(2) 반복(-1을 누르면 종료)
public class Q1_while {
	public static void main(String[] args) {
		int computer, i;
		Scanner sc = new Scanner(System.in);
		while(true) {
			System.out.print("가위(0), 바위(1), 보(2)를 입력하세요. 종료를 원하시면 -1을 입력하세요.");
			i=sc.nextInt();
			if(i==-1) {
				System.out.print("종료합니다");
				break;
			}
			computer = (int)(Math.random()*3); //0~3미만의 정수 난수
			if(i<0 || i>=3) {
				System.out.println("잘못 입력하셨습니다");
			}else if((i+2)%3==computer) {
				System.out.println("당신 승리");
			}else if(i==computer) {
				System.out.println("무승부");
			}else {
				System.out.println("컴퓨터 승리");
			}//if
		}//while
		sc.close();
	}//main
}
