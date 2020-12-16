package com.lec.ex05_library;
//20-12-16_Exception		ⓒcherryuki(ji)

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class BookLib implements ILendable{
	private String bookNo;		//도서 번호
	private String bookTitle;	//책 제목
	private String writer;		//저자
	private String borrower;	//대출인
	private Date checkOutDate;	//대출 날짜
	private byte state;			//도서 상태(대출 가능, 대출 중)
	public BookLib() {}
	public BookLib(String bookNo, String bookTitle, String writer) {
		this.bookNo=bookNo;
		this.bookTitle=bookTitle;
		this.writer=writer;
		state=STATE_NORMAL;
	}
	
	@Override
	public void checkOut(String borrower) throws Exception {
		if(state==STATE_BORROWED) {//예외 발생
			throw new Exception("대출 중인 도서입니다");
		}
		//대출 처리
		this.borrower=borrower;
		checkOutDate = new Date();
		state=STATE_BORROWED;
		System.out.println('"'+bookTitle+"\"도서가 ★대출★되었습니다");
		System.out.println("[대출인]"+borrower);
		SimpleDateFormat sdf = new SimpleDateFormat("yyyy년 MM월 dd일(E)");
		System.out.println("[대출일]"+sdf.format(checkOutDate));
	}

	@Override
	public void checkIn() throws Exception {
		if(state==STATE_NORMAL) {//예외 발생
			throw new Exception("대출 중인 도서가 아닙니다");
		}
		//반납 처리(연체료: 1일 100원)
		Date now = new Date(); //현재 시점
		long diff = now.getTime() - checkOutDate.getTime();
		long day = diff/(1000*60*60*24);
		if(day>14) {
			day -= 14;
			System.out.println("연체료는 일일 100원씩 입니다");
			System.out.print("연체료 "+day*100+"원 을 받으셨나요(Y/N)? ");
			Scanner sc = new Scanner(System.in);
			String yesNo = sc.next();
			if(!yesNo.equalsIgnoreCase("y")) {
				System.out.println("연체료를 내셔야 반납처리 가능합니다");
				return;
			}
		}
		//반납처리
		borrower=null;
		checkOutDate=null;
		state=STATE_NORMAL;
		System.out.println('"'+bookTitle+"\"도서가 ★반납★되었습니다");
		
	}
	
	@Override
	public String toString() {
		if(state==STATE_NORMAL) {
			return '"'+bookTitle+"("+bookNo+") "+writer+" 저 대출가능";
		}else if(state==STATE_BORROWED) {
			SimpleDateFormat sdf = new SimpleDateFormat("(yy-MM-dd E요일)");
			return '"'+bookTitle+"("+bookNo+") "+writer+" 저 대출"+sdf.format(checkOutDate)+"중";
		}else {
			return "도서 상태를 확인 할 수 없습니다";
		}
	}
	//getter&setter
	public String getBookNo() {
		return bookNo;
	}
	public void setBookNo(String bookNo) {
		this.bookNo = bookNo;
	}
	public String getBookTitle() {
		return bookTitle;
	}
	public void setBookTitle(String bookTitle) {
		this.bookTitle = bookTitle;
	}
	public String getWriter() {
		return writer;
	}
	public void setWriter(String writer) {
		this.writer = writer;
	}
	public String getBorrower() {
		return borrower;
	}
	public void setBorrower(String borrower) {
		this.borrower = borrower;
	}
	public Date getCheckOutDate() {
		return checkOutDate;
	}
	public void setCheckOutDate(Date checkOutDate) {
		this.checkOutDate = checkOutDate;
	}
	public byte getState() {
		return state;
	}
	public void setState(byte state) {
		this.state = state;
	}
	

}
