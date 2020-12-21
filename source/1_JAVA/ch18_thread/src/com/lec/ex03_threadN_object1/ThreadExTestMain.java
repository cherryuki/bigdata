package com.lec.ex03_threadN_object1;
//20-12-21_Thread		ⓒcherryuki(ji)
public class ThreadExTestMain {
	public static void main(String[] args) {
		Runnable target = new ThreadEx(); //작업객체 1개 쓰레드 공유
		Thread t1 = new Thread(target, "A");
		Thread t2 = new Thread(target, "B");
		t1.start();
		t2.start();
	}
}
