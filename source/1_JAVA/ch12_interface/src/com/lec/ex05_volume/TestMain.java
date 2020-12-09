package com.lec.ex05_volume;
//20-12-09_interface	ⓒcherryuki(ji)
public class TestMain {
	public static void main(String[] args) {
		//IVolume[] device = {new Radio(), new TV()}; //불가능
		Radio radio = new Radio(5);
		TV tv = new TV(10);
		IVolume[] device = new IVolume[2];
		device[0]=radio;
		device[1]=tv;
		radio.volumeUp(10);
		tv.volumeUp();
		System.out.println("이제부터는 인터페이스를 이용한 호출입니다");
		for(int i=0; i<device.length; i++) {
			device[i].volumeUp(5);
		}
		for(IVolume d:device) {
			d.volumeUp();
			d.volumeDouwn(20);
		}
	}
}
