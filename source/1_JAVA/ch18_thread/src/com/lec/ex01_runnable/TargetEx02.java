package com.lec.ex01_runnable;
//20-12-21_Thread		ⓒcherryuki(ji)
public class TargetEx02 implements Runnable {

	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			System.out.println("반갑습니다-"+i);
			try {
				Thread.sleep(500);//0.5초 동안 대기 상태
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

}
