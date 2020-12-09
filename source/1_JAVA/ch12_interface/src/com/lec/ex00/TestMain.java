package com.lec.ex00;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
//		InterfaceEx1 ex1 = new InterfaceEx1(); //불가능
//		InterfaceEx2 ex2 = new InterfaceEx2(); //불가능
		InterfaceClass obj1 = new InterfaceClass();
		obj1.method1();
		obj1.method2();
		InterfaceEx1 obj2 = new InterfaceClass();
		obj2.method1();
//		obj2.method2(); //불가능(InterfaceEx1엔 method2()가 없음)
		InterfaceEx2 obj3 = new InterfaceClass();
		if(obj3 instanceof InterfaceClass) {//명시적 형변환을 위한 확인 단계
			((InterfaceClass)obj3).method1();//명시적 형변환
		}
//		obj3.method1(); //불가능(InterFaceEx2엔 method1()이 없음)
		obj3.method2();
	}
}
