package com.lec.ex06_toy;
//20-12-09_interface	ⓒcherryuki(ji)
public class AirplaneToy implements ILight, IMissile {
	public AirplaneToy() {
		System.out.println("비행기 장난감");
		canLight();
		canMissile();
		System.out.println("----------------------");
	}
	@Override
	public void canMissile() {
		System.out.println("미사일 쏠 수 있습니다.");
	}

	@Override
	public void canLight() {
		System.out.println("불빛 발사 가능합니다.");
	}
	@Override
	public String toString() {
		return "미사일 쏘고 불빛 발사 가능한 비행기 장난감";
	}
}
