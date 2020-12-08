package com.lec.ex08_person;
//20-12-07_inheritance ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		Person papa = new Person("아빠곰", "뚱뚱해");
		Person mama = new Person("엄마곰", "날씬해");
		papa.intro();
		mama.intro();
		System.out.println("-------------------");
		Baby child1 = new Baby();
		child1.setName("아기곰1");
		child1.setCharacter("사랑스러워");
		child1.intro();
		Baby child2 = new Baby("아기곰2","귀여워");
		child2.cry();
	}
}
