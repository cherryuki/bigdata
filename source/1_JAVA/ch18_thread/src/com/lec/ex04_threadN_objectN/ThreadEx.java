package com.lec.ex04_threadN_objectN;
//20-12-21_Thread		ⓒcherryuki(ji)

public class ThreadEx implements Runnable {
	private int num=0; 
	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			String threadName = Thread.currentThread().getName();
			if(threadName.equals("A")) {
				System.out.println("~~~A수행중~~~");
				num++;
			}
			System.out.println(threadName+"의 num="+num);
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		
	}

}
