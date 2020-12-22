package com.lec.ex02_swing;
//20-12-22_GUI(swing)		ⓒcherryuki(ji)

public class Person {
	private String name;
	private String tel;
	private int age;
	public Person(String name, String tel, int age) {
		this.name=name;
		this.tel=tel;
		this.age=age;
	}
	@Override
	public String toString() {
		return "[이름]"+name+" [전화]"+tel+" [나이]"+age;
	}
	//getter&setter
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getTel() {
		return tel;
	}
	public void setTel(String tel) {
		this.tel = tel;
	}
	public int getAge() {
		return age;
	}
	public void setAge(int age) {
		this.age = age;
	}
	
}
