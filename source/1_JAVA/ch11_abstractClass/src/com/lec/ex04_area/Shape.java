package com.lec.ex04_area;
//20-12-08_abstract class	ⓒcherryuki(ji)
public abstract class Shape {//추상 메소드를 1개 이상 가진 추상 클래스
	public void draw() {
		System.out.println("도형을 그려요");
	}
	public abstract void computeArea(); //추상 메소드
}