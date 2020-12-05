package com.lec.ex2_man;
//Man kim = new Man(20, 160, 50, "010-1111-1111");
//Man lee = new Man(30, 170, 60);
//Man park = new Man(25, "010-999-9999");
public class Man {
	private int age;
	private int height;
	private int weight;
	private String tel; //int나 double로 넣으면 첫번째 0이 사라지므로 주의!(전화번호는 문자 취급)
	public Man() {}//디폴트 생성자
	public Man(int age, int height, int weight, String tel) {
		this.age=age;
		this.height=height;
		this.weight=weight;
		this.tel=tel;
	}
	public Man(int age, int height, int weight) {
		this.age=age;
		this.height=height;
		this.weight=weight;
	}
	public Man(int age, String tel) {
		this.age=age;
		this.tel=tel;
	}
	//BMI지수를 반환하는 메소드
	public double calculateBMI() {
		double result = weight / ((height*0.01)*(height*0.01));
		return result;
	}
	//(age, height, weight, tel)의 setter&getter
	public void setAge(int age) {
		this.age=age;
	}
	public void setHeight(int height) {
		this.height=height;
	}
	public void setWeight(int weight) {
		this.weight=weight;
	}
	public void setTel(String tel) {
		this.tel=tel;
	}
	public int getAge() {
		return age;
	}
	public int getHeight() {
		return height;
	}
	public int getWeight() {
		return weight;
	}
	public String getTel() {
		return tel;
	}
}
