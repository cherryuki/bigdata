package com.lec.ex05_synchronize;
//20-12-21_Thread		ⓒcherryuki(ji)

//스레드 N개가 작업객체 1개를 공유 - Runnable 이용
//synchronized method() 수행 중에는 아무도 못껴들게 함(synchronized는 함수 앞에만 붙을 수 있음)
public class ThreadEx implements Runnable {
	private int num=0; //공유 병수
	
	@Override
	public void run() {
		for(int i=0; i<10; i++) {
			out(); //synchronized를 함수 앞에 붙이기 위해 method를 생성
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}//for

	}//run

	private synchronized void out() {
		String threadName = Thread.currentThread().getName();
		if(threadName.equals("A")) {
			System.out.println("~~~A 수행 중~~~");
			num++;
		}
		System.out.println(threadName+"의 num="+num);
		
	}

}
