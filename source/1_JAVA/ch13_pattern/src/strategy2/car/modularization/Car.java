package strategy2.car.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy2.car.component.IEngine;
import strategy2.car.component.IFuel;
import strategy2.car.component.IKm;

public class Car {
	private IEngine engine;
	private IKm		km;
	private IFuel	fuel;
	public void shape() {
		System.out.println("door, sheet, handle이 있습니다");
	}
	public void drive() {
		System.out.println("드라이브 할 수 있습니다");
	}
	public void isEngine() {
		engine.engine();
	}
	public void isKm() {
		km.km();
	}
	public void isFuel() {
		fuel.fuel();
	}
	public void setEngine(IEngine engine) {
		this.engine = engine;
	}
	public void setKm(IKm km) {
		this.km = km;
	}
	public void setFuel(IFuel fuel) {
		this.fuel = fuel;
	}
}
