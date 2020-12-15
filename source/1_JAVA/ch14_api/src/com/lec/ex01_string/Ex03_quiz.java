package com.lec.ex01_string;
//20-12-11_API(String)		ⓒcherryuki(ji)
import java.util.Scanner;

public class Ex03_quiz {
	public static void main(String[] args) {
		Ex03_quiz ex = new Ex03_quiz();
		System.out.println(ex.getClass().getName().substring((ex.getClass().getName().lastIndexOf(".")+1)));
		Scanner sc = new Scanner(System.in);
		while(true) {
			System.out.println("전화번호를 입력하세요(000-000-0000)");
			String tel = sc.next();
			if(tel.equalsIgnoreCase("x")) break;
			System.out.println("입력하신 전화번호: "+tel);
			System.out.print("짝수번째 문자열: ");
			for(int i=0; i<tel.length(); i++) {
				if(i%2==0) {
					System.out.print(tel.charAt(i)+" ");
				}//if
			}//for
			System.out.print("\n문자를 거꾸로: ");
			for(int i=tel.length()-1; i>-1; i--) {
				System.out.print(tel.charAt(i));
			}
			System.out.println();
			System.out.println("전화번호 맨앞자리는: "+tel.substring(0,(tel.indexOf("-"))));
			System.out.println("전화번호 뒷자리는: "+tel.substring((tel.lastIndexOf("-")+1)));
		}
		System.out.println("종료합니다");
		sc.close();
	}
}
