package com.lec.loop;

import java.util.Scanner;

public class Ex04_doWhile {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num;
		do {
			System.out.print("짝수를 입력하세요: ");
			num = sc.nextInt(); //사용자로부터 입력받은 수를 num에 할당
		}while(num%2==1 || num%2==-1 || num==0);
			System.out.println("입력하신 짝수는 "+num);
			sc.close();
	}
}
