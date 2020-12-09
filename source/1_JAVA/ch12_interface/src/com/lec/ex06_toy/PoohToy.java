package com.lec.ex06_toy;
//20-12-09_interface	ⓒcherryuki(ji)
public class PoohToy implements IMoveArmLeg {
	public PoohToy() {
		System.out.println("곰돌이 푸");
		canMoveArmLeg();
		System.out.println("----------------------");
	}
	@Override
	public void canMoveArmLeg() {
		System.out.println("팔다리를 움직일 수 있습니다.");
	}
	@Override
	public String toString() {//Object Class에 있는 toString() 오버라이드
		return "팔다리를 움직이는 곰돌이 푸";
	}
}
