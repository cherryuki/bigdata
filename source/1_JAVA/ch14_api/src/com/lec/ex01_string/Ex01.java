package com.lec.ex01_string;
//20-12-11_API(String)		ⓒcherryuki(ji)
public class Ex01 {
	public static void main(String[] args) {
		String str1 = "java";
		String str2 = "java";
		String str3 = new String("java"); //무조건 객체 생성
		if(str1==str2) {
			System.out.println("str1과 str2는 같은 주소");
		}else {
			System.out.println("str1과 str2는 다른 주소");
		}
		str1="java2";	
		if(str1==str2) {
			System.out.println("str1과 str2는 같은 주소");
		}else {
			System.out.println("str1과 str2는 다른 주소");
		}
		if(str2==str3) {
			System.out.println("str2과 str3는 같은 주소");
		}else {
			System.out.println("str2과 str3는 다른 주소");
		}
		System.out.println(str1.hashCode());
		System.out.println(str2.hashCode());
		System.out.println(str3.hashCode());
		System.out.println("str2와 str3은 같은 스트링? "+(str2.contentEquals(str3)?"같다":"다르다"));
	}
}
