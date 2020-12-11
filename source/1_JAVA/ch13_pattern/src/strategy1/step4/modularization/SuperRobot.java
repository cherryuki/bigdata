package strategy1.step4.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy1.step4.component.FlyYes;
import strategy1.step4.component.IFly;
import strategy1.step4.component.IKnife;
import strategy1.step4.component.IMissile;
import strategy1.step4.component.KnifeLaser;
import strategy1.step4.component.MissileYes;

//날 수 있음, 미사일 쏨, 레이저 검
public class SuperRobot extends Robot {
	private IFly 	 fly;
	private IMissile missile;
	private IKnife 	 knife;
	public SuperRobot() {
		//부품들 생성
		fly 	= new FlyYes();
		missile = new MissileYes();
		knife 	= new KnifeLaser();
//		setFly(new FlyYes());
//		setMissile(new MissileYes());
//		setKnife(new KnifeLaser());
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
