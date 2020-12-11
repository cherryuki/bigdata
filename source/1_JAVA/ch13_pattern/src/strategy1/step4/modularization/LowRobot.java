package strategy1.step4.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.*;

public class LowRobot extends Robot {
	private IFly fly;
	private IMissile missile;
	private IKnife knife;
	public LowRobot() {
		fly 	= new FlyNo();
		missile = new MissileNo();
		knife 	= new KnifeNo();
//		setFly(new FlyNo());
//		setMissile(new MissileNo());
//		setKnife(new KnifeNo());
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
