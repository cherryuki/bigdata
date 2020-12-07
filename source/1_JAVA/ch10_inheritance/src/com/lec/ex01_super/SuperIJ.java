package com.lec.ex01_super;

public class SuperIJ {
	private int i;
	private int j;
	public SuperIJ() {
		System.out.println("Super 매개 변수 없는 생성자");
	}
	public SuperIJ(int i, int j) {
		this.i=i;
		this.j=j;
		System.out.println("Super 매개 변수 있는 생성자");
	}
	public int getI() {
		return i;
	}
	public void setI(int i) {
		this.i = i;
	}
	public int getJ() {
		return j;
	}
	public void setJ(int j) {
		this.j = j;
	}
	
}
