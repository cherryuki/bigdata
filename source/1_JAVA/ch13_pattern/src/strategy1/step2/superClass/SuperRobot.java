package strategy1.step2.superClass;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class SuperRobot extends Robot {
	public void actionFly() {
		System.out.println("날 수 있습니다");
	}
	public void actionMissile() {
		System.out.println("미사일을 쏠 수 있습니다");
	}
	public void actionKnife() {
		System.out.println("레이저 검이 있습니다");
	}
}
