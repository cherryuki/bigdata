package com.lec.ex04_override;

public class TestMain {
	public static void main(String[] args) {
		ParentClass pObj1 = new ParentClass();
		ParentClass pObj2 = new ParentClass(2);
		pObj1.method1();
		pObj1.method2();
		System.out.println("****************");
		ChildClass cObj1 = new ChildClass();
		ChildClass cObj2 = new ChildClass(3);
		cObj1.method1();
		cObj1.method2();
		cObj1.mehtod3();
	}
}
