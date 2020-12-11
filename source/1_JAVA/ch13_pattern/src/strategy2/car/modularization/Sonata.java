package strategy2.car.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy2.car.component.EngineMid;
import strategy2.car.component.FuelGasoline;
import strategy2.car.component.Km15;

public class Sonata extends Car {
	public Sonata() {
		setEngine(new EngineMid());
		setKm(new Km15());
		setFuel(new FuelGasoline());
	}
	@Override
	public void shape() {
		System.out.print("소나타에는 ");
		super.shape();
	}
}
