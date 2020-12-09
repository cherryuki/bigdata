package com.lec.ex09_library;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Book book1 = new Book("123가-12나", "자바", "홍길동");
		Book book2 = new Book("124가-13다", "하둡", "이몽룡");
		book1.checkIn();
		book1.checkOut("손소유", "20-12-09"); //대출 처리
		book1.checkOut("달산", "20-12-09");
		book1.printState();
		book2.printState();
	}
}
