package com.lec.ex04_override;

public class ChildClass extends ParentClass {
	public ChildClass() {
		System.out.println("C 매개 변수 없는 생성자");
	}
	public ChildClass(int i) {
		System.out.println("C 매개 변수 있는 생성자");
	}
	@Override
	public void method1() {//오버라이딩(함수의 재정의)
		System.out.println("Child의 method1()");
	}
	public void mehtod3() {
		System.out.println("Child의 method3()");
	}
}
