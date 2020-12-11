package strategy1.step5.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.FlyYes;
import strategy1.step4.component.KnifeLaser;
import strategy1.step4.component.MissileYes;

//날 수 있음, 미사일 쏨, 레이저 검
public class SuperRobot extends Robot {

	public SuperRobot() {
		setFly(new FlyYes());
		setMissile(new MissileYes());
		setKnife(new KnifeLaser());
	}
	@Override
	public void shape() {
		System.out.println("SuperRobot은 팔, 다리, 머리, 몸통으로 이루어져있습니다");		
	}

}
