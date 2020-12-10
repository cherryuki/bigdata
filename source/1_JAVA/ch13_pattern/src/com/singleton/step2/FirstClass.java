package com.singleton.step2;
//20-12-10_singletonClass	ⓒcherryuki(ji)
public class FirstClass {
	public FirstClass() {
		SingletonClass singletonObject = SingletonClass.getInstance();
		System.out.println("FirstClass형 객체 생성");
		System.out.println(singletonObject.getI());
		singletonObject.setI(100);
		System.out.println("FirstClass에서 변경 후 i 값: "+singletonObject.getI());
		System.out.println("FirstClass형 생성자 끝.");
	}
}
