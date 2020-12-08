package com.lec.ex07_tax;
//20-12-08_abstract class	ⓒcherryuki(ji)
public class HighGradeCar extends Car {
	private int tax = 100000;
	public HighGradeCar(String color, String tire, int displacement, String handle) {
		super(color, tire, displacement, handle);
	}
	@Override
	public void getSpec() {
		System.out.println("-------------------");
		System.out.println("색상: "+getColor());
		System.out.println("타이어: "+getTire());
		System.out.println("배기량: "+getDisplacement());
		System.out.println("핸들: "+getHandle());
		if(getDisplacement()>1500) {
			tax += (getDisplacement()-1500)*200;
		}
		System.out.println("세금: "+tax+"원");
		System.out.println("-------------------");	
	}
}
