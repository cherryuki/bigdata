package com.lec.condition;

import java.util.Scanner;
//������ �Է¹޾� ������ ���
public class Q2_switch {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("������ �Է��ϼ���: ");
		int score = sc.nextInt();
		int temp = score==100? score-1:score;//100���� ��츦 ���� �ʿ�
		switch(temp/10) {
		case 9:
			System.out.println("A����"); break;
		case 8:
			System.out.println("B����"); break;
		case 7:
			System.out.println("C����"); break;
		case 6:
			System.out.println("D����"); break;
		case 5: case 4: case 3: case 1: case 0:
			System.out.println("F����"); break;
		default:
			System.out.println("��ȿ���� ���� �����Դϴ�"); break;
		}
	}
}
