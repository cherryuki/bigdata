package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Customer {
	private String tel;
	private String name;
	private int point;
	private int amount;
	public Customer(String tel, String name) {
		this.tel=tel;
		this.name=name;
		point = 3000;
	}
	@Override
	public String toString() {
		String postTel = tel.substring(tel.lastIndexOf("-")+1);
		return name+"("+postTel+") 포인트: "+point+", 누적 금액: "+amount;
	}
	@Override
	public boolean equals(Object obj) {
		if(obj!=null && obj instanceof Customer) {
			return tel.equals(((Customer)obj).tel);
		}
		return false;
	}
}
