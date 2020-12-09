package com.lec.ex05_volume;
//20-12-09_interface	ⓒcherryuki(ji)

//TV는 볼륨 2씩 조정
public class TV implements IVolume {
	private int volume;
	public TV() {}
	public TV(int volume) {
		this.volume=volume;
	}
	@Override
	public void volumeUp() {
		volume+=2;
		if(volume>=RADIO_MAX_VOLUME) {
			volume=RADIO_MAX_VOLUME;
			System.out.println("음량 최대치("+RADIO_MAX_VOLUME+")로 더이상 음량을 높일 수 없습니다");
		}else {
			System.out.println("현재 TV음량: "+volume);
		}
	}

	@Override
	public void volumeUp(int level) {
		volume += level;
		if(volume>=RADIO_MAX_VOLUME) {
			volume=RADIO_MAX_VOLUME;
			System.out.println("음량 최대치("+RADIO_MAX_VOLUME+")로 더이상 음량을 높일 수 없습니다");
		}else {
			System.out.println("현재 TV음량: "+volume);
		}
	}

	@Override
	public void volumeDown() {
		volume-=2;
		if(volume<=MIN_VOLUME) {
			volume=MIN_VOLUME;
			System.out.println("무음 상태로 더이상 음량을 줄일 수 없습니다");
		}else {
			System.out.println("현재 TV음량: "+volume);
		}

	}

	@Override
	public void volumeDouwn(int level) {
		volume -= level;
		if(volume<=MIN_VOLUME) {
			volume=MIN_VOLUME;
			System.out.println("무음 상태로 더이상 음량을 줄일 수 없습니다");
		}else {
			System.out.println("현재 TV음량: "+volume);
		}

	}

}
