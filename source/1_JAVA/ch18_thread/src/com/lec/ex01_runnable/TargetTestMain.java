package com.lec.ex01_runnable;
//20-12-21_Thread		ⓒcherryuki(ji)
public class TargetTestMain {
	public static void main(String[] args) {
		Target target = new Target();
		Thread t1 = new Thread(target, "A");//target.run()을 수행하는 "A"라는 이름의 스레드 생성
		Thread t2 = new Thread(target, "B");//target.run()을 수행하는 "B"라는 이름의 스레드 생성
		t1.start();
		t2.start();
		System.out.println(Thread.currentThread().getName());
		System.out.println("main함수 끝");
		
	}
}
