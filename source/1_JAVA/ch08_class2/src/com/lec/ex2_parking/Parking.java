package com.lec.ex2_parking;

public class Parking {
	private String no;
	private int inTime;
	private int outTime;
	private int fee;
	public Parking() {};
	public Parking(String no, int inTime) {
		this.no=no;
		this.inTime=inTime;
		System.out.println("*"+no+"*님 어서오세요");
		System.out.println("*입차시간: "+inTime);
	}
	public void out(int outTime) {
		this.outTime=outTime;
		System.out.println("*"+no+"*님 안녕히 가세요");
		System.out.println("*입차시간: "+inTime);
		System.out.println("*출차시간: "+outTime);
		System.out.println("*주차요금: "+fee+"원");
	}
	public String getNo() {
		return no;
	}
	public void setNo(String no) {
		this.no = no;
	}
	public int getInTime() {
		return inTime;
	}
	public void setInTime(int inTime) {
		this.inTime = inTime;
	}
	public int getOutTime() {
		return outTime;
	}
	public void setOutTime(int outTime) {
		this.outTime = outTime;
	}
	public int getFee() {
		return fee;
	}
	public void setFee(int fee) {
		this.fee = fee;
	}
}
