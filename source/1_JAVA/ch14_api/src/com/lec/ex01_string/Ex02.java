package com.lec.ex01_string;
//20-12-11_API(String)		ⓒcherryuki(ji)

//다양한 String의 method들
public class Ex02 {
	public static void main(String[] args) {
		String a = "abcXabc";
		String b = new String("ABCXabc");
		String c = "    ja   va    ";
		System.out.println("1.concat:"+a.concat(b));//a와 b를 붙여 줌 //abcXabcABCXabc
		System.out.println("2.substring: "+a.substring(3));//a의 3번째 문자열부터 끝까지(문자열은 0부터 시작) //Xabc
		System.out.println("3.substring(n,m): "+a.substring(3,5));//a의 3번째 문자열부터 5번째 전까지(3,4 문자열) //Xa
		System.out.println("4.length: "+a.length());//a 문자 길이//7
		System.out.println("5.toUpperCase: "+a.toUpperCase());//소문자를 대문자로//ABCXABC
		System.out.println("6.toLowerCase: "+b.toLowerCase());//대문자를 소문자로//abcxabc
		System.out.println("7.charAt(n): "+a.charAt(3));//n번째 문자//X
		System.out.println("8.indexOf(x): "+a.indexOf("b"));//첫 b가 있는 인덱스//1
		System.out.println("9.indexOf(x,n): "+a.indexOf("b",3));//3번째 이후부터 첫 b가 있는 인덱스//5
		System.out.println("10.lastIndexOf(x): "+a.lastIndexOf("b"));//마지막 b 인덱스//5
		System.out.println("11.indexOf(x): "+a.indexOf("z"));//찾는 문자가 없을 경우//-1
		System.out.println("12.equals: "+a.equals(b));//대소문자 구분해서 같으면 true, 다르면 false//false
		System.out.println("13.equalsIgnoreCase: "+a.equalsIgnoreCase(b));//대소문자 구분없이 같으면 true, 다르면 false//true
		System.out.println("14.trim: "+c.trim());//좌우 space 제거//ja   va
		System.out.println("15.replace: "+a.replace('a', '에'));//문자 교체//에bcx에bc
		System.out.println("16.replace: "+a.replace("ab", "에이비"));//문자열 교체//에이비cx에이비c
		System.out.println("최종 a: "+a);//a는 바뀌지 않음//abcXabc
		
	}
}
