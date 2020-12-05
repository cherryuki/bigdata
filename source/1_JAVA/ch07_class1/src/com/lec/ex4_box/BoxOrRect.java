package com.lec.ex4_box;
//박스 - 가로, 세로, 깊이
//직사각형 - 가로, 세로, 0
public class BoxOrRect {
	private int width;
	private int height;
	private int depth;
	private int volume; //부피나 넓이
	public BoxOrRect() {}
	public BoxOrRect(int width, int height, int depth) {//박스 객체 생성시 호출할 생성자
		this.width=width;
		this.height=height;
		this.depth=depth;
	}
	public BoxOrRect(int width, int height) {//직사각형 객체 생성시 호출할 생성자
		this.width=width;
		this.height=height;
	}
	public void calNsetVolume() {
		if(depth==0) {//직사각형의 경우 volume=width*height
			volume=width*height;
		}else {//박스의 경우 volume=width*height*depth
			volume=width*height*depth;
		}//if
	}//calVolume
	//setter&getter
	public void setWidth(int width) {
		this.width=width;
	}
	public int getWidth() {
		return width;
	}
	public void setHeight(int height) {
		this.height=height;
	}
	public int getHeight() {
		return height;
	}
	public void setDepth(int depth) {
		this.depth=depth;
	}
	public int getDepth() {
		return depth;
	}
	public void setVolume(int volume) {
		this.volume=volume;
	}
	public int getVolume() {
		return volume;
	}
	
}
