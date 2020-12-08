package com.lec.ex06_lunch;
//20-12-08_abstract class	ⓒcherryuki(ji)

//Child1 c = new Child1(350,1000,100,300,800,350);
public class Child1 extends LunchMenu {
	public Child1(int rice, int bulgogi, int soup, int banana, int milk, int almond) {
		super(rice, bulgogi, soup, banana, milk, almond);
	}
	@Override
	public int calculate() {
		return getRice()+getBulgogi()+getSoup()+getBanana()+getAlmond();
	}

}
