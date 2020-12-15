package com.lec.ex07_timer;
//20-12-15_API(timer)		ⓒcherryuki(ji)
import java.util.TimerTask;

public class TimerTaskEx01 extends TimerTask {
	//오버라이드 함수 run에 작업 정의
	@Override
	public void run() {
		System.out.println("◆작업1: 2초 후에 한 번 timer 예정");
		//"2초 후에 한 번"은 timer에서 설정해야 함
	}

}
