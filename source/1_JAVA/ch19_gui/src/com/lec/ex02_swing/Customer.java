package com.lec.ex02_swing;
//20-12-22_GUI(swing)		ⓒcherryuki(ji)

public class Customer {
	private String phone;
	private String name;
	private int point;
	public Customer(String phone, String name, int point) {
		this.phone=phone;
		this.name=name;
		this.point=point;
	}
	
	@Override
	public String toString() {
		return name+"("+phone+")님의 포인트: "+point;
	}
	//getter&setter

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getPoint() {
		return point;
	}

	public void setPoint(int point) {
		this.point = point;
	}
	

}
