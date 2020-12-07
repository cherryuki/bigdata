package com.lec.ex08_person;
//Baby p = new Baby("공유", "잘생겼다");
public class Baby extends Person {
	public Baby() {
		System.out.println("매개 변수 없는 Baby 생성자");
	}
	public Baby(String name, String character) {
		super(name, character); //부모단의 생성자(매개 변수 있는). 항상 첫 명령어로 호출되어야 함
		System.out.println("매개 변수 있는 Baby 생성자");
	}
	public void cry() {
		System.out.println("응애응애");
	}
	@Override
	public void intro() {
		super.intro();
		System.out.println(getName()+"은(는) 아기라서 엄마가 대신 소개할게");
	}
}
