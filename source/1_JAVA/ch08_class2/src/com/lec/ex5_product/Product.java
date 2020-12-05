package com.lec.ex5_product;

public class Product {
	private int serialNo; //객체 고유번호
	public static int count = 100; //생성된 인스턴스에 수를 저장하기 위한 static 변수
	public Product() {
		serialNo = ++count;
	}
	public void infoString() {
		System.out.println("serialNo: "+serialNo+"\t공유변수 count: "+count);
	}
	public void setSerialNo(int serialNo) {
		this.serialNo=serialNo;
	}
	public int getSerialNo() {
		return serialNo;
	}

}
