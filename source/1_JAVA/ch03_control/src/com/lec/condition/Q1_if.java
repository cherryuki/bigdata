package com.lec.condition;

import java.util.Scanner;
//����ڷκ��� ����(0), ����(1), ��(2) �� �Է� �ް�
//��ǻ�͵� ����(0), ����(1), ��(2) �� �ϳ��� �����ؼ� ���ڸ� ���
public class Q1_if {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("����(0), ����(1), ��(2) �� �ϳ��� �Է��ϼ���: ");
		int you = sc.nextInt();
		if (you == 0) {
			System.out.println("You: ����");
		} else if (you == 1) {
			System.out.println("You: ����");
		} else if (you == 2) {
			System.out.println("You: ��");
		} else {
			System.out.println("�߸� �Է��ϼ̽��ϴ�");
			System.exit(0);
		}
		sc.close();
		int computer = (int) (Math.random() * 3); // 0~3�̸� ����
		if (computer == 0) {
			System.out.println("��ǻ��: ����");
		} else if (computer == 1) {
			System.out.println("��ǻ��: ����");
		} else {
			System.out.println("��ǻ��: ��");
		}
		if ((you + 2) % 3 == computer) {
			System.out.println("��� �¸�");
		} else if (you == computer) {
			System.out.println("���º�");
		} else {
			System.out.println("��ǻ�� �¸�");
		}
//	if(you==0) {
//	if(computer==0) {
//		System.out.println("���º�");
//	}else if(computer==1) {
//		System.out.println("��ǻ�� �¸�");
//	}else {
//		System.out.println("��� �¸�");
//	}
//}else if(you==1) {
//	if(computer==0) {
//		System.out.println("��� �¸�");
//	}else if(computer==1) {
//		System.out.println("���º�");
//	}else {
//		System.out.println("��ǻ�� �¸�");
//	}
//}else if(you==2) {
//	if(computer==0) {
//		System.out.println("��ǻ�� �¸�");
//	}else if(computer==1) {
//		System.out.println("��� �¸�");
//	}else {
//		System.out.println("���º�");
//	}//computer if��
//}// you if��
	}// main�Լ�
}// class
