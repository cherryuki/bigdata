package com.lec.ex05_synchronize;
//20-12-21_Thread		ⓒcherryuki(ji)

public class ThreadExTestMain {
	public static void main(String[] args) {
		Runnable target = new ThreadEx(); //작업객체 1개를 N개의 스레드 공유
		Thread t1 = new Thread(target, "A");
		Thread t2 = new Thread(target, "B");
		t1.start();
		t2.start();
	}
}
