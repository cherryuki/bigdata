package strategy1.step3.abst;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public abstract class Robot {//추상 클래스
	public void shape() {
		System.out.println(getClass().getName()+"은 팔, 다리, 머리, 몸통으로 이루어져 있습니다");
	}
	public void actionWalk() {
		System.out.println("걸을 수 있습니다");
	}
	public void actionRun() {
		System.out.println("뛸 수 있습니다");
	}
	public abstract void actionFly(); //추상 메소드 생성(상속 받은 클래스에서 Override하게)
	public abstract void actionMissile();
	public abstract void actionKnife();
}
