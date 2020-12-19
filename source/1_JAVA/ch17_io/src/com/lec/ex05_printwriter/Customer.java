package com.lec.ex05_printwriter;
//20-12-18_input&output Stream		ⓒcherryuki(ji)

public class Customer {
	private String name;
	private String tel;
	private String birth;
	private String address;
	public Customer() {}
	public Customer(String name, String tel, String birth, String address) {
		this.name=name;
		this.tel=tel;
		this.birth=birth;
		this.address=address;
	}
	@Override
	public String toString() {
		return name+"\t"+tel+"\t"+birth+"생\t"+address;
	}
}
