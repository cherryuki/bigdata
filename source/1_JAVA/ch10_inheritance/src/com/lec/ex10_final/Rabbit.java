package com.lec.ex10_final;

public class Rabbit extends Animal{
	@Override
	public void running() {
		speed += 30;
		System.out.println("토끼가 껑충껑충 뛰어요. 현재 속도: "+speed);
	}
}
