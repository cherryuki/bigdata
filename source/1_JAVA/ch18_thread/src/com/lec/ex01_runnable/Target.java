package com.lec.ex01_runnable;
//20-12-21_Thread		ⓒcherryuki(ji)
public class Target implements Runnable {

	@Override
	public void run() {
		System.out.println(Thread.currentThread().getName());
		System.out.println("Thread Target");
		for(int i=0; i<10; i++) {
			System.out.println(Thread.currentThread().getName()+"의 i="+i);
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}

}
