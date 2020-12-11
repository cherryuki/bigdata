package strategy1.step4.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.FlyNo;
import strategy1.step4.component.IFly;
import strategy1.step4.component.IKnife;
import strategy1.step4.component.IMissile;
import strategy1.step4.component.KnifeWood;
import strategy1.step4.component.MissileYes;

//날 수 없음, 미사일 쏠 수 있음, 목검
public class StandardRobot extends Robot {
	private IFly fly;
	private IMissile missile;
	private IKnife knife;
	public StandardRobot() {
		fly 	= new FlyNo();
		missile = new MissileYes();
		knife 	= new KnifeWood();
//		setFly(new FlyNo());
//		setMissile(new MissileYes());
//		setKnife(new KnifeWood());
	}
	@Override
	public void actionFly() {
		fly.fly();
	}

	@Override
	public void actionMissile() {
		missile.missile();
	}

	@Override
	public void actionKnife() {
		knife.knife();
	}
	//setter
	public void setFly(IFly fly) {
		this.fly = fly;
	}
	public void setMissile(IMissile missile) {
		this.missile = missile;
	}
	public void setKnife(IKnife knife) {
		this.knife = knife;
	}

}
