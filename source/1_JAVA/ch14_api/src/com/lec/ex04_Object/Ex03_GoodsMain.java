package com.lec.ex04_Object;
//20-12-15_API(Object)		ⓒcherryuki(ji)

public class Ex03_GoodsMain {
	public static void main(String[] args) {
		Goods s1 = new Goods("a001", "고구마깡", 1100, 10);
		Goods s2 = new Goods("a002", "쵸코츄러스", 2000, 10);
		Goods s3 = new Goods("m003", "맛있는 우유", 850, 20);
		System.out.println(s1);
		System.out.println(s2);
		System.out.println(s3);
		Customer c1 = new Customer("010-9999-9999", "홍길동");
		Customer c2 = new Customer("010-8888-8888", "이몽룡");
		Customer c3 = new Customer("010-8888-8888", "성춘향");
		System.out.println(c1);
		System.out.println(c2);
		System.out.println(c3);
		System.out.println(c2.equals(c3));
	}
}

