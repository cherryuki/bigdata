package com.lec.ex05_volume;
//20-12-09_interface	ⓒcherryuki(ji)
public interface IVolume {
	public int TV_MAX_VOLUME = 50; 
	public int RADIO_MAX_VOLUME = 30;
	public int MIN_VOLUME = 0;
	public void volumeUp();
	public void volumeUp(int level);
	public void volumeDown();
	public void volumeDouwn(int level);
	public default void mute() {//일반 메소드는 넣을 수 없으므로 default 예약어를 이용해서 default method 생성
			System.out.println("무음 처리합니다");
	}
}
