package com.singleton.step1;
//20-12-10_singletonClass	ⓒcherryuki(ji)
public class SingletonClass {
	private int i;
	private static SingletonClass INSTANCE; //SingletonClass형 객체 주소
	public static SingletonClass getInstance() {
		if(INSTANCE==null) {
			INSTANCE = new SingletonClass();
		}
		return INSTANCE;
	}
	private SingletonClass() {
		i=10;
	}
	public int getI() {
		return i;
	}
	public void setI(int i) {
		this.i = i;
	}
}
