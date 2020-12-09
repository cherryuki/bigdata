package com.lec.ex04_multi;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		TestChildClass test = new TestChildClass();
		System.out.println(test.i1+", "+test.i2);
		System.out.println(test.i3+", "+test.i11);
		test.m1();
		test.m2();
		test.m3();
		test.m11();
		TestClass cTest = test;
		cTest.m1();
		cTest.m2();
		cTest.m3();
		//cTest.m11(); //불가능
	}
}
