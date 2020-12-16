package com.lec.ex03_exceptionExs;
//20-12-16_Exception		ⓒcherryuki(ji)
public class Ex01_nullPoint {
	public static void main(String[] args) {
		String greeting = "Hello";
		System.out.println(greeting.toUpperCase());
		greeting=null;
//		System.out.println(greeting.toUpperCase());//NullPointerException
	}
}
