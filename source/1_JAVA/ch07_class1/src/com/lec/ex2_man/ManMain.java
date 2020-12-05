package com.lec.ex2_man;

public class ManMain {
	public static void main(String[] args) {
		Man kim = new Man(20, 160, 50, "010-1111-1111");
		Man lee = new Man(30, 150, 60);
		Man park = new Man(25, "010-999-9999");
		Man[] student = {kim, park};
		lee.setTel("010-2222-2000");
		park.setHeight(180);
		park.setWeight(75);
		double biman = kim.calculateBMI();
		if(biman>24) {
			System.out.println("비만이니 건강 조심");
		}else {
			System.out.println("다이어트 금지");
		}
		biman = lee.calculateBMI();
		System.out.println(biman>24? "비만이니 건강 조심":"다이어트 금지");
		biman = park.calculateBMI();
		System.out.println(biman>24? "비만이니 건강 조심":"다이어트 금지");
	}
}
