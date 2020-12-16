package com.lec.ex05_library;
//20-12-16_Exception		ⓒcherryuki(ji)
public interface ILendable {
	public byte STATE_BORROWED=1; //대여중
	public byte STATE_NORMAL=0; //대여 가능
	public void checkOut(String borrower) throws Exception;
	public void checkIn() throws Exception;
}
