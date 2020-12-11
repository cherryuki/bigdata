package strategy1.step5.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.FlyNo;
import strategy1.step4.component.KnifeNo;
import strategy1.step4.component.MissileNo;

public class LowRobot extends Robot {
	public LowRobot() {

		setFly(new FlyNo());
		setMissile(new MissileNo());
		setKnife(new KnifeNo());
	}

	@Override
	public void shape() {
		System.out.println("LowRobot은 팔, 다리, 머리, 몸통으로 이루어져있습니다");
	}


}
