package com.lec.ex01_tryCatch;
//20-12-16_Exception		ⓒcherryuki(ji)
import java.util.Scanner;

public class Ex02 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int i, j;
		System.out.print("첫번째 수는? ");
		i=sc.nextInt();
		System.out.print("두번째 수는? ");
		j=sc.nextInt();
		System.out.println("i="+i+", j="+j);
		System.out.println("i*j="+(i*j));
		try {
			System.out.println("i/j="+(i/j));//예외 발생할 수 있는 부분			
		}catch(ArithmeticException e) {
//			e.printStackTrace();//예외 사항을 자세히 출력
			System.out.println(e.getMessage());//예외 메시지만 출력
		}
		System.out.println("i+j="+(i+j));
		System.out.println("i-j="+(i-j));
		System.out.println("Done");
		sc.close();
	}
}
