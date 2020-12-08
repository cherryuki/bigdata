package com.lec.ex07_grand;
//20-12-07_inheritance ⓒcherryuki(ji)
public class GrandChild extends Child1 {
	private int gc = 3;
	public GrandChild() {
		System.out.println("GrandChild형 객체 생성");
	}
	public int getGc() {
		return gc;
	}
	public void setGc(int gc) {
		this.gc = gc;
	}
	
}
