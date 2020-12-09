package com.lec.ex00;
//20-12-09_interface	ⓒcherryuki(ji)

//InterfaceEx1 (CONSTANT_NUM, method1())
//InterfaceEx2 (CONSTANT_STRING, method2())
public class InterfaceClass implements InterfaceEx1, InterfaceEx2 {
	@Override
	public void method1() {
		System.out.println("실제 구현은 implements한 클래스에서 구현");
	}	
	@Override
	public String method2() {
		System.out.println("실제 구현은 implements한 클래스에서 구현");
		return null;
	}
}
