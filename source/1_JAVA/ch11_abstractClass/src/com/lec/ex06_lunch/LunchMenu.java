package com.lec.ex06_lunch;
//20-12-08_abstract class	ⓒcherryuki(ji)

//Child1 c = new Child1(350,1000,100,300,800,350);
//Child2 c = new Child2(350,1000,100,300,800,350);
public abstract class LunchMenu {
	private int rice;		//밥 값(1인)
	private int bulgogi;	//불고기 값(1인)
	private int soup;		//국 값(1인)
	private int banana;		//바나나 값(1인)
	private int milk;		//우유 값(1인)
	private int almond;		//아몬드 값(1인)
	public LunchMenu() {}
	public LunchMenu(int rice, int bulgogi, int soup, int banana, int milk, int almond) {
		this.rice=rice;
		this.bulgogi=bulgogi;
		this.soup=soup;
		this.banana=banana;
		this.milk=milk;
		this.almond=almond;
	}
	//식대 계산하는 메소드는 추상 메소드
	public abstract int calculate();
	//getter
	public int getRice() {
		return rice;
	}
	public int getBulgogi() {
		return bulgogi;
	}
	public int getSoup() {
		return soup;
	}
	public int getBanana() {
		return banana;
	}
	public int getMilk() {
		return milk;
	}
	public int getAlmond() {
		return almond;
	}
	
}
