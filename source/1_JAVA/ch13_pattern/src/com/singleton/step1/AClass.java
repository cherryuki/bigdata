package com.singleton.step1;
//20-12-10_singletonClass	ⓒcherryuki(ji)
public class AClass {
	private int intVar;
	private static AClass INSTANCE; //2.생성자를 대신할 변수를 만든다
	public static AClass getInstance() {//3.public static AClass getInstance() {if null이면 만들고 아니면 return;} 
		if(INSTANCE==null) {
			INSTANCE = new AClass();
		}
		return INSTANCE;
	}
	private AClass() {} //1. 생성자를 private로 바꾼다
	public int getIntVar() {
		return intVar;
	}
	public void setIntVar(int intVar) {
		this.intVar=intVar;
	}
}
