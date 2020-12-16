package com.lec.ex03_exceptionExs;
//20-12-16_Exception		ⓒcherryuki(ji)
public class Ex03_numberFormat {
	public static void main(String[] args) {
		String str = "";
		int i=0;
		try {
			i=Integer.parseInt(str.trim());//trim()으로 앞 뒤 스페이스 제거
		}catch(NumberFormatException e) {
			System.out.println(e.getMessage());
		}
		System.out.println(i);
	}
}
