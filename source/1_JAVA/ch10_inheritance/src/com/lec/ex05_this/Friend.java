package com.lec.ex05_this;

public class Friend {
	private String name;
	private String tel;
	public Friend() {
		System.out.println("매개 변수 0개짜리");
	}
	public Friend(String name) {
		//this. : 내 객체의
		//this() : 현 클래스의 생성자 함수
		this();
		this.name=name;
		System.out.println("매개 변수 1개짜리");
	}
	public Friend(String name, String tel) {
		this(name); //this.name=name;
		this.tel=tel;
	}
}
