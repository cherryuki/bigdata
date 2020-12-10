package com.lec.ex10_booklib;
//20-12-10_interface	ⓒcherryuki(ji)
public class BookInfo {
	private String bookNo;
	private String bookTitle;
	private String writer;
	public BookInfo() { }
	public BookInfo(String bookNo, String bookTitle, String writer) {
		this.bookNo=bookNo;
		this.bookTitle=bookTitle;
		this.writer=writer;
	}
	public String getBookNo() {
		return bookNo;
	}
	public String getBookTitle() {
		return bookTitle;
	}
	public String getWriter() {
		return writer;
	}
}
