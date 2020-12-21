package com.lec.ex02_thread;
//20-12-21_Thread		ⓒcherryuki(ji)
public class TargetExTestMain {
	public static void main(String[] args) {
		Thread target01 = new TargetEx01();//target01.run()을 수행하는 스레드 생성
		target01.setName("A");//스레드 이름 세팅
		Thread target02 = new TargetEx02();
		target02.setName("B");
		target01.start();
		target02.start();
		for(int i=0; i<10; i++) {
			System.out.println("나는 "+Thread.currentThread().getName());
			try {
				Thread.sleep(500);
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}

