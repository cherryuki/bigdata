package com.lec.ex07_use;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		User user = new User();
		A a = new A();
		B b = new B();
		user.aorbUse(a);
		user.aorbUse(b);
	}
}
