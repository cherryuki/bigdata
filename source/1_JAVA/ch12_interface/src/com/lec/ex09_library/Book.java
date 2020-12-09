package com.lec.ex09_library;
//20-12-09_interface	ⓒcherryuki(ji)
public class Book implements ILendable {
	private String bookNo; 			//책 번호
	private String bookTitle; 		//책 제목
	private String writer;			//저자
	private String borrower;		//대출인(입력)
	private String checkOutDate;	//대출일(입력)
	private byte state;
	public Book() {} //디폴트 생성자
	public Book(String bookNo, String bookTitle, String writer) {
		this.bookNo=bookNo;
		this.bookTitle=bookTitle;
		this.writer=writer;
		borrower=null;
		checkOutDate=null;
		state=STATE_NORMAL;
	}
	//Book b = new Book("123가-12나", "자바", "홍길동")
	//b.checkOut("손소유", "20-12-09")
	@Override
	public void checkOut(String borrower, String checkOutDate) {
		if(state==STATE_BORROWED) {
			System.out.println("대출 중인 도서입니다");
			return;
		}
		//대출 처리 로직
		this.borrower=borrower;
		this.checkOutDate=checkOutDate;
		state=STATE_BORROWED;
		//"자바"도서가 대출되었습니다 //"표시하는 두가지 방법 ('"' or "\"), """는 불가능 
		System.out.println('"'+bookTitle+'"'+"도서가 대출되었습니다");
//		System.out.println("\""+bookTitle+"\"도서가 대출되었습니다");
	}
	//b.checkIn()
	@Override
	public void checkIn() {
		if(state==STATE_NORMAL) {
			System.out.println("대출 중인 도서가 아닙니다");
			return;
		}
		//반납 처리 로직
		borrower=null;
		checkOutDate=null;
		state=STATE_NORMAL;
		//"자바"도서가 반납되었습니다
		System.out.println("\""+bookTitle+"\"도서가 반납되었습니다");
	}
	//b.printState() -> 자바(홍길동 저), 대출 가능(or 대출 중)
	@Override
	public void printState() {
		if(state==STATE_NORMAL) {
			System.out.printf("%s(%s 저), 대출 가능\n", bookTitle, writer);
		}else if(state==STATE_BORROWED) {
			System.out.printf("%s(%s 저), 대출 중\n", bookTitle, writer);
		}else {
			System.out.printf("%s(%s 저)의 상태를 확인 할 수 없습니다\n", bookTitle, writer);
		}
//		String msg=bookTitle+"("+writer+"저 ),";
//		msg += state==STATE_NORMAL? "대출 가능":"대출 중";
//		System.out.println(msg);
	}

}
