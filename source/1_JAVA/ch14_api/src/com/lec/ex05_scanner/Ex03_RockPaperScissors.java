package com.lec.ex05_scanner;
//20-12-15_API(Scanner)		ⓒcherryuki(ji)
import java.util.Scanner;

//가위, 바위, 보(이길 때까지)
public class Ex03_RockPaperScissors {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String i; //가위, 바위, 보
		int computer;
		while(true){
			System.out.println("가위, 바위, 보 중에 하나를 입력하세요(당신이 이길 때까지)");
			i=sc.nextLine().trim(); //i = sc.next();
			computer = (int)(Math.random()*3); //0:가위, 1:바위, 2:보
			if(i.equals("가위")) {
				if(computer==0) {
					System.out.println("컴퓨터: 가위, 무승부");
				}else if(computer==1) {
					System.out.println("컴퓨터: 바위, 컴퓨터 승리");
				}else if(computer==2) {
					System.out.println("컴퓨터: 보, 승리하셨습니다. 종료합니다");
					break;
				}
			}
			if(i.equals("바위")) {
				if(computer==0) {
					System.out.println("컴퓨터: 가위, 승리하셨습니다. 종료합니다");
					break;
				}else if(computer==1) {
					System.out.println("컴퓨터: 바위, 무승부");
				}else if(computer==2) {
					System.out.println("컴퓨터: 보, 컴퓨터 승리");
				}
			}
			if(i.equals("보")) {
				if(computer==0) {
					System.out.println("컴퓨터: 가위, 컴퓨터 승리");
				}else if(computer==1) {
					System.out.println("컴퓨터: 바위, 승리하셨습니다. 종료합니다");
					break;
				}else if(computer==2) {
					System.out.println("컴퓨터: 보, 무승부");
				}
			}
		 }//while
		sc.close();
		System.out.println("bye");
	}//main
}//class

