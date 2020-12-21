package com.lec.ex04_threadN_objectN;
//20-12-21_Thread		ⓒcherryuki(ji)

public class ThreadEx02TestMain {
	public static void main(String[] args) {
		Thread t1 = new ThreadEx02("A");
		Thread t2 = new ThreadEx02("B");
		t1.start();
		t2.start();
	}
}
