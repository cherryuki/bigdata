package com.lec.ex;

public class CarTestMain {
	public static void main(String[] args) {
		//Scanner sc = new Scanner(System.in); //처럼 사용
		Car myPorshe = new Car();
		Car yourPorshe = new Car();
		myPorshe.drive();
		yourPorshe.drive();
		myPorshe.park();
		yourPorshe.park();
		myPorshe.setColor("red"); //myPorshe.color="red"'
		System.out.println("내 포르쉐 색상: "+myPorshe.getColor());
		System.out.println("네 포르쉐 색상: "+yourPorshe.getColor());
		System.out.println("내 포르쉐 배기량: "+myPorshe.getCc());
	}
}
