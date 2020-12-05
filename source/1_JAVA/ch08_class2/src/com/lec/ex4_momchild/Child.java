package com.lec.ex4_momchild;
//Child child1 = new Child("첫째");
//child1.takeMoney(100);
public class Child {
	private String no;
	static MomPouch momPouch = new MomPouch();
	public Child(String no) {
		this.no=no;
	}
	public void takeMoney(int money) {
		if(momPouch.money>=money) {
			momPouch.money -= money;
			System.out.println(no+"가 "+money+"원 가져가서 엄마 지갑엔 "+momPouch.money+"원 있어");
		}else {
			System.out.println("돈이 모자라서 "+no+"에게 돈을 못줘 현재 엄마 지갑엔 "+momPouch.money+"원 있어");
		}
	}
}
