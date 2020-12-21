package com.lec.ex03_threadN_object1;
//20-12-21_Thread		ⓒcherryuki(ji)

//스레드 N개가 작업객체 1개를 공유 - Runnable 이용
public class ThreadEx implements Runnable {
	private int num=0; //공유 변수
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
