package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Ex01_Person {
	public static void main(String[] args) {
		String str1 = "java";
		String str2 = new String("java");
		if(str1.equals(str2)) {
			System.out.println("str1과 str2는 같은 문자열");
		}else {
			System.out.println("str1과 str2는 다른 문자열");
		}
		Person p1 = new Person(9312301234567L);//long형으로 맨 뒤에 L붙여줘야 함
		Person p2 = new Person(9312301234567L);
		if(p1.equals(p2)) {
			System.out.println("같은 Person 객체");
		}else {
			System.out.println("다른 Person 객체");
		}
	}
}
