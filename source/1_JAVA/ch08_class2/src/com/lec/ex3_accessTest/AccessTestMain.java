package com.lec.ex3_accessTest;

public class AccessTestMain {
	public static void main(String[] args) {
		AccessTest obj = new AccessTest();
		//System.out.println(obj.privateMember); //클래스가 달라서 불가능
		System.out.println(obj.defaultMember); //동일 패키지라 가능
		System.out.println(obj.protectedMember); //동일 패키지라 가능
		System.out.println(obj.publicMember);
		//obj.privateMethod(); //클래스가 달라서 불가능
		obj.defaultMethod();
		obj.protectedMethod();
		obj.publicMethod();
	}

}
