package com.lec.ex02_phone;
//20-12-09_interface	ⓒcherryuki(ji)

//A전자에서 A제품, B제품, C제품
public interface IAcor {//작업 명세서
	public void dmbReceive(); //dmb수신 여부 구현은 클래스에서
	public void lte();
	public void tvRemoteControl();
}
