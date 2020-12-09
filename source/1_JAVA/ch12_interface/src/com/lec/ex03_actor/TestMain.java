package com.lec.ex03_actor;
//20-12-09_interface	ⓒcherryuki(ji)

//다중 implements(다중 구현)을 이용한 다형성
public class TestMain {
	public static void main(String[] args) {
		Actor park = new Actor("박보검");
		park.canCatchCriminal();
		park.canSerch();
		park.cookPasta();
		park.makePizza();
		park.outFire();
		park.saveMan();
		IFireFighter firePark = park;
		firePark.outFire();
		firePark.saveMan();
		//firePark.canCatchCriminal(); //불가능
		IPoliceMan policePark = park;
		policePark.canCatchCriminal();
		policePark.canSerch();
		IChef chefPark = park;
		chefPark.cookPasta();
		chefPark.makePizza();
		//chefPark.saveMan(); //불가능
	}
}
