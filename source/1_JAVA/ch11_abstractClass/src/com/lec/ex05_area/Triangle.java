package com.lec.ex05_area;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class Triangle extends Shape {
	private int w; //밑변
	private int h; //높이
	public Triangle() {}
	public Triangle(int w, int h) {
		super();
		this.w=w;
		this.h=h;
	}
	@Override
	public double computeArea() {
//		System.out.println("삼각형의 넓이는 "+(w*h*0.5)); //(w*h)/2.0 가능
		return w*h*0.5;
	}
	@Override
	public void draw() {
		System.out.print("삼각형 ");
		super.draw();
	}

}
