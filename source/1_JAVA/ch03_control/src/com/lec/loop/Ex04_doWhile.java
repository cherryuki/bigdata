package com.lec.loop;

import java.util.Scanner;

public class Ex04_doWhile {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int num;
		do {
			System.out.print("¦���� �Է��ϼ���: ");
			num = sc.nextInt(); //����ڷκ��� �Է¹��� ���� num�� �Ҵ�
		}while(num%2==1 || num%2==-1 || num==0);
			System.out.println("�Է��Ͻ� ¦���� "+num);
			sc.close();
	}
}
