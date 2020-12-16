package com.lec.ex01_tryCatch;
//20-12-16_Exception		ⓒcherryuki(ji)
public class Ex04_finally {
	public static void main(String[] args) {
		int[] iArr = {0,1,2};
		for(int i=0; i<=iArr.length; i++) {
			try {
				System.out.println("iArr["+i+"] = "+iArr[i]);
			}catch(ArrayIndexOutOfBoundsException e) {
				System.out.println("예외 메시지: "+e.getMessage());
			}finally {
				System.out.println("예외여부 상관 없이 항상 실행");
			}
		}//for
		System.out.println("프로그램 끝");
	}
}
