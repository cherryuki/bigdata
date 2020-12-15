package com.lec.ex07_timer;
//20-12-15_API(timer)		ⓒcherryuki(ji)
import java.util.TimerTask;

public class TimerTaskEx02 extends TimerTask {

	@Override
	public void run() {
		System.out.println("◇작업2: 1초마다 수행할 예정");//여기서는 무슨일 할지 정함
		//몇 초마다 수행할지는 timer에서 설정
	}

}
