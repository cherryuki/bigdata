package com.lec.oper;
//나이를 입력받아 입력받은 나이가 65세 이상일 때, "경로우대" 출력, 아니면 "일반" 출력
import java.util.Scanner;

public class Q2_oper {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("나이를 입력하세요");
		int age = sc.nextInt();
		System.out.println(age>=65? "경로우대":"일반");
		sc.close();
	}
}
