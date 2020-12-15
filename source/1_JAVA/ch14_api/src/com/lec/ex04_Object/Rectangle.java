package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)
public class Rectangle {
	private int w; //가로
	private int d; //세로
	private String color;
	public Rectangle() {
		color="검정";
	}
	public Rectangle(int w, int d, String color) {
		this.w=w;
		this.d=d;
		this.color=color;
	}
	@Override
	public String toString() {
		return "[가로 "+w+"cm, 세로 "+d+"cm의 "+color+"색 사각형]";
	}
	@Override
	public boolean equals(Object obj) {
		if(obj!=null && obj instanceof Rectangle) {
			return w==((Rectangle)obj).w && d==((Rectangle)obj).d 
					&& color.equals(((Rectangle)obj).color);
		}
		return false;
	}
}
