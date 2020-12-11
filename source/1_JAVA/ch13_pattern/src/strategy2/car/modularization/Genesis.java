package strategy2.car.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy2.car.component.EngineHigh;
import strategy2.car.component.FuelGasoline;
import strategy2.car.component.Km10;

public class Genesis extends Car {
	public Genesis() {
		setEngine(new EngineHigh()); //engine = new EngineHigh();
		setKm(new Km10());
		setFuel(new FuelGasoline());
	}
	@Override
	public void shape() {
		System.out.print("제네시스에는 ");
		super.shape();//Car shaper에 있는 값 가져옴
	}
}
