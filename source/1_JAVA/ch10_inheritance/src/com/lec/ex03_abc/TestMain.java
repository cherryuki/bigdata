package com.lec.ex03_abc;

public class TestMain {
	public static void main(String[] args) {
		S s = new S();
		S a = new A(); //A a = new A();
		//Object a = new A(); 
		System.out.println(a.s);
		S b = new B();
		S c = new C();
		System.out.println();
		S[] sArr = {new A(), new B(), new C()};
	}
}
