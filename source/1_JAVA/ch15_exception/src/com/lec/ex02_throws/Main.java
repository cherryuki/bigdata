package com.lec.ex02_throws;
//20-12-16_Exception		ⓒcherryuki(ji)
public class Main {
	public static void main(String[] args) {//메인함수에서는 가능한 throws 하지 않아야 함
		try {
			new ThrowsEx();
		} catch (Exception e) {
			System.out.println("에러 메시지: "+e.getMessage());
		}
	}
}
