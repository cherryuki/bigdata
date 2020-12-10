package com.singleton.step2;
//20-12-10_singletonClass	ⓒcherryuki(ji)
public class SingletonClass {
	private static SingletonClass INSTANCE = new SingletonClass(); //if문 처리한 부분을 이렇게 쓰기도 함
	private int i;
	private SingletonClass() {
		i=10;
	}
	public static SingletonClass getInstance() {
//		if(INSTANCE==null) {
//			INSTANCE = new SingletonClass();
//		}
		return INSTANCE;
	}
	public int getI() {
		return i;
	}
	public void setI(int i) {
		this.i = i;
	}
}
