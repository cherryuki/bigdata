package com.lec.ex02;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		//Super s = new Super(); 추상 클래스라 객체 생성 불가
		Child c1 = new Child();
		c1.method1();
		c1.method2();
		c1.method3();
		Super c2 = new Child();
		c2.method1();
		c2.method2();
		//c2.method3(); 불가(c2변수가 Super타입이므로 Super의 것만 가능)
	}
}
