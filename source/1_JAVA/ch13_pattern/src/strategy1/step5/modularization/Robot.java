package strategy1.step5.modularization;

import strategy1.step4.component.IFly;
import strategy1.step4.component.IKnife;
import strategy1.step4.component.IMissile;

//20-12-11_strategy pattern		ⓒcherryuki(ji)
public abstract class Robot {
	private IFly fly;
	private IMissile missile;
	private IKnife knife;
	
	public abstract void shape(); 
	public void actionWalk( ) {
		System.out.println("걸을 수 있습니다");
	}
	public void actionRun() {
		System.out.println("뛸 수 있습니다");
	}
	public void actionFly() {
		fly.fly();
	}
	public void actionMissile() {
		missile.missile();
	}
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
