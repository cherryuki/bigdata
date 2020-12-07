package com.lec.ex06_super;

public class ParentClass {
	private String pStr = "부모클래스";
	public ParentClass() {
		System.out.println("부모 생성자");
	}
	public void getPapaName() {
		System.out.println("아빠 유재석");
	}
	public void getMamiName() {
		System.out.println("엄마 나경은");
	}
	public String getpStr() {
		return pStr;
	}
	public void setpStr(String pStr) {
		this.pStr=pStr;
	}
}
