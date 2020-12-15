package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)
public class Person {
	private long juminNo;
	public Person(long juminNo) {
		this.juminNo=juminNo;
	}
	@Override
	public boolean equals(Object obj) {
		if(obj!=null && obj instanceof Person) {
			return juminNo==((Person)obj).juminNo;
		}//if
		return false;
	}//equals
}//class
