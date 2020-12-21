package com.lec.ex02_thread;
//20-12-21_Thread		ⓒcherryuki(ji)
public class TargetEx01 extends Thread {
	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			System.out.println("안녕하세요-"+i);
		}
		try {
			Thread.sleep(500);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}
}
