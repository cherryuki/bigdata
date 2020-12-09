package com.lec.ex09_library;
//20-12-09_interface	ⓒcherryuki(ji)
public interface ILendable {
	public byte STATE_BORROWED = 1; //대출 중
	public byte STATE_NORMAL = 0; //대출 가능
	public void checkOut(String borrower, String checkOutDate); //대출
	public void checkIn(); //반납
	public void printState(); //ex) "자바" 홍길동저 대출 가능
}
