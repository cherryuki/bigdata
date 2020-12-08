package com.lec.ex01_super;
//20-12-07_inheritance ⓒcherryuki(ji)
public class Child extends SuperIJ{//extends 상속받고자 하는 클래스(부모클래스)
	private int total;
	public Child(int i, int j) {
		setI(i); //this.i=i;
		setJ(j); //this.j=j;
	}
	public void sum() {
		//total에 i+j를 할당
		total = getI()+getJ();
		System.out.println("본 객체의 total: "+total);
	}
}
