package strategy1.step4.component;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class MissileNo implements IMissile {

	@Override
	public void missile() {
		System.out.println("미사일을 쏠 수 없습니다");
	}

}
