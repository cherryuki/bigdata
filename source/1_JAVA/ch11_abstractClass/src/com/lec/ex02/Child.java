package com.lec.ex02;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class Child extends Super {
	@Override
	public void method1() {
		System.out.println("Child의 method1() - 추상 메소드라 꼭 오버라이드");
	}
	public void method3() {
		System.out.println("Child의 method3()");
	}
}
