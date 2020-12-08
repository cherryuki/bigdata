package com.lec.ex03;
//20-12-08_abstract class	ⓒcherryuki(ji)
public abstract class ChildClass extends SuperClass {
	//추상 클래스를 상속받아 오버라이드를 하지 않기 위해선 상속 받은 클래스도 추상 클래스여야 함 
	//SuperClass로 부터 받은 추상 메소드 method1() 
	@Override
	public void method2() {
		System.out.println("ChildClass의 method2()");
	}
	public void method3() {
		System.out.println("ChildClass의 method3()");
	}
}

//SuperClass - 추상 method1(), 일반 method2()
