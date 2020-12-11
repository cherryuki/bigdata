package strategy1.step5.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.FlyNo;
import strategy1.step4.component.KnifeWood;
import strategy1.step4.component.MissileYes;

//날 수 없음, 미사일 쏠 수 있음, 목검
public class StandardRobot extends Robot {
	public StandardRobot() {
		setFly(new FlyNo());
		setMissile(new MissileYes());
		setKnife(new KnifeWood());
	}
	@Override
	public void shape() {
		System.out.println("StandardRobot은 팔, 다리, 머리, 몸통으로 이루어져있습니다");		
	}

}
