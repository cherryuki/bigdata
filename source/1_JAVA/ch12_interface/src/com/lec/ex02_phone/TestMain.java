package com.lec.ex02_phone;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		AModel aPhone = new AModel();
		BModel bPhone = new BModel();
		CModel cPhone = new CModel();
		IAcor[] phones = {aPhone, bPhone, cPhone};
		for(IAcor phone:phones) {
			//객체의 클래스 타입
			System.out.println(phone.getClass().getName());
			phone.dmbReceive();
			phone.lte();
			phone.tvRemoteControl();
		}
	}
}

