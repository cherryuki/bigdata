package com.lec.ex01_runnable;
//20-12-21_Thread		ⓒcherryuki(ji)
public class TargetExTestMain {
	public static void main(String[] args) {
		Runnable target01 = new TargetEx01();//TargetEx01 target01 = new TargetEx01();
		Runnable target02 = new TargetEx02();//TargetEx02 target02 = new TargetEx02();
		Thread threadA = new Thread(target01, "A"); //target01.run()을 수행하는 "A"라는 이름의 스레드
		Thread threadB = new Thread(target02, "B"); //target02.run()을 수행하는 "B"라는 이름의 스레드
		threadA.start();
		threadB.start();
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
