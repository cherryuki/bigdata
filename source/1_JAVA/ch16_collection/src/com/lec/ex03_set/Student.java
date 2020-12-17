package com.lec.ex03_set;
//20-12-17_Collection		ⓒcherryuki(ji)
public class Student {
	private String name;
	private int grade;
	public Student(String name, int grade) {
		this.name=name;
		this.grade=grade;
	}
	@Override
	public String toString() {
		return name+":"+grade+"학년";
	}
	@Override
	public boolean equals(Object obj) {
		if(obj!=null && obj instanceof Student) {
			return name.equals(((Student)obj).name) && grade==((Student)obj).grade;
//			return toString().equals(obj.toString());
		}
		return false;
	}
	@Override
	public int hashCode() {
		return toString().hashCode();
	}
}
