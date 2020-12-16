package com.lec.ex05_library;
//20-12-16_Exception		ⓒcherryuki(ji)

import java.util.Scanner;

public class BookMain {
	public static void main(String[] args) {
		BookLib[] books = {new BookLib("j01-100", "java", "김자바"),
				new BookLib("j01-125", "hadoop", "홍하둡"),
				new BookLib("j01-200", "JAVA3", "이자바"),
				new BookLib("p01-100", "python", "박파이"),
				new BookLib("p01-123", "person", "정사람")};
		Scanner sc = new Scanner(System.in);
		String bookTitle, borrower;
		int fn, idx=0; //기능번호(0.도서현황, 1.대출, 2.반납, 그 외:종료), 도서 인덱스
		do {
			System.out.print("0:전체 도서 조회 | 1:대출 | 2:반납 |그 외:종료 ");
			try {
				fn=sc.nextInt();
			}catch(Exception e) {
				break;
			}
			switch(fn) {
			case 0: 
				for(BookLib book:books) {
					System.out.println(book);
				}break;
			case 1://대출
				System.out.print("대출을 원하는 도서명을 입력하세요: ");
				bookTitle=sc.next();
				for(idx=0; idx<books.length; idx++) {
					if(bookTitle.equalsIgnoreCase(books[idx].getBookTitle())) {
						break;
					}
				}
				if(idx==books.length) {//도서가 없을 경우
					System.out.println("해당 도서를 찾을 수 없습니다");
				}else {
					if(books[idx].getState()==BookLib.STATE_BORROWED) {//이미 빌린 도서일 경우
						System.out.println("현재 대출 중인 도서입니다");
					}else {//대출
						System.out.print("대출하시는 분의 이름을 입력하세요: ");
						borrower=sc.next();
						try {
							books[idx].checkOut(borrower);//대출 처리
						}catch(Exception e) {
							System.out.println(e.getMessage());
						}
					}
				}break;
			case 2://반납
				System.out.print("반납할 도서명을 입력하세요: ");
				bookTitle=sc.next();
				for(idx=0; idx<books.length; idx++) {
					if(bookTitle.equalsIgnoreCase(books[idx].getBookTitle())) {
						break;
					}
				}
				if(idx==books.length) {
					System.out.println("해당 도서는 본 도서관 책이 아닙니다");
				}else {
					try {
						books[idx].checkIn(); //반납
					}catch(Exception e) {
						System.out.println(e.getMessage());
					}
				}
			}
		}while(fn==0 || fn==1 || fn==2);
		System.out.println("종료합니다");
		sc.close();
	}
}
