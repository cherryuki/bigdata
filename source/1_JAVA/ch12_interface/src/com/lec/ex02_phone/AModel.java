package com.lec.ex02_phone;
//20-12-09_interface	ⓒcherryuki(ji)

//a제품: DMB 송수신 불가, 5G, TV리모콘 미탑재
public class AModel implements IAcor{
	private String modelName;
	public AModel() {
		modelName="A제품";
	}
	@Override
	public void dmbReceive() {
		System.out.println(modelName+"은 DMB 송수신 불가");
	}

	@Override
	public void lte() {
		System.out.println(modelName+"은 5G");
	}

	@Override
	public void tvRemoteControl() {
		System.out.println(modelName+"은 TV리모콘 미탑재");
	}

}
