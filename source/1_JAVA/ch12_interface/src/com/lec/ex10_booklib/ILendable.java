package com.lec.ex10_booklib;
//20-12-10_interface	ⓒcherryuki(ji)
public interface ILendable {
	public byte STATE_BORROWED = 1; //대출 중
	public byte STATE_NORMAL = 0; //대출 가능
	public void checkOut(String borrwer, String checkOutDate); //대출
	public void checkIn(); //반납
	public void printState(); //대출 가능여부 확인
}
