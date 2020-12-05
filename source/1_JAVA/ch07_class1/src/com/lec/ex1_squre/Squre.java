package com.lec.ex1_squre;
//Squre s1 = new Squre()
//Squre s2 = new Squre(10);
public class Squre {
	private int side;
	public Squre() {//매개변수 없는 생성자 -> 생성자 오버로딩
		System.out.println("매개변수 없는 생성자 호출");
	}
	public Squre(int side) {//매개변수 있는 생성자
		this.side=side;
		System.out.println("매개변수 있는 생성자 호출");
	}
	public int area() {
		return side*side;
	}
	public int getSide() {//~.getSide() 사용
		return side;
	}
	public void setSide(int side) {//~.setSide(10)
		this.side=side;
	}
}
