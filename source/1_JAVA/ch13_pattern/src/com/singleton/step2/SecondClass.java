package com.singleton.step2;
//20-12-10_singletonClass	ⓒcherryuki(ji)
public class SecondClass {
	public SecondClass() {
		SingletonClass singletonObject = SingletonClass.getInstance();
		System.out.println("SecondClass 생성자");
		System.out.println(singletonObject.getI());
		System.out.println("SecondClass 생성자 끝.");
	}
}
