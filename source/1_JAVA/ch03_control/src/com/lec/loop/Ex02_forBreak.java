package com.lec.loop;

public class Ex02_forBreak {
	public static void main(String[] args) {
		for(int i=1 ; i<11 ; i++) {
			if(i==5) {
				//break; //�ݺ��� ���� ���� ����
				continue; //���������� �ö�
			}
			System.out.print(i+" ");
		}
	}
}
