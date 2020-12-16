package com.lec.ex01_tryCatch;
//20-12-16_Exception		ⓒcherryuki(ji)
import java.util.InputMismatchException;
import java.util.Scanner;

public class Ex03 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i, j=1;
		do {
			try {
				System.out.print("첫번째 수는? ");
				i=sc.nextInt();
				break;
			}catch(InputMismatchException e) {
				System.out.println(e.getMessage());
				System.out.println("첫번째 수에 문자를 입력할 수 없습니다");
				sc.nextLine();
			}
		}while(true);
		System.out.print("두번째 수는? ");
		try {
			j=sc.nextInt();
			System.out.println("i="+i+", j="+j);
			System.out.println("i*j="+(i*j));
			System.out.println("i/j="+(i/j));
		}catch(InputMismatchException e) {
			System.out.println(e.getMessage());
			System.out.println("두번째 수에 문자를 입력해서 1로 초기화 하였습니다");
		}catch(ArithmeticException e) {
			System.out.println(e.getMessage()+"0으로 나눌 수 없어 패스");
		}catch(Exception e) {
			System.out.println("무슨 에러? "+e.getMessage());
		}
		System.out.println("i+j="+(i+j));
		System.out.println("i-j="+(i-j));
		System.out.println("Done");
		sc.close();
	}
}
