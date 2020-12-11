package strategy1.step3.abst;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class StandardRobot extends Robot{
	@Override
	public void actionFly() {
		System.out.println("날 수 없습니다");
	}
	@Override
	public void actionMissile() {
		System.out.println("미사일을 쏠 수 있습니다");
	}
	@Override
	public void actionKnife() {
		System.out.println("목검이 있습니다");
	}
}
