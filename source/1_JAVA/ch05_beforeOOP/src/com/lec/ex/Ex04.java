package com.lec.ex;

public class Ex04 {
	public static void main(String[] args) {
		printCh();
		System.out.println("Hello, World!");
		printCh('=');
		System.out.println("Hello, Java");
		printCh('-', 30);
	}		
	private static void printCh(char ch, int count) {
		for(int cnt=1; cnt<=count; cnt++) {//ch가 count개 있는 라인
			System.out.print(ch);
		}
		System.out.println();//개행
	}
	private static void printCh(char ch) {
		for(int cnt=1; cnt<=20; cnt++) {//ch가 20개 있는 라인
			System.out.print(ch);
		}
		System.out.println();//개행
	}
	private static void printCh() {
		for(int cnt=1; cnt<=20; cnt++) {//*이 20개 있는 라인
			System.out.print("*");
		}
		System.out.println();//개행
	}
}

