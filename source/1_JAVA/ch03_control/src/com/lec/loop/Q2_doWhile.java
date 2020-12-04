package com.lec.loop;

import java.util.Scanner;
//가위(0),바위(1),보(2) 반복(당신이 이기면 종료) - do while 사용
public class Q2_doWhile {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int computer, i;
		do {
			System.out.println("가위(0), 바위(1), 보(2) 중 하나를 선택하세요.(당신이 이길 때까지)");
			i = sc.nextInt();
			computer = (int)(Math.random()*3); 
			if(i<0||i>2) {
				System.out.println("잘못 입력하셨습니다");
			}else if((i+2)%3==computer) {
				System.out.println("당신 승리");
				break;
			}else if(i==computer) {
				System.out.println("무승부");
			}else if((i+1)%3==computer ){
				System.out.println("컴퓨터 승리");
			}
			}while( (i>-1 || i<3) || ((i+1)%3!=computer)); 
			sc.close();
			System.out.println("bye");
	}

}
