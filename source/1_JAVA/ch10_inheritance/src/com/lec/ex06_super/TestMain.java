package com.lec.ex06_super;
//20-12-07_inheritance ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		ChildClass obj = new ChildClass();
		System.out.println(obj.getcStr());
		System.out.println(obj.getpStr());
		obj.getPapaName();
		obj.getMamiName();
	}
}
