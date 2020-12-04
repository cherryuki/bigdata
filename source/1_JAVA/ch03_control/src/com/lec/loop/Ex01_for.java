package com.lec.loop;

public class Ex01_for {
	public static void main(String[] args) {
		for(int i=1 ; i<=5 ; i++) {
			for(int j=1 ; j<=i ; j++) {
				System.out.print('*');
			}
			System.out.println();//개행
		}
//		for (int j=1 ; j<=5 ; j++) {
//			System.out.print('*');
//		}
	}
}
