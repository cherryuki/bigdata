package strategy2.car.component;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class FuelGasoline implements IFuel {

	@Override
	public void fuel() {
		System.out.println("휘발유 차량");
	}

}
