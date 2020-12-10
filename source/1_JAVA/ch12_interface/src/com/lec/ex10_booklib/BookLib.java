package com.lec.ex10_booklib;
//20-12-10_interface	ⓒcherryuki(ji)
public class BookLib extends BookInfo implements ILendable {
	private String borrower;
	private String checkOutDate;
	private byte state;
	public BookLib() {}
	public BookLib(String bookNo, String bookTitle, String writer) {
		super(bookNo, bookTitle, writer);
		borrower=null;
		checkOutDate=null;
		state=STATE_NORMAL;
	}
	@Override
	public void checkOut(String borrower, String checkOutDate) {
		if(state==STATE_BORROWED) {
			System.out.println("대출 중인 도서입니다");
			return;
		}
		//대출 처리
		this.borrower=borrower;
		this.checkOutDate=checkOutDate;
		state=STATE_BORROWED;
		System.out.println("\""+getBookTitle()+"\"도서가 대출 되었습니다");
	}

	@Override
	public void checkIn() {
		if(state==STATE_NORMAL) {
			System.out.println("해당 도서는 대출 중인 도서가 아닙니다.");
			return;
		}
		//반납 처리
		borrower=null;
		checkOutDate=null;
		state=STATE_NORMAL;
		System.out.println("\""+getBookTitle()+"\"도서가 반납되었습니다");
	}

	@Override
	public void printState() {
		if(state==STATE_NORMAL) {
			System.out.printf("%s(%s 저), 대출 가능\n", getBookTitle(), getWriter());
		}else if(state==STATE_BORROWED) {
			System.out.printf("%s(%s 저), 대출 중\n", getBookTitle(), getWriter());
		}else {
			System.out.printf("%s(%s 저)의 상태를 확인할 수 없습니다\n", getBookTitle(), getWriter());
		}
	}
	public String getBorrower() {
		return borrower;
	}
	public String getCheckOutDate() {
		return checkOutDate;
	}
	public byte getState() {
		return state;
	}

}
