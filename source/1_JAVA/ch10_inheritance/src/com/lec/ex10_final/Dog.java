package com.lec.ex10_final;

public final class Dog extends Animal {//final class: 클래스 상속 불가
	@Override
	public void running() {
		speed += 10;
		System.out.println("강아지가 꼬리를 흔들며 뛰고 있어요. 현재 속도: "+speed);
	}
	public void method() {
		System.out.println("method()");
	}
}
