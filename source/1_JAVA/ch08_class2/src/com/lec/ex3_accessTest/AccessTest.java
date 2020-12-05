package com.lec.ex3_accessTest;

public class AccessTest {
	private int privateMember;  //동일 클래스 내에서만
	int defaultMember;			//디폴트: 동일 패키지 내에서만
	protected int protectedMember; //동일 패키지나 상속받은 하위 클래스
	public int publicMember; 	//아무데서나(외부 가능)
	private void privateMethod() { //동일 클래스 내에서만
		System.out.println("private 메소드 호출");
	}
	void defaultMethod() {		//동일 패키지에서만
		System.out.println("default 메소드 호출");
	}
	protected void protectedMethod() {
		System.out.println("protected 메소드 호출");
	}
	public void publicMethod() {
		System.out.println("public 메소드 호출");
	}
}
