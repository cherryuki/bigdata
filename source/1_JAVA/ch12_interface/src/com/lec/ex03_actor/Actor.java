package com.lec.ex03_actor;
//20-12-09_interface	ⓒcherryuki(ji)
public class Actor implements IFireFighter, IPoliceMan, IChef {
	private String name;
	public Actor(String name) {
		this.name=name;
	}
	@Override
	public void makePizza() {
		System.out.println(name+"은 피자를 만들 수 있다");
	}

	@Override
	public void cookPasta() {
		System.out.println(name+"은 파스타를 만들 수 있다");
	}

	@Override
	public void canCatchCriminal() {
		System.out.println(name+"은 범인을 잘을 수 있다");
	}

	@Override
	public void canSerch() {
		System.out.println(name+"은 물건을 찾을 수 있다");
	}

	@Override
	public void outFire() {
		System.out.println(name+"은 불을 끌 수 있다");
	}

	@Override
	public void saveMan() {
		System.out.println(name+"은 사람을 구할 수 있다");
	}

}
