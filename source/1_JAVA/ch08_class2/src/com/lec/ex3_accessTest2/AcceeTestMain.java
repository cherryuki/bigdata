package com.lec.ex3_accessTest2;

import com.lec.ex3_accessTest.AccessTest;

public class AcceeTestMain {
	public static void main(String[] args) {
		AccessTest obj = new AccessTest();
		//System.out.println(obj.privateMember); //동일 클래스만 가능
		//System.out.println(obj.defaultMember); //동일 패키지만 가능 
		//System.out.println(obj.protectedMember); //동일 패키지 or 상속 받은 하위 클래스 가능
		System.out.println(obj.publicMember);
		//obj.privateMethod(); //동일 클래스만 가능
		//obj.defaultMethod(); //동일 패키지만 가능
		//obj.protectedMethod(); //동일 패키지 or 상속 받은 하위 클래스 가능
		obj.publicMethod();
	}
}
