package com.lec.ex03;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class GrandChildClass extends ChildClass {
	@Override
	public void method1() {
		System.out.println("GrandChild의 method1()");
	}
}

//ChildClass - 추상 method1(), 일반 method2(), 일반 method3()
