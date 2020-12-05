package com.lec.ex;
//Car myPorsche = new Car();
//Scanner sc = new Scanner(~);
public class Car {
	private String color; //데이터->private
	private int cc;
	private int speed;
	public Car() {//생성자 함수: 리턴타입이 없고 클래스명과 동일한 이름의 메소드
				  //디폴트 생성자 함수는 생성자 함수가 하나도 없을 때 JVM이 자동 생성
				  //객체변수가 생성될 때 자동 호출
		cc=1000;
	}
	public void drive() {//메소드(public)들
		speed=60;
		System.out.println("운전, 현재 속도: "+speed);
	}
	public void park() {
		speed=0;
		System.out.println("주차, 현재 속도: "+speed);
	}
	public void race() {
		speed=120;
		System.out.println("레이싱, 현재 속도: "+speed);
	}
	//~.setColor("red")
	public void setColor(String color) {
		this.color=color;
	}
	//~.getColor
	public String getColor() {
		return color;
	}
	//~.getCc()
	public int getCc() {
		return cc;
	}
}
