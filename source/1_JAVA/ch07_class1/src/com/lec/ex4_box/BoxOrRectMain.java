package com.lec.ex4_box;

public class BoxOrRectMain {
	public static void main(String[] args) {
		BoxOrRect box = new BoxOrRect(5,6,10); //3차원 박스
		BoxOrRect rect = new BoxOrRect(5,10); //2차원 직사각형
		box.calNsetVolume();
		rect.calNsetVolume();
		System.out.println("박스 부피: "+box.getVolume());
		System.out.println("직사각형 넓이: "+rect.getVolume());
	}
}
