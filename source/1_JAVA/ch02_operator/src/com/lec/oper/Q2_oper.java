package com.lec.oper;
//���̸� �Է¹޾� �Է¹��� ���̰� 65�� �̻��� ��, "��ο��" ���, �ƴϸ� "�Ϲ�" ���
import java.util.Scanner;

public class Q2_oper {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("���̸� �Է��ϼ���");
		int age = sc.nextInt();
		System.out.println(age>=65? "��ο��":"�Ϲ�");
		sc.close();
	}
}
