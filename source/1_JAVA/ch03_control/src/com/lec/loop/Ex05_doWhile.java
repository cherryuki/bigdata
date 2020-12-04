package com.lec.loop;

import java.util.Scanner;

//로또 번호(1~45) 하나 맞추기
public class Ex05_doWhile {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int lotto = (int)(Math.random()*45)+1; //컴퓨터 로또 난수
		int num; //사용자에게 입력받은 수를 저장하는 변수
		int min = 1;
		int max = 45;
		do {
			System.out.printf("%d부터 %d까지 번호 한 개를 알아 맞춰 보세요\n", min, max);
			num = sc.nextInt();
			if(num>lotto) {
				System.out.println(num+"보다 작은 수 입니다");
				max=num-1;
			}else if(num<lotto) {
				System.out.println(num+"보다 큰 수 입니다");
				min=num+1;
			} 
		}while(num!=lotto);
		System.out.println("축하합니다. 맞추셨습니다");
		sc.close();
	}
}
