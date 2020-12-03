package com.lec.oper;
//입력한 두 수를 비교연산자를 이용하여, 비교한 결과가 true이면 O, false이면 X를 출력
import java.util.Scanner;

public class Q1_oper {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.print("첫번째 수: ");
		int num1 = scanner.nextInt();
		System.out.print("두번째 수: ");
		int num2 = scanner.nextInt();
		String result = num1 == num2 ? "O" :"X";
		System.out.println("num1==num2의 결과는 "+ result);
		boolean result2 = num1 > num2;
		System.out.println("num1>num2의 결과는 "+ ((result2==true)? "O":"X"));
		scanner.close();
	}
}
