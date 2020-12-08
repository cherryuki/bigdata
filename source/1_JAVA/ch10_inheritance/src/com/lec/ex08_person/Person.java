package com.lec.ex08_person;
//20-12-07_inheritance ⓒcherryuki(ji)
//Person p = new Person("공유", "잘생겼다");
public class Person {
	private String name;
	private String character;
	public Person() {
		System.out.println("매개 변수 없는 Person 생성자");
	}
	public Person(String name, String character) {
		this.name=name;
		this.character=character;
		System.out.println("매개 변수 있는 Person 생성자");
	}
	public void intro() {
		System.out.println(name+"은(는) "+character);
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getCharacter() {
		return character;
	}
	public void setCharacter(String character) {
		this.character = character;
	}
	
	
}
