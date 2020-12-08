package com.lec.ex03;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		//SuperClass sup = new Superclass(); //불가능
		//ChildClass child = new ChildClass(); //불가능
		SuperClass sup = new GrandChildClass(); //super는 예약어이므로 변수로 사용 불가
		sup.method1();
		sup.method2();
		//sup.method3(); //불가능
		ChildClass child = new GrandChildClass();
		child.method1();
		child.method2();
		child.method3();
		GrandChildClass grand = new GrandChildClass();
		grand.method1();
		grand.method2();
		grand.method3();
	}

}
