package com.lec.condition;

import java.util.Scanner;
//두 수를 입력받아 최대값 출력
public class Ex02_if {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("첫번째 수: ");
		int num1 = scanner.nextInt();
		System.out.print("두번째 수: ");
		int num2 = scanner.nextInt();
		if(num1>=num2) {
			System.out.println("입력하신 값들의 최대값은 "+num1);
		}else {
			System.out.println("입력하신 값들의 최대값은 "+num2);
		}
	}
}
