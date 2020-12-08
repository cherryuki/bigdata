package com.lec.ex10_final;

public class Animal {
	protected int speed; //protected: 동일 패키지 or 상속받은 하위 클래스
	public void running() {
		speed +=5;
		System.out.println("뛰고 있어요. 현재 속도: "+speed);
	}
	public final void stop() {//final method(): 오버라이드 불가
		speed = 0;
		System.out.println("멈춤");
	}
}
