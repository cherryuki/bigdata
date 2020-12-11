package strategy2.car.modularization;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
import strategy2.car.component.EngineLow;
import strategy2.car.component.FuelDiesel;
import strategy2.car.component.Km20;

public class Accent extends Car {
	public Accent() {
		setEngine(new EngineLow());
		setKm(new Km20());
		setFuel(new FuelDiesel());
	}
	@Override
	public void shape() {
		System.out.print("액센트에는 ");
		super.shape();
	}
}
