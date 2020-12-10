package com.lec.ex10_booklib;
//20-12-10_interface	ⓒcherryuki(ji)
import java.util.Scanner;

public class LibMain {
	public static void main(String[] args) {
		BookLib[] books = {new BookLib("j01-100", "java", "김정호"),
					new BookLib("j01-125", "Java", "율곡"),
					new BookLib("j01-200", "JAVA", "도산"),
					new BookLib("p01-100", "python", "매화"),
					new BookLib("p01-123", "Python", "다산")};
		Scanner sc = new Scanner(System.in);
		int fn, idx=0; //기능 번호(1.대출, 2.반납, 3.도서 현황, 0.종료), 도서 인덱스
		String bookTitle, borrower, checkOutDate; //책제목, 대출인, 대출 날짜
		do {
			System.out.print("1:대출 | 2:반납 | 3:도서 현황 | 0:종료 ");
			fn=sc.nextInt();
			switch(fn) {
			case 1: //도서 조회(도서명 입력) -> (보유 도서면)대출 가능 여부 확인 -> (가능하다면) 대출 진행(대출인, 대출 날짜 입력)
				System.out.println("대출할 도서명을 입력해주세요");
				bookTitle=sc.next();
				for(idx=0; idx<books.length; idx++) {
					if(bookTitle.equals(books[idx].getBookTitle())) {
						break;
					}
				}
				if(idx==books.length) {
					System.out.println("본 도서관에는 해당 도서가 없습니다");
				}else if(books[idx].getState()==ILendable.STATE_BORROWED) {
					System.out.println(bookTitle+" 도서는 대출 중입니다");
				}else {
					//대출인, 대출 날짜 입력받아 대출 진행
					System.out.println("대출하시는 분의 성함을 입력해 주세요");
					borrower=sc.next();
					System.out.println("대출 날짜를 입력해주세요(YY-MM-DD)");
					checkOutDate=sc.next();
					books[idx].checkOut(borrower, checkOutDate);
				}break;
			case 2: //도서 조회(도서명 입력) -> (보유 도서면)도서 상태 확인 -> 반납
				System.out.println("반납할 도서명을 입력해주세요");
				bookTitle=sc.next();
				for(idx=0; idx<books.length; idx++) {
					if(bookTitle.equals(books[idx].getBookTitle())) {
						break;
					}
				}
					if(idx==books.length) {
						System.out.println("해당 도서는 본 도서관 책이 아닙니다");
					}else {
						books[idx].checkIn();
					}break;
				case 3: //확장for문을 이용해서 도서 상태 출력
					for(BookLib book:books) {
						book.printState();
					}
				}
		}while(fn!=0);
		sc.close();
		System.out.println("시스템을 종료합니다");			
	}
}

