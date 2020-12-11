package strategy2.car.component;
//20-12-11_strategy pattern		ⓒcherryuki(ji)
public class FuelDiesel implements IFuel {

	@Override
	public void fuel() {
		System.out.println("경유 차량");
	}

}
