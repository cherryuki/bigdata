package com.lec.ex07_tax;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class LowGradeCar extends Car {
	private int tax = 50000;
	public LowGradeCar(String color, String tire, int displacement, String handle) {
		super(color, tire, displacement, handle);
	}
	@Override
	public void getSpec() {//spec 출력(tax포함)
		System.out.println("-------------------");
		System.out.println("색상: "+getColor());
		System.out.println("타이어: "+getTire());
		System.out.println("배기량: "+getDisplacement());
		System.out.println("핸들: "+getHandle());
		if(getDisplacement()>1000) {
			tax += (getDisplacement()-1000)*200;
		}
		System.out.println("세금: "+tax+"원");
		System.out.println("-------------------");		
	}
}
