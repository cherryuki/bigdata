package com.lec.loop;
// 10. 9. 8. 7. ... 2. 1.
public class Ex03_while {
	public static void main(String[] args) {
		int i=10;
		while(i>=1) {
			System.out.print(i+". ");
			i--;
		}
		System.out.println();//개행 추가
		for(int j=10; j>=1; j--) {
			System.out.print(j+". ");
		}
	}
}
