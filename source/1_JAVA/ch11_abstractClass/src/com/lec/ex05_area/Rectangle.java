package com.lec.ex05_area;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class Rectangle extends Shape {
	private int w; //가로
	private int h; //세로
	public Rectangle() {}
	public Rectangle(int w, int h) {
		super();
		this.w=w;
		this.h=h;
	}
	public int getW() {
		return w;
	}
	public void setW(int w) {
		this.w = w;
	}
	public int getH() {
		return h;
	}
	public void setH(int h) {
		this.h = h;
	}
	@Override
	public double computeArea() {
//		System.out.println("직사각형의 넓이는 "+(w*h));
		return w*h;
	}
	@Override
	public void draw() {
		System.out.print("직사각형");
		super.draw();
	}
}
